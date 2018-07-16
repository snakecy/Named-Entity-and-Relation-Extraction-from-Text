# Named-Entity-and-Relation-Extraction-from-Text
Here in my Code I am going to show you how to easily extract Named Entities and their relationship from Text.



#-*- coding: utf-8 -*- 



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
 


# Tokenizing the words and Tagging them according to Parts-of-Speech 
tokens = nltk.wordpunct_tokenize(text)

for w in tokens: 
        if w not in stop_words and string.punctuation: 
            tokens1.append(w)

posTagged=pos_tag(tokens) 
 
# Implementation of the concepts of : i.Named Entity Recognition ii.Relation Extraction 

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



# Output

(CLAUSE
  (NP Tata/NNP Consultancy/NNP Services/NNP Limited/NNP)
  (VP is/VBZ)
  (NP an/DT Indian/JJ multinational/JJ information/NN technology/NN))
=====================
(CLAUSE
  (NP business/NN solutions/NNS company/NN)
  (VP headquartered/VBD)
  (NP in/IN Mumbai/NNP))
=====================
(CLAUSE (NP TCS/NNP) (VP is/VBZ) (NP one/CD of/IN the/DT))
=====================
(CLAUSE
  (NP valuable/JJ IT/NNP services/NNS)
  (VP brands/VBZ)
  (NP worldwide/JJ))
=====================
(CLAUSE (NP 8/CD) (VP ]/VBD) (NP The/DT parent/NN group/NN))
=====================
(CLAUSE
  (NP TCS/NNP)
  (VP is/VBZ ranked/VBN)
  (NP 64th/CD overall/JJ in/IN the/DT Forbes/NNP World/NNP))
=====================
(CLAUSE
  (NP TCS/NNP)
  (VP became/VBD)
  (NP the/DT first/JJ Indian/JJ IT/NNP company/NN))
=====================
(CLAUSE (NP cap/NN) (VP stood/VBD) (NP at/IN Rs/NNP 6/CD))
=====================
(CLAUSE
  (NP Tamil/NNP Nadu/NNP 600096/CD)
  (VP is/VBZ)
  (NP postal/JJ address/NN of/IN chennai/NN office/NN))
=====================
(CLAUSE
  (NP TCS/NNP)
  (VP established/VBD)
  (NP
    the/DT
    first/JJ
    software/NN
    research/NN
    center/NN
    in/IN
    India/NNP))
=====================
(CLAUSE
  (NP create/VB code/NNS)
  (VP based/VBN)
  (NP on/IN a/DT model/NN of/IN a/DT software/NN))
=====================
(CLAUSE
  (NP rewrite/VB the/DT code/NN)
  (VP based/VBN)
  (NP on/IN the/DT user/NN))
=====================
(CLAUSE (NP be/VB) (VP manufactured/VBN) (NP using/VBG))
=====================
(CLAUSE
  (NP TCS/NNP)
  (VP deployed/VBD)
  (NP
    thousands/NNS
    of/IN
    these/DT
    filters/NNS
    in/IN
    the/DT
    Indian/JJ
    Ocean/NNP
    tsunami/NN
    disaster/NN
    of/IN
    2004/CD
    as/IN
    part/NN
    of/IN))
=====================
(CLAUSE
  (NP This/DT product/NN)
  (VP has/VBZ been/VBN marketed/VBN)
  (NP in/IN India/NNP as/IN Tata/NNP swach/NN))
=====================
(CLAUSE (NP TCS/NNP) (VP is/VBZ) (NP one/CD of/IN the/DT))
=====================
(CLAUSE
  (NP 102/CD ]/JJ TCS/NNP)
  (VP had/VBD)
  (NP a/DT total/NN of/IN 387/CD))
=====================
(CLAUSE (NP 31/CD %/NN) (VP were/VBD) (NP women/NNS))
=====================
(CLAUSE (NP Indian/JJ nationals/NNS) (VP was/VBD) (NP 21/CD))
=====================
(CLAUSE (NP 13/CD) (VP were/VBD) (NP US/NNP))
=====================
(CLAUSE
  (NP TCS/NNP)
  (VP recruited/VBD)
  (NP a/DT total/NN of/IN 69/CD))
=====================
(CLAUSE (NP 276/CD) (VP were/VBD based/VBN) (NP in/IN India/NNP))
=====================
(CLAUSE
  (NP 452/CD)
  (VP were/VBD based/VBN)
  (NP in/IN the/DT rest/NN of/IN the/DT world/NN))
=====================
(CLAUSE
  (NP the/DT rate/NN of/IN attrition/NN)
  (VP was/VBD)
  (NP 10/CD))
=====================
(CLAUSE
  (NP 69/CD)
  (VP ]/VBD)
  (NP The/DT average/JJ age/NN of/IN a/DT TCS/NNP employee/NN))
=====================
(CLAUSE
  (NP 69/CD)
  (VP ]/VBD)
  (NP The/DT employee/NN utilisation/NN rate/NN))
=====================
(CLAUSE (NP 13/CD) (VP was/VBD) (NP 82/CD %/NN))
=====================
(CLAUSE (NP 69/CD ]/JJ TCS/NNP) (VP was/VBD) (NP the/DT fifth/JJ))
=====================
(CLAUSE
  (NP United/NNP States/NNPS)
  (VP visa/VBP)
  (NP recipient/NN in/IN 2008/CD))
