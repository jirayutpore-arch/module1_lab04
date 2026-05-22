import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io

# --- Page Config ---
st.set_page_config(page_title="Red Bull Data Analytics", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- Title ---
st.title("🐂 Red Bull Data Cleaning & Analytics")
st.write("เครื่องมือวิเคราะห์และทำความสะอาดข้อมูลยอดขายอัตโนมัติ")

# --- Sidebar ---
st.sidebar.header("📂 Upload & Settings")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df_raw = pd.read_csv(uploaded_file)
    df = df_raw.copy()

    # 1. Overview Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Rows", f"{len(df):,}")
    col2.metric("Duplicate Rows", f"{df.duplicated().sum()}")
    col3.metric("Missing Values", f"{df.isnull().sum().sum()}")
    col4.metric("Avg Unit Price", f"{df['Unit_Price'].mean():.2f}")

    # 2. Tabs for Workflow
    tab_raw, tab_clean, tab_viz = st.tabs(["📊 Raw Data", "🧹 Cleaning Process", "📈 Visual Insights"])

    with tab_raw:
        st.subheader("สำรวจข้อมูลเบื้องต้น")
        st.dataframe(df.head(10), use_container_width=True)
        st.write("**Data Summary:**")
        st.write(df.describe())

    with tab_clean:
        st.subheader("ขั้นตอนการลีนข้อมูล")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.checkbox("ลบข้อมูลซ้ำ (Remove Duplicates)"):
                df = df.drop_duplicates()
                st.success("Done!")
            
            if st.checkbox("จัดการข้อมูลที่ไม่สอดคล้องกัน (Standardize Text)"):
                for col in ['Region', 'Product_Variant', 'Channel']:
                    df[col] = df[col].str.strip().str.title()
                st.success("Text Standardized!")

        with c2:
            if st.button("เติมค่าว่าง (Fill Missing Values)"):
                for col in df.select_dtypes(include=[np.number]).columns:
                    df[col] = df[col].fillna(df[col].median())
                st.success("Missing values filled with Median!")

        st.divider()
        st.write("**ข้อมูลหลังปรับปรุง:**")
        st.dataframe(df.head(), use_container_width=True)

    with tab_viz:
        st.subheader("วิเคราะห์ข้อมูลผ่านกราฟ")
        
        v_col1, v_col2 = st.columns(2)
        
        with v_col1:
            st.write("**ยอดขายตามภูมิภาค (Sales by Region)**")
            if 'Region' in df.columns:
                fig, ax = plt.subplots()
                sns.countplot(data=df, y='Region', palette='viridis', ax=ax)
                st.pyplot(fig)

        with v_col2:
            st.write("**การกระจายของคะแนนลูกค้า (Score Distribution)**")
            if 'Customer_Score' in df.columns:
                fig, ax = plt.subplots()
                sns.histplot(df['Customer_Score'], bins=10, kde=True, color='red', ax=ax)
                st.pyplot(fig)

    # Download Section
    st.sidebar.divider()
    csv = df.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button("📥 Download Clean Data", data=csv, file_name="cleaned_redbull.csv", mime="text/csv")

else:
    st.info("กรุณาอัปโหลดไฟล์ CSV เพื่อเริ่มต้นใช้งาน")
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")
