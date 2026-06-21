"""
Module for initializing LLM (via Ollama), processing PDF documents with RAG,
and handling user prompts for the private data chatbot.
"""

import logging
from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
# Replaced IBM Watsonx with local Ollama
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Global state variables (module-level)
CONVERSATION_RETRIEVAL_CHAIN = None
CHAT_HISTORY = []
LLM_HUB = None
EMBEDDINGS = None

# placeholder for Watsonx_API and Project_id incase you need to use the code outside this environment
#Watsonx_API = "Your WatsonX API"
#Project_id= "Your Project ID"

def init_llm():
    """Initialize the LLM (via Ollama) and embeddings model."""
    global LLM_HUB, EMBEDDINGS  # pylint: disable=global-statement

    logger.info("Initializing Ollama LLM and embeddings...")

    # Local Ollama model configuration (replaces previous cloud Watsonx/IBM setup)
    # Use the specific GGUF Q8_0 model from HF (already present on this system):
    # https://huggingface.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF
    # Exact tag: hf.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF:gemma4-v2-Q8_0.gguf
    # Requirements: ollama serve must be running
    ollama_model = "hf.co/yuxinlu1/gemma-4-12B-agentic-fable5-composer2.5-v2-3.5x-tau2-GGUF:gemma4-v2-Q8_0.gguf"

    # Use the same parameters as before:
    #   num_predict (max tokens): 256, TEMPERATURE: 0.1
    model_parameters = {
        # "decoding_method": "greedy",
        "num_predict": 256,
        "temperature": 0.1,
    }

    # Initialize local LLM via Ollama
    LLM_HUB = OllamaLLM(
        model=ollama_model,
        **model_parameters
    )
    logger.debug("Ollama LLM initialized: %s", LLM_HUB)

    # Initialize embeddings using a local Ollama model (100% local, no Hugging Face).
    EMBEDDINGS = OllamaEmbeddings(
        model="nomic-embed-text"
    )
    logger.debug("Embeddings initialized.")


def process_document(document_path):
    """Load PDF, split into chunks, create Chroma vector store and RetrievalQA chain."""
    global CONVERSATION_RETRIEVAL_CHAIN  # pylint: disable=global-statement

    logger.info("Loading document from path: %s", document_path)
    # Load the document
    loader = PyPDFLoader(document_path)
    documents = loader.load()
    logger.debug("Loaded %d document(s)", len(documents))

    # Split the document into chunks, set chunk_size=1024, and chunk_overlap=64.
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
    texts = text_splitter.split_documents(documents)
    logger.debug("Document split into %d text chunks", len(texts))

    # Create an embeddings database using Chroma from the split text chunks.
    logger.info("Initializing Chroma vector store from documents...")
    db = Chroma.from_documents(texts, embedding=EMBEDDINGS)
    logger.debug("Chroma vector store initialized.")

    # Optional: Log available collections if accessible (this may be internal API)
    try:
        collections = db._client.list_collections()  # pylint: disable=protected-access
        logger.debug("Available collections in Chroma: %s", collections)
    except Exception as e:  # pylint: disable=broad-exception-caught
        logger.warning("Could not retrieve collections from Chroma: %s", e)

    # Build the QA chain, which utilizes the LLM and retriever for answering questions.
    CONVERSATION_RETRIEVAL_CHAIN = RetrievalQA.from_chain_type(
        llm=LLM_HUB,
        chain_type="stuff",
        retriever=db.as_retriever(
            search_type="mmr", search_kwargs={"k": 6, "lambda_mult": 0.25}
        ),
        return_source_documents=False,
        input_key="question"
        # chain_type_kwargs={"prompt": prompt}  # if you are using a prompt template, uncomment this part
    )
    logger.info("RetrievalQA chain created successfully.")


def process_prompt(prompt):
    """Process a user prompt using the retrieval chain and update chat history."""
    global CONVERSATION_RETRIEVAL_CHAIN  # pylint: disable=global-variable-not-assigned
    global CHAT_HISTORY  # pylint: disable=global-variable-not-assigned

    logger.info("Processing prompt: %s", prompt)
    # Query the model using the new .invoke() method
    output = CONVERSATION_RETRIEVAL_CHAIN.invoke({"question": prompt, "chat_history": CHAT_HISTORY})
    answer = output["result"]
    logger.debug("Model response: %s", answer)

    # Update the chat history
    CHAT_HISTORY.append((prompt, answer))
    logger.debug("Chat history updated. Total exchanges: %d", len(CHAT_HISTORY))

    # Return the model's response
    return answer


# Initialize the language model
init_llm()
logger.info("LLM and embeddings initialization complete.")