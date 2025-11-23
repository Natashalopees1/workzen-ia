
## Visão geral

Este projeto simples faz análise facial (detecção de emoção) em imagens usando a biblioteca DeepFace. O script principal é `main.py` e espera imagens no diretório do projeto. Durante a configuração notei que as imagens fornecidas estão no formato AVIF (com extensão `.png`) — o código contém um fallback que usa Pillow para abrir AVIF e converter para um array compatível com OpenCV/DeepFace.

## O que o código faz

- Lê uma imagem (caminho definido em `main.py`).
- Tenta ler com OpenCV (`cv2.imread`). Se isso falhar (por exemplo, para arquivos AVIF), o código usa Pillow para abrir a imagem e converte para um array BGR.
- Chama `DeepFace.analyze` para extrair emoções (ação: `emotion`) e imprime o resultado.

## Bibliotecas usadas (breve descrição)

- opencv-python (cv2): leitura/manipulação de imagens e interoperabilidade com DeepFace.
- Pillow (PIL): fallback para abrir imagens em formatos que a build do OpenCV local não reconhece (ex.: AVIF). Usado para abrir e converter para RGB antes de transformar em numpy array.
- numpy: representação em array das imagens (shape HxWx3) e conversão RGB->BGR.
- deepface: framework de análise facial que encapsula modelos para emoção, idade, gênero e verificação de rosto; usamos a função `DeepFace.analyze` com `actions=("emotion",)`.
- tensorflow / keras: dependências necessárias do DeepFace para carregar e executar os modelos (instaladas automaticamente quando você instala `deepface`).

## Como rodar (macOS / zsh)

1) Garanta que você tem um Python apropriado disponível. Recomendamos usar Python 3.11 (no meu sistema usei `/opt/homebrew/bin/python3.11`). O Homebrew Python 3.14 pode ser marcado como "externally managed" e impedir instalações via pip (PEP 668).

2) Criar e ativar um virtualenv (exemplo usando Python 3.11):

```bash
/opt/homebrew/bin/python3.11 -m venv .venv311
source .venv311/bin/activate
```

3) Atualizar ferramentas e instalar dependências mínimas:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install opencv-python deepface pillow numpy
# se não precisar de UI (ex.: em servidor), considere opencv-python-headless
```

4) Rodar o projeto:

```bash
source .venv311/bin/activate
python main.py
```

Observação: `deepface` fará download automático de pesos de modelos (armazenados em `~/.deepface/weights/`), então a primeira execução pode demorar para baixar arquivos.

## Notas sobre formatos de imagem e o fallback

- Se `cv2.imread` retornar `None` (p.ex. para AVIF), `main.py` tentará abrir a imagem com Pillow e convertê-la para um numpy array BGR. Isso resolve o problema com imagens AVIF quando a build do OpenCV local não tem suporte a AVIF.
- Se preferir, você pode converter as imagens para PNG/JPEG usando Pillow antes de rodar.


## Nova API: análise via HTTP

Criei um arquivo `api.py` que expõe uma API FastAPI com um endpoint POST `/analyze` que recebe JSON com a chave `image_base64` (imagem em base64 ou data URI) e retorna a emoção dominante e as probabilidades por emoção.

Exemplo de payload JSON:

```json
{ "image_base64": "data:image/png;base64,iVBORw0KG..." }
```

Para rodar a API localmente (após criar e ativar o virtualenv e instalar dependências):

```bash
# ativar venv
source .venv311/bin/activate
# instalar dependências (se não usou requirements.txt ainda)
python -m pip install -r requirements.txt
# rodar a API
python api.py
```

Por padrão o servidor será executado em `http://0.0.0.0:8000`. Você pode testar com `curl` ou com o Swagger UI em `http://127.0.0.1:8000/docs`.


