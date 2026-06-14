import streamlit as st
import re

from database import (
    add_user,
    user_exists
)

# ================= PAGE CONFIG ================= #

st.set_page_config(
    page_title="Signup",
    page_icon="📝",
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

    max-width: 1400px !important;

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

.stTextInput input {

    background-color: #1e293b !important;

    color: white !important;

    border-radius: 16px !important;

    border: 1px solid #334155 !important;

    height: 60px !important;

    font-size: 20px !important;

    padding: 0 20px !important;
}

/* ================= PASSWORD FIX ================= */

.stTextInput div[data-baseweb="input"] {

    display: flex !important;

    align-items: center !important;

    height: 60px !important;

    background-color: #1e293b !important;

    border-radius: 16px !important;
}

.stTextInput div[data-baseweb="base-input"] {

    display: flex !important;

    align-items: center !important;
}

/* ================= CARD ================= */

[data-testid="stVerticalBlockBorderWrapper"] {

    border-radius: 35px !important;

    border: 1px solid rgba(255,255,255,0.10) !important;

    background: rgba(255,255,255,0.04) !important;

    padding: 50px !important;

    box-shadow:
        0px 8px 30px rgba(0,0,0,0.45);
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

    border-radius: 18px !important;

    width: 100% !important;

    padding: 18px !important;

    font-size: 22px !important;

    font-weight: bold !important;

    transition: 0.3s ease !important;

    box-shadow:
        0 0 25px rgba(59,130,246,0.40);
}

.stButton>button:hover {

    transform:
        translateY(-4px);

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
            
/* REMOVE PRESS ENTER TO APPLY */

[data-testid="InputInstructions"] {
    display: none !important;
}
/* ================= PASSWORD FIX ================= */

.stTextInput div[data-baseweb="input"] {

    background-color: #1e293b !important;

    border-radius: 16px !important;

    border: 1px solid #334155 !important;

    height: 60px !important;

    overflow: hidden !important;
}

/* INPUT FIELD */

.stTextInput input {

    background: transparent !important;

    border: none !important;

    color: white !important;

    height: 60px !important;

    font-size: 20px !important;

    padding: 0 20px !important;

    width: 100% !important;
}

/* REMOVE PASSWORD EYE SPACE */

# button[aria-label="Show password text"],
# button[aria-label="Hide password text"] {

#     display: none !important;

#     width: 0px !important;

#     padding: 0px !important;

#     margin: 0px !important;
# }

</style>

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

# ================= CENTERED WIDE CARD ================= #

left_space, center_col, right_space = st.columns([0.5,4,0.5])

with center_col:

    with st.container(border=True):

        st.markdown("""
        <h1 style="
        text-align:center;
        font-size:72px;
        font-weight:bold;
        margin-bottom:50px;
        ">
        🔐 Create Account
        </h1>
        """, unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        password = st.text_input(
            "🔒 Password",
            type="password"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        confirm_password = st.text_input(
            "🔑 Confirm Password",
            type="password"
        )

        st.markdown("<br><br>", unsafe_allow_html=True)

        signup_btn = st.button(
            "✨ Create Account",
            width="stretch"
        )

        # ================= VALIDATION ================= #

        if signup_btn:

            if username == "" or password == "":

                st.error(
                    "Please fill all fields"
                )

            elif user_exists(username):

                st.error(
                    "Username already exists"
                )

            elif password != confirm_password:

                st.error(
                    "Passwords do not match"
                )

            elif len(password) < 8:

                st.error(
                    "Password must be at least 8 characters long"
                )

            elif not re.search(r"[A-Z]", password):

                st.error(
                    "Password must contain 1 uppercase letter"
                )

            elif not re.search(r"[a-z]", password):

                st.error(
                    "Password must contain 1 lowercase letter"
                )

            elif not re.search(r"[0-9]", password):

                st.error(
                    "Password must contain 1 number"
                )

            elif not re.search(
                r"[!@#$%^&*(),.?\":{}|<>]",
                password
            ):

                st.error(
                    "Password must contain 1 special character"
                )

            else:

                success = add_user(
                    username,
                    password
                )

                if success:

                    st.success(
                        "🎉 Account Created Successfully"
                    )

                    st.balloons()

                    st.switch_page(
                        "pages/Login.py"
                    )

                else:

                    st.error(
                        "Signup Failed"
                    )

# ================= LOGIN BUTTON ================= #

st.markdown("<br><br>", unsafe_allow_html=True)

left_btn, center_btn, right_btn = st.columns([0.5,4,0.5])

with center_btn:

    if st.button(
        "🚀 Continue To Login",
        width="stretch"
    ):
        st.switch_page(
            "pages/Login.py"
        )

# ================= FOOTER ================= #

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)