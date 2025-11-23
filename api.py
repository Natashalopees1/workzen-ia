from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import analyze_image

class ImageRequest(BaseModel):
    image_base64: str

app = FastAPI(title="Emotion Detection API")

@app.post("/face/analyze")
async def analyze_image(req: ImageRequest):
    """Recebe JSON com chave `image_base64` contendo a imagem codificada em base64.
    Retorna a emoção dominante e as probabilidades por emoção.
    """
    if not req.image_base64:
        raise HTTPException(status_code=400, detail="image_base64 is required")

    emotion = analyze_image(req.image_base64)

    return {
        "emotion": emotion,
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=False)
