import streamlit as st
from database import login_user

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
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

st.set_page_config(
    page_title="Home",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
[data-testid="collapsedControl"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ================= BACK BUTTON =================

col1, col2 = st.columns([1, 8])

with col1:
    if st.button("⬅ Back"):
        st.switch_page("app.py")   # Change if your home page filename is different

# ================= CSS ================= #

st.markdown("""
<style>

/* ================= HIDE STREAMLIT ================= */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stAppDeployButton {
    display: none;
}

/* ================= MAIN BACKGROUND ================= */

.stApp {

    background: linear-gradient(
        135deg,
        #020617,
        #071226,
        #0f172a
    );

    color: white;
}

/* ================= PAGE WIDTH ================= */

.block-container {

    max-width: 1600px !important;

    padding-top: 2rem !important;

    padding-bottom: 2rem !important;

    margin: auto !important;
}

/* ================= TEXT ================= */

h1,h2,h3,h4,h5,h6,p,label {

    color: white !important;
}

/* BIGGER INPUT LABELS */

div[data-testid="stTextInput"] label p {

    font-size: 36px !important;

    font-weight: 700 !important;

    color: white !important;
}

/* ================= INPUT BOX ================= */

.stTextInput div[data-baseweb="input"] {

    background-color: #1e293b !important;

    border-radius: 16px !important;

    border: 1px solid #334155 !important;

    height: 70px !important;

    overflow: hidden !important;
}

/* ================= INPUT FIELD ================= */

.stTextInput input {

    background: transparent !important;

    border: none !important;

    color: white !important;

    height: 70px !important;

    font-size: 22px !important;

    padding: 0 20px !important;

    width: 100% !important;
}

/* ================= REMOVE INPUT MESSAGE ================= */

[data-testid="InputInstructions"] {

    display: none !important;
}

/* ================= REMOVE PASSWORD EYE ================= */

# button[aria-label="Show password text"],
# button[aria-label="Hide password text"] {

#     display: none !important;

#     width: 0px !important;

#     padding: 0px !important;

#     margin: 0px !important;
# }

/* ================= CONTAINER CARD ================= */

[data-testid="stVerticalBlockBorderWrapper"] {

    border-radius: 25px !important;

    border: 1px solid rgba(255,255,255,0.10) !important;

    background: rgba(255,255,255,0.03) !important;

    padding: 45px !important;

    box-shadow:
        0px 8px 30px rgba(0,0,0,0.35);
}

/* ================= BUTTON ================= */

.stButton>button {

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 16px !important;

    width: 100% !important;

    padding: 22px !important;

    font-size: 24px !important;

    font-weight: bold !important;

    transition: 0.3s ease !important;

    box-shadow:
        0 0 25px rgba(59,130,246,0.40);
}

.stButton>button:hover {

    transform: translateY(-4px);

    box-shadow:
        0 0 40px rgba(59,130,246,0.70);
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

# ================= HEADER ================= #

st.markdown("""
<h1 style="
text-align:center;
font-size:90px;
font-weight:900;
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
">
🛰️ SatChange AI
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:28px;
color:#cbd5e1;
margin-bottom:70px;
">
AI Powered Satellite Change Detection Platform
</p>
""", unsafe_allow_html=True)

# ================= CENTER LOGIN FORM ================= #

left_space, center_col, right_space = st.columns([0.5,4,0.5])

with center_col:

    with st.container(border=True):

        st.markdown("""
        <h1 style="
        text-align:center;
        font-size:55px;
        font-weight:800;
        margin-bottom:10px;
        color:white;
        ">
        🔐 Login
        </h1>

        <p style="
        text-align:center;
        font-size:20px;
        color:#cbd5e1;
        margin-bottom:50px;
        ">
        Access your AI dashboard and satellite analytics.
        </p>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        login_btn = st.button(
            "🚀 Login",
            width="stretch"
        )

        # ================= LOGIN ================= #

        if login_btn:

            user = login_user(
                username,
                password
            )

            if user:

                st.session_state.authenticated = True

                st.session_state.username = username

                st.success(
                    "🎉 Login Successful"
                )

                st.balloons()

                st.switch_page(
                    "pages/1_Dashboard.py"
                )

            else:

                st.error(
                    "Invalid Username or Password"
                )

# ================= SIGNUP BUTTON ================= #

st.markdown("<br><br>", unsafe_allow_html=True)

left_btn, center_btn, right_btn = st.columns([0.5,4,0.5])

with center_btn:

    if st.button(
        "✨ Create New Account",
        width="stretch"
    ):

        st.switch_page(
            "pages/Signup.py"
        )

# ================= FOOTER ================= #

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)