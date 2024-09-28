import requests
from bs4 import BeautifulSoup

response = requests.get("https://player.quizalize.com/quiz/9581333f-e73c-45b0-8b8e-a2f51ff1a88e?&quizMode=standard&fbclid=IwAR3Sn1wvEupW9lmQWNBioaP85fck5be9Z5Lxe34KNIY4VT4IJMVD4mI9qvY")
soup = BeautifulSoup(response.content, "html.parser")
html_content = str(soup.html)
print(html_content)
