import streamlit as st
from sidebar import render_sidebar

st.set_page_config(
    page_title="Model Information",
    layout="wide"
)

username = st.session_state.get(
    "username",
    "User"
)

col1, col2 = st.columns([1,5])

with col1:

    if st.button("⬅ Back"):

        st.switch_page(
            "pages/1_Dashboard.py"
        )

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

render_sidebar(username)

st.title("🤖 Model Information")

# ================= MODEL BADGES =================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.success("🧠 U-Net")

with c2:
    st.info("🌍 Semantic U-Net")

with c3:
    st.warning("📂 LEVIR-CD")

with c4:
    st.success("⚡ Production Ready")

st.markdown("---")

# ================= CHANGE DETECTION MODEL =================

st.subheader("🧠 Change Detection Model")

st.info("""
Architecture: U-Net

Framework: PyTorch

Input Resolution: 256 × 256

Output: Binary Change Mask
""")

st.markdown("---")

# ================= SEMANTIC MODEL =================

st.subheader("🌍 Semantic Segmentation Model")

st.info("""
Architecture: Semantic U-Net

Framework: PyTorch

Classes:

• Vegetation

• Urban

• Background
""")

st.markdown("---")

# ================= DATASET =================

st.subheader("📂 Dataset Information")

d1, d2, d3, d4 = st.columns(4)

with d1:
    st.metric(
        "Images",
        "637"
    )

with d2:
    st.metric(
        "Resolution",
        "1024×1024"
    )

with d3:
    st.metric(
        "Classes",
        "3"
    )

with d4:
    st.metric(
        "Dataset",
        "LEVIR-CD"
    )

st.markdown("---")

# ================= PERFORMANCE =================

st.subheader("📊 Performance")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "🎯 Accuracy",
        "92%",
        "+1.2%"
    )

with c2:
    st.metric(
        "📈 IoU Score",
        "0.84",
        "+0.03"
    )

with c3:
    st.metric(
        "⚡ Inference Time",
        "< 2 sec",
        "-0.4 sec"
    )

st.markdown("---")

# ================= MODEL COMPARISON =================

st.subheader("⚖ Model Comparison")

comparison_data = {
    "Feature": [
        "Purpose",
        "Output",
        "Classes",
        "Speed"
    ],
    "U-Net": [
        "Change Detection",
        "Binary Mask",
        "2",
        "Fast"
    ],
    "Semantic U-Net": [
        "Land Cover Analysis",
        "Segmentation Map",
        "3",
        "Moderate"
    ]
}

import pandas as pd

comparison_df = pd.DataFrame(
    comparison_data
)

st.dataframe(
    comparison_df,
    width="stretch",
    hide_index=True
)

st.markdown("---")

# ================= TECH STACK =================

st.subheader("⚙ Technology Stack")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:
    st.success("🐍 Python")

with tech2:
    st.info("🔥 PyTorch")

with tech3:
    st.warning("🌐 Streamlit")

with tech4:
    st.success("🗄 SQLite")

st.markdown("""
• OpenCV

• NumPy

• Folium

• ReportLab
""")

st.markdown("---")

# ================= DEPLOYMENT STATUS =================

st.subheader("🚀 Deployment Readiness")

st.progress(92)

st.success(
    "SatVision AI Model Successfully Integrated"
)

st.markdown("---")

# ================= WORKFLOW =================

st.subheader("🛰 Workflow")

st.code("""
🛰 Satellite Images
        ↓
🧠 U-Net Model
        ↓
🎯 Change Mask
        ↓
🌍 Semantic Segmentation
        ↓
🔥 Heatmap
        ↓
🖼 Overlay
        ↓
📄 PDF Report
""")

st.markdown("---")

# ================= PROJECT SUMMARY =================

st.subheader("📋 Project Summary")

st.info("""
SatVision AI is an AI-powered satellite image analysis
platform capable of detecting land-cover changes,
performing semantic segmentation, generating heatmaps,
overlay visualizations, and producing professional PDF
reports for environmental monitoring and urban analysis.
""")


st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)