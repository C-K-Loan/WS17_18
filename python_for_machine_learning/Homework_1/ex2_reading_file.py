# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def read_data_ex2( file_name): #ex2
    f = open(file_name, 'r')
    L = []
    split_line = ""
    smoker = "yes"
    age = 0
    diet = "good"
    tuple_list = []
    data_tuple =("first","second","third")
    for line in f :   #read data line by line 
        split_line = line.split(',')
        smoker = split_line[0]
        age = split_line[1]
        diet = split_line[2][:-1]
        data_tuple = (str(smoker), int(age), str(diet))
#        print(str(data_tuple))
        tuple_list.append(data_tuple)

    
    return tuple_list
    
def  classifier (input_data) : #ex1
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
        
    #print("Predicted " + str(prediction) +" for  input : " + str(input_data))
    return prediction
   
 

def calculate_percantage_more_risk(data):#ex3 Done
    less_risk_count = 0
    more_risk_count = 0
    classsifier_result = ""
    one_perc_data_count = 0
    for patient in data:
        classifier_result = classifier(patient)
        if classifier_result == "more risk" : more_risk_count +=1
        if classifier_result == "less risk" : less_risk_count +=1
        
    data_count = float(less_risk_count + more_risk_count )
    print(str(data_count))
    one_perc_data_count = float(data_count / 100)
    print(one_perc_data_count)
    more_risk_perc = float(more_risk_count / one_perc_data_count)
    
    print("more risk : " + str(more_risk_perc))
    return more_risk_prerc
    

    
def read_train_data_ex4(file_name): #ex4
    f = open(file_name, 'r')
    L = []
    split_line = ""
    smoker = "yes"
    age = 0
    diet = "good"
    risk = ""
    tuple_list = []
    data_tuple =(("first","second","third"),("risk"))
    for line in f :   #read data line by line 
        split_line = line.split(',')
        smoker = split_line[0]
        age = split_line[1]
        diet = split_line[2]
        risk = split_line[3][:-1]
        data_tuple = (str(smoker), int(age), str(diet),str(risk))
#        print(str(data_tuple))
        tuple_list.append(data_tuple)

    
    print(tuple_list)
    return tuple_list
    

    

def distance_function(a,b):
   distance = (a[0]!= b[0]) + ((a[1]-b[1])/50)**2 + (a[2]!= b[2])
   #print(str(distance))
   return distance



def exercise5a(input_data, example):## nearest neighbour
    distance_data = ""
    result = input_data[3]

    smallest = distance_function(input_data[0], example)
    for data in input_data:
        if(distance_function(data, example)<  smallest):
            result = data[3]
     #       print("RESULT BECOMES" , data[3])
    #    print(data[2])
    print("result is :" + str(result)) 
    return result
          
         

def exercicse5a_sol():        
    data_list = read_train_data_ex4("health-train.txt")
    exercise5a(data_list,("yes",31,"good")) 

def exercicse5b_sol():
    test_list = read_data_ex2("health-test.txt")
    train_data = read_train_data_ex4("health-train.txt")
    disagree = []
    for point in test_list:         
        knn = exercise5a(train_data,point)
        tree = classifier(point)
        if (knn != tree): 
            print("KNN PREDIT : " + str(knn) + " and Tree " + str(  tree))
            disagree.append(point)
    print("RESULT : " + str(disagree)) 




exercicse5b_sol()


class solutions:
    #todo constructor
    def exercise3(self): 
        data_list = read_data_ex2("health-test.txt")
        calculate_percantage_more_risk(data_list)

    
    def exercise4(self):
        read_train_data_ex4("health-train.txt")
