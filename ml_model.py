import io
import base64
import logging
from PIL import Image

# Import both Gemini and OpenAI helpers for disease analysis
from gemini_helper import analyze_plant_image as gemini_analyze
from openai_helper import analyze_plant_image as openai_analyze

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Dictionary of fallback disease information in case API calls fail
FALLBACK_DISEASES = {
    'Unknown': {
        'name': 'Unknown Disease or Plant',
        'severity': 'medium',
        'description': 'Unable to analyze the plant image at this time. Please try again later.',
        'treatment': 'For better identification, take clear photos in good lighting. Consider consulting a local agricultural extension office for in-person diagnosis.'
    }
}

def load_model():
    """
    Placeholder function to maintain API compatibility.
    With Gemini handling the predictions, no local model loading is needed.
    """
    logging.info("Using Gemini for plant disease detection with OpenAI as fallback")
    return True

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
    Predict the disease from the preprocessed image using Gemini
    with OpenAI as a fallback option
    
    Args:
        image_base64: Base64 encoded image string
        lang: Language code for the response
        
    Returns:
        Tuple containing (disease_name, confidence, severity, description, treatment)
    """
    try:
        # First try Gemini Vision API
        logging.info("Attempting disease detection with Gemini")
        result = gemini_analyze(image_base64, lang)
        logging.info(f"Gemini predicted disease: {result[0]} with confidence {result[1]}")
        return result
        
    except Exception as e:
        logging.error(f"Error predicting disease with Gemini: {str(e)}")
        
        # Try OpenAI as fallback
        try:
            logging.info("Falling back to OpenAI for disease detection")
            result = openai_analyze(image_base64, lang)
            logging.info(f"OpenAI fallback predicted disease: {result[0]}")
            return result
            
        except Exception as e2:
            logging.error(f"Error with fallback to OpenAI: {str(e2)}")
            
            # Return unknown disease if both prediction methods fail
            unknown = FALLBACK_DISEASES['Unknown']
            return (
                unknown['name'],
                0.0,
                unknown['severity'],
                unknown['description'],
                unknown['treatment']
            )
