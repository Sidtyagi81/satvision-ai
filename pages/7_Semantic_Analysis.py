import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sidebar import render_sidebar

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Semantic Analysis",
    layout="wide"
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

# ================= SIDEBAR =================

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

st.title("🧠 Semantic Analysis")

# ================= CHECK DATA =================

if "semantic_prediction" not in st.session_state:

    st.warning(
        "Please run Change Detection from Dashboard first."
    )

    st.stop()

# ================= LOAD RESULTS =================

prediction = st.session_state.semantic_prediction

vegetation = st.session_state.vegetation
urban = st.session_state.urban
background = st.session_state.background

change_percentage = st.session_state.get(
    "change_percentage",
    0
)

# ================= METRICS =================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🌍 Change",
        f"{change_percentage:.2f}%"
    )

with c2:
    st.metric(
        "🌳 Vegetation",
        f"{vegetation:.2f}%"
    )

with c3:
    st.metric(
        "🏢 Urban",
        f"{urban:.2f}%"
    )

with c4:
    st.metric(
        "⬜ Background",
        f"{background:.2f}%"
    )

st.markdown("---")

st.subheader(
    "🛰️ Input Images"
)

if (
    "before" in st.session_state
    and
    "after" in st.session_state
):

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            st.session_state.before,
            caption="Before Image",
            width="stretch"
        )

    with col2:
        st.image(
            st.session_state.after,
            caption="After Image",
            width="stretch"
        )

# ================= SEMANTIC MAP =================

st.subheader(
    "🗺️ Semantic Prediction Map"
)

semantic_map = np.zeros(
    (
        prediction.shape[0],
        prediction.shape[1],
        3
    ),
    dtype=np.uint8
)

semantic_map[
    prediction == 0
] = [0, 255, 0]

semantic_map[
    prediction == 1
] = [255, 0, 0]

semantic_map[
    prediction == 2
] = [255, 255, 255]

st.image(
    semantic_map,
    caption="""
    Green = Vegetation
    | Red = Urban
    | White = Background
    """,
    width="stretch"
)

# ================= CLASS DISTRIBUTION =================

st.subheader(
    "📊 Land Cover Distribution"
)

chart_data = {
    "Vegetation": vegetation,
    "Urban": urban,
    "Background": background
}

fig, ax = plt.subplots(
    figsize=(6,6)
)

ax.pie(
    [
        vegetation,
        urban,
        background
    ],
    labels=[
        "Vegetation",
        "Urban",
        "Background"
    ],
    autopct="%1.1f%%"
)

st.pyplot(fig)

# ================= AI INSIGHT =================

st.subheader(
    "🤖 AI Insight"
)

insights = []

if vegetation > 60:

    insights.append(
        f"🌳 High vegetation coverage detected ({vegetation:.1f}%)."
    )

elif vegetation > 30:

    insights.append(
        f"🌿 Moderate vegetation coverage detected ({vegetation:.1f}%)."
    )

else:

    insights.append(
        f"⚠️ Low vegetation coverage detected ({vegetation:.1f}%)."
    )

if urban > 50:

    insights.append(
        f"🏢 Urban development dominates the region ({urban:.1f}%)."
    )

elif urban > 20:

    insights.append(
        f"🏘️ Moderate urban presence observed ({urban:.1f}%)."
    )

if change_percentage > 40:

    insights.append(
        f"🔥 Significant land-cover change detected ({change_percentage:.1f}%)."
    )

elif change_percentage > 15:

    insights.append(
        f"📈 Moderate environmental transformation detected ({change_percentage:.1f}%)."
    )

else:

    insights.append(
        f"✅ Low environmental change detected ({change_percentage:.1f}%)."
    )

for insight in insights:

    st.success(insight)

# ================= AI GENERATED REPORT =================

st.subheader(
    "📄 AI Generated Report"
)

st.markdown(
    f"""
### Analysis Summary

- Change Detected: **{change_percentage:.2f}%**
- Vegetation Coverage: **{vegetation:.2f}%**
- Urban Coverage: **{urban:.2f}%**
- Background Coverage: **{background:.2f}%**

### Observation

The satellite imagery indicates a land-cover transformation of
**{change_percentage:.2f}%**.

Vegetation occupies **{vegetation:.2f}%**
of the analyzed area while urban structures occupy
**{urban:.2f}%**.

Background/open land accounts for
**{background:.2f}%** of the region.

These results were generated using the trained
Semantic U-Net model.
"""
)

st.info(
    "Results were automatically generated during Dashboard analysis."
)

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)