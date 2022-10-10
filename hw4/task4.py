from io import StringIO
import csv

def read(scvString):
    f = StringIO(scvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    return out

# all = read('1,2\n1,3\n2,4')
# print(all)

def task(csvString):
    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    out = []
    for row in reader:
        out.append(row)
    n = 0
    print(out)
    for item in out:
        item[0] = int(item[0])
        item[1] = int(item[1])
        if item[0] > n:
            n = item[0]
        if item[1] > n:
            n = item[1]
    m = 2
    mat = [ [0] * m for i in range(n)]
    for item in out:
        mat[item[0] - 1][0] += 1
        mat[item[1] - 1][1] += 1
    for item in mat:
        print(item)

with open('task3.csv') as file:
     csvString = file.read()
     result = task(csvString)
print(result)

