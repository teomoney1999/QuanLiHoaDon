import os
import json
import hanghoa
import costumer

danhsachhoadon = []

hanghoaban = {}

def tao_sohoadon():
    files = os.listdir("../Data/HoaDon/")
    file = files[-1]
    file = file[0:len(file)-5]
    sohoadon = int(file) + 1
    return sohoadon
       

def tim_hoadon(id=None):
    filename = id + '.json'
    for file in os.listdir('../Data/HoaDon/'):
        if file == filename:
            return 1
    

def tao_filehoadon(sohoadon=None ,data=None):
    filename = sohoadon + '.json'
    with open('../Data/HoaDon/'+filename, 'w') as f:
        json.dump(data, f)
    print('Da tao thanh cong file hoa don')
            




def tao_hoadon():
    hoadon={}
    sohoadon = tao_sohoadon()
    sohoadon = str(sohoadon)
    hoadon["sohoadon"] = str(sohoadon)
    hoadon["ngayhoadon"]= input("nhap ngay hoa don :")
    hoadon["nguoimua"]= input("nhap nguoi mua hang :")
    hoadon["tongtientruocthue"] = 0
    hoadon["thue"] = 0.1
    hoadon["tongtien"] = 0
    hoadon["danhsachhanghoa"] = []
    hanghoaban = {}

    nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")

    while nhaphanghoa.upper() == 'Y':
        thongtinhanghoa = {}
        #thongtinhanghoa["stt"] = thongtinhanghoa["stt"] + 1
        thongtinhanghoa["id"] = 0
        id_hanghoa = input("nhap id hang hoa: ")
        test_id_hanghoa = hanghoa.tim_hanghoa(id_hanghoa)
        if test_id_hanghoa == 1:
            thongtinhanghoa["id"] = id_hanghoa
        #lay thong tin gia cua san pham tu class hanghoa
        thongtin_hanghoa = hanghoa.laythongtin_hanghoa(id_hanghoa)
        soluong = input("nhap so luong: ")
        thongtinhanghoa["soluong"] = int(soluong)
        thongtinhanghoa["dongia"] = int(thongtin_hanghoa["giaban"])
        thongtinhanghoa["thanhtien"] = thongtinhanghoa["soluong"] * thongtinhanghoa["dongia"]
        
        if thongtinhanghoa["id"] in hanghoaban:
            hanghoaban[thongtinhanghoa["id"]]["tongso"] = hanghoaban[thongtinhanghoa["id"]]["tongso"] + thongtinhanghoa["soluong"]
            hanghoaban[thongtinhanghoa["id"]]["doanhthu"] = hanghoaban[thongtinhanghoa["id"]]["doanhthu"] + thongtinhanghoa["thanhtien"]
        else:
            hanghoaban[thongtinhanghoa["id"]] = {
                "tongso": thongtinhanghoa["soluong"],
                "doanhthu": thongtinhanghoa["thanhtien"]
            }
        tao_filehanghoaban(thongtinhanghoa["id"], hanghoaban)                                                                      
        hoadon["danhsachhanghoa"].append(thongtinhanghoa)

        hoadon["tongtientruocthue"] = hoadon["tongtientruocthue"] + thongtinhanghoa["thanhtien"]

        nhaphanghoa = input("=> Ban co muon nhap hang hoa khong (y/n): ")
        
    hoadon["tongtien"] = hoadon["tongtientruocthue"] + hoadon["tongtientruocthue"]*hoadon["thue"]
    danhsachhoadon.append(hoadon)
    tao_filehoadon(sohoadon, hoadon)
    # def tao_filethongtin bi loi (name is not defined)
    tao_filethongtinmua(sohoadon, hanghoaban)
    



    
def laythongtin_hoadon(sohoadon = None):
    thongtinhoadon = {}
    filename = sohoadon + '.json'
    with open('../Data/HoaDon/'+filename, 'r') as f:
        data = json.load(f)
        thongtinhoadon["sohoadon"] = data["sohoadon"]
        thongtinhoadon["ngayhoadon"] = data["ngayhoadon"]
        thongtinhoadon["nguoimua"] = data["nguoimua"]
        thongtinhoadon["danhsachmua"] = []
        for hanghoa in data["danhsachhanghoa"]:
            danhsachmua = {}
            danhsachmua["stt"] = hanghoa["stt"]
            danhsachmua["id"] = hanghoa["id"]
            danhsachmua["soluong"] = hanghoa["soluong"]
            danhsachmua["dongia"] = hanghoa['dongia']
            danhsachmua["thanhtien"] = hanghoa["thanhtien"]
        thongtinhoadon["danhsachmua"].append(danhsachmua)
        thongtinhoadon["thue"] = data["thue"]
        thongtinhoadon["tongtien"] = data["tongtien"]
        return thongtinhoadon

def tao_filethongtinmua(sohoadon=None, tenkhach=None, data=None):
    thongtinhoadon = {}
    filename = tenkhach + ".csv"
    thongtinhoadon = laythongtin_hoadon(sohoadon)
    for file in os.listdir("../Data/khachhang"):
        if filename == file:
            costumer.bosung_khach(tenkhach, thongtinhoadon["tongtien"])
            print("Them thong tin khach thanh cong!!!")
        else:
            costumer.tao_thongtinkhachmoi(tenkhach, thongtinhoadon["tongtien"])
            print("Tao thong tin khach hang moi thanh cong!!!")

def tao_filehanghoaban(idHang=None, data=None):
    filename = idHang + '.json'
    with open('..Data/hoadon/hanghoaban'+filename, 'w') as f:
        json.dump(data, f)

def xem_hoadon():
            sohoadon_canxem = input("nhap so hoa don can xem:")
            sohoadon_daco = tim_hoadon(sohoadon_canxem)
            if sohoadon_daco is None:
                print('So hoa don khong ton tai!!!')
            else:
                hoadon = laythongtin_hoadon(sohoadon_canxem)
                #Hoa don se in o day
                print("                          HOA DON MUA HANG                                   ")
                print("so hoa don:",hoadon["sohoadon"])
                print("ngay xuat:",hoadon["ngayhoadon"])
                print("ten khach hang:",hoadon["nguoimua"])
                print("_____________________________thong tin hoa don_______________________________")
                print("+----------+------------------+----------+---------------+------------------+")
                print("|   STT    |     hang hoa     | so luong |    don gia    |    thanh tien    |")
                print("+----------+------------------+----------+---------------+------------------+")



                print("In dong hang hoa o day")
                #print("| "+stt_x+"  | " +tenhanghoa+ " | "+soluong_x+" | "+dongia_x+" | "+thanhtien_x+" |")
                print("+----------+------------------+----------+---------------+------------------+")
             #end of Hoa don se






