from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_ANIMATION = ASSETS / "animation_newyear.json"


# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="🌟", font_size=20, falling_speed=5, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["from WRWS"])[0]


# Page configuration
st.set_page_config(page_title="Happy Holidays", page_icon="🎉")

# Run snowfall animation
run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display header with personalized name
PERSON_NAME = get_person_name()
_= """
st.header(f"Happy Holidays, {PERSON_NAME}! "🎉", anchor=False)
"""
header_html = f"<h1 style='color: red;'>Happy Holidays, {PERSON_NAME}! 🎄</h1>"
st.markdown(header_html, unsafe_allow_html=True)

# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

# Personalized holiday message
st.markdown(
    f"Dear <span style='color: red; font-size: 40px'>{PERSON_NAME}</span>, wishing you a wonderful holiday season filled with joy and peace. 🌟",
    unsafe_allow_html=True
)
