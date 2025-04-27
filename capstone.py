import streamlit as st
import pandas as pd
import pickle
import time
from PIL import Image

#Konfigurasi halaman dan judul
st.set_page_config(page_title="Capstone Project",
                   page_icon="rocket",
                   layout="wide",
                   initial_sidebar_state="auto")

#Introduction
st.write("""
         # Welcome to my machine learning dashboard
         This dashboard created by: [Madeleine](https://id.linkedin.com/in/madeleine-hart-filiapuspa)
         """)

#Memanggil model yang sudah dilatih
with open("output_decision_tree (2).pkl","rb")as file:
    model_loaded=pickle.load(file)

#Menampilkan sidebar
st.sidebar.title("Pilih use case yang mau digunakan")
st.sidebar.write("Pilih salah satu use case berikut")
use_case=st.sidebar.selectbox("Use Case",(
    "Iris Species","Heart Disease","Wine Quality","Titanic Survival"
    , "Bank Marketing","Credit Card Fraud Detection"))

def input_user_heart_disease():
    st.sidebar.header("Manual Input")
    sex = st.sidebar.selectbox("Jenis Kelamin",("Pria","Perempuan"))
    if sex=="Pria":
        sex=1
    else:
        sex=0

    cp=st.sidebar.selectbox("Tipe Nyeri Dada",("typical angina",
                                               "atypical angina",
                                               "non-anginal pain",
                                               "asymtomatic"))
    if cp=="typical angina":
        cp=0
    elif cp=="atypical angina":
        cp=1
    elif cp=="non-anginal pain":
        cp==2
    else:
        cp==3

    thalach = st.sidebar.number_input("Heart Rate",min_value=1, max_value=3,value=2)

    slope=st.sidebar.selectbox("Slope",("downsloping","flat","upsloping"))
    if slope =="downsloping":
        slope=0
    elif slope=="flat":
        slope=1
    else:
        slope=2
    
    oldpeak=st.sidebar.number_input("Old Peak",min_value=1,max_value=7,value=2)
    
    exang=st.sidebar.selectbox("Exang",("Ya","Tidak"))
    if exang=="Ya":
        exang=1
    else:
        exang=0
    
    ca=st.sidebar.selectbox("Jumlah Pembuluh Darah",("0","1","2","3"))

    thal=st.sidebar.selectbox("Thal",("normal","fixed defect","reversable defect"))
    if thal == "normal":
        thal=1
    elif thal =="fixed defect":
        thal=2
    else:
        thal=3
    
    age=st.sidebar.number_input("Usia",min_value=20,max_value=100,value=50)
    data={'sex':sex,
          'cp':cp,
          'thalach':thalach,
          'slope':slope,
          'oldpeak':oldpeak,
          'exang':exang,
          'ca':ca,
          'thal':thal,
          'age':age}
    features=pd.DataFrame(data,index=[0])
    return features

#Function untuk menampilkan per use case
def heart_disease():
    st.write("""
    Ini adalah aplikasi yang dapat memprediksi penyakit jantung
    berdasarkan data yang diberikan.
    Silakan masukkan data yang diperlukan pada samping ini
    """)
    st.sidebar.title("Input Data")
    st.sidebar.write("Silakan masukkan data berikut")
    upload_file=st.sidebar.file_uploader("Upload file CSV",type=["csv"])
    if upload_file is not None:
        input_data=pd.read_csv(upload_file)
    else:
        #skip
        st.sidebar.write("Di bawah adalah inputan data manual")
        input_data=input_user_heart_disease()
    
    #show image heart disease
    img=Image.open("heart-disease.jpg")
    st.image(img,caption="Heart Disease",use_container_width=True)
    if st.sidebar.button("Go!"):
        df=input_data
        st.write(df)
        prediction=model_loaded.predict(df)
        st.write("Hasil prediksi:")
        result=["No Heart Disease" if prediction==0 else "Yes Heart Disease"]
        output=str(result[0])
        with st.spinner("Loading..."):
            time.sleep(2)
            st.success(f"Prediksi yang dihasilkan adalah:{output}")

if use_case=="Iris Species":
    st.write("""
    Ini adalah aplikasi yang dapat memprediksi spesies bunga iris
    berdasarkan data yang diberikan.
    Silakan masukkan data yang diperlukan pada samping ini
    """)
    st.sidebar.title("Input Data")
elif use_case=="Heart Disease":
    heart_disease()