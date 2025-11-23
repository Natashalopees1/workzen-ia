# WorkZen IA - API de Detecção de Emoções

API REST desenvolvida com FastAPI para análise de emoções em imagens usando DeepFace. O sistema recebe imagens codificadas em base64 e retorna a emoção dominante detectada.

## 📋 Sobre o Projeto

Este projeto utiliza inteligência artificial para detectar emoções em imagens de rostos. A API processa imagens enviadas em formato base64 e utiliza o modelo DeepFace para identificar a emoção dominante presente na imagem.

## 🚀 Funcionalidades

- ✅ Análise de emoções em imagens de rostos
- ✅ API REST com FastAPI
- ✅ Suporte a imagens em formato base64
- ✅ Retorno da emoção dominante detectada

## 🛠️ Tecnologias Utilizadas

- **FastAPI**: Framework web moderno e rápido para construção de APIs
- **DeepFace**: Biblioteca de análise facial com deep learning
- **OpenCV**: Processamento de imagens
- **TensorFlow**: Framework de machine learning
- **Uvicorn**: Servidor ASGI para FastAPI
- **Pillow**: Manipulação de imagens
- **NumPy**: Computação numérica

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos para instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd workzen-ia
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

### Iniciando o servidor

Execute o seguinte comando para iniciar a API:

```bash
python api.py
```

A API estará disponível em `http://localhost:8000`

### Documentação interativa

Após iniciar o servidor, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Endpoint disponível

#### POST `/face/analyze`

Analisa uma imagem e retorna a emoção dominante detectada.

**Request Body:**
```json
{
  "image_base64": "string_base64_da_imagem"
}
```

**Response:**
```json
{
  "emotion": "happy"
}
```

**Exemplo de uso com cURL:**
```bash
curl -X POST "http://localhost:8000/face/analyze" \
  -H "Content-Type: application/json" \
  -d '{"image_base64": "iVBORw0KGgoAAAANSUhEUgAA..."}'
```

**Exemplo de uso com Python:**
```python
import requests
import base64

# Codificar imagem em base64
with open("caminho/para/imagem.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

# Enviar requisição
response = requests.post(
    "http://localhost:8000/face/analyze",
    json={"image_base64": encoded_string}
)

print(response.json())
```

## 📁 Estrutura do Projeto

```
workzen-ia/
├── api.py              # API FastAPI principal
├── main.py             # Função de análise de imagens
├── requirements.txt    # Dependências do projeto
├── README.md          # Este arquivo
└── fotos/             # Diretório com imagens de exemplo
```

## ⚙️ Configuração

A API está configurada para rodar na porta `8000` por padrão. Para alterar a porta, edite o arquivo `api.py`:

```python
uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=False)
```

## 🔍 Emoções Detectadas

O modelo DeepFace pode detectar as seguintes emoções:
- `angry` (raiva)
- `disgust` (nojo)
- `fear` (medo)
- `happy` (felicidade)
- `sad` (tristeza)
- `surprise` (surpresa)
- `neutral` (neutro)

## ⚠️ Observações

- A primeira execução pode demorar mais tempo, pois o DeepFace precisa baixar os modelos necessários
- Certifique-se de que as imagens enviadas contenham rostos visíveis para melhor precisão
- O processamento de imagens grandes pode consumir mais recursos

## 📝 Licença

Este projeto é de uso livre para fins educacionais e comerciais.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através dos canais do projeto.

