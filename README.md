Brain Tumor Detection Using EfficientNet-B0

Project Overview: Brain Tumor Detection is a deep learning-based medical image classification system developed to automatically identify the presence of brain tumors from MRI scans. The project utilizes the EfficientNet-B0 architecture through transfer learning to classify MRI images into two categories:

* **Yes** – Tumor Present
* **No** – No Tumor Present

The deployed application allows users to upload a brain MRI image and receive an instant prediction regarding tumor presence.

Objectives"
* Develop an automated brain tumor detection system using deep learning.
* Reduce manual diagnostic effort through AI-assisted screening.
* Evaluate the performance of multiple CNN architectures.
* Deploy the best-performing model as an interactive web application.

Dataset: The dataset consists of brain MRI images categorized into two classes:

| Class | Description      |
| ----- | ---------------- |
| Yes   | Tumor Present    |
| No    | No Tumor Present |


Dataset Characteristics:
* Binary image classification
* MRI brain scans
* Images resized to **224 × 224 pixels**
* Data augmentation applied to improve model generalization

Data Augmentation: To improve robustness and reduce overfitting, the following augmentation techniques were applied:
* Rotation (20°)
* Horizontal Flipping
* Zooming (20%)
* Brightness Adjustment
* Nearest Fill Mode

Deep Learning Models Evaluated:Three state-of-the-art transfer learning models were compared:

1. EfficientNet-B0
* Compound scaling architecture
* Lightweight and efficient
* Achieved the highest classification performance

2. MobileNetV2
* Mobile-friendly architecture
* Low computational complexity

3. ResNet18
* Residual learning framework
* Strong feature extraction capability

Selected Model: After comparative evaluation, **EfficientNet-B0** was selected for deployment due to its superior performance in tumor classification.

Technologies Used:
* Python
* TensorFlow
* Keras
* NumPy
* Pillow
* Google Colab
* Gradio
* Hugging Face Spaces

Model Workflow:
1. Upload MRI Image
2. Image Preprocessing
3. Resize to 224 × 224
4. EfficientNet-B0 Prediction
5. Tumor / No Tumor Classification
6. Display Result

DeploymenT:The application is deployed using:
* Hugging Face Spaces
* Gradio Interface

Users can upload MRI images directly through the web interface and obtain predictions instantly.


Future Enhancements:
* Multi-class brain tumor classification
* Tumor localization and segmentation
* Explainable AI using Grad-CAM
* Clinical decision support integration
* Mobile application deployment



License
This project is intended for educational and research purposes only and should not be used as a substitute for professional medical diagnosis.


Project Structure

```text
brain-tumor-detection/
│
├── app.py
├── requirements.txt
├── README.md
└── model/
    └── best_efficientnet_model.h5

