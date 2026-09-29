import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

st.markdown("""
<style>

/* Hide Streamlit header */
header{
    visibility:hidden;
}

/* Remove top padding */
.block-container{
    padding-top:0rem;
    padding-left:2rem;
    padding-right:2rem;
    padding-bottom:0rem;
}

/* Main page */
.stApp{
    background-color:rgb(29,29,31);
    min-height:100vh;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#171717;
    border-right:2px solid #2b2b2b;
    width:300px;
    margin-top: -70px;
}

/* Sidebar content */
[data-testid="stSidebar"] > div:first-child{
    background:#171717;
    height:100vh;
    padding-top:20px;

}

/* Logo */
[data-testid="stSidebar"] img{
    margin-left:-25px;
    margin-bottom:30px;
    margin-top:-20px;
}

/* Sidebar menu items */
[data-testid="stSidebar"] .css-1d391kg{
    color:#fff;
    font-size:18px;
    font-weight:600;
    padding:10px 20px;
    border-radius:5px;
    margin-top:-70px;
}
.st-ak {
    gap: 38px;
    margin-top: -70px;
}

/* img */
image{
    margin-top:-70px;
    margin-right:20px;
}

.st-emotion-cache-3uj0rx {
    font-family: "Source Sans", sans-serif;
    font-size: 1.25rem;
    margin-bottom: -1rem;
    color: floralwhite;
    max-width: 100%;
    overflow-wrap: break-word;
    font-size: 25px;
    font-style: oblique;

}


.st-emotion-cache-r3ry0f {
    display: flex;
    gap: 4rem;
    width: 100%;
    max-width: 100%;
    height: auto;
    min-width: 1rem;
    flex-flow: wrap;
    flex: 1 1 0%;
    -webkit-box-align: stretch;
    align-items: stretch;
    -webkit-box-pack: start;
    justify-content: start;
    overflow: visible;
    # background: black;
    border-radius: 25px;

.st-emotion-cache-gi0tri et2rgd23{
    font-family: "Source Sans", sans-serif;
    font-size: 1.25rem;}    

</style>
""", unsafe_allow_html=True)

# ================= Sidebar =================

st.sidebar.image("logo pic.png", width=180)

menu = st.sidebar.radio(
    "",
    [
        "📊 Dashboard",
        "🛒 Products",
        "📦 Categories",
        "👥 Customers",
        "📦 Orders",
        "🏷️ Coupons",
        "👨‍💼 Staff",
    ],
)

# ================= Main Page =================
left, bell, moon, profile = st.columns([10, 1, 1, 1])
with left:
    st.image("icons8-menu-50 (2).png", width=25)

with bell:
    st.markdown("<h3 style='text-align:center;'>🔔</h3>", unsafe_allow_html=True)

with moon:
    st.markdown("<h3 style='text-align:center;'>🌙</h3>", unsafe_allow_html=True)

with profile:
    st.markdown("<h3 style='text-align:center;'>👤</h3>", unsafe_allow_html=True)

st.markdown("Dashboard Overview")
col1, col2, col3, col4, col5 = st.columns(5, gap="large")

with col1:
    st.markdown("""
    <div class="metric-card" style="background:#18a39b;border-radius: 10px; padding: 5px; color: #fff;">
        <div class="icon">📦</div>
        <div class="title">Today Orders</div>
        <div class="value">$1,200</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="background:#ff9838;border-radius: 10px; padding: 5px; color: #fff; ">
        <div class="icon">📦</div>
        <div class="title">Y day Orders</div>
        <div class="value">$850</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card" style="background:#3f7df2;border-radius: 10px; padding: 5px; color: #fff;  ">
        <div class="icon">🔄</div>
        <div class="title">This Month</div>
        <div class="value">$32,000</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card" style="background:#f23f3f;border-radius: 10px; padding: 5px; color: #fff; ">
        <div class="icon">📈</div>
        <div class="title">Last Month</div>
        <div class="value">$28,500</div>
    </div>
    """, unsafe_allow_html=True)    

with col5:
    st.markdown("""
    <div class="metric-card" style="background:#f2c23f;border-radius: 10px; padding: 5px; color: #fff; ">
        <div class="icon">💰</div>
        <div class="title">Total sales</div>
        <div class="value">$120,000</div>
    </div>
    """, unsafe_allow_html=True)


colu1, colu2, colu3, colu4, colu5 = st.columns(5, gap="large")    
with colu1:
    st.markdown("""
    <div class="metric-card" style="background: rgb(35 39 39);border-radius: 10px; padding: 5px; color: #fff; font-weight: 100;margin: 20px;width: 100%;height: 100%;font-size:15px;">
        <div class="icon",>📦</div>
        <div class="title">Total Orders</div>
        <div class="value">$1,200</div>
    </div>
    """, unsafe_allow_html=True)

with colu2:
    st.markdown("""
    <div class="metric-card" style="background: rgb(35 39 39);border-radius: 10px; padding: 5px; color: #fff;font-weight: 100;margin: 20px;width: 100%;height: 100%; font-size:15px;">
        <div class="icon">📦</div>
        <div class="title">Order pending</div>
        <div class="value">$850</div>
    </div>
    """, unsafe_allow_html=True)    

with colu3:
    st.markdown("""
    <div class="metric-card" style="background: rgb(35 39 39);border-radius: 10px; padding: 5px; color: #fff; font-weight: 100;margin: 20px; width: 100%;height: 100%;font-size:15px;">
        <div class="icon">🔄</div>
        <div class="title">Order processing</div>
        <div class="value">$32,000</div>
    </div>
    """, unsafe_allow_html=True)

with colu4:
    st.markdown("""
    <div class="metric-card" style="background: rgb(35 39 39) ;border-radius: 10px; padding: 5px; color: #fff; font-weight: 100;margin: 20px; width: 100%;height: 100%;font-size:15px;">
        <div class="icon">📈</div>
        <div class="title"> Order delivered</div>
        <div class="value">$28,500</div>
    </div>
    """, unsafe_allow_html=True)    

with colu5:
    st.markdown("""
    <div class="metric-card" style="background: rgb(35 39 39) ;border-radius: 10px; padding: 5px; color: #fff; font-weight: 100;margin: 20px; width: 100%;height: 100%;font-size:15px;">
        <div class="icon">💰</div>
        <div class="title"> Total sales</div>
        <div class="value">$120,000</div>
    </div>
    """, unsafe_allow_html=True)    


st.image("34dc00bd-9c58-465c--removebg-preview.png")
