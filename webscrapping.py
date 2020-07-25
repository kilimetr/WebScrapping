# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr


import bs4 as BeautifulSoup
import requests
import csv

csv_file = open("lidl.csv", "w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["polozka", "cena"])

source = requests.get("https://www.lidl.cz/aktualni-nabidka").text

soup = BeautifulSoup.BeautifulSoup(source, "lxml")

nabidka = soup.find("div", class_ = "row")

polozky = nabidka.find_all("div")

for polozka in polozky:
	# print(polozka.prettify())
	try:
		polozka_nazev = polozka["data-name"]
		polozka_cena  = polozka["data-price"]

		csv_writer.writerow([polozka_nazev, polozka_cena])

		print(polozka_nazev)
		print(polozka_cena)

		print()
	except Exception as e:
		polozka_nazev = None
		polozka_cena  = None


csv_file.close()