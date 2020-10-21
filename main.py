import requests
import math
import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import json

data = []

with open(askopenfilename()) as csv_file:  # öffnet das csv-file
    csv_reader = csv.reader(csv_file, delimiter=',')  # initialisiert den Reader fürs csv
    for row in csv_reader:
        data.append(row)


file = open(askopenfilename(), 'r')
dist = []
print(data)
for line in file:
    b = 0
    a=0
    for k in range(len(line)):
        if line[k]=='\t':

            if float(line[:k]) >= -8.5 and float(line[:k]) <= -3:
                b=1
                a=k
            break

    if b==0:
        continue

    for k in range(len(line)-a):
        if line[k+a+1] == '\t':

            if float(line[a:k+a+1]) >= 45 and float(line[:k]) <= 60:
                b = 1
            break

    if b == 0:
        continue


    dist.append(line)




file.close()


for row in data:
    if row[0]=='Timecode':
        continue

    long = float(row[26])
    f= (long+0.02)/0.04
    li_f = int(f)
    if (li_f-f)>(f-(li_f-1)):
        long = ((li_f-1)*0.04)-0.02
    else:
        long = (li_f*0.04)-0.02

    print(li_f)
    lat = float(row[27])
    f = (lat-0.02) / 0.04
    li_f = int(f)
    if (f-li_f) > ((li_f+1)-f):
        lat = (float(li_f + 1)) * 0.04 +0.02
    else:
        lat = float(li_f) * 0.04+0.02

    strlat = str(lat)
    strlong = str(long)
    print(strlat)
    print(strlong)

    n = len(strlat)
    for k in range(len(strlat)):
        if strlat[k] == '.':
            print(strlat[k])
            for i in range(min(len(strlat)-k,4)):
                print(strlat[i + k])
                if (strlat[i + k] == '0' or strlat[i + k] == '9') and i>1:
                    n = i + k
                    print(n)
                    break
                if (strlat[i+k] == '9') and i>1:
                    n = i+k
                    liste = list(strlat)
                    liste[k+i-1] = chr(int(liste[k+i-1])+1)
                    strlat = "".join(liste)
                    print(n)
                    break

            break

    strlat = strlat[:n]
    n = len(strlong)
    for k in range(len(strlong)):
        if strlong[k] == '.':
            for i in range(min(4,len(strlong)-k)):
                print("strlong[i+k] :" +strlong[i+k])
                if (strlong[i+k] == '0') and i>1:
                    n = i+k
                    print(n)
                    break
                if (strlong[i+k] == '9') and i>1:
                    n = i+k
                    liste = list(strlong)
                    liste[k + i - 1] = str(int(liste[k + i - 1]) + 1)
                    print(liste)
                    strlong = "".join(liste)
                    print("n : "+str(n))
                    break
            break


    strlong = strlong[:n]


    print((strlong+"\t"+strlat))
    res = [i for i in dist if (strlong+"\t"+strlat+"\t") in i]
    distancestring = res[0]
    print(distancestring)
    print(len(distancestring))
    n=1
    for k in range(len(distancestring)):
        print(k)
        if distancestring[len(distancestring)-k-1] == '\t':
            n = k
            break
    print(distancestring[-n:])
    row.append(float(distancestring[-n:]))


with open(askopenfilename(), mode='w', newline='') as resultate:
    resultatewriter = csv.writer(resultate, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        resultatewriter.writerow(row)

# -179.98 89.98	712.935
# -179.94	89.98	712.934