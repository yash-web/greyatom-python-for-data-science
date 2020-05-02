# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)


print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))
#Code starts here
print(data.shape)
census=np.concatenate((data,new_record),axis=0)
census.shape
age=np.array(data[:,0])
race=np.array(data[:,2])
print("yash")
max_age=np.max(age)
print(max_age)
min_age=np.min(age)

print(min_age)
age_mean=round(np.mean(age),2)

print(age_mean)
age_std= round(np.std(age),2)
print(age_std)
race_0=(race==0)
len_0=np.sum(race_0)
print(len_0)
race_1=(race==1)
len_1=np.sum(race_1)
print(len_1)
race_2=(race==2)
len_2=np.sum(race_2)
print(len_2)
race_3=(race==3)
len_3=np.sum(race_3)
print(len_3)
race_4=(race==4)
len_4=np.sum(race_4)
print(len_4)
k=np.array([len_0,len_1,len_2,len_3,len_4])
l=np.min(k)
if(l==len_0):
    minority_race=0
if(l==len_1):
    minority_race=1
if(l==len_2):
    minority_race=2
if(l==len_3):
    minority_race=3
if(l==len_4):
    minority_race=4
senior_citizens=census[census[:,0]>60,:]
working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
avg_working_hours=round((working_hours_sum/senior_citizens_len),2)
print(avg_working_hours)
high=census[census[:,1]>10,:]
low=census[census[:,1]<=10,:]
avg_pay_high=round(np.mean(high[:,7]),2)
print(avg_pay_high)
avg_pay_low=round(np.mean(low[:,7]),2)
print(avg_pay_low)



