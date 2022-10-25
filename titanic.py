import pandas as pd
dataframe=pd.read_csv("titanic_train.csv")
#NOT IMPORTANT FOR SURVIVED/NOT SURVIVED
del dataframe["PassengerId"]
del dataframe["Name"]
del dataframe["Fare"]
del dataframe["SibSp"]
del dataframe["Parch"]
del dataframe["Cabin"]
del dataframe["Ticket"]
number_of_passengers_Embarked_from_S=dataframe[dataframe.Embarked=='S'].shape[0]
number_of_passengers_Embarked_from_S_and_survived=dataframe[dataframe.Embarked=='S'][dataframe.Survived==1].shape[0]
print("Embarked = S :",number_of_passengers_Embarked_from_S_and_survived/number_of_passengers_Embarked_from_S)
number_of_passengers_Embarked_from_C=dataframe[dataframe.Embarked=='C'].shape[0]
number_of_passengers_Embarked_from_C_and_survived=dataframe[dataframe.Embarked=='C'][dataframe.Survived==1].shape[0]
print("Embarked = C :",number_of_passengers_Embarked_from_C_and_survived/number_of_passengers_Embarked_from_C)
number_of_passengers_Embarked_from_Q=dataframe[dataframe.Embarked=='Q'].shape[0]
number_of_passengers_Embarked_from_Q_and_survived=dataframe[dataframe.Embarked=='Q'][dataframe.Survived==1].shape[0]
print("Embarked = Q :",number_of_passengers_Embarked_from_Q_and_survived/number_of_passengers_Embarked_from_Q)
#so can't ignore embarked column

#mapping for gender male-1 and female-0
def mapping(s):
    if(s=="male"):
        return 1
    elif(s=="female"):
        return 0
dataframe["Gender"]=dataframe.Sex.apply(mapping)
del dataframe["Sex"]
x4=dataframe[dataframe.Gender==1].shape[0]
y4=dataframe[dataframe.Gender==1][dataframe.Survived==1].shape[0]
print("Gender = Male :",y4/x4)
x5=dataframe[dataframe.Gender==0].shape[0]
y5=dataframe[dataframe.Gender==0][dataframe.Survived==1].shape[0]
print("Gender = Female :",y5/x5)
#so can't ignore male and female similar to embarked logic
import numpy as np
print("Number of Null age : ",dataframe["Age"].isnull().sum())
#so significant number
#finding mean survived age
meanS= dataframe[dataframe.Survived==1].Age.mean()
dataframe["age"]=np.where(pd.isnull(dataframe.Age) & dataframe["Survived"]==1  ,meanS, dataframe["Age"])
meanNS=dataframe[dataframe.Survived==0].Age.mean()
dataframe.age.fillna(meanNS,inplace=True)#as baaki bache are NA for unsurvived
print(dataframe)
#so aise data cleaning using pandas
import matplotlib.pyplot as plt
plt.title("Analysis wrt Embarked(tells ki kitne percentage survived given titanic mei corresponding places se chadhe)")
labels=["Southampton","Cherbourg","Queenstown"]
p=number_of_passengers_Embarked_from_S_and_survived/number_of_passengers_Embarked_from_S
q=number_of_passengers_Embarked_from_C_and_survived/number_of_passengers_Embarked_from_C
r=number_of_passengers_Embarked_from_Q_and_survived/number_of_passengers_Embarked_from_Q
n=p+q+r
#doing this so that actual values dikhaye and not relative percentages
sizes=[p/n,q/n,r/n]
plt.pie(sizes,labels=labels,autopct="%.2f")
plt.axis("equal")
plt.show()
plt.title("Analysis wrt Gender(kitne percentage male and female survived)")
label=["Male","Female"]
p1=y4/x4
p2=y5/x5
n1=p1+p2
size=[p1/n1,p2/n1]
plt.pie(size,labels=label,autopct="%.2f")
plt.axis("equal")
plt.show()