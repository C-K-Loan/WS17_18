# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
classifier(("yes",33,"good"))
def  classifier (input_data) :
    prediction = ""
    if input_data[0] == "yes" : #smoker
        if input_data[1] < 29.5:
            prediction = "less risk"
        else: prediction = "more risk"
    else : #non smoker
        if input_data[2] == "good" : 
            prediction = "less risk"
        else :
            prediction = "more risk" 
        
    print("Predicted " + str(prediction) +"for  input : " + str(input_data))