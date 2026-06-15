import streamlit as st

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="SatChange AI",
    page_icon="🛰️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* Hide sidebar */
section[data-testid="stSidebar"] {
    display: none !important;
}

/* Hide expand button (>>) */
[data-testid="collapsedControl"] {
    display: none !important;
}

/* Hide page navigation */
[data-testid="stSidebarNav"] {
    display: none !important;
}

/* Hide header */
header[data-testid="stHeader"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)
# ================= CSS =================

st.markdown("""
<style>

/* ================= BACKGROUND ================= */

.stApp{
    background: linear-gradient(to bottom,#000814,#001d3d);
    color:white;
    overflow-x:hidden;
}

/* Hide Streamlit Default */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* ================= TITLE ================= */

/* ================= TITLE EFFECT ================= */

.main-title{

    text-align:center;

    font-size:82px;

    font-weight:900;

    margin-top:-15px;

    margin-bottom:10px;

    background: linear-gradient(
        90deg,
        #60a5fa,
        #3b82f6,
        #8b5cf6,
        #ec4899
    );

    -webkit-background-clip:text;

    -webkit-text-fill-color:transparent;

    text-shadow:
        0 0 35px rgba(59,130,246,0.35);

    letter-spacing:1px;

    transition:0.5s ease;

    cursor:pointer;
}

/* Hover Effect */

.main-title:hover{

    transform:
        scale(1.04)
        translateY(-4px);

    text-shadow:
        0 0 50px rgba(96,165,250,0.8),
        0 0 80px rgba(168,85,247,0.55);
}

/* ================= SUBTITLE ================= */

.sub-title{

    text-align:center;

    color:#cbd5e1;

    font-size:24px;

    margin-top:-5px;

    margin-bottom:70px;

    font-weight:500;

    transition:0.4s ease;

    letter-spacing:0.5px;
}

.sub-title:hover{

    color:#93c5fd;

    transform:scale(1.02);
}

/* ================= AUTH CARDS ================= */

.auth-card{
    background: rgba(15,23,42,0.92);

    border:1px solid rgba(255,255,255,0.08);

    border-radius:28px;

    padding:45px 30px;

    text-align:center;

    min-height:330px;

    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    transition:0.4s ease;

    box-shadow:0 10px 25px rgba(0,0,0,0.35);
}

/* Hover Effect */
.auth-card:hover{
    transform:translateY(-12px) scale(1.03);

    border:1px solid rgba(59,130,246,0.45);

    box-shadow:0 22px 45px rgba(37,99,235,0.35);
}

/* Icon */
.auth-icon{
    font-size:75px;

    margin-bottom:22px;

    transition:0.4s ease;
}

.auth-card:hover .auth-icon{
    transform:scale(1.12) rotate(8deg);
}

/* Title */
.auth-title{
    font-size:38px;

    font-weight:800;

    color:white;

    margin-bottom:15px;
}

/* Text */
.auth-text{
    color:#cbd5e1;

    font-size:17px;

    line-height:1.8;

    max-width:85%;
}

/* ================= BUTTON ================= */

.stButton > button{
    width:100%;

    border:none;

    border-radius:16px;

    padding:0.95rem 1rem;

    font-size:18px;

    font-weight:700;

    color:white;

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6,
        #6366f1
    );

    transition:0.3s ease;

    box-shadow:0 10px 25px rgba(37,99,235,0.35);

    margin-top:15px;
}

.stButton > button:hover{
    transform:scale(1.05);

    box-shadow:0 16px 35px rgba(37,99,235,0.55);
}

/* ================= SECTION TITLE ================= */

.section-title{
    text-align:center;

    font-size:48px;

    font-weight:800;

    color:white;

    margin-top:90px;

    margin-bottom:50px;
}

/* ================= FEATURE CARDS ================= */

.feature-card{
    background: rgba(15,23,42,0.92);

    border-radius:26px;

    padding:40px 25px;

    text-align:center;

    height:650px;

    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    align-items:center;

    border:1px solid rgba(255,255,255,0.08);

    transition:0.4s ease;

    box-shadow:0 10px 25px rgba(0,0,0,0.3);
}

/* Hover */
.feature-card:hover{
    transform:translateY(-12px) scale(1.03);

    border:1px solid rgba(59,130,246,0.45);

    box-shadow:0 20px 40px rgba(37,99,235,0.35);
}

/* Feature Icon */
.feature-icon{
    font-size:85px;

    margin-top:20px;

    margin-bottom:30px;

    transition:0.4s ease;
}

.feature-card:hover .feature-icon{
    transform:scale(1.15) rotate(6deg);
}

/* Feature Title */
.feature-title{
    font-size:40px;

    font-weight:800;

    color:white;

    margin-top:25px;

    margin-bottom:25px;

    min-height:110px;

    display:flex;
    align-items:center;
    justify-content:center;

    text-align:center;
}

/* Feature Text */
.feature-text{
    color:#cbd5e1;

    line-height:1.9;

    font-size:18px;

    max-width:90%;

    margin:auto;

    min-height:140px;

    text-align:center;
}

/* ================= FOOTER ================= */

.footer {

    width: 100%;

    background: rgba(15,23,42,0.92);

    color: white;

    text-align: center;

    padding: 28px;

    font-size: 18px;

    border-top: 1px solid rgba(255,255,255,0.1);

    border-radius: 30px 30px 0px 0px;

    margin-top: 50px;

    margin-bottom: -1000px;
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================

st.markdown("""
<div class="main-title">
🛰️ SatChange AI
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="sub-title">
AI Powered Satellite Change Detection Platform
</div>
""", unsafe_allow_html=True)

# ================= LOGIN / SIGNUP =================

col1, col2 = st.columns(2, gap="large")

# LOGIN CARD
with col1:

    st.markdown(
        '<div class="auth-card">'
        '<div class="auth-icon">🔐</div>'
        '<div class="auth-title">Login</div>'
        '<div class="auth-text">Access your satellite analytics dashboard, heatmaps and AI reports instantly.</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button("🚀 Continue To Login", key="login_btn"):
        st.switch_page("pages/Login.py")

# SIGNUP CARD
with col2:

    st.markdown(
        '<div class="auth-card">'
        '<div class="auth-icon">👤</div>'
        '<div class="auth-title">Signup</div>'
        '<div class="auth-text">Create your AI account and start detecting satellite changes with AI.</div>'
        '</div>',
        unsafe_allow_html=True
    )

    if st.button("✨ Create Account", key="signup_btn"):
        st.switch_page("pages/Signup.py")

# ================= FEATURES =================

st.markdown("""
<div class="section-title">
✨ Platform Features
</div>
""", unsafe_allow_html=True)

f1, f2, f3 = st.columns(3, gap="large")

# FEATURE 1
with f1:

    st.markdown(
        '<div class="feature-card">'
        '<div class="feature-icon">🌍</div>'
        '<div class="feature-title">Change Detection</div>'
        '<div class="feature-text">Detect land and environmental changes using Deep Learning models.</div>'
        '</div>',
        unsafe_allow_html=True
    )

# FEATURE 2
with f2:

    st.markdown(
        '<div class="feature-card">'
        '<div class="feature-icon">🔥</div>'
        '<div class="feature-title">Heatmaps</div>'
        '<div class="feature-text">Generate AI heatmaps for satellite image visualization.</div>'
        '</div>',
        unsafe_allow_html=True
    )

# FEATURE 3
with f3:

    st.markdown(
        '<div class="feature-card">'
        '<div class="feature-icon">📊</div>'
        '<div class="feature-title">Analytics</div>'
        '<div class="feature-text">Analyze changed area percentage and pixel statistics instantly.</div>'
        '</div>',
        unsafe_allow_html=True
    )


# ================= FOOTER =================

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)