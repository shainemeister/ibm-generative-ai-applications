"""
Automated Image Captioning Script - Local Files
This script is part of IBM Generative AI Applications project.
Processes images locally in a specified directory using BLIP model.
"""

import os
import glob
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load the pretrained processor and model
# Note: For even better results, you can switch to Blip2 (Salesforce/blip2-opt-2.7b)
# but it requires ~10GB of space
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Specify the directory where your images are
IMAGE_DIR = "sample_images"  # Update this path
image_exts = ["*.jpg", "*.jpeg", "*.png"]  # Specify the image file extensions to search for

# Open a file to write the captions
with open("automate_local_captions.txt", "w", encoding="utf-8") as caption_file:
    # Iterate over each image file in the directory
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(IMAGE_DIR, image_ext)):
            try:
                # Load your image
                raw_image = Image.open(img_path).convert("RGB")

                # Skip very small images
                if raw_image.size[0] * raw_image.size[1] < 200:
                    continue

                # Process the image with a text prompt
                text = "the image of"
                inputs = processor(images=raw_image, text=text, return_tensors="pt")
                out = model.generate(**inputs, max_new_tokens=50)
                caption = processor.decode(out[0], skip_special_tokens=True)

                # Write the caption to the file, prepended by the image filename
                caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")
                print(f"Caption saved for {os.path.basename(img_path)}")

            except Exception as e:
                print(f"Error processing {img_path}: {e}")
                continue
