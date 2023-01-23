from PIL import Image
import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:images/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/engineer.jpg')    

def main():
    st.title('Asphalt Pavement Degradation Detector')
    html_text = '<p style="font-family:sans-serif; color:"Navy Blue"; font-size:16px; font-style:italic;"> <i>Welcome to the contact page. To keep intouch or for enquiries please find contacts below.</i></p>'
    st.markdown(html_text, unsafe_allow_html=True)
    
    html_text = '<p style="font-family:sans-serif; color:"Navy Blue"; font-size:16px; font-style:italic;">EMAIL ADDRESS: <i>inuwamobarak@gmail.com</i></p>'
    st.markdown(html_text, unsafe_allow_html=True)
    
    html_text = '<p style="font-family:sans-serif; color:"Navy Blue"; font-size:16px; font-style:italic;">LinkedIn: <i><a>https://www.linkedin.com/in/mobarak-inuwa/</a></i></p>'
    st.markdown(html_text, unsafe_allow_html=True)
    
    html_text = '<p style="font-family:sans-serif; color:"Navy Blue"; font-size:16px; font-style:italic;">Twitter: <i><a>https://https://twitter.com/InuwaAbraham</a></i></p>'
    st.markdown(html_text, unsafe_allow_html=True)


if __name__ == '__main__':
    main()
