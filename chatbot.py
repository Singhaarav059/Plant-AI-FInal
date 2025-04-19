import logging
from gemini_helper import get_chatbot_response as gemini_response
from openai_helper import get_chatbot_response as openai_response

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
    try:
        # First try using Gemini for the response
        logging.info(f"Requesting Gemini response for: {question[:50]}...")
        response = gemini_response(question, lang)
        logging.info("Successfully generated Gemini chatbot response")
        return response
        
    except Exception as e:
        logging.error(f"Error getting Gemini chatbot response: {str(e)}")
        
        # Fall back to OpenAI if Gemini fails
        try:
            logging.info(f"Falling back to OpenAI for chatbot response")
            response = openai_response(question, lang)
            logging.info("Successfully generated OpenAI fallback response")
            return response
            
        except Exception as e2:
            logging.error(f"Error with OpenAI fallback: {str(e2)}")
            
            # Fallback responses if both APIs fail
            fallbacks = {
                'en': "I'm having trouble connecting right now. Please try again later.",
                'hi': "मुझे अभी कनेक्ट करने में परेशानी हो रही है। कृपया बाद में पुनः प्रयास करें।",
                'ta': "இப்போது இணைக்க எனக்கு சிரமம். தயவுசெய்து பின்னர் மீண்டும் முயற்சிக்கவும்.",
                'te': "ప్రస్తుతం కనెక్ట్ చేయడంలో నాకు సమస్య ఉంది. దయచేసి తర్వాత మళ్లీ ప్రయత్నించండి.",
                'bn': "আমি এখন সংযোগ করতে সমস্যা হচ্ছে। অনুগ্রহ করে পরে আবার চেষ্টা করুন।",
                'gu': "મને હાલમાં કનેક્ટ કરવામાં મુશ્કેલી છે. કૃપા કરીને થોડા સમય પછી ફરી પ્રયાસ કરો."
            }
            
            return fallbacks.get(lang, fallbacks['en'])