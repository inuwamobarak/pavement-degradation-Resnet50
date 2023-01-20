import io
from PIL import Image
import streamlit as st
import torch
from torchvision import transforms
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

MODEL_PATH = 'model/model-APD-pytorch-res50-92accuracy.pt'
LABELS_PATH = 'model/model_classes.txt'


def load_image():
    uploaded_file = st.file_uploader(label='Pick a banknote to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)
        return Image.open(io.BytesIO(image_data))
    else:
        return None


def load_model(model_path):
    model = torch.load(model_path, map_location='cpu')
    model.eval()
    return model


def load_labels(labels_file):
    with open(labels_file, "r") as f:
        categories = [s.strip() for s in f.readlines()]
        return categories


def predict(model, categories, image):
    preprocess = transforms.Compose([
        transforms.Resize(300),
        transforms.CenterCrop(300),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)

    with torch.no_grad():
        output = model(input_batch)

    probabilities = torch.nn.functional.softmax(output[0], dim=0)

    all_prob, all_catid = torch.topk(probabilities, len(categories))
    for i in range(all_prob.size(0)):
        st.write(categories[all_catid[i]], all_prob[i].item())


def main():
    st.title('Asphalt Pavement Degradation Detector')
    html_text = '<p style="font-family:sans-serif; color:"Navy Blue"; font-size:16px; font-style:italic;"> <i>According to Asphalt Magazine, before the appropriate repair strategy can be applied to a distressed asphalt pavement, the type and extent of the deterioration must be understood, and the cause of the distress must be identified. This will help to know how to appropriately implement the best repiar strategy.</i></p>'
    st.markdown(html_text, unsafe_allow_html=True)
    
    
    model = load_model(MODEL_PATH)
    categories = load_labels(LABELS_PATH)
    image = load_image()
    result = st.button('Predict image')
    if result:
        st.write('Checking...')
        predict(model, categories, image)


if __name__ == '__main__':
    main()
