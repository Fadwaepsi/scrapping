def list_pair(list):
    listPair=[]
    for a in list:
        if a % 2 == 0 :
            print("a est paire")
            listPair.append(a)
        else:
            print("a est impair")
    return listPair

list1=[1,2,4,8,7]
result=list_pair(list1)
print (result)



def fusionListe(liste1,liste2):
    listefusion=[]
    for i in  range(len(liste1)):
        listefusion.append(liste1[i]+liste2[i])

#

def dabl_list(list):
    list_Final=[]
    for e in list :
        if e not in list_Final :
            list_Final.append(e)
        else: 
            print("list_Final")
    return list_Final

list1=[1,1,2,3,4,4]
result=list_Final(list1)
print(result)


def return_list(list):
    list_F=[]
    e=len(list)-1
    for e in list :
        while e>=0:
            list_F.append(list(e))
            e=e-1
        return list_F
    
list2=(1,2,3,4)
result=list_F(list2)
print(result)
    


