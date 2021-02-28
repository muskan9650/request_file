import json
import requests

my_file =open("saral_request.json","r")
data = json.load(my_file)
for course in data:
    print(course)
courses=[]
for course in range(len(data["availableCourses"])):
    print(course+1,":-", data["availableCourses"][course]['name'],data["availableCourses"][course]['id'])
    courses.append(data["availableCourses"][course]['id'])
id=int(input("Select any course:- "))
parent_name=open("parent_file.json")
parent_data=json.load(parent_name)
parent_index=[]
for parents in range(len(parent_data['data'])):
    print(parents+1,":-", parent_data['data'][parents]['name'], parent_data['data'][parents]['parent_exercise_id'])
    parent_index.append(parent_data['data'][parents]['parent_exercise_id'])
    if 'childExercises' in parent_data['data'][parents]:
        for child in range(len(parent_data['data'][parents]['childExercises'])):
            print("         ",child,":-", parent_data['data'][parents]['childExercises'][child]['name'],parent_data['data'][parents]['childExercises'][child]['id'])
id1=int(input("Select any parents for knowing its child :- "))
child_index=[]
for parents in parent_data['data']:
    if parents['id']==parent_index[id1-1]:
        print(parents['name'])
        for child in range(len(parents['childExercises'])):
            print("         ",child+1,":-", parents['childExercises'][child]['id'], parents['childExercises'][child]['name'])
            child_index.append(parents['childExercises'][child]['id'])
            id3=int(input("choose id for getting slug"))