#Programma creato da Francesco Ferraro
#Prevede l'installazione della libreria python-pandas
import sys
import os
from pandas.io.parsers import read_csv
import pandas as pd

#Creo una nuova cartella per mettere i nuovi csv modificati
os.makedirs('Aggiornati',exist_ok=True)
#Cerco i file csv all'interno della cartella'
#for csvFilename in os.listdir('.'):
#    if not csvFilename.endswith('.csv'):
#        continue
#Creo un dataframe
for csvFilename in sys.argv[1:]:
    data=read_csv(csvFilename,error_bad_lines=False)
    #Seleziono i campi vuoti delle email e copio dalla colonna dopo della stessa riga
    data.loc[pd.isnull(data['mail1_waddr']),'mail1_waddr'] = data[pd.isnull(data['mail1_waddr'])]['mail1_haddr']
    #Cancello la colonna appena copiata
    del data["mail1_haddr"]
    del data["title"]
    del data["telex_waddr"]
    #Rinomino gli header correttamente
    data.rename(columns={'firstname':'FirstName' , 'lastname':'LastName' ,
    'nickname':'Suffix' , 'company_waddr':'Company' , 'mail1_waddr':'EmailAddress'
     , 'mail2_waddr':'Email2Address','mail3_waddr':'Email3Address','url3_waddr':'Email4Address'}, inplace=True)
    #Cancello le colonne vuote
    filtered_data = data.dropna(axis='columns' , how='all')
    #Scrivo il file nella cartella Aggiornati
    filtered_data.to_csv(os.path.join('Aggiornati', csvFilename),index=False)
