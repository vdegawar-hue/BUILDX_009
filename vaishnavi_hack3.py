from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

HOSPITALS = [
    {"name":"AIIMS Nagpur","type":"Government","area":"MIHAN","phone":"9404044944","emergency":"9404044944","specialties":"Trauma, Emergency, Cardiology, Neurology, Critical Care","beds":45,"status":"AVAILABLE"},
    {"name":"Government Medical College & Hospital","type":"Government","area":"Medical Square","phone":"07122701642","emergency":"07122744673","specialties":"Emergency, Trauma, General Medicine, Surgery","beds":55,"status":"AVAILABLE"},
    {"name":"Indira Gandhi Government Medical College & Hospital (Mayo)","type":"Government","area":"Central Avenue","phone":"07122725274","emergency":"07122744673","specialties":"Emergency, Trauma, Surgery, Critical Care","beds":35,"status":"AVAILABLE"},
    {"name":"Daga Memorial Government Women Hospital","type":"Government","area":"Gandhibagh","phone":"07122729333","emergency":"07122729333","specialties":"Obstetrics, Gynaecology, Women's Emergency","beds":30,"status":"AVAILABLE"},
    {"name":"Max Super Speciality Hospital Nagpur","type":"Private","area":"Mankapur","phone":"07127120000","emergency":"07127120000","specialties":"Cardiology, Neurology, Oncology, Critical Care, Trauma","beds":40,"status":"AVAILABLE"},
    {"name":"Wockhardt Super Specialty Hospital","type":"Private","area":"Shankar Nagar","phone":"07126624400","emergency":"07126624444","specialties":"Cardiology, Neurology, Emergency, Critical Care","beds":38,"status":"AVAILABLE"},
    {"name":"CARE Hospitals Nagpur","type":"Private","area":"Panchsheel Square","phone":"04068106589","emergency":"04068106589","specialties":"Cardiology, Neurology, Emergency, Critical Care","beds":30,"status":"AVAILABLE"},
    {"name":"KIMS-Kingsway Hospitals","type":"Private","area":"Kingsway","phone":"07126789100","emergency":"07126789100","specialties":"Emergency, Cardiology, Neurology, Trauma, Surgery","beds":42,"status":"AVAILABLE"},
    {"name":"KRIMS Hospitals","type":"Private","area":"Ramdaspeth","phone":"07122451188","emergency":"07122451188","specialties":"Cardiology, Neurology, Critical Care, Emergency","beds":28,"status":"AVAILABLE"},
    {"name":"VIMS Hospital","type":"Private","area":"Mohan Nagar","phone":"07123505800","emergency":"8007355123","specialties":"Trauma, Cardiac Emergency, Critical Care","beds":30,"status":"AVAILABLE"},
    {"name":"Shalinitai Meghe Hospital & Research Centre","type":"Private","area":"Wanadongri","phone":"8888402000","emergency":"8888402000","specialties":"General Medicine, Surgery, Cardiology, Orthopaedics, Emergency","beds":40,"status":"AVAILABLE"},
    {"name":"Swasthyam Superspeciality Hospital","type":"Private","area":"Vivekanand Nagar","phone":"8600888444","emergency":"8600888444","specialties":"Emergency, Critical Care, Cardiology, Surgery","beds":24,"status":"AVAILABLE"},
    {"name":"Midas Multispeciality Hospital","type":"Private","area":"Ramdaspeth","phone":"07122430511","emergency":"07122430511","specialties":"Emergency, General Medicine, Surgery, Critical Care","beds":22,"status":"AVAILABLE"},
    {"name":"Orbit Multispeciality Hospital","type":"Private","area":"Sakkardara","phone":"7770016622","emergency":"7770016622","specialties":"Emergency, General Medicine, Surgery, Orthopaedics","beds":20,"status":"AVAILABLE"},
    {"name":"Integrity Hospital","type":"Private","area":"Dighori","phone":"9801980100","emergency":"9801980100","specialties":"Emergency, General Medicine, Surgery, Critical Care","beds":20,"status":"AVAILABLE"},
    {"name":"YES Hospital","type":"Private","area":"Dighori","phone":"8446508046","emergency":"8446508046","specialties":"Emergency, General Medicine, Surgery","beds":18,"status":"AVAILABLE"},
    {"name":"Abhinav Multispeciality Hospital","type":"Private","area":"Lashkari Bagh","phone":"07122641715","emergency":"07122641715","specialties":"Emergency, General Medicine, Surgery","beds":16,"status":"AVAILABLE"},
    {"name":"Lata Mangeshkar Hospital","type":"Private","area":"Sitabuldi","phone":"07122530347","emergency":"07122530347","specialties":"Emergency, Multispeciality, Critical Care","beds":24,"status":"AVAILABLE"},
    {"name":"Super Speciality Hospital Nagpur","type":"Government","area":"Wanjari Nagar","phone":"07122750123","emergency":"07122750123","specialties":"Cardiology, Neurology, Nephrology, Emergency","beds":30,"status":"AVAILABLE"},
    {"name":"Government Dental College & Hospital","type":"Government","area":"Medical Square","phone":"07122744496","emergency":"07122744496","specialties":"Dental Emergency, Oral Surgery","beds":10,"status":"AVAILABLE"},
    {"name":"Government Ayurvedic College & Hospital","type":"Government","area":"Sakkardara","phone":"07122449198","emergency":"07122449198","specialties":"Ayurveda, General Care","beds":12,"status":"AVAILABLE"},
    {"name":"District Hospital Nagpur","type":"Government","area":"Mankapur","phone":"","emergency":"","specialties":"General Emergency, Public Health Services","beds":25,"status":"AVAILABLE"},
    {"name":"ESI Hospital Nagpur","type":"Government","area":"Somwaripeth","phone":"1800112526","emergency":"1800112526","specialties":"General Medicine, Emergency, Occupational Health","beds":20,"status":"AVAILABLE"},
    {"name":"Metro Multi Speciality Hospital","type":"Private","area":"Koradi Road","phone":"7218090250","emergency":"7218090250","specialties":"Emergency, General Medicine, Surgery","beds":15,"status":"AVAILABLE"},
]

HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MedAssist Nagpur</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:Arial,sans-serif;background:#f4f7fb;color:#172033}
nav{background:#fff;padding:18px 7%;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:10;box-shadow:0 2px 12px rgba(0,0,0,.08)}
.logo{font-size:26px;font-weight:bold;color:#d62828}
nav a{margin-left:20px;text-decoration:none;color:#333;font-weight:bold}
.hero{padding:65px 7%;background:linear-gradient(135deg,#fff5f5,#eef7ff)}
.hero h1{font-size:46px;margin:0 0 15px}.hero span{color:#d62828}.hero p{font-size:18px;line-height:1.6;max-width:760px}
.btn{border:0;padding:12px 17px;border-radius:9px;cursor:pointer;font-weight:bold;margin:5px;text-decoration:none;display:inline-block}
.red{background:#d62828;color:white}.blue{background:#1769aa;color:white}.green{background:#198754;color:white}.dark{background:#172033;color:white}
.container{width:86%;margin:40px auto}h2{font-size:29px}
.features,.twists{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.feature,.twist,.hospital,.panel{background:white;padding:22px;border-radius:15px;box-shadow:0 4px 15px rgba(0,0,0,.08)}
.feature{cursor:pointer}.feature:hover{transform:translateY(-3px)}.icon{font-size:34px}
.panel{display:none;margin-top:18px}.emergency{background:#d62828;color:white;padding:28px;border-radius:16px;margin:40px 0}
.controls{background:white;padding:18px;border-radius:14px;display:flex;gap:12px;flex-wrap:wrap}
input,select{padding:13px;border:1px solid #ccc;border-radius:8px;font-size:15px;flex:1;min-width:210px}
.hospital-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:22px}
.badge{display:inline-block;background:#dff7e8;color:#147a3d;padding:5px 9px;border-radius:20px;font-size:12px;font-weight:bold}
.result{margin-top:12px;padding:14px;background:#eef7ff;border-radius:9px}
footer{background:#172033;color:white;text-align:center;padding:28px;margin-top:50px}
@media(max-width:900px){.features,.twists,.hospital-grid{grid-template-columns:1fr 1fr}}
@media(max-width:600px){.features,.twists,.hospital-grid{grid-template-columns:1fr}.hero h1{font-size:34px}nav{flex-direction:column;gap:10px}}
</style>
</head>
<body>

<nav>
<div class="logo">MedAssist</div>
<div>
<a href="#home">Home</a>
<a href="#hospitals">Hospitals</a>
<a href="#twists">Emergency Solutions</a>
</div>
</nav>

<section class="hero" id="home">
<h1>Emergency Healthcare with <span>MedAssist</span></h1>
<p>Smart emergency healthcare assistance for finding hospitals, emergency contacts, ambulance support and faster response during critical situations.</p>
<a class="btn red" href="tel:108">CALL EMERGENCY 108</a>
<a class="btn blue" href="#hospitals">FIND HOSPITALS</a>
<button class="btn green" onclick="getLocation()">USE MY LOCATION</button>
</section>

<div class="container">

<h2>Why MedAssist?</h2>
<div class="features">
<div class="feature" onclick="showPanel('finder')"><div class="icon">🏥</div><h3>Hospital Finder</h3><p>Search hospitals by name, area or specialization.</p></div>
<div class="feature" onclick="showPanel('doctor')"><div class="icon">👨‍⚕️</div><h3>Doctor Contacts</h3><p>Access hospital emergency and casualty contacts.</p></div>
<div class="feature" onclick="showPanel('ambulance')"><div class="icon">🚑</div><h3>Ambulance</h3><p>Quick access to emergency ambulance service.</p></div>
<div class="feature" onclick="showPanel('call')"><div class="icon">📞</div><h3>One-Click Call</h3><p>Call a selected hospital directly.</p></div>
</div>

<div id="finder" class="panel"><h3>🏥 Smart Hospital Finder</h3><p>Use the hospital search below. Government and private hospitals are included.</p></div>
<div id="doctor" class="panel"><h3>👨‍⚕️ Emergency Contacts</h3><p>Hospital emergency/casualty contact numbers are shown. Personal doctor numbers are not invented.</p></div>
<div id="ambulance" class="panel"><h3>🚑 Emergency Ambulance</h3><p>For medical emergency assistance:</p><h2>108</h2><a class="btn red" href="tel:108">CALL 108</a></div>
<div id="call" class="panel"><h3>📞 One-Click Call</h3><p>Use CALL HOSPITAL or EMERGENCY CALL on any hospital card.</p></div>

<div class="emergency">
<h2>🚨 Medical Emergency?</h2>
<p>For a serious emergency, call 108 immediately.</p>
<a class="btn" style="background:white;color:#d62828" href="tel:108">CALL 108 NOW</a>
</div>

<section id="hospitals">
<h2>🏥 Recommended Emergency Hospitals - Nagpur</h2>
<p>Search is not restricted to only 24×7 hospitals.</p>
<div class="controls">
<input id="hospitalSearch" placeholder="Search hospital, area or specialization..." oninput="renderHospitals()">
<select id="typeFilter" onchange="renderHospitals()">
<option value="all">All Hospitals</option>
<option value="Government">Government</option>
<option value="Private">Private</option>
</select>
<select id="statusFilter" onchange="renderHospitals()">
<option value="all">All Availability</option>
<option value="AVAILABLE">Available</option>
<option value="LIMITED">Limited</option>
<option value="FULL">Full</option>
</select>
</div>
<div id="hospitalList" class="hospital-grid"></div>
<a class="btn blue" target="_blank" href="https://www.google.com/maps/search/hospitals+in+Nagpur">SEARCH ALL NAGPUR HOSPITALS ON MAPS</a>
</section>

<section id="twists">
<h2>🚨 Hackathon Twist Solutions</h2>
<div class="twists">

<div class="twist">
<h3>1️⃣ Emergency Surge</h3>
<p>Prioritize RED patients and distribute the load across hospitals.</p>
<button class="btn red" onclick="emergencySurge()">SIMULATE SURGE</button>
<div id="surgeResult"></div>
</div>

<div class="twist">
<h3>2️⃣ Network Blackout</h3>
<p>Keep essential hospital information available locally during network failure.</p>
<button class="btn dark" onclick="offlineMode()">ENABLE OFFLINE MODE</button>
<div id="offlineResult"></div>
</div>

<div class="twist">
<h3>3️⃣ Hospital Overflow</h3>
<p>Redirect patients from full hospitals to available alternatives.</p>
<button class="btn blue" onclick="hospitalOverflow()">SIMULATE OVERFLOW</button>
<div id="overflowResult"></div>
</div>

<div class="twist">
<h3>4️⃣ Golden Hour</h3>
<p>Use location and navigation to reach an emergency hospital faster.</p>
<button class="btn green" onclick="goldenHour()">START GOLDEN HOUR</button>
<div id="goldenResult"></div>
</div>

</div>
</section>
</div>

<footer>
<h3>MedAssist Nagpur</h3>
<p>Smart Emergency Healthcare Assistance Platform</p>
<p>Demo capacity data must be verified before real-world emergency use.</p>
</footer>

<script>
const hospitals = {{ hospitals | tojson }};

function showPanel(id){
    document.querySelectorAll(".panel").forEach(function(p){p.style.display="none";});
    const p=document.getElementById(id);
    if(p){p.style.display="block";p.scrollIntoView({behavior:"smooth",block:"center"});}
}

function renderHospitals(){
    const search=document.getElementById("hospitalSearch").value.toLowerCase();
    const type=document.getElementById("typeFilter").value;
    const status=document.getElementById("statusFilter").value;
    const list=document.getElementById("hospitalList");

    const filtered=hospitals.filter(function(h){
        const text=(h.name+" "+h.area+" "+h.specialties+" "+h.type).toLowerCase();
        return text.includes(search) &&
               (type==="all" || h.type===type) &&
               (status==="all" || h.status===status);
    });

    if(filtered.length===0){
        list.innerHTML='<div class="hospital"><h3>No hospital found</h3><p>Try another name, area or specialization.</p></div>';
        return;
    }

    list.innerHTML=filtered.map(function(h){
        const call=h.phone ? '<a class="btn green" href="tel:'+h.phone+'">CALL HOSPITAL</a>' : '';
        const emergency=h.emergency ? '<a class="btn red" href="tel:'+h.emergency+'">EMERGENCY CALL</a>' : '';
        const maps='https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(h.name+" Nagpur");

        return '<div class="hospital">'+
            '<span class="badge">'+h.status+'</span>'+
            '<h3>'+h.name+'</h3>'+
            '<p><b>Type:</b> '+h.type+'</p>'+
            '<p><b>Area:</b> '+h.area+'</p>'+
            '<p><b>Specialization:</b> '+h.specialties+'</p>'+
            '<p><b>Demo Emergency Capacity:</b> '+h.beds+' patients</p>'+
            call+emergency+
            '<a class="btn blue" target="_blank" href="'+maps+'">MAP</a>'+
            '</div>';
    }).join("");
}

function emergencySurge(){
    const red=parseInt(prompt("RED / critical patients:","50"))||0;
    const yellow=parseInt(prompt("YELLOW patients:","80"))||0;
    const green=parseInt(prompt("GREEN patients:","100"))||0;
    const total=red+yellow+green;

    document.getElementById("surgeResult").innerHTML=
        '<div class="result"><b>Surge Simulation</b>'+
        '<p>Total patients: '+total+'</p>'+
        '<p>🔴 RED: '+red+'</p>'+
        '<p>🟡 YELLOW: '+yellow+'</p>'+
        '<p>🟢 GREEN: '+green+'</p>'+
        '<p>Priority: RED → YELLOW → GREEN</p></div>';
}

function offlineMode(){
    localStorage.setItem("medassistOffline","true");
    document.getElementById("offlineResult").innerHTML=
        '<div class="result"><b>🟢 OFFLINE MODE ACTIVE</b>'+
        '<p>Local hospital information remains available.</p>'+
        '<p>Emergency number: <b>108</b></p></div>';
}

function hospitalOverflow(){
    const alternatives=hospitals.slice(5,10);
    let html='<div class="result"><b>Hospital Overflow Simulation</b>'+
        '<p>Major hospitals are simulated as FULL.</p>'+
        '<p>Suggested alternatives:</p><ul>';

    alternatives.forEach(function(h){html+='<li>'+h.name+'</li>';});
    html+='</ul></div>';

    document.getElementById("overflowResult").innerHTML=html;
}

function goldenHour(){
    if(!navigator.geolocation){
        document.getElementById("goldenResult").innerHTML='<div class="result">Location is not supported.</div>';
        return;
    }

    navigator.geolocation.getCurrentPosition(
        function(pos){
            const lat=pos.coords.latitude;
            const lon=pos.coords.longitude;
            const destination=encodeURIComponent(hospitals[0].name+" Nagpur");
            const maps="https://www.google.com/maps/dir/?api=1&origin="+lat+","+lon+"&destination="+destination;

            document.getElementById("goldenResult").innerHTML=
                '<div class="result"><b>🟢 Golden Hour Mode Activated</b>'+
                '<p>Location detected.</p>'+
                '<p>Suggested hospital: <b>'+hospitals[0].name+'</b></p>'+
                '<a class="btn green" target="_blank" href="'+maps+'">OPEN EMERGENCY ROUTE</a></div>';
        },
        function(){
            document.getElementById("goldenResult").innerHTML=
                '<div class="result">Location permission was not given. You can still use the hospital directory.</div>';
        }
    );
}

function getLocation(){
    if(!navigator.geolocation){alert("Location is not supported.");return;}
    navigator.geolocation.getCurrentPosition(
        function(pos){
            alert("Location detected successfully!\\nLatitude: "+pos.coords.latitude+"\\nLongitude: "+pos.coords.longitude);
        },
        function(){alert("Location permission was not given.");}
    );
}

renderHospitals();
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, hospitals=HOSPITALS)

@app.route("/api/hospitals")
def api_hospitals():
    return jsonify(HOSPITALS)

@app.route("/api/status")
def api_status():
    return jsonify({
        "system": "MedAssist",
        "status": "ONLINE",
        "ambulance": "108",
        "hospital_count": len(HOSPITALS)
    })

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
