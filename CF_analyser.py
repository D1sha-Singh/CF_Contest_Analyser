import requests
from datetime import datetime

name=input()
#t1 = str(input('Enter date(yyyy-mm-dd hh:mm:ss): '))
#start_datetime = datetime.strptime(t1, "%Y-%m-%d %H:%M:%S")

#t2 = str(input('Enter date(yyyy-mm-dd hh:mm:ss): '))
#end_datetime = datetime.strptime(t2, "%Y-%m-%d %H:%M:%S")

n=int(input())
prob_list=list(map(str,input("\nEnter the problem IDs : ").strip().split()))[:n]

contestID=int(prob_list[0][0:-1])

ans_list=[]
ans_dict={}
def contest_data():
    payload={'contestId': contestID, 'handle' : name}
    r=requests.get('https://codeforces.com/api/contest.status',payload)
    ob=r.json()
    for x in ob:
        if(x == 'result'):
            for i in ob[x]:
                for j in i:
                    if(j == 'verdict'):
                        #print(i[j])
                        key=i['problem']['index']
                        if(i[j] == 'OK'):
                            st=i['problem']['index']
                            #print(st)
                            st=str(contestID)+st
                            ans_list.append(st) 
                            ans_dict.setdefault(key, []).append(0)
                        elif(i[j] != "OK"):
                            key=i['problem']['index']
                            if (key in ans_dict):
                                temp=ans_dict[key]
                                tem=temp[0]
                                temp[0]=tem+1
                                ans_dict[key] = temp
                            else:
                                ans_dict.setdefault(key, []).append(0)
                    if(j == 'relativeTimeSeconds'):
                        #print(i[j])
                        key=i['problem']['index']
                        if (key in ans_dict):
                            temp=ans_dict[key]
                            temp.append(i[j])
                            ans_dict[key] = temp
    return None

#def contest_rating():
    payload={'contestId': contestID, 'handle' : name}
    r=requests.get('https://codeforces.com/api/contest.standings',payload)
    ob=r.json()
    #print(type(ob))
    for x in ob:
        #print(x)
        if(x == 'result'):
            for i in ob[x]:
                #print(i)
                if(i == 'problems'):
                    for j in i:
                        #print(j)
                        idx=i[j]['index']
                        print(ans_dict[idx])
                        if(j == 'rows'):
                            for k in i[j]:
                                if(k == 'penalty'):
                                    print(i[j]['penalty'])
                                    ans_dict[idx].append(i[j]['penalty'])
                    
    return None




contest_data()
#contest_rating()
ans_list.reverse()
print("Problems solved in contest")
print(ans_list)
print("ProblemID : Penalty(number of wrong submissions)")
for keys,values in ans_dict.items():
    print(keys,end=" : ")
    print(values)
