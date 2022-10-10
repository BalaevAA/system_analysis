import csv
import sys
from io import StringIO




def task(csvString):

    '''
    arr1 - прямое управление
    arr2 - прямое подчинение
    arr3 - косвенное управление
    arr4 - косвенное подчинение
    arr5 - соподчинение
    '''

    f = StringIO(csvString)
    reader = csv.reader(f, delimiter=',')
    graph = []
    for row in reader:
        graph.append(row)
    for x in graph:
        for y in x:
            y = int(y)

    arr1 = []
    for x in graph:
        if x[0] not in arr1:
            arr1.append(str(x[0]))

    arr2 = []
    for x in graph:
        if x[1] not in arr2:
            arr2.append(str(x[1]))

    f = graph
    g = graph
    arr3 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][0] not in arr3 and f[i][1] == g[j][0]:
                arr3.append(str(f[i][0]))

    arr4 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] not in arr4 and f[i][0] == g[j][1]:
                arr4.append(str(f[i][1]))

    arr5 = []
    for i in range(len(f)):
        for j in range(len(g)):
            if i != j and f[i][1] not in arr5 and f[i][0] == g[j][0]:
                arr5.append(str(f[i][1]))

    return [arr1, arr2, arr3, arr4, arr5]


# with open('task3.csv') as file:
#     csvString = file.read()
#     result = task(csvString)
# print(result)