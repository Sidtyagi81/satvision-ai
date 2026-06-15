import streamlit as st
import cv2
import torch
import numpy as np
import pandas as pd
import sqlite3
from PIL import Image
from PIL.ExifTags import TAGS
from model import UNet
from utils import create_overlay
from sidebar import render_sidebar
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium
from model import UNet
from semantic_model import SemanticUNet
from torchvision import transforms
from reportlab.platypus import Table
from reportlab.platypus import PageBreak
from datetime import datetime
from streamlit_image_comparison import image_comparison

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

col1, col2 = st.columns([1,5])

with col1:

    if st.button("⬅ Back"):

        st.switch_page(
            "pages/1_Dashboard.py"
        )

st.markdown("""
<style>
            
/* ================= FILE UPLOADER ================= */

[data-testid="stFileUploader"]{

    border:none !important;

    background:transparent !important;
}

[data-testid="stFileUploaderDropzone"]{

    background:linear-gradient(
        135deg,
        #1e293b,
        #0f172a
    ) !important;

    border:1px solid rgba(
        59,
        130,
        246,
        0.35
    ) !important;

    border-radius:20px !important;

    padding:25px !important;

    box-shadow:
    0 8px 20px rgba(
        0,
        0,
        0,
        0.25
    );

    transition:all 0.3s ease;
}

[data-testid="stFileUploaderDropzone"]:hover{

    border:1px solid #60a5fa !important;

    box-shadow:
    0 12px 30px rgba(
        37,
        99,
        235,
        0.35
    );
}

/* Upload Button */

[data-testid="stBaseButton-secondary"]{

    height:60px !important;

    border-radius:18px !important;

    background:linear-gradient(
        135deg,
        #1e293b,
        #0f172a
    ) !important;

    border:1px solid rgba(
        59,
        130,
        246,
        0.35
    ) !important;

    color:white !important;

    font-size:18px !important;

    font-weight:700 !important;

    transition:all 0.3s ease !important;
}

[data-testid="stBaseButton-secondary"]:hover{

    transform:translateY(-3px);

    background:
    rgba(59,130,246,0.15);

    border:
    1px solid #3b82f6;

    box-shadow:
    0 8px 25px rgba(59,130,246,0.25);
}

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
            
/* ================= UPLOADED FILE CARD ================= */

[data-testid="stFileUploaderFile"]{

    width:100% !important;

    max-width:100% !important;

    background:rgba(15,23,42,0.95) !important;

    border:1px solid rgba(
        59,
        130,
        246,
        0.35
    ) !important;

    border-radius:18px !important;

    padding:15px !important;
}

/* File name section */

[data-testid="stFileUploaderFileName"]{

    font-size:18px !important;

    color:white !important;

    font-weight:600 !important;
}

/* Uploaded file container */

[data-testid="stFileUploaderDropzone"] section{

    width:100% !important;
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
            
/* ================= DOWNLOAD BUTTON ================= */

[data-testid="stDownloadButton"] button{

    width:100%;

    height:60px;

    border-radius:18px;

    background:linear-gradient(
        135deg,
        #1e293b,
        #0f172a
    );

    border:1px solid rgba(
        59,
        130,
        246,
        0.35
    );

    color:white !important;

    font-size:18px;

    font-weight:700;

    letter-spacing:0.3px;

    box-shadow:
    0 8px 20px rgba(
        0,
        0,
        0,
        0.25
    );

    transition:all 0.3s ease;
}

[data-testid="stDownloadButton"] button:hover{
    
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

# ================= DASHBOARD METRICS =================

username = st.session_state.get(
    "username",
    "User"
)

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute(
    """
    SELECT COUNT(*)
    FROM reports
    WHERE username = ?
    """,
    (username,)
)

total_reports = cursor.fetchone()[0]

conn.close()

total_analyses = total_reports

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "🧠 AI Model",
        "U-Net"
    )

with c2:
    st.metric(
        "📍 Location",
        st.session_state.get(
            "location",
            "Not Selected"
        )
    )

with c3:
    st.metric(
        "📄 Reports",
        total_reports
    )

with c4:
    st.metric(
        "📊 Analyses",
        total_analyses
    )

st.markdown("---")

st.subheader(
    "🕒 Recent Analysis"
)

conn = sqlite3.connect("users.db")

query = """
SELECT
    location,
    change_percentage,
    created_at
FROM reports
WHERE username = ?
ORDER BY id DESC
LIMIT 1
"""

recent = pd.read_sql_query(
    query,
    conn,
    params=(username,)
)

conn.close()

if not recent.empty:

    latest = recent.iloc[0]

    st.info(
        f"""
📍 Location: {latest['location']}

📈 Change Detected: {latest['change_percentage']:.2f}%

🕒 Generated On: {latest['created_at']}
"""
    )

else:

    st.warning(
        "No analysis has been performed yet."
    )

st.info(
    f"""
🛰 Ready for satellite analysis

Logged in as: {username}
"""
)

# ================= ANALYSIS STATISTICS =================

st.subheader(
    "📊 Analysis Statistics"
)

conn = sqlite3.connect("users.db")

query = """
SELECT change_percentage
FROM reports
WHERE username = ?
"""

stats_df = pd.read_sql_query(
    query,
    conn,
    params=(username,)
)

conn.close()

if not stats_df.empty:

    avg_change = stats_df[
        "change_percentage"
    ].mean()

    max_change = stats_df[
        "change_percentage"
    ].max()

    min_change = stats_df[
        "change_percentage"
    ].min()

    s1, s2, s3 = st.columns(3)

    with s1:

        st.metric(
            "📈 Average Change",
            f"{avg_change:.2f}%"
        )

    with s2:

        st.metric(
            "🔺 Highest Change",
            f"{max_change:.2f}%"
        )

    with s3:

        st.metric(
            "🔻 Lowest Change",
            f"{min_change:.2f}%"
        )

    st.subheader(
        "📉 Change Trend"
    )

    st.line_chart(
        stats_df["change_percentage"]
    )

st.markdown("---")

# ================= CUSTOM CSS =================

@st.cache_resource
def get_geolocator():

    return Nominatim(
        user_agent="satellite_app"
    )

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

@st.cache_resource
def load_change_model():

    model = UNet().to(device)

    model.load_state_dict(
        torch.load(
            "saved_models/model.pth",
            map_location=device
        )
    )

    model.eval()

    return model


@st.cache_resource
def load_semantic_model():

    model = SemanticUNet(
        num_classes=3
    ).to(device)

    model.load_state_dict(
        torch.load(
            "semantic_model.pth",
            map_location=device
        )
    )

    model.eval()

    return model

model = load_change_model()

semantic_model = load_semantic_model()

# ================= PROFILE SECTION =================

username = st.session_state.get(
    "username",
    "User"
)

render_sidebar(username)

# ================= PAGE TITLE =================

st.markdown("""
<div style="
background:linear-gradient(
135deg,
#0f172a,
#111827
);
padding:40px;
border-radius:20px;
border:1px solid rgba(255,255,255,0.08);
box-shadow:0 10px 30px rgba(0,0,0,0.25);
margin-bottom:30px;
">

<div style="
color:#3b82f6;
font-size:13px;
font-weight:600;
letter-spacing:2px;
text-transform:uppercase;
margin-bottom:12px;
">
Satellite Intelligence Platform
</div>

<div style="
font-size:52px;
font-weight:800;
color:white;
line-height:1.1;
margin-bottom:15px;
">
Satellite Change Detection
</div>

<div style="
font-size:18px;
color:#94a3b8;
max-width:850px;
line-height:1.7;
margin-bottom:25px;
">
Advanced AI-powered monitoring system for detecting land-use changes,
urban expansion, deforestation, environmental transformations,
and infrastructure development from multi-temporal satellite imagery.
</div>

<div style="
display:flex;
gap:12px;
flex-wrap:wrap;
">

<span style="
background:rgba(59,130,246,0.12);
color:#60a5fa;
padding:10px 18px;
border-radius:999px;
font-size:14px;
font-weight:600;
border:1px solid rgba(59,130,246,0.2);
">
Deep Learning
</span>

<span style="
background:rgba(16,185,129,0.12);
color:#34d399;
padding:10px 18px;
border-radius:999px;
font-size:14px;
font-weight:600;
border:1px solid rgba(16,185,129,0.2);
">
U-Net Architecture
</span>

<span style="
background:rgba(168,85,247,0.12);
color:#c084fc;
padding:10px 18px;
border-radius:999px;
font-size:14px;
font-weight:600;
border:1px solid rgba(168,85,247,0.2);
">
Geospatial Analysis
</span>

<span style="
background:rgba(245,158,11,0.12);
color:#fbbf24;
padding:10px 18px;
border-radius:999px;
font-size:14px;
font-weight:600;
border:1px solid rgba(245,158,11,0.2);
">
Real-Time Detection
</span>

</div>

</div>
""", unsafe_allow_html=True)

location_name = st.text_input(
    "📍 Enter Location Name",
    value=st.session_state.get(
        "location",
        ""
    )
)

search_location = st.button(
    "🔍 Search Location"
)

if search_location and location_name:

    geolocator = get_geolocator()

    location = geolocator.geocode(
        location_name
    )

    if location:

        st.session_state.latitude = location.latitude
        st.session_state.longitude = location.longitude

        st.session_state.location = location_name
        st.session_state.report_location = location_name

        st.success(
            f"📍 {location.address}"
        )

    else:

        st.error(
            "Location not found."
        )

if (
    "latitude" in st.session_state
    and "longitude" in st.session_state
):

    m = folium.Map(
        location=[
            st.session_state.latitude,
            st.session_state.longitude
        ],
        zoom_start=14,
        tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
        attr="Esri"
    )

    folium.Marker(
        [
            st.session_state.latitude,
            st.session_state.longitude
        ],
        popup=st.session_state.location,
        tooltip=st.session_state.location,
        icon=folium.Icon(
            color="red",
            icon="info-sign"
        )
    ).add_to(m)

    st_folium(
    m,
        width=900,
        height=400
    )

# ================= UPLOAD SECTION =================

st.markdown("## 📤 Upload Satellite Images")

upload_col1, upload_col2 = st.columns(2)

if "upload_key" not in st.session_state:

    st.session_state.upload_key = 0

with upload_col1:
    uploaded_before = st.file_uploader(
        "📷 Before Image",
        type=["png","jpg","jpeg"],
        key=f"before_{st.session_state.upload_key}"
    )

with upload_col2:
    uploaded_after = st.file_uploader(
        "📷 After Image",
        type=["png","jpg","jpeg"],
        key=f"after_{st.session_state.upload_key}"
    )

# Save uploads permanently
if uploaded_before is not None:
    st.session_state.uploaded_before = uploaded_before

if uploaded_after is not None:
    st.session_state.uploaded_after = uploaded_after

# Recover uploads after page change
uploaded_before = st.session_state.get(
    "uploaded_before",
    None
)

uploaded_after = st.session_state.get(
    "uploaded_after",
    None
)

col1, col2 = st.columns([4,1])

with col2:

    if st.button(
        "🔄 Upload Again",
        width="stretch"
    ):

        keys_to_clear = [

            "uploaded_before",
            "uploaded_after",

            "before",
            "after",

            "mask",
            "overlay",
            "heatmap",

            "change_percentage",

            "semantic_prediction",
            "vegetation",
            "urban",
            "background",

            "analysis_done",

            "location",
            "report_location",

            "latitude",
            "longitude"
        ]

        for key in keys_to_clear:

            st.session_state.pop(
                key,
                None
            )

        st.session_state.upload_key += 1

        st.rerun()

analyze = st.button(
    "🚀 Run Change Detection",
    width="stretch"
)

if uploaded_before and uploaded_after:

    st.success("✅ Images Uploaded")

    preview_col1, preview_col2 = st.columns(2)

    if uploaded_before:

        st.image(
            uploaded_before,
            caption="Before Image Preview",
            width="stretch"
        )

    if uploaded_after:

        st.image(
            uploaded_after,
            caption="After Image Preview",
            width="stretch"
        )

# ================= ANALYSIS =================

if uploaded_before and uploaded_after and analyze:

    with st.spinner(
        "🧠 Running AI Analysis..."
    ):

        progress = st.progress(0)
        status = st.empty()

        status.info("📤 Loading Images...")
        progress.progress(25)

        before_raw = Image.open(uploaded_before)

        status.info("🧠 Running AI Model...")
        progress.progress(50)

        exif = before_raw.getexif()
        before = before_raw.convert("RGB")

        status.info("🎯 Detecting Changes...")
        progress.progress(75)

        # prediction code here

        status.info("📊 Generating Report...")
        progress.progress(100)

        status.empty()

        st.toast(
            "✅ Analysis Completed Successfully"
        )

        # ================= GPS / EXIF CHECK =================

    try:

        exif = before.getexif()

        if exif:

            st.subheader("📍 Image Metadata")

            for tag_id, value in exif.items():

                tag = TAGS.get(
                    tag_id,
                    tag_id
                )

                st.write(
                    f"{tag}: {value}"
                )

        else:

            st.info(
                "No EXIF metadata found in image."
            )

    except Exception as e:

        st.warning(
            f"Metadata Error: {e}"
        )

    # ================= SECOND IMAGE =================

    after = Image.open(
        uploaded_after
    ).convert("RGB")

    before_np = np.array(before)
    after_np = np.array(after)

    before_resized = cv2.resize(
        before_np,
        (256, 256)
    )

    after_resized = cv2.resize(
        after_np,
        (256, 256)
    )

    before_norm = before_resized / 255.0
    after_norm = after_resized / 255.0

    combined = np.concatenate(
        [before_norm, after_norm],
        axis=2
    )

    combined = np.transpose(
        combined,
        (2, 0, 1)
    )

    input_tensor = torch.tensor(
        combined,
        dtype=torch.float32
    ).unsqueeze(0).to(device)

    with torch.no_grad():
        prediction = model(
            input_tensor
        )

    mask = prediction.squeeze().cpu().numpy()

    binary_mask = (
        mask > 0.5
    ).astype(np.uint8)

    overlay = create_overlay(
        before_resized,
        binary_mask
    )

    # Save for Statistics / Heatmap / Overlay pages
    st.session_state.before = before_resized

    st.session_state.after = after_resized

    st.session_state.mask = binary_mask

    st.session_state.overlay = overlay

    st.session_state.heatmap = mask

    change_percentage = (
        np.sum(binary_mask)
        / binary_mask.size
    ) * 100

    # Save for Analytics page
    st.session_state.change_percentage = change_percentage

    st.session_state.analysis_done = True

    # ================= SEMANTIC ANALYSIS =================

    transform = transforms.Compose([
        transforms.ToTensor()
    ])

    img1_tensor = transform(
        Image.fromarray(before_resized)
    )

    img2_tensor = transform(
        Image.fromarray(after_resized)
    )

    semantic_input = torch.cat(
        [img1_tensor, img2_tensor],
        dim=0
    ).unsqueeze(0).to(device)

    with torch.no_grad():

        semantic_output = semantic_model(
            semantic_input
        )

    semantic_prediction = torch.argmax(
        semantic_output,
        dim=1
    ).squeeze().cpu().numpy()

    # Save prediction

    st.session_state.semantic_prediction = (
        semantic_prediction
    )

    # Calculate statistics

    total = semantic_prediction.size

    vegetation = (
        np.sum(
            semantic_prediction == 0
        ) / total
    ) * 100

    urban = (
        np.sum(
            semantic_prediction == 1
        ) / total
    ) * 100

    background = (
        np.sum(
            semantic_prediction == 2
        ) / total
    ) * 100

    # Save for Semantic Analysis page

    st.session_state.vegetation = vegetation

    st.session_state.urban = urban

    st.session_state.background = background

    if "history" not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({
        "location": location_name,
        "change": round(change_percentage, 2),
        "time": datetime.now().strftime(
            "%d-%m-%Y %H:%M"
        )
    })

    # ================= METRICS =================

    st.markdown("## 📊 Detection Summary")

    st.markdown("## 🧠 AI Insights")

    if change_percentage < 10:

        st.success("""
        Minimal land surface changes detected.

        The monitored region appears stable.
        """)

    elif change_percentage < 30:

        st.warning("""
        Moderate changes detected.

        Possible causes:

        • Urban development
        • Vegetation changes
        • Infrastructure expansion
        """)

    else:

        st.error("""
        Significant land transformation detected.

        Possible causes:

        • Large-scale construction
        • Deforestation
        • Flooding impact
        • Major environmental change
        """)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "🎯 Change %",
            f"{change_percentage:.2f}%"
        )

        st.progress(
            change_percentage / 100
        )

        if change_percentage > 50:

            st.error("🔴 High Change Detected")

        elif change_percentage > 20:

            st.warning("🟡 Medium Change Detected")

        else:

            st.success("🟢 Low Change Detected")

    with m2:
        st.metric(
            "🔥 Changed Pixels",
            int(np.sum(binary_mask))
        )

    with m3:
        st.metric(
            "🖼 Resolution",
            "256 × 256"
        )

    st.markdown("---")

    st.subheader(
        "🚨 Risk Assessment"
    )

    st.subheader(
        "🤖 AI Recommendation"
    )

    if change_percentage < 10:

        st.success(
            """
            🌳 Region appears stable.

            Recommendation:
            Continue routine monitoring.
            No immediate intervention required.
            """
        )

    elif change_percentage < 30:

        st.warning(
            """
            🟡 Moderate environmental change detected.

            Recommendation:
            Increase monitoring frequency.
            Verify urban expansion or vegetation loss.
            """
        )

    else:

        st.error(
            """
            🔴 Significant land transformation detected.

            Recommendation:
            Immediate investigation recommended.
            Consider environmental impact assessment.
            """
        )

    if change_percentage < 10:

        st.success(
            """
            🟢 LOW RISK

            Minimal land-cover transformation detected.
            """
        )

    elif change_percentage < 30:

        st.warning(
            """
            🟡 MODERATE RISK

            Noticeable changes detected.

            Periodic monitoring recommended.
            """
        )

    else:

        st.error(
            """
            🔴 HIGH RISK

            Significant environmental or urban transformation detected.

            Immediate monitoring recommended.
            """
        )

    st.subheader(
        "🛰 Interactive Change Comparison"
    )

    image_comparison(
        img1=Image.fromarray(before_resized),
        img2=Image.fromarray(after_resized),
        label1="Before",
        label2="After",
        width=800
    )

    # ================= TABS =================

    tab1, tab2, tab3, tab4 = st.tabs([
        "📷 Before",
        "📷 After",
        "🎯 Mask",
        "🔥 Overlay"
    ])

    with tab1:
        st.image(
            before_resized,
            width="stretch"
        )

    with tab2:
        st.image(
            after_resized,
            width="stretch"
        )

    with tab3:
        st.image(
            binary_mask * 255,
            width="stretch"
        )

    with tab4:
        st.image(
            overlay,
            width="stretch"
        )

    st.success(
        f"Change Detection Complete • {change_percentage:.2f}% change detected"
    )

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Image as PDFImage,
    Spacer,
    Table
)

from reportlab.lib.styles import getSampleStyleSheet

if st.button("📄 Generate Report"):
    
    report_id = datetime.now().strftime(
        "SAT-%Y%m%d-%H%M%S"
    )

    Image.fromarray(
        st.session_state.before
    ).save("before_image.png")

    Image.fromarray(
        st.session_state.after
    ).save("after_image.png")

    Image.fromarray(
        (st.session_state.mask * 255).astype(np.uint8)
    ).save("mask.png")

    Image.fromarray(
        st.session_state.overlay.astype(np.uint8)
    ).save("overlay.png")

    import matplotlib.pyplot as plt

    plt.figure(figsize=(5,5))

    plt.imshow(
        st.session_state.semantic_prediction,
        cmap="viridis"
    )

    plt.axis("off")

    plt.savefig(
        "semantic_map.png",
        bbox_inches="tight"
    )

    plt.close()

    pdf = SimpleDocTemplate(
        "Satellite_Report.pdf"
    )

    pdf.author = "SatVision AI"
    pdf.title = "Satellite Change Detection Report"
    pdf.subject = "Satellite Change Detection Analysis"
    pdf.author = "SatVision AI"

    styles = getSampleStyleSheet()

    content = [

            Spacer(1,60),

        PDFImage(
            "logo.png",
            width=220,
            height=220
        ),

        Spacer(1,20),

        Paragraph(
            "SatVision AI",
            styles["Title"]
        ),

        Spacer(1,30),

        Paragraph(
            "Version 1.0",
            styles["Normal"]
        ),

        Paragraph(
            "AI Powered Geospatial Intelligence Platform",
            styles["Italic"]
        ),

        Paragraph(
            "Satellite Change Detection Report",
            styles["Heading1"]
        ),

        Paragraph(
            "────────────────────────────────────────",
            styles["Normal"]
        ),

        Spacer(1,20),

        Paragraph(
            f"<b>📍 Location:</b> {st.session_state.get('report_location','Unknown')}",
            styles["Heading2"]
        ),

        Spacer(1,20),

        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        ),

        Spacer(1,40),

        Paragraph(
            f"Report ID: {report_id}",
            styles["Normal"]
        ),

        Spacer(1,20),

        PageBreak(),

        Paragraph(
            "Satellite Change Detection Report",
            styles["Title"]
        ),

        Paragraph(
            f"Location: {st.session_state.get('report_location', 'Unknown')}",
            styles["Normal"]
        ),

        Paragraph(
            f"Generated On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
            styles["Normal"]
        ),

        Paragraph(
            f"Change Percentage: {st.session_state.get('change_percentage', 0):.2f}%",
            styles["Normal"]
        ),

        Paragraph(
            "<br/><b>Semantic Analysis Results</b>",
            styles["Heading2"]
        ),

        Paragraph(
            f"Vegetation Coverage: {st.session_state.get('vegetation', 0):.2f}%",
            styles["Normal"]
        ),

        Paragraph(
            f"Urban Coverage: {st.session_state.get('urban', 0):.2f}%",
            styles["Normal"]
        ),

        Paragraph(
            f"Background Coverage: {st.session_state.get('background', 0):.2f}%",
            styles["Normal"]
        ),

        Spacer(1, 20),

        Paragraph(
            "Before & After Satellite Images",
            styles["Heading2"]
        )
    ]

    table = Table([
        [
            PDFImage(
                "before_image.png",
                width=200,
                height=200
            ),
            PDFImage(
                "after_image.png",
                width=200,
                height=200
            )
        ]
    ])

    content.append(table)

    content.append(
        Spacer(1, 20)
    )

    content.append(
        Paragraph(
            "Change Detection Results",
            styles["Heading2"]
        )
    )

    content.append(
        PDFImage(
            "semantic_map.png",
            width=180,
            height=180
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "Mask & Overlay Images",
            styles["Heading3"]
        )
    )

    mask_table = Table([
        [
            PDFImage(
                "mask.png",
                width=200,
                height=200
            ),
            PDFImage(
                "overlay.png",
                width=200,
                height=200
            )
        ]
    ])

    content.append(mask_table)

    content.append(
        Spacer(1, 20)
    )

    plt.figure(figsize=(5,5))

    plt.pie(
        [
            st.session_state.vegetation,
            st.session_state.urban,
            st.session_state.background
        ],
        labels=[
            "Vegetation",
            "Urban",
            "Background"
        ],
        autopct="%1.1f%%"
    )

    plt.savefig(
        "landcover_pie.png",
        bbox_inches="tight"
    )

    plt.close()

    # ================= PIE CHART =================
    
    content.append(
        Paragraph(
            "Land Cover Distribution",
            styles["Heading2"]
        )
    )

    content.append(
        PDFImage(
            "landcover_pie.png",
            width=250,
            height=250
        )
    )

    content.append(
        Spacer(1,20)
    )

    # ================= AI REPORT =================

    content.append(
        Paragraph(
            "AI Generated Analysis",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"""
            The analysis detected
            {st.session_state.get('change_percentage',0):.2f}% land-cover change.

            Vegetation coverage is
            {st.session_state.get('vegetation',0):.2f}%.

            Urban coverage is
            {st.session_state.get('urban',0):.2f}%.

            Background coverage is
            {st.session_state.get('background',0):.2f}%.
            """,
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"""
            This report presents the results of AI-powered
            satellite change detection performed using
            SatVision AI.

            The analysis detected
            <b>{st.session_state.get('change_percentage',0):.2f}%</b>
            land-cover change in the selected region.

            The report includes:
            • Change Detection Analysis<br/>
            • Semantic Segmentation<br/>
            • Land Cover Distribution<br/>
            • Risk Assessment<br/>
            • Overlay Visualization
            """,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "Conclusion",
            styles["Heading2"]
        )
    )

    dominant = max(
        [
            ("Vegetation", st.session_state.vegetation),
            ("Urban", st.session_state.urban),
            ("Background", st.session_state.background)
        ],
        key=lambda x: x[1]
    )

    content.append(
        Paragraph(
            f"""
            The AI analysis detected
            {st.session_state.change_percentage:.2f}% change
            in the selected region.

            The dominant land-cover category is
            <b>{dominant[0]}</b>
            with {dominant[1]:.2f}% coverage.

            Based on the satellite imagery,
            significant land-cover transformation
            has been observed and future monitoring
            is recommended.
            """,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
    Paragraph(
        "Change Severity Assessment",
        styles["Heading2"]
    )
)

    change = st.session_state.change_percentage

    if change < 10:

        severity = "LOW"
        recommendation = """
        The monitored region appears stable.
        No significant land-cover transformation detected.
        """

    elif change < 30:

        severity = "MODERATE"
        recommendation = """
        Moderate environmental or urban changes detected.
        Periodic monitoring is recommended.
        """

    else:

        severity = "HIGH"
        recommendation = """
        Significant land-cover transformation detected.
        Immediate monitoring and investigation recommended.
        """

    content.append(
        Paragraph(
            f"""
            <b>Severity Level:</b> {severity}<br/>
            {recommendation}
            """,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    # Model Information
    content.append(
        Paragraph(
            "Model Information",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            """
            • Change Detection Model: U-Net<br/>
            • Semantic Segmentation Model: Semantic U-Net<br/>
            • Input Resolution: 256 × 256<br/>
            • Framework: PyTorch<br/>
            • Platform: SatVision AI
            """,
            styles["Normal"]
        )
    )

    content.append(
        Spacer(1,20)
    )

    content.append(
        Paragraph(
            "────────────────────────────────────────",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            "Generated automatically by SatVision AI © 2026",
            styles["Italic"]
        )
    )

    pdf.build(content)

    st.toast(
        "📄 PDF Report Generated Successfully"
    )

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reports
        (
            username,
            location,
            change_percentage,
            report_path
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            st.session_state.get(
                "username",
                "User"
            ),
            st.session_state.get(
                "report_location",
                "Unknown"
            ),
            st.session_state.get(
                "change_percentage",
                0
            ),
            "Satellite_Report.pdf"
        )
    )

    conn.commit()
    conn.close()

    with open(
        "Satellite_Report.pdf",
        "rb"
    ) as f:

        st.download_button(
            "⬇ Download PDF",
            f,
            file_name="Satellite_Report.pdf"
        )

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)