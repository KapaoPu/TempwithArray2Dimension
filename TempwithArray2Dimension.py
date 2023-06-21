import numpy as np
a = np.array([])
for i in range(7):
    b = int(input("ใส่ค่าอุณหภูมิสูงสุด : "))
    a =(np.append(a,b))
    c = int(input("ใส่ค่าอุณภูมิต่ำสุด : "))
    a =(np.append(a,c))
a = np.array(a,dtype="int32")
a = a.reshape(-1,2)
# num = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# num = num.reshape(-1,2)
# print(num)
# row = 0 - 16
# column = 0 , 1
for l in range(1,8):
    match l:
        case 1:
            print("วันจันทร์อุณภูมิสูงสุด : ",a[0][0])
            print("วันจันทร์อุณภูมิสูงสุด : ",a[0][1])
        case 2:
            print("วันอังคารอุณภูมิสูงสุด : ",a[1][0])
            print("วันอังคารอุณภูมิต่ำสุด : ",a[1][1])
        case 3:
            print("วันพุทธอุณภูมิสูงสุด : ",a[2][0])
            print("วันพุทธอุณภูมิต่ำสุด : ",a[2][1])
        case 4:
            print("วันพฤหัสบดีอุณภูมิสูงสุด : ",a[3][0])
            print("วันพฤหัสบดีอุณภูมิต่ำสุด : ",a[3][1])
        case 5:
            print("วันศุกร์อุณภูมิสูงสุด : ",a[4][0])
            print("วันศุกร์อุณภูมิต่ำสุด : ",a[4][1])
        case 6:
            print("วันเสาร์อุณภูมิสูงสุด : ",a[5][0])
            print("วันเสาร์อุณภูมิต่ำสุด : ",a[5][1])
        case 7:
            print("วันอาทิตย์อุณภูมิสูงสุด : ",a[6][0])
            print("วันอาทิตย์อุณภูมิต่ำสุด : ",a[6][1])
print("อุณหภูมิสูงสุดของอาทิตย์ : ",a.max())
print("อุณหภูมิต่ำสุดของอาทิตย์ : ",a.min())
mean = np.mean(a,axis=0)
meanhightemp = mean[0]
print("ค่าเฉลี่ยอุณหภูมิสูงสุด : ",meanhightemp)
meanlowtemp = mean[1]
print("ค่าเฉลี่ยอุณหภูมิต้ำสุด : ",meanlowtemp)