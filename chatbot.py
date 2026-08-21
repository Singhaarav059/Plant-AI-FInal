import logging
from gemini_helper import get_chatbot_response as gemini_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def get_response(question, lang='en'):
    """
    Get an AI-powered response to a farming or plant disease question

    Args:
        question: The user's question
        lang: The language code ('en', 'hi', 'ta', 'te', 'bn', 'gu')

    Returns:
        String response from the chatbot
    """
    return gemini_response(question, lang)
