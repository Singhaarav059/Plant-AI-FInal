import os
import json
import base64
import logging
import google.generativeai as genai
from PIL import Image
import io

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Gemini
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Models - using latest Gemini model names
TEXT_MODEL = "gemini-1.5-flash"  # For text-based chatbot interactions
VISION_MODEL = "gemini-1.5-flash"  # For image and text analysis (unified model)

def analyze_plant_image(image_base64, language='en'):
    """
    Analyze a plant image to detect diseases using Gemini Pro Vision.
    
    Args:
        image_base64: Base64 encoded image data
        language: Language code for the response
    
    Returns:
        Tuple containing (disease_name, confidence, severity, description, treatment)
    """
    try:
        # Decode base64 image
        image_data = base64.b64decode(image_base64)
        image = Image.open(io.BytesIO(image_data))
        
        # Create Gemini model instance
        model = genai.GenerativeModel(VISION_MODEL)
        
        # Map language codes to specific prompts in each language
        language_prompts = {
            'en': {
                'instruction': "You are an expert agricultural plant pathologist with specialization in Indian crop diseases. Analyze this plant image and identify any disease present.",
                'response_lang': "English",
                'json_example': """
                {
                    "disease_name": "Full name of the disease (if healthy, state 'Healthy Plant')",
                    "confidence": 0.85,
                    "severity": "medium",
                    "description": "Detailed description of the disease, symptoms, and causes",
                    "treatment": "Detailed treatment recommendations including organic and chemical options"
                }
                """
            },
            'hi': {
                'instruction': "आप भारतीय फसल रोगों में विशेषज्ञता वाले एक विशेषज्ञ कृषि पौध रोगविज्ञानी हैं। इस पौधे की छवि का विश्लेषण करें और मौजूद किसी भी बीमारी की पहचान करें।",
                'response_lang': "हिंदी",
                'json_example': """
                {
                    "disease_name": "रोग का पूरा नाम (यदि स्वस्थ है, तो 'स्वस्थ पौधा' लिखें)",
                    "confidence": 0.85,
                    "severity": "medium",
                    "description": "रोग का विस्तृत विवरण, लक्षण और कारण",
                    "treatment": "जैविक और रासायनिक विकल्पों सहित विस्तृत उपचार सिफारिशें"
                }
                """
            },
            'ta': {
                'instruction': "நீங்கள் இந்திய பயிர் நோய்களில் நிபுணத்துவம் பெற்ற ஒரு நிபுணர் விவசாய தாவர நோயியல் நிபுணர். இந்த தாவர படத்தை ஆராய்ந்து, ஏதேனும் நோய் இருந்தால் அடையாளம் காணவும்.",
                'response_lang': "தமிழ்",
                'json_example': """
                {
                    "disease_name": "நோயின் முழு பெயர் (ஆரோக்கியமாக இருந்தால், 'ஆரோக்கியமான தாவரம்' என குறிப்பிடவும்)",
                    "confidence": 0.85,
                    "severity": "medium",
                    "description": "நோய் பற்றிய விரிவான விளக்கம், அறிகுறிகள் மற்றும் காரணங்கள்",
                    "treatment": "ஆர்கானிக் மற்றும் இரசாயன விருப்பங்கள் உட்பட விரிவான சிகிச்சை பரிந்துரைகள்"
                }
                """
            },
            'te': {
                'instruction': "మీరు భారతీయ పంట వ్యాధులలో ప్రత్యేకత కలిగిన నిపుణ వ్యవసాయ మొక్క వ్యాధి నిపుణులు. ఈ మొక్క చిత్రాన్ని విశ్లేషించి, ఏదైనా వ్యాధి ఉంటే గుర్తించండి.",
                'response_lang': "తెలుగు",
                'json_example': """
                {
                    "disease_name": "వ్యాధి పూర్తి పేరు (ఆరోగ్యంగా ఉంటే, 'ఆరోగ్యకరమైన మొక్క' అని పేర్కొనండి)",
                    "confidence": 0.85,
                    "severity": "medium",
                    "description": "వ్యాధి గురించి వివరణాత్మక వివరణ, లక్షణాలు మరియు కారణాలు",
                    "treatment": "ఆర్గానిక్ మరియు రసాయన ఎంపికలతో సహా వివరణాత్మక చికిత్స సిఫార్సులు"
                }
                """
            },
            'bn': {
                'instruction': "আপনি ভারতীয় ফসলের রোগে বিশেষজ্ঞতা সহ একজন বিশেষজ্ঞ কৃষি উদ্ভিদ রোগবিদ। এই উদ্ভিদের ছবিটি বিশ্লেষণ করুন এবং কোনও রোগ উপস্থিত থাকলে সনাক্ত করুন।",
                'response_lang': "বাংলা",
                'json_example': """
                {
                    "disease_name": "রোগের পূর্ণ নাম (যদি সুস্থ হয়, তবে 'সুস্থ উদ্ভিদ' লিখুন)",
                    "confidence": 0.85,
                    "severity": "medium",
                    "description": "রোগের বিস্তারিত বিবরণ, লক্ষণ এবং কারণ",
                    "treatment": "জৈব এবং রাসায়নিক বিকল্প সহ বিস্তারিত চিকিৎসার সুপারিশ"
                }
                """
            },
            'gu': {
                'instruction': "તમે ભારતીય પાક રોગોમાં વિશેષતા ધરાવતા નિષ્ણાત કૃષિ વનસ્પતિ રોગશાસ્ત્રી છો. આ છોડની છબીનું વિશ્લેષણ કરો અને જો કોઈ રોગ હાજર હોય તો ઓળખો.",
                'response_lang': "ગુજરાતી",
                'json_example': """
                {
                    "disease_name": "રોગનું પૂરું નામ (જો સ્વસ્થ હોય, તો 'સ્વસ્થ છોડ' લખો)",
                    "confidence": 0.85,
                    "severity": "medium",
                    "description": "રોગનું વિગતવાર વર્ણન, લક્ષણો અને કારણો",
                    "treatment": "ઓર્ગેનિક અને રાસાયણિક વિકલ્પો સહિત વિગતવાર સારવારની ભલામણો"
                }
                """
            }
        }
        
        # Use the language-specific prompts or default to English if not found
        prompts = language_prompts.get(language, language_prompts['en'])
        
        # Format prompt with language-specific instructions
        prompt = f"""
        {prompts['instruction']}
        
        IMPORTANT RULES:
        1. Respond ONLY in valid JSON format (no explanations outside the JSON)
        2. The JSON must have exactly these fields: "disease_name", "confidence", "severity", "description", "treatment"
        3. Confidence must be a number between 0.0 and 1.0
        4. Severity must be exactly one of: "low", "medium", or "high"
        5. Focus on diseases common in Indian agriculture
        6. Your entire response must be in {prompts['response_lang']} language
        
        JSON FORMAT:
        {prompts['json_example']}
        """
        
        # Configure safety settings to allow content generation
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        
        # Generate response with safety settings
        response = model.generate_content(
            contents=[prompt, image],
            safety_settings=safety_settings
        )
        
        # Process the response
        response_text = response.text
        
        # Extract JSON content from the response, handling potential code blocks in markdown
        if "```json" in response_text:
            json_text = response_text.split("```json")[1].split("```")[0].strip()
        elif "```" in response_text:
            json_text = response_text.split("```")[1].split("```")[0].strip()
        else:
            json_text = response_text.strip()
            
        # Parse the JSON result
        result = json.loads(json_text)
        
        logging.info(f"Plant analysis complete: {result['disease_name']}")
        
        return (
            result["disease_name"],
            result["confidence"],
            result["severity"],
            result["description"],
            result["treatment"]
        )
        
    except Exception as e:
        logging.error(f"Error analyzing plant image with Gemini: {str(e)}")
        # Return default values in case of error
        return (
            "Unknown Disease",
            0.5,
            "medium",
            "Could not analyze the image properly. Please try again with a clearer image.",
            "Consider consulting with a local agricultural extension office for in-person diagnosis."
        )

def get_chatbot_response(question, language='en'):
    """
    Get a response from Gemini for farmer questions.
    
    Args:
        question: The user's question
        language: Language code for the response
    
    Returns:
        String response from the chatbot
    """
    try:
        # Create Gemini model instance
        model = genai.GenerativeModel(TEXT_MODEL)
        
        # Map language codes to specific prompts in each language
        language_prompts = {
            'en': {
                'system': "You are KrishiSahayak AI, an agricultural expert for Indian farmers. Provide helpful advice about farming, crops, diseases, and agricultural practices. Keep responses informative but concise.",
                'question_prefix': "Question:",
                'answer_prefix': "Answer (in English):"
            },
            'hi': {
                'system': "आप कृषिसहायक AI हैं, भारतीय किसानों के लिए एक कृषि विशेषज्ञ। खेती, फसलों, बीमारियों और कृषि प्रथाओं के बारे में उपयोगी सलाह प्रदान करें। जवाब जानकारीपूर्ण लेकिन संक्षिप्त रखें।",
                'question_prefix': "प्रश्न:",
                'answer_prefix': "उत्तर (हिंदी में):"
            },
            'ta': {
                'system': "நீங்கள் கிருஷிசஹாயக் AI, இந்திய விவசாயிகளுக்கான வேளாண் நிபுணர். விவசாயம், பயிர்கள், நோய்கள் மற்றும் வேளாண் நடைமுறைகள் பற்றிய பயனுள்ள ஆலோசனையை வழங்குங்கள். பதில்களை தகவல் நிறைந்ததாகவும் சுருக்கமாகவும் வைத்திருங்கள்.",
                'question_prefix': "கேள்வி:",
                'answer_prefix': "பதில் (தமிழில்):"
            },
            'te': {
                'system': "మీరు కృషిసహాయక్ AI, భారతీయ రైతులకు వ్యవసాయ నిపుణులు. వ్యవసాయం, పంటలు, వ్యాధులు మరియు వ్యవసాయ పద్ధతుల గురించి సహాయకరమైన సలహాలు అందించండి. సమాధానాలను సమాచారాత్మకంగా కానీ సంక్షిప్తంగా ఉంచండి.",
                'question_prefix': "ప్రశ్న:",
                'answer_prefix': "సమాధానం (తెలుగులో):"
            },
            'bn': {
                'system': "আপনি কৃষিসহায়ক AI, ভারতীয় কৃষকদের জন্য একজন কৃষি বিশেষজ্ঞ। কৃষি, ফসল, রোগ এবং কৃষি পদ্ধতি সম্পর্কে সহায়ক পরামর্শ প্রদান করুন। উত্তরগুলি তথ্যপূর্ণ কিন্তু সংক্ষিপ্ত রাখুন।",
                'question_prefix': "প্রশ্ন:",
                'answer_prefix': "উত্তর (বাংলায়):"
            },
            'gu': {
                'system': "તમે કૃષિસહાયક AI છો, ભારતીય ખેડૂતો માટે કૃષિ નિષ્ણાત. ખેતી, પાકો, રોગો અને કૃષિ પદ્ધતિઓ વિશે ઉપયોગી સલાહ આપો. જવાબો માહિતીપ્રદ પરંતુ સંક્ષિપ્ત રાખો.",
                'question_prefix': "પ્રશ્ન:",
                'answer_prefix': "જવાબ (ગુજરાતીમાં):"
            }
        }
        
        # Use the language-specific prompts or default to English if not found
        prompts = language_prompts.get(language, language_prompts['en'])
        
        # Create a combined prompt in the target language
        combined_prompt = f"""{prompts['system']}

{prompts['question_prefix']} {question}

{prompts['answer_prefix']}"""
        
        # Configure safety settings to allow more flexible content
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            }
        ]
        
        # Generate response with safety settings
        response = model.generate_content(
            contents=combined_prompt,
            safety_settings=safety_settings
        )
        
        return response.text
        
    except Exception as e:
        logging.error(f"Error getting chatbot response from Gemini: {str(e)}")
        
        # Default responses for different languages
        default_responses = {
            'en': "I'm sorry, I couldn't process your question at the moment. Please try again later.",
            'hi': "मुझे खेद है, मैं अभी आपके प्रश्न को संसाधित नहीं कर सका। कृपया बाद में पुनः प्रयास करें।",
            'ta': "மன்னிக்கவும், இப்போது உங்கள் கேள்வியை செயலாக்க முடியவில்லை. தயவுசெய்து பின்னர் மீண்டும் முயற்சிக்கவும்.",
            'te': "క్షమించండి, నేను ప్రస్తుతం మీ ప్రశ్నను ప్రాసెస్ చేయలేకపోయాను. దయచేసి తర్వాత మళ్లీ ప్రయత్నించండి.",
            'bn': "দুঃখিত, আমি এই মুহূর্তে আপনার প্রশ্ন প্রক্রিয়া করতে পারিনি। অনুগ্রহ করে পরে আবার চেষ্টা করুন।",
            'gu': "માફ કરશો, હું અત્યારે તમારા પ્રશ્નની પ્રક્રિયા કરી શક્યો નથી. કૃપા કરીને પછીથી ફરી પ્રયાસ કરો."
        }
        
        return default_responses.get(language, default_responses['en'])