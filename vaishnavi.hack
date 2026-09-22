from flask import Flask, request, render_template_string

app = Flask(__name__)

# =========================================================
# CITY-WISE HOSPITAL DATA
# =========================================================

HOSPITALS = {

    "Nagpur": [
        {
            "name": "Government Medical College & Hospital",
            "area": "Medical Square",
            "distance": 4,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "07122751100"
        },
        {
            "name": "AIIMS Nagpur",
            "area": "MIHAN",
            "distance": 9,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "07120391000"
        },
        {
            "name": "Wockhardt Hospitals",
            "area": "Shankar Nagar",
            "distance": 6,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "07126622222"
        },
        {
            "name": "Alexis Multispeciality Hospital",
            "area": "Mankapur",
            "distance": 8,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "07126677777"
        },
        {
            "name": "Kingsway Hospitals",
            "area": "Kasturba Nagar",
            "distance": 7,
            "icu": True,
            "trauma": True,
            "neuro": False,
            "blood": True,
            "ambulance": True,
            "phone": "07126616161"
        }
    ],

    "Mumbai": [
        {
            "name": "KEM Hospital",
            "area": "Parel",
            "distance": 5,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02224107000"
        },
        {
            "name": "Sion Hospital",
            "area": "Sion",
            "distance": 7,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02224092020"
        },
        {
            "name": "Nanavati Max Hospital",
            "area": "Vile Parle",
            "distance": 10,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02226267500"
        },
        {
            "name": "Kokilaben Hospital",
            "area": "Andheri",
            "distance": 12,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02242696969"
        }
    ],

    "Pune": [
        {
            "name": "Sassoon General Hospital",
            "area": "Pune Station",
            "distance": 4,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02026128000"
        },
        {
            "name": "Ruby Hall Clinic",
            "area": "Sassoon Road",
            "distance": 6,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02066455100"
        },
        {
            "name": "Jehangir Hospital",
            "area": "Sassoon Road",
            "distance": 7,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02066819999"
        },
        {
            "name": "Deenanath Mangeshkar Hospital",
            "area": "Erandwane",
            "distance": 10,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "02040151000"
        }
    ],

    "Delhi": [
        {
            "name": "AIIMS New Delhi",
            "area": "Ansari Nagar",
            "distance": 5,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "01126588500"
        },
        {
            "name": "Safdarjung Hospital",
            "area": "Ansari Nagar",
            "distance": 6,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "01126707444"
        },
        {
            "name": "GTB Hospital",
            "area": "Dilshad Garden",
            "distance": 10,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "01122586262"
        },
        {
            "name": "Max Super Speciality Hospital",
            "area": "Saket",
            "distance": 12,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "01126515050"
        }
    ],

    "Bengaluru": [
        {
            "name": "Victoria Hospital",
            "area": "Kalasipalya",
            "distance": 5,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "08026701150"
        },
        {
            "name": "Manipal Hospital",
            "area": "Old Airport Road",
            "distance": 8,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "08025023344"
        },
        {
            "name": "Narayana Health",
            "area": "Bommasandra",
            "distance": 11,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "08071222222"
        },
        {
            "name": "St. John's Medical College Hospital",
            "area": "Koramangala",
            "distance": 7,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "08049467000"
        }
    ],

    "Hyderabad": [
        {
            "name": "Osmania General Hospital",
            "area": "Afzal Gunj",
            "distance": 4,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "04024600146"
        },
        {
            "name": "Apollo Hospitals",
            "area": "Jubilee Hills",
            "distance": 9,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "04023607777"
        },
        {
            "name": "Yashoda Hospitals",
            "area": "Secunderabad",
            "distance": 8,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "04045674567"
        },
        {
            "name": "CARE Hospitals",
            "area": "Banjara Hills",
            "distance": 10,
            "icu": True,
            "trauma": True,
            "neuro": True,
            "blood": True,
            "ambulance": True,
            "phone": "04030418888"
        }
    ]
}


# =========================================================
# AI RECOMMENDATION SYSTEM
# =========================================================

def recommend(city, emergency, severity, blood_group):

    hospitals = HOSPITALS.get(city, [])

    results = []

    for hospital in hospitals:

        score = 0
        reasons = []

        # Distance
        if hospital["distance"] <= 5:
            score += 30
            reasons.append("Very close to emergency location")

        elif hospital["distance"] <= 8:
            score += 20
            reasons.append("Nearby hospital")

        else:
            score += 10
            reasons.append("Hospital available in selected city")

        # Severity
        if severity == "Critical":

            if hospital["icu"]:
                score += 30
                reasons.append("ICU facility available")

            if hospital["ambulance"]:
                score += 20
                reasons.append("Ambulance service available")

        elif severity == "Severe":

            if hospital["icu"]:
                score += 20
                reasons.append("ICU facility available")

        else:

            score += 10
            reasons.append("Suitable for moderate emergency")

        # Emergency type
        if emergency == "Accident / Trauma":

            if hospital["trauma"]:
                score += 30
                reasons.append("Trauma care available")

        elif emergency == "Head Injury":

            if hospital["neuro"]:
                score += 30