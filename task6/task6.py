import numpy as np
import json


def to_json(s):
    js = json.loads(s)
    s1 = []
    for j in js:
        if isinstance(j, list):
            s1.append(j)
        if isinstance(j, str):
            a = []
            a.append(j)
            s1.append(a)
    return s1


def task(js):
    j = to_json(js)
    experts_matrices = []
    for eval in j:
        exp = np.zeros((len(eval), len(eval)))
        for i in range(len(eval)):
            for j in range(len(eval)):
                if eval[i] < eval[j]:
                    exp[i][j] = 1
                if eval[i] == eval[j]:
                    exp[i][j] = 0.5
                if eval[i] > eval[j]:
                    exp[i][j] = 0
        experts_matrices.append(exp)

    m = np.zeros(experts_matrices[0].shape)
    for i in range(experts_matrices[0].shape[0]):
        for j in range(experts_matrices[0].shape[0]):
            for k in range(len(experts_matrices)):
                m[i][j] += 1 / experts_matrices[k].shape[0] * experts_matrices[k][i][j]

    k0 = []
    for i in range(experts_matrices[0].shape[0]):
        k0.append(1 / experts_matrices[0].shape[0])

    y = np.dot(m, k0)
    l = np.dot(np.array([1, 1, 1]), y)
    k1 = np.dot(1 / l, y)

    while max(abs(k1 - k0)) >= 0.001:
        k0 = k1
        y = np.dot(m, k0)
        l = np.dot(np.array([1, 1, 1]), y)
        k1 = np.dot(1 / l, y)
    deli_ans = ['%.3f' % elem for elem in k1]
    ans = [float(x) for x in deli_ans]
    return ans


# str1 = '[[1,3,2],[2,2,2],[1.5,3,1.5]]'
# res = [0.468, 0.169, 0.363]
# r = task(str1)
# print(r)
# print(r == res)
