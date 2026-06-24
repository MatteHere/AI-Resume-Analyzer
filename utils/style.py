import streamlit as st


def apply_custom_style():
    st.markdown("""
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #1e3a8a, #020617 45%, #000000);
        color: #ffffff;
    }

    .main-title {
        font-size: 54px;
        font-weight: 900;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 18px rgba(56, 189, 248, 0.8);
        margin-top: 10px;
    }

    .subtitle {
        font-size: 19px;
        text-align: center;
        color: #cbd5e1;
        margin-bottom: 35px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.10);
        border: 1px solid rgba(255, 255, 255, 0.22);
        border-radius: 22px;
        padding: 24px;
        margin: 14px 0;
        box-shadow: 0 18px 45px rgba(0, 0, 0, 0.45);
        backdrop-filter: blur(14px);
    }

    .metric-3d {
        background: linear-gradient(145deg, rgba(59,130,246,0.35), rgba(14,165,233,0.12));
        border: 1px solid rgba(125, 211, 252, 0.35);
        border-radius: 22px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 16px 35px rgba(14, 165, 233, 0.22);
    }

    .metric-3d h3 {
        color: #bae6fd;
        font-size: 16px;
        margin-bottom: 8px;
    }

    .metric-3d h1 {
        color: #ffffff;
        font-size: 38px;
        margin: 0;
        text-shadow: 0 0 14px rgba(56, 189, 248, 0.8);
    }

    .section-title {
        font-size: 30px;
        font-weight: 850;
        color: #ffffff;
        margin-top: 36px;
        margin-bottom: 18px;
        text-shadow: 0 0 10px rgba(14, 165, 233, 0.45);
    }

    .profile-card {
        background: rgba(255, 255, 255, 0.11);
        border-radius: 20px;
        padding: 18px;
        border: 1px solid rgba(255,255,255,0.18);
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
        min-height: 115px;
    }

    .profile-card h4 {
        color: #7dd3fc;
        margin-bottom: 10px;
        font-size: 16px;
    }

    .profile-card p {
        color: #ffffff;
        font-size: 16px;
        word-break: break-word;
    }

    .skill-chip {
        display: inline-block;
        padding: 11px 18px;
        margin: 7px;
        background: linear-gradient(135deg, #38bdf8, #2563eb);
        color: white;
        border-radius: 999px;
        font-weight: 800;
        font-size: 14px;
        box-shadow: 0 10px 22px rgba(37, 99, 235, 0.45);
    }

    .stButton > button {
        background: linear-gradient(135deg, #38bdf8, #2563eb);
        color: white;
        border: none;
        border-radius: 18px;
        height: 56px;
        font-size: 19px;
        font-weight: 900;
        box-shadow: 0 14px 32px rgba(37, 99, 235, 0.45);
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0ea5e9, #1d4ed8);
        color: white;
        transform: translateY(-2px);
    }

    .stFileUploader, .stTextArea {
        background: rgba(255, 255, 255, 0.08);
        padding: 16px;
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.16);
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        margin-top: 50px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)