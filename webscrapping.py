# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr


import bs4 as BeautifulSoup
import requests
import csv

csv_file = open("lidl.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Položka", "Množství", "Cena"])

source = requests.get("https://www.lidl.cz/aktualni-nabidka").text

soup = BeautifulSoup.BeautifulSoup(source, "lxml")

nabidka = soup.find("div", class_ = "row")

polozky = nabidka.find_all("div")


for polozka in polozky:
# 	print(polozka.prettify())

	try:
		polozka_nazev = polozka["data-name"]
		polozka_cena  = polozka["data-price"]
		polozka_mnozstvi = polozka.find("div", class_ = "product__text").p.text


		csv_writer.writerow([polozka_nazev, polozka_cena, polozka_mnozstvi])

		# print(polozka_nazev)
		# print(polozka_cena)
		# print(polozka_mnozstvi)

	except Exception as e:
		polozka_nazev    = None
		polozka_cena     = None
		polozka_mnozstvi = None


csv_file.close()


