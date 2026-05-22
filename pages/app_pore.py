import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# --- Page Config ---
st.set_page_config(page_title="Professional Data Cleaner", layout="wide")

# --- Sidebar ---
st.sidebar.title("🛠 Settings")
uploaded_file = st.sidebar.file_uploader("อัปโหลดไฟล์ CSV ของคุณ", type=["csv"])

# --- Header ---
st.title("🧼 Data Cleaning Web App")
st.write("เครื่องมือสำหรับทำความสะอาดข้อมูลอัตโนมัติ ออกแบบโดย Web App Engineer")

if uploaded_file is not None:
    # 1. Load Data
    df_raw = pd.read_csv(uploaded_file)
    df = df_raw.copy()

    # 2. Tabs for Different Views
    tab1, tab2, tab3 = st.tabs(["📊 Raw Data", "🧹 Cleaning Process", "✅ Export Data"])

    with tab1:
        st.subheader("ข้อมูลดิบ (Raw Data Overview)")
        st.dataframe(df_raw.head())
        st.write(f"ขนาดข้อมูล: {df_raw.shape[0]} แถว, {df_raw.shape[1]} คอลัมน์")

    with tab2:
        st.subheader("เริ่มขั้นตอน Data Cleaning")
        
        # --- Process 1: Duplicates ---
        dups = df.duplicated().sum()
        if st.checkbox(f"ลบข้อมูลซ้ำ ({dups} แถว)"):
            df = df.drop_duplicates()
            st.success("ลบข้อมูลซ้ำเรียบร้อยแล้ว")

        # --- Process 2: Missing Values ---
        st.write("**จัดการค่าว่าง (Missing Values)**")
        if st.button("เติมค่าว่างด้วย Median"):
            for col in df.select_dtypes(include=[np.number]).columns:
                df[col] = df[col].fillna(df[col].median())
            st.success("เติมค่าว่างด้วยค่ามัธยฐานสำเร็จ")

        # --- Process 3: Inconsistent Data (Manual Fix example) ---
        if st.checkbox("ทำข้อมูลให้เป็นมาตรฐาน (Standardize Text)"):
            for col in df.select_dtypes(include=['object']).columns:
                df[col] = df[col].str.strip().str.title()
            st.success("ปรับแต่งรูปแบบตัวอักษรสำเร็จ")

        st.write("#### ข้อมูลปัจจุบันหลังการคลีน")
        st.dataframe(df.head())

    with tab3:
        st.subheader("ดาวน์โหลดข้อมูลที่สะอาดแล้ว")
        # Convert DF to CSV
        output = io.BytesIO()
        df.to_csv(output, index=False)
        processed_data = output.getvalue()

        st.download_button(
            label="📥 Download Cleaned CSV",
            data=processed_data,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

else:
    st.info("💡 กรุณาอัปโหลดไฟล์ CSV ที่แถบด้านซ้ายเพื่อเริ่มต้น")
