import streamlit as st
from rembg import remove
from PIL import Image
from streamlit-image-comparison import image_comparision
st.subheader('이미지 배경제거 서비스')
st.markdown("## sample result")
image_comparison(
    img1 = "https://raw.githubusercontent.com/jaygil8755/first_app/3ccd1f9edd28745c8c7f63f1c839f87d29d46ab8/src/animal-1.jpg",
    img2 = "https://raw.githubusercontent.com/jaygil8755/first_app/3ccd1f9edd28745c8c7f63f1c839f87d29d46ab8/src/animal_rmbg.png",
    label1 = "원본 이미지",
    label2 = "배경제거 이미지",
    show_labels=True,
    make_responsive=True,
    in_memory=True)

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    input = Image.open(uploaded_file)
    st.image(input, caption='원본 이미지', use_column_width=True)
    output = remove(input)
    st.image(output, caption='배경 제거 이미지', use_column_width=True)
