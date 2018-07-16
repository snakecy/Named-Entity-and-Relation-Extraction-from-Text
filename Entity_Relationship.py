


# -*- coding: utf-8 -*- 



#import PyPDF2 
import nltk 
from nltk.collocations import * 
from nltk import * 
from geotext import GeoText 

from nltk.corpus import stopwords 
import re 
import io 
import string
from nltk.stem import WordNetLemmatizer 


bigram_measures = nltk.collocations.BigramAssocMeasures() 
stop_words = set(stopwords.words('english')) 

filename = "Report.txt" 
with open(filename,encoding ="utf8") as my_file: 
    text = my_file.read() 
 


#Tokenizing the words and Tagging them according to Parts-of-Speech 
tokens = nltk.wordpunct_tokenize(text)

for w in tokens: 
        if w not in stop_words and string.punctuation: 
            tokens1.append(w)

posTagged=pos_tag(tokens) 
 
#Implementation of the concepts of : i.Named Entity Recognition ii.Relation Extraction 

grammar = r""" 
  NP: {<DT*|NN.*|\$?\d+(\.\d+)?%?|VBG*|[][.,;"'?():-_`]|IN*|,|CD*|JJ|NN.*>+} 
  VP:{<V.*>+}  
  CLAUSE: {<NP><VP><NP>}         
  """ 
    
         
cp=nltk.RegexpParser(grammar) 
tree1=cp.parse(posTagged) 


for lines in text.split('.'): 
    for phrase in lines.split(','): 
        posTagged1 = pos_tag(nltk.wordpunct_tokenize(phrase)) 
        tree=cp.parse(posTagged1) 
        for sub in tree.subtrees(): 
            if sub.label() == 'CLAUSE': 
                print("=====================") 
                print(sub) 




