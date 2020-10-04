# author Dominik Capkovic 
# contact: domcapkovic@gmail.com; https://www.linkedin.com/in/dominik-čapkovič-b0ab8575/
# GitHub: https://github.com/kilimetr


def letter_conv_fun(input_phrase):
	abeceda = {"A": "a", "B": "b", "C": "c", "D": "d", "E": "e", "F": "f", "G": "g", "H": "h", "I": "i", "J": "j", "K": "k", "L": "l", "M": "m", "N": "n", "O": "o", "P": "p",
			   "Q": "q", "R": "r", "S": "s", "T": "t", "Ť": "ť", "U": "u", "V": "v", "W": "w", "X": "x", "Y": "y", "Z": "z", "Á": "á", "Č": "č", "É": "é", "Ě": "ě", "Í": "í", 
			   "Ó": "ó", "Š": "š", "Ř": "ř", "Ž": "ž", "Ý": "ý"}


	i = 1
	for key in abeceda.keys():
		for pismeno in input_phrase:
			if pismeno == key:
				pismeno_nove = abeceda[key]

				output_phrase = input_phrase.replace(pismeno, pismeno_nove)

		i = i + 1


	output_phrase = output_phrase.title()

	print(output_phrase)
	print("done")

	return output_phrase


