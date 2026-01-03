# you can add multiple dictionary names for finding the highest number
marks={
    'ram':{'hindi':25,'english':35,'mathes':99},
    'shyam':{'hindi':57,'english':85,'mathes':37},
    'kiran':{'hindi':75,'english':86,'mathes':67},
}
highestmarks=0
highestname=''
for name,subjects in marks.items():
    sum=0
    for subject,mark in subjects.items():
        sum=sum+mark
        if sum>highestmarks:
            highestmarks=sum
            highestname=name
print('highest marks = ', highestmarks)
print('highest name = ' , highestname)