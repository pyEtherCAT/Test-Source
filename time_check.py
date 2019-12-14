from pyEtherCAT import MasterEtherCAT #ライブラリの読出し
import time #実行時間計測用のtimeライブラリ
nic = "eth0" # ネットワークカードのアドレスを記載
cat = MasterEtherCAT.MasterEtherCAT(nic)  

ADP = 0x0000 #1台目
ADDR = 0x0138 #コアレジスタのアドレス
data = [0]*1

## 1回目の計測
data[0] = 0x10 | 0x00
start = time.time()     #実行時間のスタート計算
cat.APWR(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=data) #データ書き込み
(DATA, WKC) = cat.socket_read() #結果を読出し
#print("[0x{:04X}]= 0x{:02x}".format(ADDR, DATA[0])) #読み出したデータを表示する
print ("time:{0}".format(time.time() - start) + "[sec]")     #実行時間のエンド計算と表示まで

## 2回目の計測
data[0] = 0x10 | 0x0D
start = time.time()     #実行時間のスタート計算
cat.APWR(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=data) #データ書き込み
(DATA, WKC) = cat.socket_read() #結果を読出し
#print("[0x{:04X}]= 0x{:02x}".format(ADDR, DATA[0])) #読み出したデータを表示する
print ("time:{0}".format(time.time() - start) + "[sec]")     #実行時間のエンド計算と表示まで

## 3回目の計測
data[0] = 0x10 | 0x00
start = time.time()     #実行時間のスタート計算
cat.APWR(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=data) #データ書き込み
(DATA, WKC) = cat.socket_read() #結果を読出し
#print("[0x{:04X}]= 0x{:02x}".format(ADDR, DATA[0])) #読み出したデータを表示する
print ("time:{0}".format(time.time() - start) + "[sec]")     #実行時間のエンド計算と表示まで
