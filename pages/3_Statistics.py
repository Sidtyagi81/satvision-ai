import streamlit as st
import numpy as np
from sidebar import render_sidebar

st.set_page_config(
    page_title="Statistics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= CSS =================

st.markdown("""
<style>

/* ================= HIDE STREAMLIT ================= */

[data-testid="stSidebarNav"]{
    display:none !important;
}

[data-testid="stSidebarCollapseButton"]{
    display:none !important;
}

[data-testid="stAppDeployButton"]{
    display:none !important;
}

[data-testid="stToolbar"]{
    display:none !important;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* ================= MAIN APP ================= */

.stApp{
    background:
    radial-gradient(circle at top left,
    rgba(37,99,235,0.15),
    transparent 40%),
    linear-gradient(
    135deg,
    #020617,
    #071330,
    #020617
    );

    color:white;
}

/* ================= CONTAINER ================= */

.block-container{
    padding-top:1rem !important;
    padding-left:3rem !important;
    padding-right:3rem !important;
    max-width:1400px;
}

/* ================= TITLES ================= */

h1{
    font-size:3rem !important;
    font-weight:800 !important;
    color:white !important;
    letter-spacing:-1px;
}

h2{
    font-weight:700 !important;
    color:white !important;
}

h3{
    font-weight:600 !important;
    color:#e2e8f0 !important;
}

/* ================= SIDEBAR ================= */

section[data-testid="stSidebar"]{

    background:
    linear-gradient(
    180deg,
    #0f172a,
    #111827
    );

    border-right:
    1px solid rgba(255,255,255,0.08);

    box-shadow:
    5px 0px 30px rgba(0,0,0,0.35);
}

/* ================= BUTTONS ================= */

.stButton button{

    width:100%;

    height:58px;

    border-radius:18px;

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    color:white;

    font-size:18px;

    font-weight:600;

    transition:all .3s ease;
}

.stButton button:hover{

    transform:translateY(-3px);

    background:
    rgba(59,130,246,0.15);

    border:
    1px solid #3b82f6;

    box-shadow:
    0 8px 25px rgba(59,130,246,0.25);
}

/* ================= INPUTS ================= */

.stTextInput input{

    border-radius:16px !important;

    background:
    rgba(255,255,255,0.05) !important;

    color:white !important;

    border:
    1px solid rgba(255,255,255,0.1) !important;

    padding:12px !important;
}

.stTextInput input:focus{

    border:
    1px solid #3b82f6 !important;

    box-shadow:
    0 0 15px rgba(59,130,246,0.4);
}

/* ================= METRICS ================= */

[data-testid="metric-container"]{

    background:
    linear-gradient(
    145deg,
    rgba(15,23,42,0.95),
    rgba(30,41,59,0.95)
    );

    border:
    1px solid rgba(255,255,255,0.08);

    border-radius:22px;

    padding:25px;

    box-shadow:
    0 10px 25px rgba(0,0,0,0.25);

    transition:all .3s ease;
}

[data-testid="metric-container"]:hover{

    transform:translateY(-5px);

    border:
    1px solid #3b82f6;
}

/* ================= DATAFRAME ================= */

[data-testid="stDataFrame"]{

    border-radius:20px !important;

    overflow:hidden !important;

    border:
    1px solid rgba(255,255,255,0.08);
}

/* ================= SUCCESS ================= */

.stSuccess{

    border-radius:18px;

    border-left:
    5px solid #22c55e;
}

/* ================= WARNING ================= */

.stWarning{

    border-radius:18px;

    border-left:
    5px solid #eab308;
}
            
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

/* ================= ERROR ================= */

.stError{

    border-radius:18px;

    border-left:
    5px solid #ef4444;
}

/* ================= INFO ================= */

.stInfo{

    border-radius:18px;

    border-left:
    5px solid #3b82f6;
}

/* ================= CODE BLOCK ================= */

pre{

    border-radius:20px !important;

    border:
    1px solid rgba(255,255,255,0.08);

    background:
    #111827 !important;
}

/* ================= SCROLLBAR ================= */

::-webkit-scrollbar{
    width:10px;
}

::-webkit-scrollbar-track{
    background:#0f172a;
}

::-webkit-scrollbar-thumb{
    background:#334155;
    border-radius:20px;
}

::-webkit-scrollbar-thumb:hover{
    background:#3b82f6;
}

</style>
""", unsafe_allow_html=True)

# ================= PROFILE =================

username = st.session_state.get(
    "username",
    "User"
)

username = st.session_state.get(
    "username",
    "User"
)
render_sidebar(username)

col1, col2 = st.columns([1,5])

with col1:

    if st.button("⬅ Back"):

        st.switch_page(
            "pages/1_Dashboard.py"
        )

# ================= TITLE =================

st.title("📊 Statistics")

# ================= CHECK ANALYSIS =================

if "mask" not in st.session_state:

    st.error(
        "No analysis available."
    )

    st.info(
        "Please go to Dashboard, upload images and click 'Run Change Detection'."
    )

    if st.button(
        "🏠 Go To Dashboard",
        width="stretch"
    ):
        st.switch_page(
            "pages/1_Dashboard.py"
        )

    st.stop()

# ================= LOAD DATA =================

binary_mask = st.session_state.mask

changed_pixels = int(
    np.sum(binary_mask)
)

total_pixels = int(
    binary_mask.shape[0] *
    binary_mask.shape[1]
)

change_percentage = (
    changed_pixels /
    total_pixels
) * 100

unchanged_pixels = (
    total_pixels -
    changed_pixels
)

# ================= METRICS =================

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "Changed Area",
        f"{change_percentage:.2f}%"
    )

with m2:
    st.metric(
        "Changed Pixels",
        f"{changed_pixels:,}"
    )

with m3:
    st.metric(
        "Unchanged Pixels",
        f"{unchanged_pixels:,}"
    )

with m4:
    st.metric(
        "Model",
        "U-Net"
    )

st.markdown("---")

# ================= SUMMARY =================

col1, col2 = st.columns(2)

with col1:

    st.subheader("📈 Detection Summary")

    st.write(
        f"Total Pixels: {total_pixels:,}"
    )

    st.write(
        f"Changed Pixels: {changed_pixels:,}"
    )

    st.write(
        f"Unchanged Pixels: {unchanged_pixels:,}"
    )

    st.write(
        f"Change Percentage: {change_percentage:.2f}%"
    )

with col2:

    st.subheader("⚡ Severity")

    if change_percentage > 50:

        st.error(
            "High Change Detected"
        )

    elif change_percentage > 20:

        st.warning(
            "Medium Change Detected"
        )

    else:

        st.success(
            "Low Change Detected"
        )

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)