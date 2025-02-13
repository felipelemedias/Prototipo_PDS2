import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from datetime import datetime
from model import Model_MenuNav
from database import get_db

def scraping_ufu(db: Session):
    url = "https://www.ufu.br"
    response = requests.get(url)

    if response.status_code != 200:
        return {"Erro": "Não foi possível acessar o site da UFU."}

    soup = BeautifulSoup(response.text, 'html.parser')

    # Pegando o rodapé da página
    footer = soup.find('footer')
    if not footer:
        return {"Erro": "Rodapé não encontrado!"}

    links = footer.find_all('a')

    data_to_insert = []

    for link in links:
        text = link.get_text(strip=True)
        href = link.get('href')

        if text and href:
            full_link = href if href.startswith("http") else f"https://www.ufu.br{href}"
            menu_item = Model_MenuNav(menuNav=text, link=full_link, created_at=datetime.utcnow())
            data_to_insert.append(menu_item)

    db.bulk_save_objects(data_to_insert)
    db.commit()

    return {"Mensagem": f"{len(data_to_insert)} links salvos com sucesso!"}
