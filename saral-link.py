imimport json
import requests

resp ='http://saral.navgurukul.org/api/courses'
var1= requests.get(resp)
data = var1.json()
my_file =open("saral_request.json","w")
Data = json.dump(data,my_file,indent=4)
my_file.close()
for course in data:
    print(course)
courses=[]
for course in range(len(data["availableCourses"])):
    print(course+1,":-", data["availableCourses"][course]['name'],data["availableCourses"][course]['id'])
    courses.append(data["availableCourses"][course]['id'])
id=int(input("Select any course:- "))
parent_link= "http://saral.navgurukul.org/api/courses/"+courses[id-1]+"/exercises" 
parent_responce=requests.get(parent_link)
parent_data=parent_responce.json()
parent_name=open("parent_file.json","w")
parent=json.dumps(parent_data, indent=4)
parent_name.write(parent)
parent_name.close()
parent_index=[]
for parents in range(len(parent_data['data'])):
    print(parents+1,":-", parent_data['data'][parents]['name'], parent_data['data'][parents]['parent_exercise_id'])
    parent_index.append(parent_data['data'][parents]['parent_exercise_id'])
    if 'childExercises' in parent_data['data'][parents]:
        for child in range(len(parent_data['data'][parents]['childExercises'])):
            print("         ",child,":-", parent_data['data'][parents]['childExercises'][child]['name'],parent_data['data'][parents]['childExercises'][child]['id'])
            child_data=parent_data['data'][parents]['childExercises'][child]
            child_name=open("child_file.json","a")
            child_du=json.dumps(child_data, indent=4)
            child_name.write(child_du)
            child_name.close()

id1=int(input("Select any parents :- "))
child_index=[]
for parents in parent_data['data']:
    if parents['id']==parent_index[id1-1]:
        print(parents['name'])
        for child in range(len(parents['childExercises'])):
            print("         ",child+1,":-", parents['childExercises'][child]['id'], parents['childExercises'][child]['name'])
            child_index.append(parents['childExercises'][child]['id'])
        slugs=[] 
        for i in range(len(parents['childExercises'])):
            slug=parents['childExercises'][i]['slug']
            id=parents['childExercises'][i]['id']
            slug_link='http://saral.navgurukul.org/api/courses/'+id+'/exercise/getBySlug?slug='+slug
            slug_request= requests.get(slug_link)
            sluging = slug_request.json()
            slugs.append(sluging['content'])
        id3=int(input("choose id for getting slug"))
        slug=slugs[id3]
        print(slug)
        k=id3
        while i <= len(slugs):
            pre_next=input("what next contant you want (p/n)")
            if pre_next=="p":
                k=k-1
                if k==0:
                    print("last page")
                    break
                else:
                    print(k)
                    print(slugs[k])
                    continue
            elif pre_next=="n":
                k=k+1
                if k==len(slugs)+1:
                    print("last page")
                    break
                else:
                    print(k)
                    print(slugs[id3])
                    continue
            else:
                print("write properly")
                continue
            i+=1