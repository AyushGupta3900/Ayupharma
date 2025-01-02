from ayupharma import app, db
from ayupharma.models import Disease

data_to_insert = [
    Disease(
        disease='Arthritis',
        symptoms='Joint pain, stiffness, swelling, reduced range of motion',
        ayurvedic_herbs='Turmeric, Ashwagandha, Boswellia, Guggul',
        yoga_practices='Surya Namaskar (Sun Salutation), Tadasana (Mountain Pose), Bhujangasana (Cobra Pose)',
        questions='''Have you experienced joint pain?,
                   Do you have stiffness in your joints?,
                   Have you noticed swelling in your joints?,
                   Is there a reduced range of motion in your joints?'''
    ),
    Disease(
        disease='Constipation',
        symptoms='Difficulty passing stool, infrequent bowel movements',
        ayurvedic_herbs='Triphala, Senna, Psyllium Husk',
        yoga_practices='Pawanmuktasana (Wind-Relieving Pose), Trikonasana (Triangle Pose), Balasana (Child''s Pose)',
        questions='''Do you experience difficulty passing stool?,
                   Are your bowel movements infrequent?'''
    ),
    Disease(
        disease='Cough and Cold',
        symptoms='Runny or stuffy nose, sneezing, cough, sore throat',
        ayurvedic_herbs='Tulsi (Holy Basil), Ginger, Black Pepper, Long Pepper',
        yoga_practices='Bhastrika Pranayama (Bellows Breath), Anulom Vilom (Alternate Nostril Breathing), Tadasana (Mountain Pose)',
        questions='''Do you have a runny or stuffy nose?,
                   Are you experiencing sneezing?,
                   Do you have a cough?,
                   Is your throat sore?'''
    ),
    Disease(
        disease='Wet Cough',
        symptoms='Excessive mucus production, productive cough',
        ayurvedic_herbs='Vasa, Kantakari, Yashtimadhu',
        yoga_practices='Bhastrika Pranayama (Bellows Breath), Ujjayi Pranayama (Victorious Breath), Matsyasana (Fish Pose)',
        questions='''Do you produce excessive mucus?,
                   Does your cough produce phlegm or sputum?'''
    ),
    Disease(
        disease='Dry Cough',
        symptoms='Irritating, non-productive cough',
        ayurvedic_herbs='Sitopaladi Churna, Licorice (Yashtimadhu), Honey',
        yoga_practices='Bhastrika Pranayama (Bellows Breath), Ujjayi Pranayama (Victorious Breath), Bhujangasana (Cobra Pose)',
        questions='''Do you have an irritating cough?,
                   Is your cough non-productive, meaning it doesn't produce phlegm?'''
    ),
    Disease(
        disease='Diarrhea',
        symptoms='Frequent loose, watery stools',
        ayurvedic_herbs='Bilva, Kutaja, Pomegranate Peel',
        yoga_practices='Balasana (Child''s Pose), Vajrasana (Thunderbolt Pose), Ardha Matsyendrasana (Half Lord of the Fishes Pose)',
        questions='''Do you have frequent loose or watery stools?'''
    ),
    Disease(
        disease='Dry Eyes',
        symptoms='Itchy, red, or dry eyes',
        ayurvedic_herbs='Triphala, Ghee, Amla',
        yoga_practices='Palm-Pressing Exercise, Trataka (Candle Gazing), Bhujangasana (Cobra Pose)',
        questions='''Are your eyes itchy?,
                   Are your eyes red?,
                   Do you experience dryness in your eyes?'''
    ),
    Disease(
        disease='Ear Infection',
        symptoms='Ear pain, hearing loss, discharge from the ear',
        ayurvedic_herbs='Neem, Garlic, Mullein Oil',
        yoga_practices='Pranayama (Breathing Exercises), Bhramari Pranayama (Humming Bee Breath), Gomukhasana (Cow Face Pose)',
        questions='''Do you have ear pain?,
                   Have you noticed any hearing loss?,
                   Is there a discharge from your ear?'''
    ),
    Disease(
        disease='Headache',
        symptoms='Head pain, can be throbbing, dull, or sharp',
        ayurvedic_herbs='Peppermint, Lavender, Brahmi',
        yoga_practices='Shavasana (Corpse Pose), Adho Mukha Svanasana (Downward-Facing Dog), Shishuasana (Child''s Pose)',
        questions='''Do you experience head pain?,
                   Does the head pain feel throbbing?,
                   Is it dull or sharp?'''
    ),
    Disease(
        disease='Heartburn',
        symptoms='Burning sensation in the chest or throat',
        ayurvedic_herbs='Amla, Haritaki, Fennel Seeds',
        yoga_practices='Vajrasana (Thunderbolt Pose), Ardha Matsyendrasana (Half Lord of the Fishes Pose), Bhujangasana (Cobra Pose)',
        questions='''Do you experience a burning sensation in your chest or throat?'''
    ),
    Disease(
        disease='Gas',
        symptoms='Excessive bloating, belching, flatulence',
        ayurvedic_herbs='Ajwain, Fennel Seeds, Hing (Asafoetida)',
        yoga_practices='Pavanmuktasana (Wind-Relieving Pose), Trikonasana (Triangle Pose), Balasana (Child''s Pose)',
        questions='''Do you experience excessive bloating?,
                   Are you belching frequently?,
                   Do you have excessive flatulence (gas)?'''
    ),
    Disease(
        disease='Indigestion',
        symptoms='Feeling of fullness, discomfort, and abdominal pain after eating',
        ayurvedic_herbs='Ginger, Cumin, Coriander',
        yoga_practices='Vajrasana (Thunderbolt Pose), Ardha Matsyendrasana (Half Lord of the Fishes Pose), Bhujangasana (Cobra Pose)',
        questions='''Do you feel full after eating?,
                   Do you experience discomfort after meals?,
                   Is there abdominal pain after eating?'''
    ),
    Disease(
        disease='Irritable Bowels',
        symptoms='Abdominal pain, bloating, constipation, or diarrhea',
        ayurvedic_herbs='Triphala, Fennel Seeds, Licorice',
        yoga_practices='Pavanmuktasana (Wind-Relieving Pose), Trikonasana (Triangle Pose), Balasana (Child''s Pose)',
        questions='''Do you have abdominal pain?,
                   Are you experiencing bloating?,
                   Do you have constipation?,
                   Are you experiencing diarrhea?'''
    ),
    Disease(
        disease='Lack of Hunger',
        symptoms='Loss of appetite and reduced desire to eat',
        ayurvedic_herbs='Ginger, Cardamom, Cumin',
        yoga_practices='Agastya Asana, Surya Namaskar (Sun Salutation), Tadasana (Mountain Pose)',
        questions='''Have you lost your appetite?,
                   Do you have a reduced desire to eat?'''
    ),
    Disease(
        disease='Muscle Ache',
        symptoms='Muscular pain, soreness, and stiffness',
        ayurvedic_herbs='Ashwagandha, Boswellia, Ginger, Mahanarayan Oil',
        yoga_practices='Shavasana (Corpse Pose), Adho Mukha Svanasana (Downward-Facing Dog), Balasana (Child''s Pose)',
        questions='''Do you experience muscular pain?,
                   Are your muscles sore?,
                   Do you have stiffness in your muscles?'''
    ),
    Disease(
        disease='Nausea',
        symptoms='Feeling of queasiness and the urge to vomit',
        ayurvedic_herbs='Ginger, Peppermint, Cardamom, Hingwastak Churna',
        yoga_practices='Shavasana (Corpse Pose), Adho Mukha Svanasana (Downward-Facing Dog), Balasana (Child''s Pose)',
        questions='''Do you feel queasy?,
                   Do you have the urge to vomit?'''
    ),
    Disease(
        disease='Pain',
        symptoms='Varied pain, such as localized pain, aching, or sharp pain',
        ayurvedic_herbs='Turmeric, Ginger, Boswellia, Yogaraj Guggul',
        yoga_practices='Shavasana (Corpse Pose), Adho Mukha Svanasana (Downward-Facing Dog), Balasana (Child''s Pose)',
        questions='''Are your symptoms variable depending on the cause?,
                   Do you experience localized pain?,
                   Is there aching or sharp pain?'''
    ),
    Disease(
        disease='Stress and Anxiety',
        symptoms='Restlessness, worry, tension, rapid heartbeat',
        ayurvedic_herbs='Brahmi, Ashwagandha, Jatamansi, Brahmi Vati',
        yoga_practices='Pranayama (Breathing Exercises), Bhramari Pranayama (Humming Bee Breath), Shavasana (Corpse Pose)',
        questions='''Do you feel restless?,
                   Are you experiencing worry or tension?,
                   Do you have a rapid heartbeat?'''
    ),
    Disease(
        disease='Sunburn',
        symptoms='Redness, pain, and peeling of the skin due to sun exposure',
        ayurvedic_herbs='Aloe Vera, Chandan (Sandalwood), Coconut Oil, Chandanadi Vati',
        yoga_practices='Shavasana (Corpse Pose), Adho Mukha Svanasana (Downward-Facing Dog), Balasana (Child''s Pose)',
        questions='''Does your skin show redness due to sun exposure?,
                   Are you experiencing pain due to sunburn?,
                   Is your skin peeling because of sun exposure?'''
    ),
    Disease(
        disease='Insomnia',
        symptoms='Difficulty falling asleep or staying asleep, fatigue',
        ayurvedic_herbs='Valerian Root, Ashwagandha, Brahmi, Ashwagandha Churna',
        yoga_practices='Shavasana (Corpse Pose), Yoga Nidra, Anulom Vilom (Alternate Nostril Breathing)',
        questions='''Are you experiencing insomnia?,
                   Do you have difficulty falling asleep or staying asleep?,
                   Are you often fatigued?'''
    ),
    Disease(
        disease='High Blood Pressure',
        symptoms='Elevated blood pressure, dizziness, headache',
        ayurvedic_herbs='Garlic, Arjuna, Sarpagandha, Mukta Vati',
        yoga_practices='Savasana (Corpse Pose), Bhujangasana (Cobra Pose), Ardhachakrasana (Half Wheel Pose)',
        questions='''Have you been aware of elevated blood pressure?,
                   Do you experience dizziness?,
                   Do you have headaches?'''
    ),
    Disease(
        disease='Allergies',
        symptoms='Sneezing, runny or stuffy nose, itchy eyes',
        ayurvedic_herbs='Turmeric, Licorice, Nettle Leaf, Haridrakhand',
        yoga_practices='Bhastrika Pranayama (Bellows Breath), Matsyasana (Fish Pose), Balasana (Child''s Pose)',
        questions='''Are you sneezing frequently?,
                   Do you have itchy eyes?,
                   Is your nose runny or stuffy?'''
    ),
    Disease(
        disease='Acne',
        symptoms='Pimples, blackheads, redness on the skin',
        ayurvedic_herbs='Neem, Turmeric, Aloe Vera, Gandhak Rasayan',
        yoga_practices='Shirshasana (Headstand), Sarvangasana (Shoulder Stand), Trikonasana (Triangle Pose)',
        questions='''Are you experiencing pimples?,
                   Do you have blackheads?,
                   Is there redness on your skin?'''
    ),
    Disease(
        disease='Migraine',
        symptoms='Intense headaches, often with nausea and sensitivity to light',
        ayurvedic_herbs='Feverfew, Butterbur, Lavender, Pathyadi Kwath',
        yoga_practices='Shavasana (Corpse Pose), Ardha Chandrasana (Half Moon Pose), Bhramari Pranayama (Humming Bee Breath)',
        questions='''Do you experience intense headaches?,
               Are you often nauseated with your headaches?,
               Are you sensitive to light during headaches?'''
    ),
    Disease(
        disease='Eczema',
        symptoms='Itchy, inflamed skin with rashes and dry patches',
        ayurvedic_herbs='Neem, Turmeric, Coconut Oil, Khadirarishta',
        yoga_practices='Matsyasana (Fish Pose), Bhujangasana (Cobra Pose), Vajrasana (Thunderbolt Pose)',
        questions='''Is your skin itchy?,
                   Do you have inflamed skin with rashes?,
                   Are there dry patches on your skin?'''
    ),
    Disease(
        disease='Osteoporosis',
        symptoms='Weak and brittle bones, fractures, loss of height',
        ayurvedic_herbs='Shatavari, Ashwagandha, Arjuna, Praval Pishti',
        yoga_practices='Tadasana (Mountain Pose), Vrikshasana (Tree Pose), Setu Bandhasana (Bridge Pose)',
        questions='''Have you noticed a loss of height?,
                   Do you have weak and brittle bones?,
                   Have you experienced fractures?'''
    ),
    Disease(
        disease='Depression',
        symptoms='Persistent sadness, loss of interest, fatigue',
        ayurvedic_herbs="St. John's Wort, Brahmi, Saffron, Saraswatarishta",
        yoga_practices='Pranayama (Breathing Exercises), Ustrasana (Camel Pose), Balasana (Child''s Pose)',
        questions='''Are you persistently sad?,
                   Have you lost interest in activities you used to enjoy?,
                   Do you often feel fatigued?'''
    ),
    Disease(
        disease='Tinnitus',
        symptoms='Ringing or buzzing in the ears',
        ayurvedic_herbs='Ginkgo Biloba, Sesame Oil, Ashwagandha, Shirodhara',
        yoga_practices='Bhramari Pranayama (Humming Bee Breath), Gomukhasana (Cow Face Pose), Sarvangasana (Shoulder Stand)',
        questions='''Do you hear ringing or buzzing in your ears?,
                   Are you experiencing ear-related symptoms?,
                   Have you noticed changes in your hearing?'''
    ),
    Disease(
        disease='Acid Reflux',
        symptoms='Heartburn, regurgitation, chest pain',
        ayurvedic_herbs='Amla, Haritaki, Fennel Seeds, Avipattikar Churna',
        yoga_practices='Vajrasana (Thunderbolt Pose), Ardha Matsyendrasana (Half Lord of the Fishes Pose), Bhujangasana (Cobra Pose)',
        questions='''Do you experience regurgitation?,
                   Is there chest pain or discomfort?,
                   Are you experiencing heartburn?'''
    ),
    Disease(
        disease='Insulin Resistance',
        symptoms='Weight gain, high blood sugar, fatigue',
        ayurvedic_herbs='Cinnamon, Fenugreek, Bitter Melon, Gurmar',
        yoga_practices='Ardha Matsyendrasana (Half Lord of the Fishes Pose), Dhanurasana (Bow Pose), Bhujangasana (Cobra Pose)',
        questions='''Have you gained weight?,
                   Is your blood sugar elevated?,
                   Are you frequently fatigued?'''
    ),
    Disease(
        disease='Urinary Tract Infection',
        symptoms='Frequent urination, pain, burning sensation',
        ayurvedic_herbs='Cranberry, Uva Ursi, Gokshura, Chandraprabha Vati',
        yoga_practices='Bhujangasana (Cobra Pose), Vajrasana (Thunderbolt Pose), Ustrasana (Camel Pose)',
        questions='''Are you urinating frequently?,
                   Do you experience a burning sensation while urinating?,
                   Have you noticed pain in the urinary tract?'''
    ),
    Disease(
        disease='Asthma',
        symptoms='Wheezing, shortness of breath, coughing',
        ayurvedic_herbs='Vasaka, Licorice, Adhatoda (Vasaka), Sitopaladi Churna',
        yoga_practices='Anulom Vilom (Alternate Nostril Breathing), Matsyasana (Fish Pose), Setu Bandhasana (Bridge Pose)',
        questions='''Do you experience wheezing?,
                   Are you short of breath?,
                   Do you have a persistent cough?'''
    ),
    Disease(
        disease='Thyroid Disorders',
        symptoms='Fatigue, weight changes, mood swings',
        ayurvedic_herbs='Ashwagandha, Guggul, Bladderwrack, Kanchnar Guggul',
        yoga_practices='Sarvangasana (Shoulder Stand), Halasana (Plow Pose), Matsyasana (Fish Pose)',
        questions='''Have you noticed changes in your weight?,
                   Are you experiencing mood swings?,
                   Do you have fatigue or mood-related symptoms?'''
    ),
    Disease(
        disease='High Cholesterol',
        symptoms='Elevated cholesterol levels in the blood',
        ayurvedic_herbs='Guggul, Garlic, Arjuna, Arjunarishta',
        yoga_practices='Surya Namaskar (Sun Salutation), Trikonasana (Triangle Pose), Bhujangasana (Cobra Pose)',
        questions='''Are your cholesterol levels elevated?,
                   Have you had a blood cholesterol test?,
                   Do you experience symptoms like dizziness or headache?'''
    ),
    Disease(
        disease='Kidney Stones',
        symptoms='Severe pain, blood in urine, frequent urination',
        ayurvedic_herbs='Punarnava, Varuna, Gokshura, Stone Go',
        yoga_practices='Dhanurasana (Bow Pose), Pawanmuktasana (Wind-Relieving Pose), Ardha Matsyendrasana (Half Lord of the Fishes Pose)',
        questions='''Have you experienced severe pain?,
                   Do you see blood in your urine?,
                   Are you urinating more frequently?'''
    ),
    Disease(
        disease='Hypothyroidism',
        symptoms='Fatigue, weight gain, cold intolerance',
        ayurvedic_herbs='Ashwagandha, Guggul, Bladderwrack, Thyronil Capsules',
        yoga_practices='Matsyasana (Fish Pose), Ustrasana (Camel Pose), Halasana (Plow Pose)',
        questions='''Are you experiencing fatigue?,
                   Have you noticed weight changes?,
                   Are you sensitive to cold?'''
    )
]

with app.app_context():
    db.create_all()
    for entry in data_to_insert:
        db.session.add(entry)
    db.session.commit()