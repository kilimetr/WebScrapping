# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr



import sys
import json


json_retezec = """
    {
     "Kontakty": {
     			  "Rodina":
     			  		   {
     			  		    "Blízká":   {"Mamka": "777-777-777", "Taťka": "777-777-771"},
     			  		    "Vzdálená": {"Sestřenice_1": "888-888-881", "Sestřenice_2": "888-888-882"}
     			  		   },
     			  "Kamarádi": {"K_1": "222-222-221", "K_2": "222-222-222", "K_3": "222-222-223"}
     }
    }
"""


# json_retezec = """
#     {
#       "jméno": "Anna",
#       "město": "Brno",
#       "jazyky": ["čeština", "angličtina", "Python"],
#       "věk": 26
#     }
# """

data = json.loads(json_retezec)

# print(data)
# print(sys.getsizeof(data))

# for value in data.values():
# 	print(value)


# for k1, v1 in data.items():
#     for k2, v2 in v1.items():
#         for k3, v3 in v2.items():
#             print(k1, k2, k3, v3)
#             print(v3)
            # for k4, v4 in v3.items():
           		# print(k4, v4)



def projdi(path, obj):
	if isinstance(obj, dict):
		for k, v in obj.items():
			projdi(path + [k], v)
	else:
		print(path, obj)
		# pass

projdi([], data)




