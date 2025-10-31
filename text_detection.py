import cv2
import pytesseract
import streamlit

st.header("Image Processing"")  

uploaded_file = st.file_uploader("Please upload an image to detect text", type=["jpg", "png", "jpeg"])

img = cv2.imread(filename, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

text = pytesseract.image_to_string(thresh, lang='eng')
print(text)
