import streamlit as st
import sqlite3
import pandas as pd
from sidebar import render_sidebar

st.set_page_config(
    page_title="Semantic Analysis",
    layout="wide"
)

col1, col2 = st.columns([1,5])

with col1:

    if st.button("⬅ Back"):

        st.switch_page(
            "pages/1_Dashboard.py"
        )

st.title("📜 History")

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

    cursor:pointer;

    box-shadow:
    0 8px 20px rgba(
        0,
        0,
        0,
        0.25
    );

    transition:
    all 0.3s ease;
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

[data-testid="stDownloadButton"] button:active{

    transform:
    scale(0.98);
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

# ================= DATABASE =================

current_user = st.session_state.get(
    "username",
    "User"
)

conn = sqlite3.connect("users.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT,

    location TEXT,

    change_percentage REAL,

    report_path TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

conn.commit()

query = """
SELECT
    id,
    location,
    change_percentage,
    report_path,
    created_at
FROM reports
WHERE username = ?
ORDER BY id DESC
"""

df = pd.read_sql_query(
    query,
    conn,
    params=(current_user,)
)

conn.close()
# ================= NO DATA =================

if len(df) == 0:

    st.warning(
        "No reports generated yet."
    )

# ================= SHOW DATA =================

else:

    # Search Box

    search = st.text_input(
        "🔍 Search Location"
    )

    if search:

        df = df[
            df["location"].str.contains(
                search,
                case=False
            )
        ]
    
    if df.empty:

        st.info(
            "🔍 No matching reports found."
        )

        st.stop()

    # Severity Column

    def severity(val):

        if val < 10:
            return "🟢 Low"

        elif val < 30:
            return "🟡 Moderate"

        else:
            return "🔴 High"

    df["severity"] = df[
        "change_percentage"
    ].apply(severity)

    # Summary Cards

    total_reports = len(df)

    avg_change = df[
        "change_percentage"
    ].mean()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "📄 Total Reports",
            total_reports
        )

    with c2:

        st.metric(
            "📈 Avg Change",
            f"{avg_change:.2f}%"
        )

    with c3:

        st.metric(
            "📍 Locations",
            df["location"].nunique()
        )

    st.markdown("---")

    # Latest Analysis


    latest = df.iloc[0]

    st.markdown(
        f"""
    ### 🛰 Latest Analysis

    **Location:** {latest['location']}

    **Change Detected:** {latest['change_percentage']:.2f}%

    **Generated On:** {latest['created_at']}
    """
    )

    st.markdown("---")

    # Trend Chart

    st.subheader(
        "📊 Change Detection Trend"
    )

    trend_df = df[
        ["location", "change_percentage"]
    ]

    trend_df = trend_df.set_index(
        "location"
    )

    st.line_chart(
        trend_df
    )

    st.markdown("---")

    # Rename Columns

    df = df.rename(
        columns={
            "id": "ID",
            "location": "Location",
            "change_percentage": "Change %",
            "report_path": "Report File",
            "created_at": "Generated On",
            "severity": "Severity"
        }
    )

    st.subheader(
        "📜 Report Archive"
    )

    # ================= CSV EXPORT =================

    export_df = df.copy()

    export_df["Generated On"] = pd.to_datetime(
        export_df["Generated On"]
    ).dt.strftime("%d-%m-%Y %I:%M %p")

    export_df["Severity"] = export_df["Severity"].replace({
        "🟢 Low": "Low",
        "🟡 Moderate": "Moderate",
        "🔴 High": "High"
    })

    csv = export_df.to_csv(
        index=False
    ).encode("utf-8-sig")

    st.download_button(
        label="📊 Export History CSV",
        data=csv,
        file_name="Satellite_History.csv",
        mime="text/csv",
        width="stretch"
    )

    st.markdown("---")

    st.dataframe(
        df,
        width="stretch",
        hide_index=True
    )

    st.markdown("---")

    st.subheader(
        "📥 Download Latest Report"
    )

    try:

        with open(
            "Satellite_Report.pdf",
            "rb"
        ) as pdf_file:

            st.download_button(
                label="📄 Download PDF Report",
                data=pdf_file,
                file_name="Satellite_Report.pdf",
                mime="application/pdf"
            )

    except:

        st.info(
            "No PDF report available yet."
        )

    st.markdown("---")

    st.subheader(
        "🗑 Delete All History"
    )

    if st.button(
        "Delete My Reports"
    ):

        conn = sqlite3.connect(
            "users.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE FROM reports
            WHERE username = ?
            """,
            (
                current_user,
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "History deleted successfully."
        )

        st.rerun()

st.markdown("""
<div class="footer">

Made with ❤️ using Streamlit + PyTorch

</div>
""", unsafe_allow_html=True)