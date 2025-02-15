#!/usr/bin/env python3
import logging
import os
import pytesseract
from PIL import Image
from google import genai
import keys
import prompt  # Import the prompt module for subject-specific prompt functions

# ----------------------------- Configuration -----------------------------
# Update this if Tesseract is not in your PATH.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Folder where screenshots are stored (images are already here)
SCREENSHOT_FOLDER = r"C:\Users\lampe\OneDrive\Afbeeldingen\Screenshots"

# Output file for the final summary
OUTPUT_FILE = "output.txt"

# Initialize API client
API_KEY = keys.API_KEY
client = genai.Client(api_key=API_KEY,
    http_options={'api_version':'v1alpha'},
)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ----------------------------- OCR Processing -----------------------------
def ocr_folder_images(folder_path: str) -> str:
    if not os.path.exists(folder_path):
        logging.error("The folder does not exist.")
        return ""
    
    valid_extensions = {'.png', '.jpg', '.jpeg', '.bmp', '.tiff'}
    image_files = [f for f in os.listdir(folder_path)
                   if os.path.splitext(f)[1].lower() in valid_extensions]
    image_files.sort() 

    all_text = ""
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        try:
            img = Image.open(image_path)
            text = pytesseract.image_to_string(img)
            all_text += f"--- Text from {image_file} ---\n{text}\n\n"
        except Exception as e:
            logging.error(f"Error processing {image_file}: {e}")
    
    if not all_text:
        logging.warning("No text was extracted from images.")
    else:
        logging.info("OCR processing complete.")
    return all_text

# ----------------------------- GenAI Summarization -----------------------------
def summarize_content(prompt_message: str) -> str:
    """
    Sends the prompt_message to the GenAI API and returns the summary.
    """
    logging.info("Initiating API call to generate summary.")
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-thinking-exp-01-21', 
            contents=prompt_message
        )
        # Extract text content from response
        content = response.text if hasattr(response, 'text') else str(response)
        return content.strip()
    except Exception as e:
        logging.error(f"Error generating summary: {e}")
        return f"Error generating summary: {e}"
# ----------------------------- Main Flow -----------------------------
if __name__ == '__main__':
    # Run OCR on the existing screenshots folder
    logging.info(f"Starting OCR processing on images in: {SCREENSHOT_FOLDER}")
    extracted_text = ocr_folder_images(SCREENSHOT_FOLDER)
    
    if not extracted_text:
        logging.error("No text extracted. Exiting.")
        exit(1)
    
    # Define available subjects and their corresponding prompt functions from prompt.py
    subjects = {
        1: ("Bio", prompt.bio),
        2: ("Fysica", prompt.fysica),
        3: ("Aardrijkskunde", prompt.aardrijkskunde),
    }
    
    print('='*30+'\n')
    # Display the subject options to the user
    print("Choose a subject:")
    for num, (subject_name, _) in subjects.items():
        print(f"  {num}: {subject_name}")
    
    # Get a valid subject choice from the user
    while True:
        try:
            subject_choice = int(input("Your choice: "))
            if subject_choice in subjects:
                break
            else:
                print("Invalid choice. Please choose one of:", ', '.join(map(str, subjects.keys())))
        except ValueError:
            print("Please enter a valid number.")
    print('\n'+'='*30)
    
    # Retrieve the subject's name and its corresponding prompt function
    subject_name, subject_func = subjects[subject_choice]
    combined_prompt = subject_func(extracted_text)
    
    # Call the GenAI summarization API
    summary = summarize_content(combined_prompt)
    
    # Write the final summary to the output file
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(summary)
        logging.info(f"Summary successfully written to {OUTPUT_FILE}")
    except Exception as e:
        logging.error(f"Failed to write summary to {OUTPUT_FILE}: {e}")
    
    print("\n----- SUMMARY GENERATED -----\n")
