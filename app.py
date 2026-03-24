import streamlit as st
import feedparser
import requests

st.set_page_config(page_title="Omer Intelligence Radar", layout="wide")

st.title("🧠 Omer Intelligence Radar")

col1, col2 = st.columns(2)

# --- HAVA ---
with col1:
    st.subheader("🌤 Izmir")
    try:
        weather = requests.get("https://wttr.in/Izmir?format=3").text
        st.info(weather)
    except:
        st.warning("Weather data unavailable")

# --- EKONOMİ ---
with col2:
    st.subheader("💰 Turkish Economy")
    feed = feedparser.parse("https://www.bloomberght.com/rss")
    for item in feed.entries[:5]:
        st.markdown(f"- [{item.title}]({item.link})")

st.divider()

# --- DÜNYA ---
st.subheader("🌍 Global Events")
world = feedparser.parse("http://feeds.bbci.co.uk/news/world/rss.xml")
for item in world.entries[:5]:
    st.markdown(f"- [{item.title}]({item.link})")

# --- SPOR ---
st.subheader("🏀⚽ Sports")
sports = feedparser.parse("https://www.espn.com/espn/rss/news")
for item in sports.entries[:5]:
    st.markdown(f"- [{item.title}]({item.link})")

# --- AFET ---
st.subheader("🚨 Critical Incidents")
disaster = feedparser.parse("https://www.gdacs.org/xml/rss.xml")
for item in disaster.entries[:5]:
    st.markdown(f"- [{item.title}]({item.link})")
