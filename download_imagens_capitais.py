import os
import pandas as pd 
import csv

def main():
	dtypes = {
	"codigo_ibge": "category",
    "nome": "category",
    "latitude": "category",
    "longitude": "category",
    "capital": "category",
	"codigo_uf":"category",
	"estado":"category"
	}
	
	df = pd.read_csv("municipios.csv",  dtype=dtypes, usecols=list(dtypes))

	estados = df['estado'].drop_duplicates()
	for estado in estados: 
		municipios = df.loc[df['estado'] == estado]
		for index, municipio in municipios.iterrows():

			# opcoes de resolucao: '>8MP', '>10MP', '>12MP', '>15MP', '>20MP', '>40MP', '>70MP'

			if municipio['capital'] == '1':
				num_images = 30
				resolucao = 70
			else:
				num_images = 10
				resolucao = 8

			#baixando as fotos apenas das capitais
			if municipio['capital'] == '1':
				cmd = "python3 bing_scraper.py --search \"" + str(municipio['nome']) +" "+ str(municipio['estado']) +"\" --limit "+str(num_images)+" --download --chromedriver /usr/bin/chromedriver --size '>"+str(resolucao)+"MP' --usage_rights labeled-for-reuse"
				os.system(cmd)
			
if __name__ == "__main__": 
	main()

