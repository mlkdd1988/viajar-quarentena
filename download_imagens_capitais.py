import os
import pandas as pd 
import csv
from pathlib import Path
import shutil 

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
	
	base_path = os.getcwd() +"/"
	print(base_path)
		
	for estado in estados: 
		estado_path = "images/"+estado
		Path(estado_path).mkdir(parents=True, exist_ok=True)

		municipios = df.loc[df['estado'] == estado]
		for index, municipio in municipios.iterrows():

			# opcoes de resolucao: 'large','medium','icon','>400*300','>640*480','>800*600','>1024*768','>2MP','>4MP','>6MP','>8MP','>10MP','>12MP','>15MP','>20MP','>40MP','>70MP'

			if municipio['capital'] == '1':
				num_images = 30
				resolucao = '>1024*768'
			else:
				num_images = 10
				resolucao = '>800*600'
						
			search_keyword = str(municipio['nome']) +" "+ str(municipio['estado'])
			cmd = "python3 bing_scraper.py --search \"" + search_keyword +"\" --limit "+str(num_images)+" --download --chromedriver /usr/bin/chromedriver --size '"+str(resolucao)+"' --usage_rights labeled-for-reuse -o "+estado_path + " --extract_metadata " 
				
			#print (cmd)
			os.system(cmd)

			municipio_path = estado_path + "/"+str(municipio['nome'])
			old_name = estado_path +"/"+search_keyword.replace(" ", "_")
			new_name = base_path+municipio_path

			#apaga a pasta de destino se ela existir
			shutil.rmtree(new_name,ignore_errors=True)
			
			os.rename(old_name,new_name) 
			shutil.move('logs',new_name)
			
		
			
if __name__ == "__main__": 
	main()

