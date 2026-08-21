import io
import base64
import logging
from PIL import Image

from gemini_helper import analyze_plant_image as gemini_analyze

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def preprocess_image(image_data):
    """
    Preprocess the image for Gemini Vision API

    Args:
        image_data: Binary image data

    Returns:
        Base64 encoded image string
    """
    try:
        # Open image from binary data to verify it's a valid image
        img = Image.open(io.BytesIO(image_data))

        # Convert to RGB (in case of RGBA or other formats)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Re-encode as JPEG to standardize format
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Convert to base64
        base64_encoded = base64.b64encode(img_byte_arr).decode('utf-8')

        logging.info("Image preprocessed successfully")
        return base64_encoded

    except Exception as e:
        logging.error(f"Error preprocessing image: {str(e)}")
        raise

def predict_disease(image_base64, lang='en'):
    """
    Predict the disease from the preprocessed image using Vertex AI Gemini

    Args:
        image_base64: Base64 encoded image string
        lang: Language code for the response

    Returns:
        Tuple containing (disease_name, confidence, severity, description, treatment)
    """
    return gemini_analyze(image_base64, lang)
