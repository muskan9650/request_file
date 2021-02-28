import json
import requests
resp ='http://saral.navgurukul.org/api/courses'
var1= requests.get(resp)
data = var1.json()
for i in data:
    print(i)
a=[]
for j in range(len(data["availableCourses"])):
    print(j,":-", data["availableCourses"][j]['name'],data["availableCourses"][j]['id'])
    a.append(data["availableCourses"][j]['id'])
# print(a)
id=int(input("Select any course:- "))
s1= "http://saral.navgurukul.org/api/courses/"+a[id]+"/exercises" 
s2=requests.get(s1)
s3=s2.json()
x=[]
for k in range(len(s3['data'])):
    print(k,":-", s3['data'][k]['name'], s3['data'][k]['parent_exercise_id'])
    x.append(s3['data'][k]['parent_exercise_id'])
    if 'childExercises' in s3['data'][k]:
        for i in range(len(s3['data'][k]['childExercises'])):
            print("         ",i,":-", s3['data'][k]['childExercises'][i]['name'],s3['data'][k]['childExercises'][i]['id'])
id1=int(input("Select any parents :- "))
r=[]
for k in s3['data']:
    if k['id']==x[id1]:
        print(k['name'])
        for i in range(len(k['childExercises'])):
            print("         ",i,":-", k['childExercises'][i]['id'], k['childExercises'][i]['name'])
            r.append(k['childExercises'][i]['id'])
        # id3=int(input("choose id"))
        slugs=[] 
        for i in range(len(k['childExercises'])):
            slug=k['childExercises'][i]['slug']
            id=k['childExercises'][i]['id']
            m1='http://saral.navgurukul.org/api/courses/'+id+'/exercise/getBySlug?slug='+slug
            m2= requests.get(m1)
            m3 = m2.json()
            # print(m3['content'])
            slugs.append(m3['content'])
        id3=int(input("choose id"))
        slug=slugs[id3]
        print(slug)
        k=id3
        while i < len(slugs):
            pre_next=input("what next contant you want (p/n)")
            if pre_next=="p":
                k=k-1
                if k==-1:
                    print("last page")
                    break
                else:
                    print(k)
                    print(slugs[k])
                    continue
            elif pre_next=="n":
                k=k+1
                if k==len(slugs)
                    print("last page")
                    break
                else:
                    print(k)
                    print(slugs[id3+1])
                    continue
            else:
                print("write properly")
                continue
            i+=1
            


        