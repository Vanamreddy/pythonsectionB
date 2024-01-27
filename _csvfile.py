import csv
# file = open('sample.csv','w')
with open('sample.csv','w',newline='') as file:
    data=[
        [1,'chandan',23],
        [2,'nandan',34],
        [3,'bandan',19]

      ]
    record=csv.writer(file)
    record. writerow(['id','Name','age'])
    record.writerows(data)