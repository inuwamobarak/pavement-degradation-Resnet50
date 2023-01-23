# Asphalt Pavement Degradation
Cloud link (Demo): https://inuwamobarak-pavement-degradation-resnet50-home-0ec0l3.streamlit.app/
## Problem Statement
According to Asphalt Magazine, before the appropriate repair strategy can be applied to a distressed asphalt pavement, the type and extent of the deterioration must be understood, and the cause of the distress must be identified. This will help to know how to appropriately implement the best repiar strategy.
## 
![download](https://user-images.githubusercontent.com/65142149/213781019-b07e0ac4-1846-490c-9804-e653e32387c7.png)
## Approach
This projects builds a model for classifying 3 prevalent asphalt degredations including Fatigue Cracking, Linear Cracking and Potholes providing engineers a tool to quickly know how to efficiently foster the approate solution. 

The model is built using PyTorch(https://pytorch.org/), an open source machine learning framework for building state of the art models to production deployment.

Transfer learning was used to transfer pretrained weights from the resnt50 architecture after webscraping about 10,000 images.

Dataset link: https://drive.google.com/drive/folders/1HbsTu1BuMpTGQpnS6lfQODgEfvj7n-Fo?usp=share_link
