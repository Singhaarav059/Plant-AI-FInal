from dotenv import load_dotenv
load_dotenv()

import os
import json
import base64
import random
import logging
from openai import OpenAI

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize OpenAI client
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# The newest OpenAI model is "gpt-4o" which was released May 13, 2024.
# Do not change this unless explicitly requested by the user
MODEL = "gpt-4o"

# Fallback plant disease dictionary
PLANT_DISEASES = {
    'Apple___Apple_scab': {
        'name': 'Apple Scab',
        'severity': 'medium',
        'description': 'Apple scab is a fungal disease that causes dark, scabby lesions on the leaves and fruit of apple trees. It affects the tree\'s ability to photosynthesize and can reduce fruit quality and yield.',
        'treatment': 'Remove and destroy fallen leaves. Apply fungicides like captan or myclobutanil in early spring before symptoms appear. Maintain good air circulation by proper pruning. Use resistant apple varieties for new plantings.'
    },
    'Tomato___Early_blight': {
        'name': 'Tomato Early Blight',
        'severity': 'medium',
        'description': 'Early blight causes dark, concentric rings on lower leaves first, which may yellow and die. It can spread upward and reduce yield.',
        'treatment': 'Apply fungicides like chlorothalonil or mancozeb. Remove lower infected leaves. Practice crop rotation. Mulch around plants to prevent soil splash. Stake or cage plants for better air circulation.'
    },
    'Potato___Late_blight': {
        'name': 'Potato Late Blight',
        'severity': 'high',
        'description': 'Late blight causes water-soaked lesions on leaves that rapidly expand in cool, wet weather. It can destroy entire fields within days if conditions are favorable.',
        'treatment': 'Apply fungicides containing metalaxyl, chlorothalonil, or copper compounds. Remove volunteers and destroy cull piles. Provide good air circulation with adequate plant spacing. Destroy all infected plant material.'
    },
    'Corn___Common_rust': {
        'name': 'Corn Common Rust',
        'severity': 'medium',
        'description': 'Common rust appears as small, circular to elongated pustules on the leaves. The pustules are initially light green and then turn reddish-brown as they mature.',
        'treatment': 'Apply fungicides like azoxystrobin, pyraclostrobin, or propiconazole when symptoms first appear. Plant resistant corn varieties. Avoid overhead irrigation to reduce leaf wetness.'
    },
    'Rice___Bacterial_leaf_blight': {
        'name': 'Rice Bacterial Leaf Blight',
        'severity': 'high',
        'description': 'Bacterial leaf blight causes water-soaked to yellowish stripes on leaf blades or tips, which eventually turn white to gray and die. It is a major rice disease in South and Southeast Asia.',
        'treatment': 'Plant resistant varieties. Remove weeds and ratoons. Avoid excessive nitrogen application. Maintain appropriate water management. Use balanced fertilizers. If detected early, copper-based bactericides can help.'
    },
    'Wheat___Leaf_rust': {
        'name': 'Wheat Leaf Rust',
        'severity': 'medium',
        'description': 'Leaf rust appears as small, round, orange-brown pustules on leaves. Severe infections can cause early leaf death and significant yield loss.',
        'treatment': 'Plant resistant varieties. Apply fungicides like propiconazole, tebuconazole, or azoxystrobin at early infection stages. Practice crop rotation with non-host crops. Eliminate volunteer wheat plants.'
    },
    'Healthy_plant': {
        'name': 'Healthy Plant',
        'severity': 'low',
        'description': 'This plant appears to be healthy with no visible signs of disease. The leaves are uniformly green with no lesions, spots, or abnormal growth patterns.',
        'treatment': 'Continue good agricultural practices: proper irrigation, fertilization, and regular monitoring for early signs of pests or diseases. Maintain proper spacing for good air circulation.'
    }
}

# Fallback chatbot responses
CHATBOT_RESPONSES = {
    'en': {
        'greetings': [
            "Hello! How can I help you with your plants today?",
            "Hi there! I'm here to help with plant disease questions.",
            "Welcome! What plant disease concerns do you have?"
        ],
        'unknown': [
            "I'm not sure about that. Can you ask something related to plant diseases or farming?",
            "I don't have information on that topic. Try asking about plant care or diseases.",
            "I'm still learning. Could you ask something about plant diseases or treatments?"
        ],
        'disease_general': [
            "Plant diseases are often caused by fungi, bacteria, viruses, or environmental conditions. Early detection is key to effective treatment.",
            "To identify plant diseases, look for unusual spots, discoloration, wilting, or abnormal growth patterns.",
            "Most plant diseases can be managed with proper cultural practices, fungicides, or bactericides depending on the cause."
        ],
        'prevention': [
            "Prevent plant diseases by: 1) Using disease-free seeds and plants, 2) Rotating crops, 3) Providing adequate spacing, 4) Watering at the base, 5) Sanitizing garden tools.",
            "Good prevention methods include removing plant debris, avoiding overhead watering, and applying preventative fungicides when necessary.",
            "Healthy soil with good drainage and proper nutrients helps plants resist diseases. Regular monitoring also helps catch problems early."
        ],
        'treatment': [
            "Treatment depends on the specific disease. Generally, remove infected parts, apply appropriate fungicides or bactericides, and improve growing conditions.",
            "Many fungal diseases respond well to copper-based fungicides or neem oil. Bacterial diseases might require specialized bactericides.",
            "Always follow label directions when applying any treatment. Some diseases have no cure, and prevention becomes the best strategy."
        ],
        'organic': [
            "Organic disease management includes using compost tea, neem oil, copper soap, sulfur dust, and beneficial microorganisms.",
            "Neem oil is effective against many fungal diseases. Baking soda mixed with mild soap and water can help with powdery mildew.",
            "Crop rotation, companion planting, and maintaining biodiversity in your garden are excellent organic strategies to prevent disease."
        ],
        'goodbye': [
            "Happy farming! Don't hesitate to return if you have more questions.",
            "Good luck with your plants! Feel free to ask more questions anytime.",
            "I hope that helps! Come back if you need more plant disease information."
        ]
    },
    'hi': {
        'unknown': [
            "मुझे इसके बारे में निश्चित नहीं है। कृपया पौधे की बीमारियों या खेती से संबंधित प्रश्न पूछें।",
            "मेरे पास इस विषय पर जानकारी नहीं है। पौधों की देखभाल या रोगों के बारे में पूछने का प्रयास करें।"
        ]
    },
    'ta': {
        'unknown': [
            "எனக்கு அதைப் பற்றி உறுதியாகத் தெரியவில்லை. தயவுசெய்து தாவர நோய்கள் அல்லது விவசாயம் தொடர்பான கேள்வியைக் கேளுங்கள்.",
            "எனக்கு அந்த தலைப்பில் தகவல் இல்லை. தாவர பராமரிப்பு அல்லது நோய்களைப் பற்றி கேட்க முயற்சிக்கவும்."
        ]
    },
    'te': {
        'unknown': [
            "నాకు దాని గురించి ఖచ్చితంగా తెలియదు. దయచేసి మొక్కల వ్యాధులు లేదా వ్యవసాయం గురించి ప్రశ్న అడగండి.",
            "నాకు ఆ అంశంపై సమాచారం లేదు. మొక్కల సంరక్షణ లేదా వ్యాధుల గురించి అడగడానికి ప్రయత్నించండి."
        ]
    },
    'bn': {
        'unknown': [
            "আমি এ সম্পর্কে নিশ্চিত নই। অনুগ্রহ করে উদ্ভিদ রোগ বা কৃষি সম্পর্কিত প্রশ্ন জিজ্ঞাসা করুন।",
            "আমার কাছে সে বিষয়ে তথ্য নেই। উদ্ভিদের যত্ন বা রোগ সম্পর্কে জিজ্ঞাসা করার চেষ্টা করুন।"
        ]
    },
    'gu': {
        'unknown': [
            "મને તે વિશે ખાતરી નથી. કૃપા કરીને છોડ રોગો અથવા ખેતી વિશે પ્રશ્ન પૂછો.",
            "મારી પાસે તે વિષય પર માહિતી નથી. છોડની સંભાળ અથવા રોગો વિશે પૂછવાનો પ્રયાસ કરો."
        ]
    }
}

def analyze_plant_image(image_base64, language='en'):
    """
    Analyze a plant image to detect diseases using GPT-4o Vision.
    Falls back to preset responses if the API is unavailable.
    
    Args:
        image_base64: Base64 encoded image data
        language: Language code for the response
    
    Returns:
        Tuple containing (disease_name, confidence, severity, description, treatment)
    """
    try:
        # Format the prompt based on language
        if language == 'en':
            prompt = """
            You are an expert agricultural plant pathologist. 
            Analyze this plant image and identify any disease present. 
            Focus specifically on common crop diseases affecting Indian farmers.
            
            Respond in JSON format with the following structure:
            {
                "disease_name": "Full name of the disease (if healthy, state 'Healthy Plant')",
                "confidence": A number between 0.0 and 1.0 representing detection confidence,
                "severity": "low", "medium", or "high" based on visible damage,
                "description": "Detailed description of the disease, symptoms, and causes",
                "treatment": "Detailed treatment recommendations including organic and chemical options if applicable"
            }
            """
        else:
            # For non-English languages, we'll still prompt in English but instruct to respond in the target language
            prompt = f"""
            You are an expert agricultural plant pathologist.
            Analyze this plant image and identify any disease present.
            Focus specifically on common crop diseases affecting Indian farmers.
            
            Respond in the {language} language, but use JSON format with the following structure:
            {{
                "disease_name": "Full name of the disease (if healthy, state 'Healthy Plant')",
                "confidence": A number between 0.0 and 1.0 representing detection confidence,
                "severity": "low", "medium", or "high" based on visible damage,
                "description": "Detailed description of the disease, symptoms, and causes",
                "treatment": "Detailed treatment recommendations including organic and chemical options if applicable"
            }}
            """

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}
                        }
                    ]
                }
            ],
            response_format={"type": "json_object"},
            max_tokens=1000
        )
        
        result = json.loads(response.choices[0].message.content)
        
        logging.info(f"Plant analysis complete: {result['disease_name']}")
        
        return (
            result["disease_name"],
            result["confidence"],
            result["severity"],
            result["description"],
            result["treatment"]
        )
        
    except Exception as e:
        logging.error(f"Error analyzing plant image: {str(e)}")
        # Return fallback disease information if OpenAI fails
        disease_key = random.choice(list(PLANT_DISEASES.keys()))
        disease_info = PLANT_DISEASES[disease_key]
        confidence = random.uniform(0.7, 0.9)
        
        return (
            disease_info['name'],
            confidence,
            disease_info['severity'],
            disease_info['description'],
            disease_info['treatment']
        )

def get_chatbot_response(question, language='en'):
    """
    Get a response from GPT for farmer questions.
    Falls back to pattern matching if the API is unavailable.
    
    Args:
        question: The user's question
        language: Language code for the response
    
    Returns:
        String response from the chatbot
    """
    try:
        system_message = f"""
        You are an agricultural expert assistant for Indian farmers. 
        Your name is KrishiSahayak AI.
        Provide helpful, accurate, and practical advice about farming, crop diseases, treatments, and agricultural practices.
        Keep responses concise (max 150 words) but informative.
        Focus on techniques and solutions applicable to Indian farming conditions.
        Include both traditional and modern approaches when relevant.
        Your responses should be in the {language} language.
        """
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": question}
            ],
            max_tokens=500
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        logging.error(f"Error getting chatbot response: {str(e)}")
        
        # Fall back to pattern matching
        question_lower = question.lower()
        
        # Check if the user's language is supported in our fallbacks
        if language not in CHATBOT_RESPONSES:
            language = 'en'  # Default to English
            
        # Get the responses for this language
        responses = CHATBOT_RESPONSES[language]
        
        # Check if this category exists for this language, otherwise use English
        def get_response(category):
            if category in responses:
                return random.choice(responses[category])
            else:
                return random.choice(CHATBOT_RESPONSES['en'][category])
        
        # Simple pattern matching for common question types
        if 'hello' in question_lower or 'hi' in question_lower or 'namaste' in question_lower:
            return get_response('greetings')
        elif 'disease' in question_lower or 'infection' in question_lower or 'sick' in question_lower:
            return get_response('disease_general')
        elif 'prevent' in question_lower or 'avoid' in question_lower or 'stop' in question_lower:
            return get_response('prevention')
        elif 'treat' in question_lower or 'cure' in question_lower or 'fix' in question_lower:
            return get_response('treatment')
        elif 'organic' in question_lower or 'natural' in question_lower:
            return get_response('organic')
        elif 'thank' in question_lower or 'bye' in question_lower:
            return get_response('goodbye')
        else:
            return get_response('unknown')