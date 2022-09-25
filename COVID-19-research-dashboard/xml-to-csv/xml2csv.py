from errno import EIDRM
from operator import attrgetter
from unicodedata import name
import pandas as pd
from bs4 import BeautifulSoup
import os 
import csv 
import xml.etree.ElementTree as Xet
from lxml import objectify
 
#pick path depending on your machine 
path="/Users/vanessaklotzman/Documents/GitHub/COVID-19/documents/mendeley_library_files/xml_files/"
dirListing = os.listdir(path)
editFiles = []
for item in dirListing:
    if ".xml" in item:
        editFiles.append(path+''+item)

for j in range((len(editFiles))):

    file = open(editFiles[j],'r')
    contents = file.read()   


    data = {'titles':[],'periodicals':[],'urls':[],'keywords':[],'abstract':[],'dates':[]}

    soup = BeautifulSoup(contents, 'xml')
    for i  in soup.find_all("record"):
        titles=i.find('titles').text
        periodicals=i.find('periodical').text
        dates=getattr(i.find('dates'), 'text', None)
        urls=i.find('urls').text
        abstract= getattr(i.find('abstract'), 'text', None)
        print(abstract)
        keywords=i.find('keywords').text
        data['titles'].append(titles)
        data['periodicals'].append(periodicals)
        data['dates'].append(dates)
        data['urls'].append(urls)
        data['abstract'].append(abstract)
        data['keywords'].append(keywords)
    #print(data)
    df=pd.DataFrame(data)
    df.to_csv(editFiles[j]+".csv")

 

        


    

        
        
       


        

    


        
        







    
  
        

            
                

