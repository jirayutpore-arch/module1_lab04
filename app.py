import streamlit as st

st.set_page_config(page_title="MyApp", layout="wide")

st.title("🏠 หน้าหลัก ")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.markdown("""
    <link href='https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&display=swap' rel='stylesheet'>
    <style>
        /* ปรับแต่งฟอนต์ทั้งหน้า */
        html, body, [class*='css']  {
            font-family: 'Kanit', sans-serif;
        }
        
        /* ปรับแต่งกล่องสถานะ LA Version */
        .la-container {
            background: linear-gradient(135deg, #001D3D 0%, #003566 100%);
            padding: 25px;
            border-radius: 15px;
            border-left: 8px solid #FFD60A;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            color: white;
            text-align: center;
            margin: 20px 0;
        }
        
        .la-title {
            color: #FFD60A;
            font-size: 28px;
            font-weight: 600;
            letter-spacing: 3px;
            margin-bottom: 5px;
        }

        .la-subtitle {
            color: #E0E0E0;
            font-size: 14px;
            font-style: italic;
        }
    </style>

    <div class='la-container'>
        <div style='font-size: 40px;'>🚀</div>
        <div class='la-title'>||| LA VERSION 2.0 |||</div>
        <div style='color: #00ff00; font-weight: bold;'>SYSTEM ONLINE & READY</div>
        <div class='la-subtitle'>Optimized by TCP Data Engineering Elite</div>
    </div>
""", unsafe_allow_html=True)
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("ทำความสะอาดข้อมูล"):
    st.switch_page("pages/clean_app_pore.py")
