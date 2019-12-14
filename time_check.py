from pyEtherCAT import MasterEtherCAT #ライブラリの読出し
import time #実行時間計測用のtimeライブラリ
nic = "eth0" # ネットワークカードのアドレスを記載
cat = MasterEtherCAT.MasterEtherCAT(nic)  
print(" ")

## 1回目の計測
endsum =0
tmax = 0
tmin = 1

print("1回目の計測")
time.sleep(2)
for i in range(10):
    ADP = 0x0000 #1台目
    ADDR = 0x0E00 #コアレジスタのアドレス
    start = time.time()     #実行時間のスタート計算
    cat.APRD(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=[0,0,0,0,0,0,0,0]) #DATAは０を８個(64bit分)の枠を指示
    (DATA, WKC) = cat.socket_read() #結果を読出し
    endsum = endsum + (time.time() - start)
    tmax = (time.time() - start) if(tmax < (time.time() - start)) else tmax
    tmin = (time.time() - start) if(tmin > (time.time() - start)) else tmin
end = endsum / i
print ("平均　time:{0}".format( (end)*1000) + "[msec]")     #実行時間のエンド計算と表示まで
print ("最大　time:{0}".format( (tmax)*1000) + "[msec]")     #実行時間のエンド計算と表示まで
print ("最小　time:{0}".format( (tmin)*1000) + "[msec]")     #実行時間のエンド計算と表示まで
print("[0x{:04X}]= 0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x}".format(ADDR, DATA[7],DATA[6],DATA[5],DATA[4],DATA[3],DATA[2],DATA[1],DATA[0]))
exit()
endsum =0
print("2回目の計測")
time.sleep(2)
for i in range(10):
    ADP = 0x0000-1 #1台目
    ADDR = 0x0E00 #コアレジスタのアドレス
    start = time.time()     #実行時間のスタート計算
    cat.APRD(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=[0,0,0,0,0,0,0,0]) #DATAは０を８個(64bit分)の枠を指示
    (DATA, WKC) = cat.socket_read() #結果を読出し
    endsum = endsum + time.time() - start
end = endsum / i
print ("平均　time:{0}".format( (end)*1000) + "[msec]")     #実行時間のエンド計算と表示まで
print("[0x{:04X}]= 0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x}".format(ADDR, DATA[7],DATA[6],DATA[5],DATA[4],DATA[3],DATA[2],DATA[1],DATA[0]))

endsum =0
print("3回目の計測")
time.sleep(2)
for i in range(10):
    ADP = 0x0000-2 #1台目
    ADDR = 0x0E00 #コアレジスタのアドレス
    start = time.time()     #実行時間のスタート計算
    cat.APRD(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=[0,0,0,0,0,0,0,0]) #DATAは０を８個(64bit分)の枠を指示
    (DATA, WKC) = cat.socket_read() #結果を読出し
    endsum = endsum + time.time() - start
end = endsum / i
print ("平均　time:{0}".format( (end)*1000) + "[msec]")     #実行時間のエンド計算と表示まで
print("[0x{:04X}]= 0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x}".format(ADDR, DATA[7],DATA[6],DATA[5],DATA[4],DATA[3],DATA[2],DATA[1],DATA[0]))

endsum =0
print("4回目の計測")
time.sleep(2)
for i in range(10):
    ADP = 0x0000-3 #1台目
    ADDR = 0x0E00 #コアレジスタのアドレス
    start = time.time()     #実行時間のスタート計算
    cat.APRD(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=[0,0,0,0,0,0,0,0]) #DATAは０を８個(64bit分)の枠を指示
    (DATA, WKC) = cat.socket_read() #結果を読出し
    endsum = endsum + time.time() - start
end = endsum / i
print ("平均　time:{0}".format( (end)*1000) + "[msec]")     #実行時間のエンド計算と表示まで
print("[0x{:04X}]= 0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x},0x{:02x}{:02x}".format(ADDR, DATA[7],DATA[6],DATA[5],DATA[4],DATA[3],DATA[2],DATA[1],DATA[0]))
print(" ")
