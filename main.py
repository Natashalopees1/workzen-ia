import os
import sys
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2

def analyze_image(image_base64: str):
    """Analisa a imagem codificada em base64 e retorna as emoções detectadas."""
    imagem = cv2.imread(image_base64)
    resultado = DeepFace.analyze(imagem, actions=("emotion",))
    return resultado[0]['dominant_emotion']
