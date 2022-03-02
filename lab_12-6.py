# Author: SCT (AMDG) 3/1/22

grades = {'End S1 Labs':100,'Start S2 Labs':100,'cycle 10 labs':100,'Mid-year Project Proposal':100,'cycle 10 practice quiz':100,'cycle 10 quiz':60}

print(grades.values())

for (k, v) in grades.items():
    print(k,v)


for (k,v) in grades.items():
    if v > 70:
        print(k,v)

for (k,v) in grades.items():
    if v < 50:
        print(k,v)