import os
import sys
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
import base64
import numpy as np
from PIL import Image
import io

def analyze_image(image_base64: str):
    """Analisa a imagem codificada em base64 e retorna as emoções detectadas."""
    
    image_bytes = base64.b64decode(image_base64)

    try:
        pil_image = Image.open(io.BytesIO(image_bytes))
        imagem_rgb = np.array(pil_image.convert('RGB'))
        imagem = cv2.cvtColor(imagem_rgb, cv2.COLOR_RGB2BGR)
        
    except Exception as e:
        raise ValueError(f"Falha ao decodificar a imagem: {e}")
    
    resultado = DeepFace.analyze(imagem, actions=("emotion",))
    return resultado[0]['dominant_emotion']
