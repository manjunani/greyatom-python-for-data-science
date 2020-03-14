# --------------
# Importing header files
import numpy as np

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

#Loading data file and saving it into a new numpy array 
data = np.genfromtxt(path, delimiter=",", skip_header=1)

print(data.shape)

#Concatenating the new record to the existing numpy array
census=np.concatenate((data, new_record),axis = 0)

print(census.shape)



# --------------
import numpy as np
#Code starts here
age = census[:,0]
max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)
print(max_age)
print(min_age)
print(age_mean)
print(age_std)


# --------------
import numpy as np
#Code starts here
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]
len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)
race_list = [len_0,len_1,len_2,len_3,len_4]
minority_race = race_list.index(min(race_list))
print(minority_race)



# --------------
import numpy as np
senior_citizens = np.array(census[census[:,0]>60])
working_hours_sum = sum(senior_citizens[:,6])
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum / senior_citizens_len
print(avg_working_hours)



# --------------
#Code starts here
import numpy as np
high = np.array(census[census[:,1] > 10])
low = np.array(census[census[:,1] <= 10])
income_high = high[:,7]
income_low  = low[:,7]
avg_pay_high = np.mean(income_high)
avg_pay_low = np.mean(income_low)
print(avg_pay_high == avg_pay_low)


