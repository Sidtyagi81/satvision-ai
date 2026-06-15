import streamlit as st

st.markdown("""
<style>

[data-testid="stSidebarContent"]{
    padding-top:0rem !important;
}

section[data-testid="stSidebar"]{
    min-width:320px !important;
    max-width:320px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Sidebar Buttons */

section[data-testid="stSidebar"] .stButton button{

    width:100%;

    height:60px;

    border-radius:20px;

    font-size:18px;

    font-weight:600;

    margin-bottom:10px;

    background:#2a2d3a;

    border:1px solid #4b5563;

    color:white;
}

section[data-testid="stSidebar"] .stButton button:hover{

    border:1px solid #60a5fa;

    transform:translateY(-2px);

    transition:0.2s;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

section[data-testid="stSidebar"] .stButton button{

    width:100% !important;

    height:60px !important;

    min-height:60px !important;

    border-radius:20px !important;

    font-size:18px !important;

    font-weight:600 !important;

    margin-bottom:12px !important;
}

</style>
""", unsafe_allow_html=True)



def render_sidebar(username):

    with st.sidebar:

        # ================= LOGO =================

        st.markdown("""
            <div style="
            text-align:center;
            margin-top:-65px;
            margin-bottom:25px;
            padding:10px;
            ">

            <div style="
            font-size:40px;
            font-weight:800;
            color:white;
            letter-spacing:-1px;
            ">
            🛰️ SatChange AI
            </div>

            <div style="
            font-size:13px;
            color:#94a3b8;
            margin-top:5px;
            letter-spacing:1px;
            text-transform:uppercase;
            ">
            Satellite Intelligence Platform
            </div>

            <div style="
            margin-top:15px;
            display:flex;
            justify-content:center;
            gap:8px;
            flex-wrap:wrap;
            ">

            <span style="
            background:#1e293b;
            padding:4px 10px;
            border-radius:999px;
            font-size:11px;
            color:#60a5fa;
            border:1px solid #334155;
            ">
            AI Powered
            </span>

            <span style="
            background:#1e293b;
            padding:4px 10px;
            border-radius:999px;
            font-size:11px;
            color:#34d399;
            border:1px solid #334155;
            ">
            U-Net
            </span>

            <span style="
            background:#1e293b;
            padding:4px 10px;
            border-radius:999px;
            font-size:11px;
            color:#fbbf24;
            border:1px solid #334155;
            ">
            Live Analysis
            </span>

            </div>

            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")

        # ================= NAVIGATION =================

        if st.button(
            "📊 Dashboard",
            width="stretch"
        ):
            st.switch_page("pages/1_Dashboard.py")

        if st.button(
            "📈 Analytics",
            width="stretch"
        ):
            st.switch_page("pages/2_Analytics.py")

        if st.button(
            "📋 Statistics",
            width="stretch"
        ):
            st.switch_page("pages/3_Statistics.py")

        if st.button(
            "🔥 Heatmap",
            width="stretch"
        ):
            st.switch_page("pages/4_Heatmap.py")

        if st.button(
            "ℹ️ About",
            width="stretch"
        ):
            st.switch_page("pages/5_About.py")

        if st.button(
            "🖼️ Overlay",
            width="stretch"
        ):
            st.switch_page("pages/6_Overlay.py")

        if st.button(
            "🧠 Semantic Analysis",
            width="stretch"
        ):
            st.switch_page(
                "pages/7_Semantic_Analysis.py"
            )
        
        if st.button(
            "📜 History",
            width="stretch"
        ):
            st.switch_page(
                "pages/8_history.py"
            )

        if st.button(
            "🤖 Model Information",
            width="stretch"
        ):
            st.switch_page(
                "pages/9_Model_Info.py"
            )

        if st.button(
            "ℹ️ About Project",
            width="stretch"
        ):
            st.switch_page(
                "pages/10_About_Project.py"
            )

        st.markdown("---")

        # ================= USER CARD =================

        st.markdown(
            f"""
            <div style="
            background:#1f2937;
            padding:20px;
            border-radius:18px;
            border:1px solid #374151;
            ">

            <p style="
            color:#94a3b8;
            font-size:12px;
            margin-bottom:8px;
            ">
            Logged In As
            </p>

            <p style="
            color:white;
            font-size:18px;
            font-weight:600;
            ">
            👤 {username}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        # ================= LOGOUT =================

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🚪 Logout",
            width="stretch"
        ):
            st.session_state.clear()
            st.switch_page("app.py")