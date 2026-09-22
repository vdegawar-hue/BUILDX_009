from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# ============================================================
# HEALTHCARE EMERGENCY ASSISTANT - HACKATHON VERSION
# ============================================================

HOSPITALS = [
    {
        "name": "Government Medical College & Hospital",
        "type": "Government Hospital",
        "specialization": "Emergency • General Medicine • Surgery",
        "address": "Hanuman Nagar, Nagpur",
        "phone": "0712-2744673",
        "ambulance": "0712-2701180",
        "doctor": "Casualty Medical Officer",
        "doctor_phone": "0712-2820100"
    },
    {
        "name": "Indira Gandhi Government Medical College & Hospital",
        "type": "Government Hospital",
        "specialization": "Emergency • Critical Care • Surgery",
        "address": "C.A. Road, Nagpur",
        "phone": "0712-2744673",
        "ambulance": "0712-2701180",
        "doctor": "Casualty Medical Officer",
        "doctor_phone": "0712-2820100"
    },
    {
        "name": "CARE Hospitals Nagpur",
        "type": "Multispeciality Hospital",
        "specialization": "Cardiology • Neurology • Critical Care",
        "address": "Farmland Road, Panchsheel Square, Nagpur",
        "phone": "0712-6165656",
        "ambulance": "0712-6165656",
        "doctor": "Emergency Duty Doctor",
        "doctor_phone": "0712-6165656"
    },
    {
        "name": "Wockhardt Super Specialty Hospital",
        "type": "Super Specialty Hospital",
        "specialization": "Cardiology • Neurology • Emergency",
        "address": "North Ambazari Road, Nagpur",
        "phone": "0712-6624289",
        "ambulance": "0712-6624100",
        "doctor": "Emergency Duty Doctor",
        "doctor_phone": "0712-6624289"
    },
    {
        "name": "Orange City Hospital & Research Institute",
        "type": "Multispeciality Hospital",
        "specialization": "Emergency • Critical Care • General Medicine",
        "address": "Veer Sawarkar Square, Nagpur",
        "phone": "0712-2238431",
        "ambulance": "09225260606",
        "doctor": "Emergency Duty Doctor",
        "doctor_phone": "0712-2238431"
    },
    {
        "name": "Meditrina Hospital",
        "type": "Multispeciality Hospital",
        "specialization": "Emergency • Critical Care • Neurology",
        "address": "Central Bazar Road, Ramdaspeth, Nagpur",
        "phone": "0712-6669600",
        "ambulance": "0712-6669612",
        "doctor": "Emergency Duty Doctor",
        "doctor_phone": "0712-6669600"
    },
    {
        "name": "Suretech Hospital & Research Centre",
        "type": "Multispeciality Hospital",
        "specialization": "Critical Care • Cardiology • Neurology",
        "address": "Banerjee Marg, Dhantoli, Nagpur",
        "phone": "0712-6636800",
        "ambulance": "0712-6636802",
        "doctor": "Emergency Duty Doctor",
        "doctor_phone": "0712-6636870"
    },
    {
        "name": "Kingway Hospital",
        "type": "Multispeciality Hospital",
        "specialization": "Emergency • General Medicine • Surgery",
        "address": "Kingsway, Nagpur",
        "phone": "0712-6789100",
        "ambulance": "0712-6789100",
        "doctor": "Emergency Duty Doctor",
        "doctor_phone": "0712-6789100"
    }
]


PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>MedAssist Nagpur | Emergency Healthcare</title>

<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial, Helvetica, sans-serif;
}

body{
    background:#f4f8fb;
    color:#17202a;
}

/* NAVBAR */

.navbar{
    background:linear-gradient(135deg,#087f8c,#064e63);
    color:white;
    padding:18px 7%;
    display:flex;
    justify-content:space-between;
    align-items:center;
    position:sticky;
    top:0;
    z-index:1000;
    box-shadow:0 4px 15px rgba(0,0,0,.15);
}

.logo{
    font-size:25px;
    font-weight:bold;
}

.logo span{
    color:#70efde;
}

.nav-links{
    display:flex;
    gap:25px;
}

.nav-links a{
    color:white;
    text-decoration:none;
    font-weight:bold;
}

/* HERO */

.hero{
    min-height:430px;
    padding:70px 7%;
    display:flex;
    align-items:center;
    justify-content:space-between;
    background:
    radial-gradient(circle at 80% 30%,rgba(112,239,222,.25),transparent 30%),
    linear-gradient(135deg,#064e63,#087f8c);
    color:white;
}

.hero-content{
    max-width:700px;
}

.badge{
    display:inline-block;
    padding:8px 15px;
    border-radius:30px;
    background:rgba(255,255,255,.15);
    border:1px solid rgba(255,255,255,.3);
    margin-bottom:20px;
}

.hero h1{
    font-size:52px;
    line-height:1.1;
    margin-bottom:20px;
}

.hero h1 span{
    color:#70efde;
}

.hero p{
    font-size:18px;
    line-height:1.7;
    color:#e2f8fa;
}

.emergency-box{
    margin-top:30px;
    display:flex;
    gap:15px;
    flex-wrap:wrap;
}

.emergency-btn{
    background:#ff4d4d;
    color:white;
    padding:15px 25px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
    box-shadow:0 8px 20px rgba(255,77,77,.3);
}

.find-btn{
    background:white;
    color:#064e63;
    padding:15px 25px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
}

/* FEATURES */

.features{
    padding:55px 7%;
}

.section-title{
    text-align:center;
    font-size:32px;
    color:#064e63;
    margin-bottom:35px;
}

.feature-grid{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
}

.feature{
    background:white;
    padding:25px;
    border-radius:18px;
    text-align:center;
    box-shadow:0 5px 20px rgba(0,0,0,.07);
    transition:.3s;
}

.feature:hover{
    transform:translateY(-6px);
}

.feature-icon{
    font-size:40px;
    margin-bottom:12px;
}

.feature h3{
    margin-bottom:8px;
    color:#064e63;
}

/* EMERGENCY STRIP */

.emergency-strip{
    margin:10px 7% 45px;
    padding:25px;
    border-radius:20px;
    background:linear-gradient(135deg,#fff1f1,#ffe0e0);
    border-left:6px solid #ff4d4d;
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:20px;
}

.emergency-strip h2{
    color:#c62828;
    margin-bottom:6px;
}

.call108{
    background:#d32f2f;
    color:white;
    padding:14px 22px;
    border-radius:12px;
    text-decoration:none;
    font-weight:bold;
    white-space:nowrap;
}

/* HOSPITAL SECTION */

.hospital-section{
    padding:30px 7% 70px;
}

.controls{
    display:flex;
    gap:15px;
    margin-bottom:30px;
    flex-wrap:wrap;
}

.search{
    flex:1;
    min-width:250px;
    padding:15px 18px;
    border:1px solid #d6e2e8;
    border-radius:12px;
    font-size:16px;
    outline:none;
}

.search:focus{
    border-color:#087f8c;
}

.filter{
    padding:15px;
    border-radius:12px;
    border:1px solid #d6e2e8;
    background:white;
    font-size:16px;
}

.hospital-grid{
    display:grid;
    grid-template-columns:repeat(2,1fr);
    gap:25px;
}

.hospital-card{
    background:white;
    border-radius:20px;
    padding:25px;
    box-shadow:0 7px 25px rgba(0,0,0,.08);
    border:1px solid #e7eef2;
    transition:.3s;
}

.hospital-card:hover{
    transform:translateY(-5px);
    box-shadow:0 12px 30px rgba(0,0,0,.12);
}

.card-top{
    display:flex;
    justify-content:space-between;
    gap:15px;
    margin-bottom:15px;
}

.hospital-name{
    font-size:21px;
    color:#064e63;
    font-weight:bold;
}

.status{
    background:#e7f8ef;
    color:#16834a;
    padding:6px 10px;
    border-radius:20px;
    font-size:12px;
    font-weight:bold;
    height:max-content;
}

.info{
    margin:12px 0;
    color:#53636b;
    line-height:1.6;
}

.info strong{
    color:#27343a;
}

.doctor-box{
    margin-top:18px;
    padding:16px;
    background:#f1f9fa;
    border-radius:14px;
    border-left:4px solid #087f8c;
}

.doctor-box h4{
    color:#064e63;
    margin-bottom:8px;
}

.buttons{
    display:flex;
    gap:10px;
    margin-top:18px;
    flex-wrap:wrap;
}

.btn{
    flex:1;
    min-width:120px;
    text-align:center;
    padding:12px;
    border-radius:10px;
    text-decoration:none;
    font-weight:bold;
}

.call{
    background:#087f8c;
    color:white;
}

.ambulance{
    background:#ff4d4d;
    color:white;
}

.map{
    background:#e9f3f6;
    color:#064e63;
}

/* STATS */

.stats{
    padding:45px 7%;
    background:#063b4a;
    color:white;
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
    text-align:center;
}

.stat h2{
    font-size:34px;
    color:#70efde;
}

.stat p{
    margin-top:8px;
    color:#d8eef1;
}

/* FOOTER */

footer{
    background:#032f3b;
    color:#c8dce0;
    text-align:center;
    padding:30px;
}

footer strong{
    color:white;
}

/* MOBILE */

@media(max-width:900px){

    .hero{
        padding:55px 6%;
    }

    .hero h1{
        font-size:40px;
    }

    .feature-grid{
        grid-template-columns:repeat(2,1fr);
    }

    .hospital-grid{
        grid-template-columns:1fr;
    }

    .stats{
        grid-template-columns:repeat(2,1fr);
    }

}

@media(max-width:600px){

    .navbar{
        padding:15px 5%;
    }

    .nav-links{
        display:none;
    }

    .hero{
        padding:45px 5%;
    }

    .hero h1{
        font-size:34px;
    }

    .feature-grid{
        grid-template-columns:1fr;
    }

    .stats{
        grid-template-columns:1fr 1fr;
    }

    .emergency-strip{
        margin:10px 5% 35px;
        flex-direction:column;
        align-items:flex-start;
    }

    .hospital-section{
        padding-left:5%;
        padding-right:5%;
    }

}

</style>
</head>

<body>

<!-- NAVBAR -->

<nav class="navbar">

<div class="logo">
🩺 Med<span>Assist</span>
</div>

<div class="nav-links">
<a href="#home">Home</a>
<a href="#hospitals">Hospitals</a>
<a href="#emergency">Emergency</a>
</div>

</nav>


<!-- HERO -->

<section class="hero" id="home">

<div class="hero-content">

<div class="badge">
🚨 AI-Powered Emergency Healthcare Assistant
</div>

<h1>
Find <span>Emergency Care</span><br>
When Every Second Matters
</h1>

<p>
MedAssist helps users quickly find nearby hospitals,
emergency doctors and ambulance services in Nagpur.
All important contact information is available in one place.
</p>

<div class="emergency-box">

<a href="tel:108" class="emergency-btn">
🚑 Call Emergency 108
</a>

<a href="#hospitals" class="find-btn">
🏥 Find Hospitals
</a>

</div>

</div>

</section>


<!-- FEATURES -->

<section class="features">

<h2 class="section-title">
Why MedAssist?
</h2>

<div class="feature-grid">

<div class="feature">
<div class="feature-icon">🏥</div>
<h3>Hospital Finder</h3>
<p>Find hospitals and emergency departments quickly.</p>
</div>

<div class="feature">
<div class="feature-icon">👨‍⚕️</div>
<h3>Doctor Contacts</h3>
<p>Access emergency doctor or hospital contact information.</p>
</div>

<div class="feature">
<div class="feature-icon">🚑</div>
<h3>Ambulance</h3>
<p>Quick access to ambulance and emergency numbers.</p>
</div>

<div class="feature">
<div class="feature-icon">📞</div>
<h3>One-Click Call</h3>
<p>Call hospitals directly without searching manually.</p>
</div>

</div>

</section>


<!-- EMERGENCY -->

<section class="emergency-strip" id="emergency">

<div>

<h2>🚨 Medical Emergency?</h2>

<p>
For emergency medical assistance in Maharashtra,
call the official 108 emergency service.
</p>

</div>

<a href="tel:108" class="call108">
📞 CALL 108
</a>

</section>


<!-- HOSPITALS -->

<section class="hospital-section" id="hospitals">

<h2 class="section-title">
Recommended Emergency Hospitals
</h2>

<div class="controls">

<input
type="text"
id="search"
class="search"
placeholder="🔎 Search hospital, doctor or specialization..."
onkeyup="filterHospitals()"
>

<select id="filter" class="filter" onchange="filterHospitals()">

<option value="all">All Hospitals</option>
<option value="Government">Government</option>
<option value="Multispeciality">Multispeciality</option>
<option value="Super Specialty">Super Specialty</option>

</select>

</div>


<div class="hospital-grid" id="hospitalGrid">

{% for hospital in hospitals %}

<div class="hospital-card"
data-search="{{ hospital.name }} {{ hospital.specialization }} {{ hospital.doctor }} {{ hospital.address }}"
data-type="{{ hospital.type }}">

<div class="card-top">

<div class="hospital-name">
{{ hospital.name }}
</div>

<div class="status">
24×7
</div>

</div>

<div class="info">
<strong>🏥 Type:</strong>
{{ hospital.type }}
</div>

<div class="info">
<strong>🩺 Services:</strong>
{{ hospital.specialization }}
</div>

<div class="info">
<strong>📍 Address:</strong>
{{ hospital.address }}
</div>

<div class="info">
<strong>☎ Hospital:</strong>
{{ hospital.phone }}
</div>

<div class="doctor-box">

<h4>👨‍⚕️ Emergency Doctor</h4>

<p>
<strong>{{ hospital.doctor }}</strong>
</p>

<p>
📞 {{ hospital.doctor_phone }}
</p>

</div>

<div class="buttons">

<a
href="tel:{{ hospital.phone }}"
class="btn call">
📞 Hospital
</a>

<a
href="tel:{{ hospital.ambulance }}"
class="btn ambulance">
🚑 Ambulance
</a>

<a
href="https://www.google.com/maps/search/?api=1&query={{ hospital.name|urlencode }}+{{ hospital.address|urlencode }}"
target="_blank"
class="btn map">
📍 Map
</a>

</div>

</div>

{% endfor %}

</div>

</section>


<!-- STATS -->

<section class="stats">

<div class="stat">
<h2>24×7</h2>
<p>Emergency Access</p>
</div>

<div class="stat">
<h2>108</h2>
<p>Emergency Helpline</p>
</div>

<div class="stat">
<h2>8+</h2>
<p>Hospital Contacts</p>
</div>

<div class="stat">
<h2>1-Click</h2>
<p>Calling System</p>
</div>

</section>


<!-- FOOTER -->

<footer>

<p>
<strong>MedAssist Nagpur</strong>
</p>

<p>
Smart Healthcare • Emergency Assistance • Faster Access
</p>

<p style="margin-top:10px;">
⚠️ In a life-threatening emergency, contact emergency medical services immediately.
</p>

</footer>


<script>

function filterHospitals(){

    const search =
        document.getElementById("search")
        .value
        .toLowerCase();

    const type =
        document.getElementById("filter")
        .value;

    const cards =
        document.querySelectorAll(".hospital-card");

    cards.forEach(card => {

        const text =
            card.dataset.search.toLowerCase();

        const cardType =
            card.dataset.type;

        const matchesSearch =
            text.includes(search);

        const matchesType =
            type === "all" ||
            cardType.includes(type);

        if(matchesSearch && matchesType){
            card.style.display = "block";
        }
        else{
            card.style.display = "none";
        }

    });

}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE, hospitals=HOSPITALS)


@app.route("/api/hospitals")
def api_hospitals():
    return jsonify(HOSPITALS)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)