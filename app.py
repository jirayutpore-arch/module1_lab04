import streamlit as st
import base64
import os

# 1. ตั้งค่า Page Config
st.set_page_config(page_title="MyApp - Pixel Edition", layout="wide", initial_sidebar_state="collapsed")

# 2. ฟังก์ชันสำหรับโหลดวิดีโอและแปลงเป็น Base64 เพื่อใช้เป็น Background
def set_bg_video(video_path):
    if os.path.exists(video_path):
        with open(video_path, 'rb') as video_file:
            video_bytes = video_file.read()
        video_base64 = base64.b64encode(video_bytes).decode()
        
        # HTML/CSS สำหรับพื้นหลังวิดีโอและ Overlay สีดำให้ตัวหนังสืออ่านง่าย
        st.markdown(f"""
            <style>
            #myVideo {{
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%;
                min-height: 100%;
                z-index: -100;
                filter: contrast(110%) saturate(120%); /* ปรับสีให้ดูเป็น Pixel มากขึ้น */
            }}
            .stApp {{
                background-color: rgba(0, 0, 0, 0.65); /* Overlay สีดำโปร่งแสง */
            }}
            </style>
            <video autoplay muted loop id="myVideo">
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
            </video>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ ไม่พบไฟล์วิดีโอ {video_path} สำหรับทำพื้นหลัง")

# เรียกใช้งาน Video Background (ระบุชื่อไฟล์ของคุณ)
set_bg_video("Pixel_art_style_Subtle_and_ge (1).mp4")

# 3. ใส่ CSS สำหรับ Pixel Art Style และ Transition
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Kanit:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        /* ตั้งค่าฟอนต์ผสมระหว่าง Pixel Font และ Kanit */
        html, body, [class*='css'], p, h1, h2, h3, h4, h5, h6 {
            font-family: 'Kanit', sans-serif;
            color: #ffffff;
        }
        
        /* สไตล์กล่องข้อความสไตล์ 8-bit / Pixel Art */
        .pixel-container {
            background-color: #001D3D;
            padding: 25px;
            border: 4px solid #FFD60A;
            box-shadow: 8px 8px 0px #000000;
            text-align: center;
            margin: 20px 0;
            image-rendering: pixelated; /* ให้ขอบดูคมแบบ Pixel */
        }
        
        .pixel-title {
            color: #FFD60A;
            font-family: 'Press Start 2P', cursive, 'Kanit';
            font-size: 24px;
            margin-bottom: 10px;
            text-shadow: 2px 2px 0px #000;
        }

        .pixel-subtitle {
            color: #00ff00;
            font-weight: bold;
            font-size: 16px;
            text-shadow: 1px 1px 0px #000;
        }

        /* Animation แบบ Smooth Fade In สำหรับสไลด์ */
        @keyframes fadeInSlide {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .smooth-slide {
            animation: fadeInSlide 0.5s ease-in-out;
            padding: 20px;
            background: rgba(255, 255, 255, 0.1);
            border: 2px dashed #FFD60A;
            border-radius: 10px;
            text-align: center;
        }
        
        /* ปรับแต่งปุ่ม Streamlit ให้เป็นทรง Pixel Art */
        div.stButton > button {
            background-color: #FFD60A;
            color: #000000 !important;
            font-weight: 800;
            border: 3px solid #000000;
            border-radius: 0px;
            box-shadow: 4px 4px 0px #000000;
            transition: all 0.2s ease;
        }
        div.stButton > button:hover {
            transform: translate(2px, 2px);
            box-shadow: 2px 2px 0px #000000;
            background-color: #ffea00;
            border: 3px solid #000000;
        }
        div.stButton > button:active {
            transform: translate(4px, 4px);
            box-shadow: 0px 0px 0px #000000;
        }
    </style>
""", unsafe_allow_html=True)

# 4. ส่วนหัวของ App
st.markdown("""
    <div class='pixel-container'>
        <div style='font-size: 40px;'>👾</div>
        <div class='pixel-title'>||| LA VERSION 2.0 |||</div>
        <div class='pixel-subtitle'>SYSTEM ONLINE & READY</div>
        <div style='color: #E0E0E0; font-size: 14px; margin-top: 5px;'>Optimized by TCP Data Engineering Elite</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center; text-shadow: 2px 2px #000;'>DAY 1: การจัดการข้อมูลพื้นฐาน</h3>", unsafe_allow_html=True)
st.write("---")

# 5. ระบบ Slider / Carousel สำหรับปุ่ม
# เก็บสถานะว่ากำลังอยู่ที่สไลด์ไหน
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

# รายการปุ่มและหน้าที่จะลิงก์ไป
pages = [
    {"icon": "💰", "label": "ระบบคำนวณส่วนลดตามยอดซื้อ", "path": "pages/app1_discount_calc.py", "desc": "โปรแกรมสำหรับคำนวณส่วนลดอัตโนมัติ"},
    {"icon": "🧹", "label": "ทำความสะอาดข้อมูล (Data Cleaning)", "path": "pages/clean_app_pore.py", "desc": "จัดการข้อมูลที่สูญหายและซ้ำซ้อน"},
    {"icon": "🔄", "label": "การแปลงข้อมูล (Data Transformation)", "path": "pages/transform_app.py", "desc": "ปรับเปลี่ยนรูปฟอร์มและประเภทของข้อมูล"}
    {"icon": "🚛", "label": "Logistics Service Time Prediction & Scheduling", "path": "pages/truck_predict.py", "desc": "แอปลิเคชันนี้ช่วยพยากรณ์เวลาบริการรถบรรทุก และจัดตารางการเข้าคิวเพื่อประสิทธิภาพสูงสุด"}
    {"icon": "🔄", "label": "การแปลงข้อมูล (Data Transformation)", "path": "pages/transform_app.py", "desc": "ปรับเปลี่ยนรูปฟอร์มและประเภทของข้อมูล"}
    {"icon": "🔄", "label": "การแปลงข้อมูล (Data Transformation)", "path": "pages/transform_app.py", "desc": "ปรับเปลี่ยนรูปฟอร์มและประเภทของข้อมูล"}
]

total_slides = len(pages)

# สร้าง Layout: [ลูกศรซ้าย] [เนื้อหาสไลด์ตรงกลาง] [ลูกศรขวา]
col_left, col_center, col_right = st.columns([1, 4, 1])

with col_left:
    st.write("") # เว้นระยะให้ปุ่มอยู่ตรงกลางแนวตั้ง
    st.write("")
    if st.button("◀ PREV"):
        st.session_state.slide_index = (st.session_state.slide_index - 1) % total_slides

with col_right:
    st.write("")
    st.write("")
    if st.button("NEXT ▶"):
        st.session_state.slide_index = (st.session_state.slide_index + 1) % total_slides

# ดึงข้อมูลหน้าที่กำลังเลือกแสดงผล
current_page = pages[st.session_state.slide_index]

with col_center:
    # ฝัง HTML สำหรับ Transition ให้ดู Smooth เวลาเปลี่ยนสไลด์
    st.markdown(f"""
        <div class="smooth-slide">
            <h1 style='font-size: 50px; margin: 0;'>{current_page['icon']}</h1>
            <h3>{current_page['label']}</h3>
            <p style='color: #FFD60A;'>{current_page['desc']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # ปุ่มกดเข้าใช้งานหน้าแอปนั้นๆ
    st.write("") # Spacer
    if st.button(f"🚀 เริ่มต้นใช้งาน: {current_page['label']}", use_container_width=True):
        try:
            st.switch_page(current_page['path'])
        except Exception as e:
            st.error(f"⚠️ กรุณาสร้างไฟล์ {current_page['path']} ในโฟลเดอร์ pages ก่อนกดใช้งาน")

# แสดง Indicator (จุดไข่ปลา) ด้านล่างสไลด์
indicator_html = "<div style='text-align: center; margin-top: 15px;'>"
for i in range(total_slides):
    color = "#FFD60A" if i == st.session_state.slide_index else "#ffffff"
    size = "15px" if i == st.session_state.slide_index else "10px"
    indicator_html += f"<span style='display: inline-block; margin: 0 5px; color: {color}; font-size: {size};'>⬤</span>"
indicator_html += "</div>"
st.markdown(indicator_html, unsafe_allow_html=True)
