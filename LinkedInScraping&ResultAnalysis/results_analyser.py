from collections import Counter

from pandas import *

# reading CSV file
data = read_csv("results.csv")

# converting column data to list
title = data['title'].tolist()
seniority_level = data['seniority_level'].tolist()
job_function = data['job_function'].tolist()
employment_type = data['employment_type'].tolist()
industries = data['industries'].tolist()



#  this would print all the items in the different fields and the number of times they occured

# print(Counter(title))
# print('\n\n')
# print(Counter(seniority_level))
# print('\n\n')
# print(Counter(job_function))
# print('\n\n')
# print(Counter(employment_type))
# print('\n\n')
# print(Counter(industries))


# this would give the the number of job in the particular field we looked into, top 5 items in different fields and the number of times they occured
sortedjobtitles={k: v for k, v in sorted(Counter(title).items(), key=lambda item: item[1], reverse=True)}
top5jobs=[]
top5jobs_with_count={}
i=0
for key,val in sortedjobtitles.items():
    i += 1
    # if i==1:
    #     continue
    top5jobs.append(key)
    top5jobs_with_count[key]=val
    if i==6:
        break
print(top5jobs)
print(top5jobs_with_count)
print('\n\n')


sortedseniority_level={k: v for k, v in sorted(Counter(seniority_level).items(), key=lambda item: item[1], reverse=True)}
top5seniority_level=[]
top5seniority_level_with_count={}
i=0
for key,val in sortedseniority_level.items():
    i += 1
    # if i==1:
    #     continue
    top5seniority_level.append(key)
    top5seniority_level_with_count[key]=val
    if i==6:
        break
print(top5seniority_level)
print(top5seniority_level_with_count)
print('\n\n')

sortedjob_function={k: v for k, v in sorted(Counter(job_function).items(), key=lambda item: item[1], reverse=True)}
top5job_function=[]
top5job_function_with_count={}
i=0
for key,val in sortedjob_function.items():
    i += 1
    # if i==1:
    #     continue
    top5job_function.append(key)
    top5job_function_with_count[key]=val
    if i==6:
        break
print(top5job_function)
print(top5job_function_with_count)
print('\n\n')

sortedemployment_type={k: v for k, v in sorted(Counter(employment_type).items(), key=lambda item: item[1], reverse=True)}
top5employment_type=[]
top5employment_type_withcount={}
i=0
for key,val in sortedemployment_type.items():
    i += 1
    # if i==1:
    #     continue
    top5employment_type.append(key)
    top5employment_type_withcount[key]=val
    if i==6:
        break
print(top5employment_type)
print(top5employment_type_withcount)
print('\n\n')

sortedindustries={k: v for k, v in sorted(Counter(industries).items(), key=lambda item: item[1], reverse=True)}
top5industries=[]
top5industrieswithcount={}
i=0
for key,value in sortedindustries.items():
    i += 1
    # if i==1:
    #     continue
    top5industries.append(key)
    top5industrieswithcount[key]=value
    if i==6:
        break
print(top5industries)
print(top5industrieswithcount)
print('\n\n')
