import requests
from bs4 import BeautifulSoup
import os

# URL da página web
url = "https://www.mercadolivre.com.br/"

# Fazer a solicitação HTTP e analisar o HTML
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todas as tags de imagem na página
image_tags = soup.find_all("img")

# Criar um diretório para salvar as imagens
if not os.path.exists("imagens"):
    os.makedirs("imagens")

# Baixar e salvar as imagens
for img_tag in image_tags:
    img_url = img_tag["src"]
    # Verificar se a URL começa com "http" ou "https"
    if img_url.startswith("http"):
        img_name = os.path.basename(img_url)
        # Remover caracteres inválidos substituindo-os por "_"
        img_name = "".join(x if x.isalnum() or x in ["-", "_", "."] else "_" for x in img_name)
        img_path = os.path.join("imagens", img_name)
        with open(img_path, "wb") as img_file:
            img_file.write(requests.get(img_url).content)

print("Imagens baixadas com sucesso!")

