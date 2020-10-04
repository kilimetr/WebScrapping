# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import bs4 as BeautifulSoup
import requests 


source = requests.get("https://www.alza.cz/logitech-mx-master-3-d5669357.htm", 
					  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0")

soup = BeautifulSoup.BeautifulSoup(source.text, "lxml")

cena = "2 590,-"

aaa = soup.find_all(text = True)

for prvek in aaa:
	if prvek == cena:
		print("našel jsem cenu")
		print(prvek)
	else:
		pass

	try:
		cena_mod = "2\u00A0590,-"

		if prvek == cena_mod:
			print("našel jsem cenu_mod")
		else:
			pass

	except Exception as e:
		pass


print()

cena = 2590
mys_cena = soup.find("span", class_ = "bigPrice").text
print(mys_cena)

