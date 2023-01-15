import numpy as np
import math
import glob
import xlwt
import itertools

# ユークリッド距離計算
def Euclid(a, b, N):
    euc = []
    for w in range(N - 1):
         P = math.sqrt((a[w] - b[w]) ** 2 + \
                  (a[w-1] - b[w-1]) ** 2)
         euc.append(P)
    E = np.mean(euc)
    return E

# コサイン類似度計算
def Cos(x, y, N):
    sim = []
    for n in range(N - 1):
        a1 = x[n]*y[n]+x[n-1]*y[n-1]
        a2 = math.sqrt(x[n]**2 + x[n-1]**2)
        a3 = math.sqrt(y[n]**2 + y[n-1]**2)
        a = a2*a3
        s = a1/a
        sim.append(s)
    S = np.mean(sim)
    return S

if __name__ == '__main__':
    list = glob.glob("./csv/*.csv")
    book = xlwt.Workbook()
    list_num = len(list)
    newSheet_1 = book.add_sheet("Euclid")
    newSheet_2 = book.add_sheet("Cosine")
    eucsim_list = []
    cossim_list = []

    for pre in range(list_num):
        name = list[pre].replace(".csv", "").replace("./csv", "")[1:]
        newSheet_1.write(0, pre + 1, name)
        newSheet_1.write(pre + 1, 0, name)
        newSheet_2.write(0, pre + 1, name)
        newSheet_2.write(pre + 1, 0, name)

    for i2 in itertools.product(list, repeat=2):
        fname1 = i2[0]
        data1 = np.loadtxt(fname1, delimiter=',', dtype='float')
        fname2 = i2[1]
        data2 = np.loadtxt(fname2, delimiter=',', dtype='float')

        eucsim = Euclid(data1, data2, 127)
        cossim = Cos(data1, data2, 127)

        print(str(i2[0].replace(".csv", "").replace("./csv", "")[1:]))
        print(str(i2[1].replace(".csv", "").replace("./csv", "")[1:]))

        print("Euc: " + str(eucsim))
        print("Cos: " + str(cossim))
        eucsim_list.append(eucsim)
        cossim_list.append(cossim)
        print("\n---------------------------------")

    b = 0
    print(cossim_list[0])
    for x in range(list_num):
        for t in range(list_num):
            newSheet_1.write(x + 1, t + 1, eucsim_list[b])
            newSheet_2.write(x + 1, t + 1, cossim_list[b])
            b += 1

    book.save("similarity.xls")

    print("\n----- Calculation finish -----\n")