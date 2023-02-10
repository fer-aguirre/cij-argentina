# Import libraries
import re
import requests
import rfeed
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# Web scraping
# Define url parameter
url = 'https://www.cij.gov.ar/sentencias.html'

# Disable warning
disable_warnings(InsecureRequestWarning)

# Make requests to the specified urls
response = requests.get(url, verify=False)

# Return content of the response
html = response.text

# Parse html
soup = BeautifulSoup(html, 'html.parser')

# Extract data from html
pdfs = ['https://www.cij.gov.ar/' + i.get("href") for i in soup.find_all('a', attrs={'class': 'download'})]

files = []
for i in soup.find_all("div",{"class": "result"}):
    files.extend(j.text for j in i.find_all("li"))

# Process data
tribunal = list(filter(lambda x: 'Tribunal:' in x, files))
expediente = list(filter(lambda x: 'Expediente N°:' in x, files))
caratula = list(filter(lambda x: 'Carátula:' in x, files))
fecha = list(filter(lambda x: 'Fecha de sentencia:' in x, files))

tribunal_clean = [x.replace('Tribunal: ', '') for x in tribunal]
expediente_clean = [x.replace('Expediente N°: ', '') for x in expediente]
caratula_clean = [x.replace('Carátula: ', '') for x in caratula]
fecha_clean = [x.replace('Fecha de sentencia: ', '') for x in fecha]

# Create RSS feed
items_ = []

for i in range(len(pdfs)):
    item = rfeed.Item(
    title=expediente_clean[i],
    link=pdfs[i],
    description = caratula_clean[i],
    author = tribunal_clean[i],
    guid = rfeed.Guid(pdfs[i]),
    )
    items_.append(item)

feed = rfeed.Feed(
	title = "Centro de Información Judicial",
	link = "https://www.cij.gov.ar/sentencias.html",
	description = "El Centro de Información Judicial es un organismo creado por la Corte Suprema para generar un nuevo puente de comunicación entre la Justicia y la comunidad",
	language = "es",
	items = items_)

rss = feed.rss()

# Save rss as 'xml' file
with open("./assets/cij.xml", "w") as f:
    f.write(rss)

