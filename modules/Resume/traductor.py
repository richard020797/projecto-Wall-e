import requests
def traductorEsToEn(texto):
	url = "https://www.googleapis.com/language/translate/v2?q="+ texto +"&target=en&format=text&source=es&fields=translations&key=AIzaSyD2Msaq4NvdE4FW23MCHSBp3tbmUROUlFs"
	response = requests.get(url)
	if response.status_code == 200:
   		results = response.json()
   		for result in results['data']['translations']:
   			return result['translatedText']
	else:
   		return "Upsis"


def traductorEnToEs(texto):
	url = "https://www.googleapis.com/language/translate/v2?q="+ texto +"&target=es&format=text&source=en&fields=translations&key=AIzaSyD2Msaq4NvdE4FW23MCHSBp3tbmUROUlFs"
	response = requests.get(url)
	if response.status_code == 200:
   		results = response.json()
   		for result in results['data']['translations']:
   			return result['translatedText']
	else:
		return "upsis"