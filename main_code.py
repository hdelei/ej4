import numpy
import scipy
import sklearn
import collections, re
import os
import txt


#texts = ['procedente', 'improcedente']


#def get_all_txt():
#    for file in os.listdir('D:/ej4/datam'):
#        # file = obtenha o radical
#        # file = passe pelo stop_words
newtxt = txt.Txt()
filenames = newtxt.get_all_filenames()
for file in filenames:    
    print(newtxt.get_path() + '\\' + file)

#texto = open('teste.txt', 'r')

#print(texto.read())

#texts = [ 'umbigo umbigo']


#bagsofwords = [collections.Counter(re.findall(r'.+', txt)) for txt in texts]


#print(bagsofwords)
