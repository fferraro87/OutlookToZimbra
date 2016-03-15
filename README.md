#README

Questo programma permette di modificare ricorsivamente ogni .csv generato per outlook e come output genera un .csv importabile correttamente in Zimbra.

Questo programma richiede l'uso di Python e di una libreria esterna python-pandas

Per installare python-pandas :

Ubuntu e Debian-Based:

sudo apt-get install python-pandas

Archlinux e Arch-based:

sudo pacman -S python-pandas

Windows :

Bisogna installare Python 2.7 scaricando l'installer da qui http://www.python.it/download/

Poi Scaricare Anaconda da qui https://www.continuum.io/downloads

Avviare Anaconda e installare python-pandas


#USO

1)Mettere il file correggicsv.py all'interno della cartella che contiene tutti i .csv da modificare 

2)Andare sul terminale, spostarsi sulla cartella

3)Dare il comando : python correggicsv.py *.csv oppure
  python correggicsv.py nomefile.csv per convertire un singolo file


#OUTPUT

Troverai tutti i file modificati all'interno della cartella Aggiornati