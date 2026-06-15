import streamlit as st
from datetime import datetime
from groq import Groq
from sidebar import render_sidebar

st.set_page_config(
    page_title="About Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= PROFILE SECTION =================

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

# ================= TITLE =================

st.title("ℹ️ About Analysis")

# ================= CHECK =================

if "change_percentage" not in st.session_state:

    st.warning(
        "Run Change Detection from Dashboard first."
    )

else:

    change_percentage = st.session_state.get(
        "change_percentage",
        0
    )

    location = st.session_state.get(
        "location",
        "Unknown Location"
    )

    before_img = st.session_state.get(
        "before",
        None
    )

    # ================= METRICS =================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📍 Location",
            location
        )

    with col2:
        st.metric(
            "📊 Change %",
            f"{change_percentage:.2f}%"
        )

    with col3:
        st.metric(
            "🤖 Model",
            "U-Net"
        )

    with col4:
        st.metric(
            "📅 Date",
            datetime.now().strftime("%d-%m-%Y")
        )

    st.markdown("---")

    # ================= IMAGE DETAILS =================

    st.subheader("🛰️ Satellite Image Information")

    if before_img is not None:

        width = before_img.shape[1]
        height = before_img.shape[0]

        col1, col2 = st.columns(2)

        with col1:
            st.info(
                f"Resolution: {width} × {height}"
            )

        with col2:
            st.info(
                f"Total Pixels: {width*height:,}"
            )

    st.markdown("---")

    # ================= CHANGE SUMMARY =================

    st.subheader("📈 Change Analysis")

    if change_percentage > 50:

        st.error(
            "High land-use change detected. Significant differences were found between the two satellite images."
        )

        severity = "High"

    elif change_percentage > 20:

        st.warning(
            "Moderate land-use change detected."
        )

        severity = "Medium"

    else:

        st.success(
            "Low land-use change detected."
        )

        severity = "Low"

    st.write(
        f"Severity Level: **{severity}**"
    )

    st.markdown("---")

    # ================= AI GENERATED REPORT =================

st.subheader("📖 AI Generated Analysis Report")

location = st.session_state.get(
    "location",
    "Unknown Location"
)

if location == "Unknown Location":

    st.info(
        "Location not entered. Please enter a location in Dashboard."
    )

else:

    try:

        client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

        prompt = f"""
        You are a satellite imagery analyst.

        Location: {location}

        Detected Change Percentage:
        {change_percentage:.2f}%

        Generate a professional report.

        Include:

        1. Overview of the location
        2. Historical background
        3. Past land usage
        4. Present condition
        5. Possible reasons for the detected change
        6. Future outlook

        Format the report nicely.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        report = response.choices[0].message.content

        st.markdown(report)

    except Exception as e:

        st.error(
            f"Groq Error: {e}"
        )

    st.markdown("---")

    # ================= IMAGE PREVIEW =================

    if (
        "before" in st.session_state and
        "after" in st.session_state
    ):

        st.subheader("🖼️ Uploaded Images")

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

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)