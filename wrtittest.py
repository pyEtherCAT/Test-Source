from pyEtherCAT import MasterEtherCAT #ライブラリの読出し
nic = "eth0" # ネットワークカードのアドレスを記載
cat = MasterEtherCAT.MasterEtherCAT(nic)  

ADP = 0x0000 #1台目
ADDR = 0x0138 #コアレジスタのアドレス
data = [0]*1
data[0] = 0x10 | 0x0D
cat.APWR(IDX=0x00, ADP=ADP, ADO=ADDR, DATA=data) #データ書き込み
(DATA, WKC) = cat.socket_read() #結果を読出し
print("[0x{:04X}]= 0x{:02x}".format(ADDR, DATA[0]))
#読み出したデータを表示する
