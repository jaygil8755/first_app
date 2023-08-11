import streamlit as st
from rembg import remove
from PIL import Image
from streamlit_image_comparison import image_comparison
import easyocr as ocr  #OCR
import numpy as np #Image Processing 

# set page config
st.set_page_config(layout="centered")

st.subheader('Remove Background - 사진 배경 제거')
st.markdown("#### sample result")
image_comparison(
    img1 = "https://raw.githubusercontent.com/jaygil8755/first_app/3ccd1f9edd28745c8c7f63f1c839f87d29d46ab8/src/animal-1.jpg",
    img2 = "https://raw.githubusercontent.com/jaygil8755/first_app/3ccd1f9edd28745c8c7f63f1c839f87d29d46ab8/src/animal_rmbg.png",
    label1 = "원본 이미지",
    label2 = "배경제거 이미지",
    show_labels=True,
    make_responsive=True,
    in_memory=True)

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

# if uploaded_file is not None:
#     input = Image.open(uploaded_file)
#     st.image(input, caption='원본 이미지', use_column_width=True)
#     output = remove(input)
#     st.image(output, caption='배경 제거 이미지', use_column_width=True)

############################################################################################
st.subheader("Easy OCR - 이미지에서 글자를 추출")

@st.cache
def load_model(): 
    reader = ocr.Reader(['ko', 'en'], model_storage_directory='.')
    return reader 

reader = load_model() #load model

if uploaded_file is not None:

    input_image = Image.open(uploaded_file)  
    st.image(input_image) 

    with st.spinner("🤖 AI is at Work! "):       

        result = reader.readtext(input_image, detail = 0) 
        st.write(result)
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("수고하셨습니다.")
