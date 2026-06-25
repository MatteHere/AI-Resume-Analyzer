import streamlit as st


def apply_custom_style():
    st.markdown("""
    <style>

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(37,99,235,0.18), transparent 35%),
            radial-gradient(circle at top right, rgba(14,165,233,0.18), transparent 35%),
            linear-gradient(135deg, #f8fbff 0%, #eef4ff 45%, #e0f2fe 100%);
        color: #0f172a;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    .main-title {
        font-size: 58px;
        font-weight: 950;
        text-align: center;
        color: #0f172a;
        margin-top: 8px;
        margin-bottom: 8px;
        letter-spacing: -1px;
        text-shadow: 0 8px 25px rgba(37, 99, 235, 0.18);
    }

    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #475569;
        margin-bottom: 32px;
        font-weight: 600;
    }

    .section-title {
        font-size: 30px;
        font-weight: 900;
        color: #0f172a;
        margin-top: 40px;
        margin-bottom: 18px;
        padding: 10px 0 10px 16px;
        border-left: 7px solid #2563eb;
        background: linear-gradient(90deg, rgba(219,234,254,0.9), transparent);
        border-radius: 12px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.82);
        border: 1px solid rgba(191, 219, 254, 0.9);
        border-radius: 26px;
        padding: 26px;
        margin: 16px 0;
        box-shadow:
            0 18px 45px rgba(15, 23, 42, 0.12),
            inset 0 1px 0 rgba(255,255,255,0.8);
        backdrop-filter: blur(20px);
        color: #0f172a;
    }

    .glass-card h1,
    .glass-card h2,
    .glass-card h3,
    .glass-card p {
        color: #0f172a;
    }

    .metric-3d {
        background: linear-gradient(145deg, #ffffff, #dbeafe);
        border: 1px solid #bfdbfe;
        border-radius: 26px;
        padding: 28px 20px;
        text-align: center;
        box-shadow:
            12px 12px 30px rgba(15, 23, 42, 0.15),
            -8px -8px 24px rgba(255, 255, 255, 0.95);
        transition: 0.25s ease;
        min-height: 150px;
    }

    .metric-3d:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow:
            16px 16px 38px rgba(15, 23, 42, 0.18),
            -10px -10px 30px rgba(255, 255, 255, 1);
    }

    .metric-3d h3 {
        color: #2563eb;
        font-size: 16px;
        margin-bottom: 10px;
        font-weight: 850;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .metric-3d h1 {
        color: #0f172a;
        font-size: 38px;
        margin: 0;
        font-weight: 950;
    }

    .profile-card {
        background: linear-gradient(145deg, rgba(255,255,255,0.96), rgba(219,234,254,0.82));
        border-radius: 24px;
        padding: 22px;
        border: 1px solid #bfdbfe;
        box-shadow:
            10px 10px 28px rgba(15, 23, 42, 0.12),
            -6px -6px 20px rgba(255, 255, 255, 0.9);
        min-height: 125px;
        margin-bottom: 16px;
        color: #0f172a;
    }

    .profile-card h4 {
        color: #1d4ed8;
        margin-bottom: 10px;
        font-size: 16px;
        font-weight: 900;
    }

    .profile-card p {
        color: #0f172a;
        font-size: 16px;
        font-weight: 650;
        word-break: break-word;
    }

    .skill-chip {
        display: inline-block;
        padding: 11px 18px;
        margin: 7px;
        background: linear-gradient(135deg, #2563eb, #38bdf8);
        color: white;
        border-radius: 999px;
        font-weight: 850;
        font-size: 14px;
        box-shadow: 0 10px 24px rgba(37, 99, 235, 0.34);
        transition: 0.2s ease-in-out;
    }

    .skill-chip:hover {
        transform: translateY(-4px);
        box-shadow: 0 15px 30px rgba(37, 99, 235, 0.48);
    }

    .stButton > button {
        background: linear-gradient(135deg, #2563eb, #38bdf8);
        color: white;
        border: none;
        border-radius: 18px;
        height: 58px;
        font-size: 19px;
        font-weight: 950;
        box-shadow: 0 16px 34px rgba(37, 99, 235, 0.35);
        transition: 0.25s ease-in-out;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #1d4ed8, #0ea5e9);
        color: white;
        transform: translateY(-3px);
    }

    .stFileUploader,
    .stTextArea {
        background: rgba(255, 255, 255, 0.84);
        padding: 18px;
        border-radius: 22px;
        border: 1px solid #bfdbfe;
        box-shadow: 0 14px 32px rgba(15, 23, 42, 0.10);
    }

    label,
    .stTextArea label,
    .stFileUploader label {
        color: #0f172a !important;
        font-weight: 900 !important;
    }

    textarea {
        color: #0f172a !important;
        background-color: #ffffff !important;
        border-radius: 14px !important;
    }

    div[data-testid="stAlert"] {
        border-radius: 18px;
        color: #0f172a;
        box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08);
    }

    div[data-testid="stPlotlyChart"] {
        background: rgba(255, 255, 255, 0.86);
        border-radius: 26px;
        padding: 18px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.12);
        border: 1px solid #bfdbfe;
    }

    div[data-testid="stProgress"] > div > div > div {
        background: linear-gradient(135deg, #2563eb, #38bdf8);
    }

    .streamlit-expanderHeader {
        color: #0f172a !important;
        font-weight: 900 !important;
    }

    .footer {
        text-align: center;
        color: #475569;
        margin-top: 55px;
        font-size: 14px;
        font-weight: 700;
    }

    </style>
    """, unsafe_allow_html=True)