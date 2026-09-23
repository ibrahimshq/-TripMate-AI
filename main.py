import streamlit as st
from google import genai
from dotenv import load_dotenv
load_dotenv(r"/Users/mohammadibrahimmohammadishaque/python.py/.env")

client = genai.Client()


# =========================================================
# 🎨 CUSTOM DESIGN
# =========================================================

st.markdown("""
<style>

/* ================= BACKGROUND ================= */

.stApp {
    background: linear-gradient(
        -45deg,
        #0f2027,
        #203a43,
        #2c5364,
        #00c6ff
    );

    background-size: 400% 400%;
    animation: gradient 15s ease infinite;
}

@keyframes gradient {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}


/* ================= FLOATING TITLE ================= */

.travel-title {
    text-align: center;
    font-size: 55px;
    font-weight: 900;
    margin-top: 20px;
    margin-bottom: 5px;

    background: linear-gradient(
        90deg,
        #ffffff,
        #00c6ff,
        #ffffff
    );

    background-size: 200% auto;

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation:
        float 3s ease-in-out infinite,
        shine 4s linear infinite;
}


.travel-subtitle {
    text-align: center;
    font-size: 19px;
    color: rgba(255,255,255,0.85);
    margin-bottom: 35px;
}


@keyframes float {

    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }

    100% {
        transform: translateY(0px);
    }
}


@keyframes shine {

    0% {
        background-position: 0% center;
    }

    100% {
        background-position: 200% center;
    }
}


/* ================= GLASS CARD ================= */

.travel-card {

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);

    border-radius: 25px;

    padding: 30px;

    border: 1px solid rgba(255,255,255,0.25);

    box-shadow:
        0 10px 40px rgba(0,0,0,0.25);

    margin-bottom: 25px;
}


/* ================= MOVING TRAVEL ICONS ================= */

.stApp::before {

    content: "✈️     ☁️          🌎       ☁️       ✈️";

    position: fixed;

    top: 15%;
    left: -100%;

    width: 200%;

    font-size: 35px;

    opacity: 0.15;

    animation: fly 25s linear infinite;

    pointer-events: none;

    z-index: 0;
}


@keyframes fly {

    from {
        transform: translateX(-20%);
    }

    to {
        transform: translateX(60%);
    }
}


/* ================= BUTTON ================= */

.stButton > button {

    width: 100%;

    border-radius: 15px;

    border: none;

    padding: 12px;

    font-size: 18px;

    font-weight: 700;

    background: linear-gradient(
        90deg,
        #00c6ff,
        #0072ff
    );

    color: white;

    box-shadow:
        0 5px 20px rgba(0,114,255,0.4);

    transition: 0.3s;
}


.stButton > button:hover {

    transform: translateY(-3px);

    box-shadow:
        0 8px 30px rgba(0,198,255,0.6);
}


/* ================= TEXT ================= */

label {
    color: white !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ✈️ TITLE
# =========================================================

st.markdown("""
<div class="travel-title">
    ✈️ TripMate
</div>

<div class="travel-subtitle">
    🌎 Your AI-powered travel planner
</div>
""", unsafe_allow_html=True)


# =========================================================
# 🧳 TRAVEL INPUTS
# =========================================================

st.markdown("""
<div class="travel-card">

<h2 style="text-align:center; color:white;">
🌎 Plan Your Dream Trip
</h2>

<p style="text-align:center; color:rgba(255,255,255,0.8);">
Tell us about your journey and let AI create your perfect itinerary ✈️
</p>

</div>
""", unsafe_allow_html=True)


trips = st.text_input( "📍 Where is your destination?")

days = st.number_input("📅 Number of days:",min_value=1,max_value=30)

travelers = st.selectbox("👥 Who is traveling?",["Solo", "Couple", "Family with kids","Family with only adults","Group of friends"])

interests = st.multiselect("🎯 What are your travel interests?",["Relaxation","Adventure","Trekking", "Skiing", "Culture", "Food", "Shopping","Nature"])

budget = st.select_slider("💰 What is your approximate budget?",["Budget-friendly","Mid-range comfort","Luxury / Splurge"])

season = st.selectbox( "🌤️ What time of the year are you planning to visit?",["Spring","Summer", "Autumn","Winter"])


# =========================================================
# 🤖 AI PROMPT
# =========================================================

prompt = f"""
You are a friendly, knowledgeable, and helpful travel planner.

Create a personalized travel plan for:

Destination: {trips}
Number of days: {days}

Traveler information:
- Who is traveling: {travelers}
- Travel interests: {", ".join(interests)}
- Budget: {budget}
- Time of year: {season}

Follow these guidelines:

1. Communicate in a friendly, natural and helpful manner.
2. Briefly describe the destination in 1-2 appealing lines.
3. Create a practical day-by-day itinerary.
4. Include:
   - Places to visit
   - Things to do
   - Suggested duration
   - Food recommendations
   - Transportation
   - Approximate budget when possible
   - Useful travel tips
5. Organize the response using clear headings,
   bullet points and numbered lists.
6. Keep the response easy to read.
7. Adapt everything to the traveler's interests,
   budget, group type and season.
8. Never pretend you checked live prices,
   hotel availability, flights or weather.
9. Make the itinerary practical rather than
   unnecessarily detailed.

Make the response engaging, practical and easy to follow.
"""


# =========================================================
# 🚀 BUTTON
# =========================================================

if st.button("🚀 Start Planning"):

    if not trips:
        st.warning("📍 Please enter your destination first!")

    else:
         # ✈️ Travel animation
        st.markdown("""
        <style>

        .plane {
        position: fixed;
        font-size: 250px;
        left: 50%;
        bottom: -80px;
        transform: translateX(-50%) rotate(-45deg);
        animation: takeoff 3s ease-in-out forwards;
        z-index: 9999;
        }

        @keyframes takeoff {

        0% {
         bottom: -80px;
         opacity: 0;
         transform: translateX(-50%) rotate(-45deg);
        }

        15% {
        opacity: 1;
        }

        50% {
        bottom: 40%;
        transform: translateX(-50%) rotate(-45deg);
        }

        100% {
        bottom: 110%;
        opacity: 0;
        transform: translateX(-50%) rotate(-45deg);
        }

       }

       </style>

       <div class="plane">✈️</div>
       """, unsafe_allow_html=True)

         # 🤖 Loading while Gemini generates
        with st.spinner("✈️ Flying to your destination... 🗺️"): 
            interaction = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt,
            extra_body={
                        "generation_config": {
                         "temperature": 0.7,
                         "top_k": 20,
                         "max_output_tokens": 1000
                        }
                       }
                )
        st.markdown("""
        <div class="travel-card">
        <h2 style="color:white;">
        🧳 Your Trip
        </h2>
        </div>
        """, unsafe_allow_html=True)

        st.write("**📍 Destination:**", trips)
        st.write("**📅 Duration:**", days, "days")

        st.write(interaction.output_text)

        st.success("🌴 Happy vacations mate! ✈️")