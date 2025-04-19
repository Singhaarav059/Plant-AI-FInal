def get_translations(lang):
    """Return translations for the specified language"""
    
    # English translations (default)
    english = {
        # Common elements
        'site_name': 'KrishiSahayak',
        'site_description': 'Plant Disease Detection & Treatment for Indian Farmers',
        'language': 'Language',
        'home': 'Home',
        'forum': 'Community Forum',
        'login': 'Login',
        'register': 'Register',
        'logout': 'Logout',
        'history': 'My History',
        
        # Error and info messages
        'no_file_selected': 'No file selected.',
        'error_processing': 'Error processing the image. Please try again.',
        'invalid_file_type': 'Invalid file type. Please upload JPG, JPEG or PNG.',
        'user_exists': 'Username or email already exists.',
        'registration_success': 'Registration successful! Please login.',
        'registration_error': 'Error during registration. Please try again.',
        'login_success': 'Login successful!',
        'invalid_credentials': 'Invalid username or password.',
        'login_required': 'Please login to access this feature.',
        'incomplete_fields': 'Please fill in all required fields.',
        'post_created': 'Post created successfully!',
        'empty_comment': 'Comment cannot be empty.',
        'comment_added': 'Comment added successfully!',
        'empty_question': 'Please enter a question.',
        
        # Home page
        'welcome_message': 'Welcome to KrishiSahayak, your plant health assistant',
        'subtitle': 'Upload a photo of your plant and get instant disease diagnosis and treatment advice',
        'upload_instruction': 'Take a clear photo of the affected plant part (leaf, stem, fruit) in good lighting',
        'upload_button': 'Upload Photo',
        'try_another': 'Try Another Photo',
        'features_heading': 'How KrishiSahayak Helps You',
        'feature_1_title': 'Disease Detection',
        'feature_1_desc': 'Instantly identify plant diseases from photos of your crops',
        'feature_2_title': 'Treatment Advice',
        'feature_2_desc': 'Get recommended treatments, including organic and chemical options',
        'feature_3_title': 'Farmer Community',
        'feature_3_desc': 'Connect with other farmers to share knowledge and get help',
        'feature_4_title': 'Disease Information',
        'feature_4_desc': 'Learn about common plant diseases, their causes and prevention',
        'ask_expert': 'Ask Our Expert',
        'ask_placeholder': 'Type your farming or plant disease question here...',
        'ask_button': 'Ask Question',
        
        # Disease result page
        'disease_detected': 'Detect Disease',
        'confidence': 'Confidence',
        'severity': 'Severity',
        'severity_low': 'Low',
        'severity_medium': 'Medium',
        'severity_high': 'High',
        'description': 'Description',
        'treatment': 'Treatment',
        'save_results': 'Save Results',
        
        # Forum page
        'forum_title': 'Farmer Community Forum',
        'forum_subtitle': 'Connect with other farmers, share experiences, and find solutions',
        'new_post': 'Create New Post',
        'post_title': 'Post Title',
        'post_content': 'Post Content',
        'submit_post': 'Submit Post',
        'recent_discussions': 'Recent Discussions',
        'posted_by': 'Posted by',
        'post_comment': 'Add Comment',
        'comment_placeholder': 'Write your comment here...',
        'submit_comment': 'Submit Comment',
        'view_comments': 'View Comments',
        'no_comments': 'No comments yet. Be the first to comment!',
        'no_posts': 'No posts yet. Start a new discussion!',
        
        # Login/Register pages
        'username': 'Username',
        'email': 'Email',
        'password': 'Password',
        'confirm_password': 'Confirm Password',
        'have_account': 'Already have an account?',
        'need_account': 'Need an account?',
        
        # History page
        'history_title': 'My Disease Detection History',
        'history_subtitle': 'View your past plant disease detections',
        'detection_date': 'Detection Date',
        'no_history': 'No detection history found. Upload a plant image to get started!',
        
        # Chatbot
        'chatbot_title': 'Plant Health Expert',
        'chatbot_greeting': 'Hello! I\'m your plant health assistant. Ask me anything about plant diseases or farming practices.',
        'chatbot_placeholder': 'Type your question here...',
        'send': 'Send',
    }
    
    # Hindi translations
    hindi = {
        # Common elements
        'site_name': 'कृषिसहायक',
        'site_description': 'भारतीय किसानों के लिए पौधों के रोगों की पहचान और उपचार',
        'language': 'भाषा',
        'home': 'होम',
        'forum': 'किसान मंच',
        'login': 'लॉग इन',
        'register': 'रजिस्टर',
        'logout': 'लॉग आउट',
        'history': 'मेरा इतिहास',
        
        # Error and info messages
        'no_file_selected': 'कोई फ़ाइल चयनित नहीं है।',
        'error_processing': 'छवि को संसाधित करने में त्रुटि। कृपया पुन: प्रयास करें।',
        'invalid_file_type': 'अमान्य फ़ाइल प्रकार। कृपया JPG, JPEG या PNG अपलोड करें।',
        'user_exists': 'उपयोगकर्ता नाम या ईमेल पहले से मौजूद है।',
        'registration_success': 'पंजीकरण सफल! कृपया लॉग इन करें।',
        'registration_error': 'पंजीकरण के दौरान त्रुटि। कृपया पुन: प्रयास करें।',
        'login_success': 'लॉगिन सफल!',
        'invalid_credentials': 'अमान्य उपयोगकर्ता नाम या पासवर्ड।',
        'login_required': 'इस सुविधा का उपयोग करने के लिए कृपया लॉगिन करें।',
        'incomplete_fields': 'कृपया सभी आवश्यक फ़ील्ड भरें।',
        'post_created': 'पोस्ट सफलतापूर्वक बनाई गई!',
        'empty_comment': 'टिप्पणी खाली नहीं हो सकती।',
        'comment_added': 'टिप्पणी सफलतापूर्वक जोड़ी गई!',
        'empty_question': 'कृपया एक प्रश्न दर्ज करें।',
        
        # Home page
        'welcome_message': 'कृषिसहायक में आपका स्वागत है, आपका पौधों का स्वास्थ्य सहायक',
        'subtitle': 'अपने पौधे की एक तस्वीर अपलोड करें और तुरंत रोग निदान और उपचार सलाह प्राप्त करें',
        'upload_instruction': 'प्रभावित पौधे के हिस्से (पत्ती, तना, फल) की अच्छी रोशनी में एक स्पष्ट तस्वीर लें',
        'upload_button': 'फोटो अपलोड करें',
        'try_another': 'दूसरी फोटो आज़माएं',
        'features_heading': 'कृषिसहायक आपकी कैसे मदद करता है',
        'feature_1_title': 'रोग पहचान',
        'feature_1_desc': 'अपनी फसलों की तस्वीरों से पौधों के रोगों की तुरंत पहचान करें',
        'feature_2_title': 'उपचार सलाह',
        'feature_2_desc': 'जैविक और रासायनिक विकल्पों सहित अनुशंसित उपचार प्राप्त करें',
        'feature_3_title': 'किसान समुदाय',
        'feature_3_desc': 'ज्ञान साझा करने और मदद प्राप्त करने के लिए अन्य किसानों से जुड़ें',
        'feature_4_title': 'रोग जानकारी',
        'feature_4_desc': 'सामान्य पौधों के रोगों, उनके कारणों और रोकथाम के बारे में जानें',
        'ask_expert': 'हमारे विशेषज्ञ से पूछें',
        'ask_placeholder': 'अपना खेती या पौधों के रोग से संबंधित प्रश्न यहां लिखें...',
        'ask_button': 'प्रश्न पूछें',
        
        # Disease result page
        'disease_detected': 'रोग का पता लगाएं',
        'confidence': 'विश्वास स्तर',
        'severity': 'गंभीरता',
        'severity_low': 'कम',
        'severity_medium': 'मध्यम',
        'severity_high': 'उच्च',
        'description': 'विवरण',
        'treatment': 'उपचार',
        'save_results': 'परिणाम सहेजें',
        
        # Forum page
        'forum_title': 'किसान समुदाय मंच',
        'forum_subtitle': 'अन्य किसानों से जुड़ें, अनुभव साझा करें और समाधान खोजें',
        'new_post': 'नई पोस्ट बनाएं',
        'post_title': 'पोस्ट का शीर्षक',
        'post_content': 'पोस्ट सामग्री',
        'submit_post': 'पोस्ट जमा करें',
        'recent_discussions': 'हाल की चर्चाएँ',
        'posted_by': 'पोस्ट किया गया',
        'post_comment': 'टिप्पणी जोड़ें',
        'comment_placeholder': 'अपनी टिप्पणी यहां लिखें...',
        'submit_comment': 'टिप्पणी जमा करें',
        'view_comments': 'टिप्पणियां देखें',
        'no_comments': 'अभी तक कोई टिप्पणी नहीं। टिप्पणी करने वाले पहले व्यक्ति बनें!',
        'no_posts': 'अभी तक कोई पोस्ट नहीं। एक नई चर्चा शुरू करें!',
        
        # Login/Register pages
        'username': 'उपयोगकर्ता नाम',
        'email': 'ईमेल',
        'password': 'पासवर्ड',
        'confirm_password': 'पासवर्ड की पुष्टि करें',
        'have_account': 'क्या आपके पास पहले से एक खाता है?',
        'need_account': 'खाते की आवश्यकता है?',
        
        # History page
        'history_title': 'मेरा रोग पहचान इतिहास',
        'history_subtitle': 'अपने पिछले पौधों के रोग पहचान देखें',
        'detection_date': 'पहचान की तारीख',
        'no_history': 'कोई पहचान इतिहास नहीं मिला। शुरू करने के लिए एक पौधे की छवि अपलोड करें!',
        
        # Chatbot
        'chatbot_title': 'पौधों के स्वास्थ्य विशेषज्ञ',
        'chatbot_greeting': 'नमस्ते! मैं आपका पौधों का स्वास्थ्य सहायक हूँ। पौधों के रोगों या खेती के तरीकों के बारे में कुछ भी पूछें।',
        'chatbot_placeholder': 'अपना प्रश्न यहां लिखें...',
        'send': 'भेजें',
    }
    
    # Tamil translations
    tamil = {
        # Common elements
        'site_name': 'கிருஷிசகாயக்',
        'site_description': 'இந்திய விவசாயிகளுக்கான தாவர நோய் கண்டறிதல் மற்றும் சிகிச்சை',
        'language': 'மொழி',
        'home': 'முகப்பு',
        'forum': 'விவசாயி சமூகம்',
        'login': 'உள்நுழைய',
        'register': 'பதிவு செய்ய',
        'logout': 'வெளியேறு',
        'history': 'எனது வரலாறு',
        
        # Error and info messages
        'no_file_selected': 'கோப்பு தேர்ந்தெடுக்கப்படவில்லை.',
        'error_processing': 'படத்தை செயலாக்குவதில் பிழை. மீண்டும் முயற்சிக்கவும்.',
        'invalid_file_type': 'தவறான கோப்பு வகை. JPG, JPEG அல்லது PNG ஐப் பதிவேற்றவும்.',
        'user_exists': 'பயனர்பெயர் அல்லது மின்னஞ்சல் ஏற்கனவே உள்ளது.',
        'registration_success': 'பதிவு வெற்றி! உள்நுழையவும்.',
        'registration_error': 'பதிவு செய்வதில் பிழை. மீண்டும் முயற்சிக்கவும்.',
        'login_success': 'உள்நுழைவு வெற்றி!',
        'invalid_credentials': 'தவறான பயனர்பெயர் அல்லது கடவுச்சொல்.',
        'login_required': 'இந்த அம்சத்தை அணுக உள்நுழையவும்.',
        'incomplete_fields': 'அனைத்து தேவையான புலங்களையும் நிரப்பவும்.',
        'post_created': 'இடுகை வெற்றிகரமாக உருவாக்கப்பட்டது!',
        'empty_comment': 'கருத்து காலியாக இருக்க முடியாது.',
        'comment_added': 'கருத்து வெற்றிகரமாக சேர்க்கப்பட்டது!',
        'empty_question': 'ஒரு கேள்வியை உள்ளிடவும்.',
        
        # Home page
        'welcome_message': 'கிருஷிசகாயக்கிற்கு வரவேற்கிறோம், உங்கள் தாவர ஆரோக்கிய உதவியாளர்',
        'subtitle': 'உங்கள் தாவரத்தின் புகைப்படத்தைப் பதிவேற்றி உடனடி நோய் கண்டறிதல் மற்றும் சிகிச்சை ஆலோசனையைப் பெறுங்கள்',
        'upload_instruction': 'பாதிக்கப்பட்ட தாவர பகுதியின் (இலை, தண்டு, பழம்) தெளிவான புகைப்படத்தை நல்ல ஒளியில் எடுக்கவும்',
        'upload_button': 'புகைப்படத்தைப் பதிவேற்றவும்',
        'try_another': 'மற்றொரு புகைப்படத்தை முயற்சிக்கவும்',
        'features_heading': 'கிருஷிசகாயக் உங்களுக்கு எவ்வாறு உதவுகிறது',
        'feature_1_title': 'நோய் கண்டறிதல்',
        'feature_1_desc': 'உங்கள் பயிர்களின் புகைப்படங்களிலிருந்து தாவர நோய்களை உடனடியாக அடையாளம் காணுங்கள்',
        'feature_2_title': 'சிகிச்சை ஆலோசனை',
        'feature_2_desc': 'இயற்கை மற்றும் இரசாயன விருப்பங்கள் உட்பட பரிந்துரைக்கப்பட்ட சிகிச்சைகளைப் பெறுங்கள்',
        'feature_3_title': 'விவசாயி சமூகம்',
        'feature_3_desc': 'அறிவைப் பகிர்ந்து கொள்ளவும் உதவி பெறவும் மற்ற விவசாயிகளுடன் இணைந்திடுங்கள்',
        'feature_4_title': 'நோய் தகவல்',
        'feature_4_desc': 'பொதுவான தாவர நோய்கள், அவற்றின் காரணங்கள் மற்றும் தடுப்பு பற்றி அறிந்து கொள்ளுங்கள்',
        'ask_expert': 'எங்கள் நிபுணரிடம் கேளுங்கள்',
        'ask_placeholder': 'உங்கள் விவசாயம் அல்லது தாவர நோய் பற்றிய கேள்வியை இங்கே தட்டச்சு செய்யவும்...',
        'ask_button': 'கேள்வி கேட்க',
        
        # Disease result page
        'disease_detected': 'நோய் கண்டறிய',
        'confidence': 'நம்பிக்கை அளவு',
        'severity': 'தீவிரம்',
        'severity_low': 'குறைவு',
        'severity_medium': 'நடுத்தரம்',
        'severity_high': 'அதிகம்',
        'description': 'விளக்கம்',
        'treatment': 'சிகிச்சை',
        'save_results': 'முடிவுகளை சேமிக்கவும்',
        
        # Forum page
        'forum_title': 'விவசாயி சமூக மன்றம்',
        'forum_subtitle': 'மற்ற விவசாயிகளுடன் இணைந்து, அனுபவங்களைப் பகிர்ந்து, தீர்வுகளைக் கண்டறியுங்கள்',
        'new_post': 'புதிய இடுகையை உருவாக்கவும்',
        'post_title': 'இடுகை தலைப்பு',
        'post_content': 'இடுகை உள்ளடக்கம்',
        'submit_post': 'இடுகையைச் சமர்ப்பிக்கவும்',
        'recent_discussions': 'சமீபத்திய விவாதங்கள்',
        'posted_by': 'பதிவிட்டவர்',
        'post_comment': 'கருத்து சேர்க்க',
        'comment_placeholder': 'உங்கள் கருத்தை இங்கே எழுதவும்...',
        'submit_comment': 'கருத்தை சமர்ப்பிக்கவும்',
        'view_comments': 'கருத்துகளைக் காண',
        'no_comments': 'இன்னும் கருத்துகள் இல்லை. கருத்து தெரிவிக்கும் முதல் நபராக இருங்கள்!',
        'no_posts': 'இன்னும் இடுகைகள் இல்லை. ஒரு புதிய விவாதத்தைத் தொடங்குங்கள்!',
        
        # Login/Register pages
        'username': 'பயனர்பெயர்',
        'email': 'மின்னஞ்சல்',
        'password': 'கடவுச்சொல்',
        'confirm_password': 'கடவுச்சொல்லை உறுதிப்படுத்தவும்',
        'have_account': 'ஏற்கனவே ஒரு கணக்கு உள்ளதா?',
        'need_account': 'கணக்கு தேவையா?',
        
        # History page
        'history_title': 'எனது நோய் கண்டறிதல் வரலாறு',
        'history_subtitle': 'உங்கள் கடந்த தாவர நோய் கண்டறிதல்களைக் காணுங்கள்',
        'detection_date': 'கண்டறிதல் தேதி',
        'no_history': 'கண்டறிதல் வரலாறு எதுவும் கிடைக்கவில்லை. தொடங்க ஒரு தாவர படத்தை பதிவேற்றவும்!',
        
        # Chatbot
        'chatbot_title': 'தாவர ஆரோக்கிய நிபுணர்',
        'chatbot_greeting': 'வணக்கம்! நான் உங்கள் தாவர ஆரோக்கிய உதவியாளர். தாவர நோய்கள் அல்லது விவசாய நடைமுறைகள் பற்றி எதையும் என்னிடம் கேளுங்கள்.',
        'chatbot_placeholder': 'உங்கள் கேள்வியை இங்கே தட்டச்சு செய்யவும்...',
        'send': 'அனுப்பு',
    }
    
    # Telugu translations
    telugu = {
        # Common elements
        'site_name': 'కృషిసహాయక్',
        'site_description': 'భారతీయ రైతుల కోసం మొక్క వ్యాధి గుర్తింపు మరియు చికిత్స',
        'language': 'భాష',
        'home': 'హోమ్',
        'forum': 'రైతు సమాజం',
        'login': 'లాగిన్',
        'register': 'నమోదు చేసుకోండి',
        'logout': 'లాగౌట్',
        'history': 'నా చరిత్ర',
        
        # Error and info messages
        'no_file_selected': 'ఫైల్ ఎంచుకోబడలేదు.',
        'error_processing': 'చిత్రాన్ని ప్రాసెస్ చేయడంలో లోపం. దయచేసి మళ్లీ ప్రయత్నించండి.',
        'invalid_file_type': 'చెల్లని ఫైల్ రకం. దయచేసి JPG, JPEG లేదా PNG అప్‌లోడ్ చేయండి.',
        'user_exists': 'వినియోగదారు పేరు లేదా ఇమెయిల్ ఇప్పటికే ఉంది.',
        'registration_success': 'నమోదు విజయవంతమైంది! దయచేసి లాగిన్ చేయండి.',
        'registration_error': 'నమోదు సమయంలో లోపం. దయచేసి మళ్లీ ప్రయత్నించండి.',
        'login_success': 'లాగిన్ విజయవంతమైంది!',
        'invalid_credentials': 'చెల్లని వినియోగదారు పేరు లేదా పాస్‌వర్డ్.',
        'login_required': 'ఈ ఫీచర్‌ను యాక్సెస్ చేయడానికి దయచేసి లాగిన్ చేయండి.',
        'incomplete_fields': 'దయచేసి అన్ని అవసరమైన ఫీల్డ్‌లను పూరించండి.',
        'post_created': 'పోస్ట్ విజయవంతంగా సృష్టించబడింది!',
        'empty_comment': 'వ్యాఖ్య ఖాళీగా ఉండకూడదు.',
        'comment_added': 'వ్యాఖ్య విజయవంతంగా జోడించబడింది!',
        'empty_question': 'దయచేసి ఒక ప్రశ్నను నమోదు చేయండి.',
        
        # Home page
        'welcome_message': 'కృషిసహాయక్‌కు స్వాగతం, మీ మొక్కల ఆరోగ్య సహాయకుడు',
        'subtitle': 'మీ మొక్క యొక్క ఫోటోను అప్‌లోడ్ చేసి తక్షణ వ్యాధి నిర్ధారణ మరియు చికిత్స సలహాను పొందండి',
        'upload_instruction': 'ప్రభావిత మొక్క భాగం (ఆకు, కాండం, పండు) యొక్క మంచి కాంతిలో స్పష్టమైన ఫోటోను తీయండి',
        'upload_button': 'ఫోటో అప్‌లోడ్ చేయండి',
        'try_another': 'మరొక ఫోటోను ప్రయత్నించండి',
        'features_heading': 'కృషిసహాయక్ మీకు ఎలా సహాయం చేస్తుంది',
        'feature_1_title': 'వ్యాధి గుర్తింపు',
        'feature_1_desc': 'మీ పంటల ఫోటోల నుండి మొక్కల వ్యాధులను వెంటనే గుర్తించండి',
        'feature_2_title': 'చికిత్స సలహా',
        'feature_2_desc': 'ఆర్గానిక్ మరియు రసాయనిక ఎంపికలతో సహా సిఫార్సు చేయబడిన చికిత్సలను పొందండి',
        'feature_3_title': 'రైతు సమాజం',
        'feature_3_desc': 'జ్ఞానాన్ని పంచుకోవడానికి మరియు సహాయం పొందడానికి ఇతర రైతులతో కనెక్ట్ అవ్వండి',
        'feature_4_title': 'వ్యాధి సమాచారం',
        'feature_4_desc': 'సాధారణ మొక్క వ్యాధుల గురించి, వాటి కారణాలు మరియు నివారణ గురించి తెలుసుకోండి',
        'ask_expert': 'మా నిపుణుడిని అడగండి',
        'ask_placeholder': 'మీ వ్యవసాయం లేదా మొక్క వ్యాధి ప్రశ్నను ఇక్కడ టైప్ చేయండి...',
        'ask_button': 'ప్రశ్న అడగండి',
        
        # Disease result page
        'disease_detected': 'వ్యాధిని గుర్తించండి',
        'confidence': 'నమ్మకం',
        'severity': 'తీవ్రత',
        'severity_low': 'తక్కువ',
        'severity_medium': 'మధ్యస్థం',
        'severity_high': 'ఎక్కువ',
        'description': 'వివరణ',
        'treatment': 'చికిత్స',
        'save_results': 'ఫలితాలను సేవ్ చేయండి',
        
        # Forum page
        'forum_title': 'రైతు సమాజ వేదిక',
        'forum_subtitle': 'ఇతర రైతులతో కనెక్ట్ అవ్వండి, అనుభవాలను పంచుకోండి మరియు పరిష్కారాలను కనుగొనండి',
        'new_post': 'కొత్త పోస్ట్ సృష్టించండి',
        'post_title': 'పోస్ట్ శీర్షిక',
        'post_content': 'పోస్ట్ కంటెంట్',
        'submit_post': 'పోస్ట్ సమర్పించండి',
        'recent_discussions': 'ఇటీవలి చర్చలు',
        'posted_by': 'పోస్ట్ చేసిన వారు',
        'post_comment': 'వ్యాఖ్య జోడించండి',
        'comment_placeholder': 'మీ వ్యాఖ్యను ఇక్కడ రాయండి...',
        'submit_comment': 'వ్యాఖ్యను సమర్పించండి',
        'view_comments': 'వ్యాఖ్యలను చూడండి',
        'no_comments': 'ఇంకా వ్యాఖ్యలు లేవు. వ్యాఖ్యానించే మొదటి వ్యక్తి అవ్వండి!',
        'no_posts': 'ఇంకా పోస్ట్‌లు లేవు. కొత్త చర్చను ప్రారంభించండి!',
        
        # Login/Register pages
        'username': 'వినియోగదారు పేరు',
        'email': 'ఇమెయిల్',
        'password': 'పాస్‌వర్డ్',
        'confirm_password': 'పాస్‌వర్డ్‌ని నిర్ధారించండి',
        'have_account': 'ఇప్పటికే ఖాతా ఉందా?',
        'need_account': 'ఖాతా అవసరమా?',
        
        # History page
        'history_title': 'నా వ్యాధి గుర్తింపు చరిత్ర',
        'history_subtitle': 'మీ గత మొక్క వ్యాధి గుర్తింపులను చూడండి',
        'detection_date': 'గుర్తింపు తేదీ',
        'no_history': 'గుర్తింపు చరిత్ర కనుగొనబడలేదు. ప్రారంభించడానికి మొక్క చిత్రాన్ని అప్‌లోడ్ చేయండి!',
        
        # Chatbot
        'chatbot_title': 'మొక్క ఆరోగ్య నిపుణుడు',
        'chatbot_greeting': 'హలో! నేను మీ మొక్క ఆరోగ్య సహాయకుడిని. మొక్కల వ్యాధులు లేదా వ్యవసాయ పద్ధతుల గురించి ఏదైనా అడగండి.',
        'chatbot_placeholder': 'మీ ప్రశ్నను ఇక్కడ టైప్ చేయండి...',
        'send': 'పంపు',
    }
    
    # Bengali translations
    bengali = {
        # Common elements
        'site_name': 'কৃষিসহায়ক',
        'site_description': 'ভারতীয় কৃষকদের জন্য উদ্ভিদের রোগ সনাক্তকরণ ও চিকিৎসা',
        'language': 'ভাষা',
        'home': 'হোম',
        'forum': 'কৃষক সম্প্রদায়',
        'login': 'লগইন',
        'register': 'নিবন্ধন',
        'logout': 'লগআউট',
        'history': 'আমার ইতিহাস',
        
        # Error and info messages
        'no_file_selected': 'কোন ফাইল নির্বাচিত হয়নি।',
        'error_processing': 'ছবি প্রক্রিয়াকরণে ত্রুটি। অনুগ্রহ করে আবার চেষ্টা করুন।',
        'invalid_file_type': 'অবৈধ ফাইল টাইপ। অনুগ্রহ করে JPG, JPEG বা PNG আপলোড করুন।',
        'user_exists': 'ব্যবহারকারীর নাম বা ইমেল ইতিমধ্যে বিদ্যমান।',
        'registration_success': 'নিবন্ধন সফল! অনুগ্রহ করে লগইন করুন।',
        'registration_error': 'নিবন্ধনের সময় ত্রুটি। অনুগ্রহ করে আবার চেষ্টা করুন।',
        'login_success': 'লগইন সফল!',
        'invalid_credentials': 'অবৈধ ব্যবহারকারীর নাম বা পাসওয়ার্ড।',
        'login_required': 'এই বৈশিষ্ট্য অ্যাক্সেস করতে অনুগ্রহ করে লগইন করুন।',
        'incomplete_fields': 'অনুগ্রহ করে সমস্ত প্রয়োজনীয় ক্ষেত্র পূরণ করুন।',
        'post_created': 'পোস্ট সফলভাবে তৈরি করা হয়েছে!',
        'empty_comment': 'মন্তব্য খালি হতে পারে না।',
        'comment_added': 'মন্তব্য সফলভাবে যোগ করা হয়েছে!',
        'empty_question': 'অনুগ্রহ করে একটি প্রশ্ন লিখুন।',
        
        # Home page
        'welcome_message': 'কৃষিসহায়কে স্বাগতম, আপনার উদ্ভিদ স্বাস্থ্য সহকারী',
        'subtitle': 'আপনার উদ্ভিদের একটি ছবি আপলোড করুন এবং তাৎক্ষণিক রোগ নির্ণয় এবং চিকিৎসা পরামর্শ পান',
        'upload_instruction': 'প্রভাবিত উদ্ভিদের অংশের (পাতা, কাণ্ড, ফল) একটি পরিষ্কার ছবি ভালো আলোতে তুলুন',
        'upload_button': 'ছবি আপলোড করুন',
        'try_another': 'অন্য ছবি চেষ্টা করুন',
        'features_heading': 'কৃষিসহায়ক কিভাবে আপনাকে সাহায্য করে',
        'feature_1_title': 'রোগ সনাক্তকরণ',
        'feature_1_desc': 'আপনার ফসলের ছবি থেকে তাৎক্ষণিকভাবে উদ্ভিদের রোগ সনাক্ত করুন',
        'feature_2_title': 'চিকিৎসা পরামর্শ',
        'feature_2_desc': 'জৈব এবং রাসায়নিক বিকল্প সহ সুপারিশকৃত চিকিৎসা পান',
        'feature_3_title': 'কৃষক সম্প্রদায়',
        'feature_3_desc': 'জ্ঞান ভাগ করে নিতে এবং সাহায্য পেতে অন্য কৃষকদের সাথে সংযোগ করুন',
        'feature_4_title': 'রোগ তথ্য',
        'feature_4_desc': 'সাধারণ উদ্ভিদের রোগ, তাদের কারণ এবং প্রতিরোধ সম্পর্কে জানুন',
        'ask_expert': 'আমাদের বিশেষজ্ঞকে জিজ্ঞাসা করুন',
        'ask_placeholder': 'আপনার কৃষি বা উদ্ভিদের রোগ সম্পর্কিত প্রশ্ন এখানে টাইপ করুন...',
        'ask_button': 'প্রশ্ন জিজ্ঞাসা করুন',
        
        # Disease result page
        'disease_detected': 'রোগ সনাক্ত করুন',
        'confidence': 'আত্মবিশ্বাস',
        'severity': 'তীব্রতা',
        'severity_low': 'কম',
        'severity_medium': 'মাঝারি',
        'severity_high': 'উচ্চ',
        'description': 'বিবরণ',
        'treatment': 'চিকিৎসা',
        'save_results': 'ফলাফল সংরক্ষণ করুন',
        
        # Forum page
        'forum_title': 'কৃষক সম্প্রদায় ফোরাম',
        'forum_subtitle': 'অন্য কৃষকদের সাথে সংযোগ করুন, অভিজ্ঞতা ভাগ করুন এবং সমাধান খুঁজুন',
        'new_post': 'নতুন পোস্ট তৈরি করুন',
        'post_title': 'পোস্টের শিরোনাম',
        'post_content': 'পোস্টের বিষয়বস্তু',
        'submit_post': 'পোস্ট জমা দিন',
        'recent_discussions': 'সাম্প্রতিক আলোচনা',
        'posted_by': 'পোস্ট করেছেন',
        'post_comment': 'মন্তব্য যোগ করুন',
        'comment_placeholder': 'আপনার মন্তব্য এখানে লিখুন...',
        'submit_comment': 'মন্তব্য জমা দিন',
        'view_comments': 'মন্তব্য দেখুন',
        'no_comments': 'এখনো কোন মন্তব্য নেই। প্রথম মন্তব্যকারী হোন!',
        'no_posts': 'এখনও কোন পোস্ট নেই। একটি নতুন আলোচনা শুরু করুন!',
        
        # Login/Register pages
        'username': 'ব্যবহারকারীর নাম',
        'email': 'ইমেল',
        'password': 'পাসওয়ার্ড',
        'confirm_password': 'পাসওয়ার্ড নিশ্চিত করুন',
        'have_account': 'ইতিমধ্যে একটি অ্যাকাউন্ট আছে?',
        'need_account': 'অ্যাকাউন্ট প্রয়োজন?',
        
        # History page
        'history_title': 'আমার রোগ সনাক্তকরণ ইতিহাস',
        'history_subtitle': 'আপনার অতীত উদ্ভিদের রোগ সনাক্তকরণ দেখুন',
        'detection_date': 'সনাক্তকরণ তারিখ',
        'no_history': 'কোন সনাক্তকরণ ইতিহাস পাওয়া যায়নি। শুরু করতে একটি উদ্ভিদের চিত্র আপলোড করুন!',
        
        # Chatbot
        'chatbot_title': 'উদ্ভিদ স্বাস্থ্য বিশেষজ্ঞ',
        'chatbot_greeting': 'হ্যালো! আমি আপনার উদ্ভিদ স্বাস্থ্য সহকারী। উদ্ভিদের রোগ বা কৃষি পদ্ধতি সম্পর্কে আমাকে যে কোনো কিছু জিজ্ঞাসা করুন।',
        'chatbot_placeholder': 'আপনার প্রশ্ন এখানে টাইপ করুন...',
        'send': 'পাঠান',
    }
    
    # Gujarati translations
    gujarati = {
        # Common elements
        'site_name': 'કૃષિસહાયક',
        'site_description': 'ભારતીય ખેડૂતો માટે છોડના રોગની ઓળખ અને સારવાર',
        'language': 'ભાષા',
        'home': 'હોમ',
        'forum': 'ખેડૂત સમુદાય',
        'login': 'લોગિન',
        'register': 'નોંધણી કરો',
        'logout': 'લોગઆઉટ',
        'history': 'મારો ઇતિહાસ',
        
        # Error and info messages
        'no_file_selected': 'કોઈ ફાઇલ પસંદ કરી નથી.',
        'error_processing': 'છબી પ્રક્રિયા કરવામાં ભૂલ. કૃપા કરી ફરી પ્રયાસ કરો.',
        'invalid_file_type': 'અમાન્ય ફાઇલ પ્રકાર. કૃપા કરીને JPG, JPEG અથવા PNG અપલોડ કરો.',
        'user_exists': 'વપરાશકર્તા નામ અથવા ઇમેઇલ પહેલેથી અસ્તિત્વમાં છે.',
        'registration_success': 'નોંધણી સફળ! કૃપા કરીને લોગિન કરો.',
        'registration_error': 'નોંધણી દરમિયાન ભૂલ. કૃપા કરી ફરી પ્રયાસ કરો.',
        'login_success': 'લોગિન સફળ!',
        'invalid_credentials': 'અમાન્ય વપરાશકર્તા નામ અથવા પાસવર્ડ.',
        'login_required': 'આ સુવિધાનો ઉપયોગ કરવા માટે કૃપા કરીને લોગિન કરો.',
        'incomplete_fields': 'કૃપા કરીને બધા જરૂરી ક્ષેત્રો ભરો.',
        'post_created': 'પોસ્ટ સફળતાપૂર્વક બનાવી!',
        'empty_comment': 'ટિપ્પણી ખાલી ન હોઈ શકે.',
        'comment_added': 'ટિપ્પણી સફળતાપૂર્વક ઉમેરાઈ!',
        'empty_question': 'કૃપા કરીને એક પ્રશ્ન દાખલ કરો.',
        
        # Home page
        'welcome_message': 'કૃષિસહાયકમાં આપનું સ્વાગત છે, તમારા છોડના આરોગ્ય સહાયક',
        'subtitle': 'તમારા છોડની એક ફોટો અપલોડ કરો અને તાત્કાલિક રોગ નિદાન અને સારવાર સલાહ મેળવો',
        'upload_instruction': 'અસરગ્રસ્ત છોડના ભાગ (પાંદડું, દાંડી, ફળ)ની સારા પ્રકાશમાં સ્પષ્ટ ફોટો લો',
        'upload_button': 'ફોટો અપલોડ કરો',
        'try_another': 'બીજી ફોટો પ્રયાસ કરો',
        'features_heading': 'કૃષિસહાયક તમને કેવી રીતે મદદ કરે છે',
        'feature_1_title': 'રોગ ઓળખ',
        'feature_1_desc': 'તમારા પાકોની ફોટો પરથી તરત જ છોડના રોગોને ઓળખો',
        'feature_2_title': 'સારવાર સલાહ',
        'feature_2_desc': 'જૈવિક અને રાસાયણિક વિકલ્પો સહિત ભલામણ કરેલી સારવારો મેળવો',
        'feature_3_title': 'ખેડૂત સમુદાય',
        'feature_3_desc': 'જ્ઞાન શેર કરવા અને મદદ મેળવવા માટે અન્ય ખેડૂતો સાથે જોડાઓ',
        'feature_4_title': 'રોગની માહિતી',
        'feature_4_desc': 'સામાન્ય છોડના રોગો, તેમના કારણો અને નિવારણ વિશે જાણો',
        'ask_expert': 'અમારા નિષ્ણાતને પૂછો',
        'ask_placeholder': 'તમારો ખેતી અથવા છોડના રોગનો પ્રશ્ન અહીં ટાઇપ કરો...',
        'ask_button': 'પ્રશ્ન પૂછો',
        
        # Disease result page
        'disease_detected': 'રોગ શોધો',
        'confidence': 'વિશ્વાસ',
        'severity': 'ગંભીરતા',
        'severity_low': 'ઓછી',
        'severity_medium': 'મધ્યમ',
        'severity_high': 'ઉચ્ચ',
        'description': 'વર્ણન',
        'treatment': 'સારવાર',
        'save_results': 'પરિણામો સાચવો',
        
        # Forum page
        'forum_title': 'ખેડૂત સમુદાય ફોરમ',
        'forum_subtitle': 'અન્ય ખેડૂતો સાથે જોડાઓ, અનુભવો શેર કરો અને ઉકેલો શોધો',
        'new_post': 'નવી પોસ્ટ બનાવો',
        'post_title': 'પોસ્ટ શીર્ષક',
        'post_content': 'પોસ્ટ સામગ્રી',
        'submit_post': 'પોસ્ટ સબમિટ કરો',
        'recent_discussions': 'તાજેતરની ચર્ચાઓ',
        'posted_by': 'દ્વારા પોસ્ટ કરાયેલ',
        'post_comment': 'ટિપ્પણી ઉમેરો',
        'comment_placeholder': 'તમારી ટિપ્પણી અહીં લખો...',
        'submit_comment': 'ટિપ્પણી સબમિટ કરો',
        'view_comments': 'ટિપ્પણીઓ જુઓ',
        'no_comments': 'હજી સુધી કોઈ ટિપ્પણી નથી. ટિપ્પણી કરનાર પ્રથમ વ્યક્તિ બનો!',
        'no_posts': 'હજી સુધી કોઈ પોસ્ટ નથી. નવી ચર્ચા શરૂ કરો!',
        
        # Login/Register pages
        'username': 'વપરાશકર્તા નામ',
        'email': 'ઇમેઇલ',
        'password': 'પાસવર્ડ',
        'confirm_password': 'પાસવર્ડની પુષ્ટિ કરો',
        'have_account': 'પહેલેથી જ એકાઉન્ટ છે?',
        'need_account': 'એકાઉન્ટની જરૂર છે?',
        
        # History page
        'history_title': 'મારો રોગ ઓળખ ઇતિહાસ',
        'history_subtitle': 'તમારા અગાઉના છોડના રોગ ઓળખ જુઓ',
        'detection_date': 'ઓળખની તારીખ',
        'no_history': 'કોઈ ઓળખ ઇતિહાસ મળ્યો નથી. શરૂ કરવા માટે છોડની છબી અપલોડ કરો!',
        
        # Chatbot
        'chatbot_title': 'છોડ આરોગ્ય નિષ્ણાત',
        'chatbot_greeting': 'હેલો! હું તમારો છોડ આરોગ્ય સહાયક છું. છોડના રોગો અથવા ખેતી પદ્ધતિઓ વિશે મને કંઈપણ પૂછો.',
        'chatbot_placeholder': 'તમારો પ્રશ્ન અહીં ટાઇપ કરો...',
        'send': 'મોકલો',
    }
    
    # Return the appropriate translations for the requested language
    if lang == 'hi':
        return hindi
    elif lang == 'ta':
        return tamil
    elif lang == 'te':
        return telugu
    elif lang == 'bn':
        return bengali
    elif lang == 'gu':
        return gujarati
    else:
        return english  # Default to English

