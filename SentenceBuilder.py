# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 11:54:30 2018

@author: Prav
"""
import re
theme = "does [ent1] have any [ent2] associated with [ent3] EOS"
global sentences
sentences =[]
def buildSentences(info):
    sen = theme.replace("[ent1]", info[0]).replace("[ent2]", info[1]).replace("[ent3]", info[2])
    sen =re.sub('\s{2,}', ' ', sen)
    sentences.append(sen)
    return sentences
        






items ={}
items['ex1']=" john,variants,Parkinson’s disease"
items['ex2']=" john,variants,Acute Myelogenous Leukemia (AML)"
items['ex3']=" john,variants,Alzheimer’s Disease (AD)"
items['ex4']=" mark,variants,Autism Spectrum Disorders (Autism)"
items['ex5']=" john,variants,Autoimmune/ immunology"
items['ex6']=" john,variants,Cardiovascular"
items['ex7']=" peter,variants,Coronary Artery Disease (General)"
items['ex8']=" john,variants,Dry Age-Related Macular Degeneration (Dry AMD) (Ophthalmology)"
items['ex9']=" john,variants,Fragile X Syndrome"
items['ex10']=" jenny,variants,Cardiovascular"
items['ex11']=" john,variants,Gastroenterology (non inflammatory bowel disease)"
items['ex12']=" joseph,variants,Glaucoma / Ocular Hypertension (Ophthalmology)"
items['ex13']=" john,variants,Healthy Controls"
items['ex14']=" john,variants,Hematology"
items['ex15']=" mark,variants,Inflammatory Bowel Disease (IBD)"
items['ex16']=" john,variants,Liver Failure / Cirrhosis"
items['ex17']=" john,variants,Macular Degeneration"
items['ex18']=" mathew,variants,Marrow Or Peripheral Blood Stimulator"
items['ex19']=" john,variants,Liver Failure / Cirrhosis"


for key, value in items.items():
    buildSentences(value.split(","))