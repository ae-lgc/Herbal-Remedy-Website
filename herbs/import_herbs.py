# herbs/import_herbs.py
from herbs.models import Herb

def import_herbs():
    # Predefined list of herb data
    herbs_data = [
        {
            "local_name": "Lagundi",
            "english_name": "Five-leaf Chaste Tree",
            "scientific_name": "Vitex negundo",
            "common_use": "Cough, asthma, colds",
            "preparation": "Boil leaves to make tea",
            "precautions": "Avoid in pregnancy; not for children under 2"
        },
        {
            "local_name": "Sambong",
            "english_name": "Blumea",
            "scientific_name": "Blumea balsamifera",
            "common_use": "Kidney stones, hypertension",
            "preparation": "Boil leaves in water, drink as tea",
            "precautions": "May cause allergic reactions; consult doctor for long-term use"
        },
        {
            "local_name": "Tsaang Gubat",
            "english_name": "Wild Tea",
            "scientific_name": "Ehretia microphylla",
            "common_use": "Stomachache, diarrhea",
            "preparation": "Boil leaves to make tea",
            "precautions": "Excessive intake can cause diarrhea"
        },
        {
            "local_name": "Niyog-niyogan",
            "english_name": "Chinese Honeysuckle",
            "scientific_name": "Quisqualis indica",
            "common_use": "Intestinal worms",
            "preparation": "Boil seeds or leaves in water",
            "precautions": "Use only under medical supervision"
        },
        {
            "local_name": "Bayabas",
            "english_name": "Guava",
            "scientific_name": "Psidium guajava",
            "common_use": "Wound disinfection, diarrhea",
            "preparation": "Use crushed leaves for poultice, drink leaf decoction",
            "precautions": "Avoid if allergic to guava"
        },
        {
            "local_name": "Akapulko",
            "english_name": "Ringworm Bush",
            "scientific_name": "Cassia alata",
            "common_use": "Skin diseases (fungal)",
            "preparation": "Apply crushed leaves directly to affected skin",
            "precautions": "Avoid contact with eyes; may cause skin irritation"
        },
        {
            "local_name": "Yerba Buena",
            "english_name": "Peppermint",
            "scientific_name": "Clinopodium douglasii",
            "common_use": "Body pain, headache, nausea",
            "preparation": "Brew fresh leaves in hot water",
            "precautions": "Avoid in large amounts; may cause heartburn"
        },
        {
            "local_name": "Bawang",
            "english_name": "Garlic",
            "scientific_name": "Allium sativum",
            "common_use": "High blood pressure, cholesterol",
            "preparation": "Eat raw or in cooking; garlic oil",
            "precautions": "May interact with blood-thinning medication"
        },
        {
            "local_name": "Ampalaya",
            "english_name": "Bitter Gourd",
            "scientific_name": "Momordica charantia",
            "common_use": "Diabetes, blood sugar control",
            "preparation": "Eat raw, as juice, or in dishes",
            "precautions": "Can cause stomach upset in some people"
        },
        {
            "local_name": "Luya",
            "english_name": "Ginger",
            "scientific_name": "Zingiber officinale",
            "common_use": "Sore throat, nausea, digestion",
            "preparation": "Boil slices in water, drink tea",
            "precautions": "Avoid in high doses; may cause heartburn"
        },
        {
            "local_name": "Luyang Dilaw",
            "english_name": "Turmeric",
            "scientific_name": "Curcuma longa",
            "common_use": "Anti-inflammatory, arthritis",
            "preparation": "Make tea, or mix in food as powder",
            "precautions": "Avoid high doses in pregnancy"
        },
        {
            "local_name": "Anonas",
            "english_name": "Soursop",
            "scientific_name": "Annona muricata",
            "common_use": "Anti-cancer (claimed), immune boost",
            "preparation": "Eat fresh or as juice",
            "precautions": "High intake may cause nerve issues (long-term use)"
        },
        {
            "local_name": "Banaba",
            "english_name": "Pride of India",
            "scientific_name": "Lagerstroemia speciosa",
            "common_use": "Diabetes, UTI",
            "preparation": "Boil leaves to make tea",
            "precautions": "Can lower blood sugar, monitor closely"
        },
        {
            "local_name": "Oregano",
            "english_name": "Oregano",
            "scientific_name": "Origanum vulgare",
            "common_use": "Cough, asthma, sore throat",
            "preparation": "Brew leaves in water as tea",
            "precautions": "Can cause allergic reactions; avoid in pregnancy"
        },
        {
            "local_name": "Tanglad",
            "english_name": "Lemongrass",
            "scientific_name": "Cymbopogon citratus",
            "common_use": "Cough, fever, digestive issues",
            "preparation": "Boil leaves to make tea",
            "precautions": "May cause skin irritation in some individuals"
        },
        {
            "local_name": "Makahiya",
            "english_name": "Sensitive Plant",
            "scientific_name": "Mimosa pudica",
            "common_use": "Wounds, menstrual cramps",
            "preparation": "Crush leaves and apply to wounds",
            "precautions": "May cause allergic reactions in sensitive individuals"
        },
        {
            "local_name": "Hilbas",
            "english_name": "Wild Sage",
            "scientific_name": "Lippia nodiflora",
            "common_use": "Stomach pain, digestion",
            "preparation": "Boil leaves to make tea",
            "precautions": "May cause nausea in large amounts"
        }
    ]

    for herb in herbs_data:
        # Import each herb if it doesn't already exist in the database
        if not Herb.objects.filter(local_name=herb['local_name']).exists():
            Herb.objects.create(**herb)

    print('✅ Herbs successfully imported!')
