from transformers import pipeline

def classify_image(image_path):
    classifier = pipeline("image-classification", model="microsoft/resnet-50")
    return classifier(image_path)
