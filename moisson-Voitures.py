# EDM5240-moisson
# Voici mon moissonage de mi-session. Par Myriam Eddahia ©.

# coding: utf-8

import csv
import requests
from bs4 import BeautifulSoup

fichier = "voitureskijiji.csv"

#J'indique à mon code d'extraire l'information ciblée de plusieurs pages.
for n in range(1,101):
	url = "https://www.kijiji.ca/b-autos-camions/ville-de-montreal/new/page-{}/c174l1700281a49?sort=priceAsc".format(n)
	print(url)

	contenu = requests.get(url)
	page = BeautifulSoup(contenu.text,"html.parser")
	# print(page)

	urlDesVoitures = page.find_all("div", class_="info-container")
	print(len(urlDesVoitures))

	for urlVoiture in urlDesVoitures:
		# voiture = []
		try:
			voiture = []
			url2 = urlVoiture.a["href"]
				# print(url2)
			url2 = "https://www.kijiji.ca" + url2
				# print(url2)
			voiture.append(url2)

			contenu2 = requests.get(url2)
			page2 = BeautifulSoup(contenu2.text,"html.parser")
			
			# Pour chaque annonce, je veux extraire son nom. Généralement, il s'agira du modèle de la voiture.

			titre = page2.title.text.split("|")[0].strip()
			print(titre)
			#voiture.append(titre)

			# Pour chaque annonce, je veux extraire le prix de la voiture.

			prix = page2.find("span", class_="currentPrice-2872355490").text
			print(prix)
			#voiture.append(prix)
			
			vroom = open(fichier,"a")
			guidon = csv.writer(vroom)
			guidon.writerow(voiture)

		except:
			print("Rien")
