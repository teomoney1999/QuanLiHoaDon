import hanghoa
import os
import json
import hoadon

'''
- Dung file json
- Thong tin hang trong kho gom: 
    + Tong so hang nhap
    + Ton kho
    + So luong ban

'''

def tao_phieunhapkho(idHang = None, data = None):
    filename = idHang + '.json'
    with open('..Data/kho/'+filename, 'w') as f:
        json.dump(data, f)
    print('Da tao thanh cong phieu nhap kho')

def capnhat_filenhapkho(idHang = None, data=None):
    filename = idHang + '.json'
    with open('..Data/kho/'+filename, 'w') as f:
        json.dump(data, f)
    print('Cap nhat thanh cong hang hoa')

def tao_hanghoa_trongkho(idHang = None, soluongnhap = None):
    thongtinhang = {}
    idHang = str(idHang)
 
    thongtinhang["idHang"] = {}
    data = hanghoa.tao_hanghoa(idHang)
    thongtinhang[data["idHang"]]["idloaihanghoa"] = data["idloaihanghoa"]
    thongtinhang[data["idhang"]]["tonkho"] = thongtinhang[data["idHang"]]["tongsoluong"]
    thongtinhang[data["idhang"]]["soluongban"] = 0
    tao_phieunhapkho(idHang, thongtinhang)

def capnhat_thongtin_trongkho(idHang = None, soluongnhap=None, soluongban = None):
    update_file_name = idHang + '.json'
    hanghoaban = {}
    with open ('../Data/kho/'+ update_file_name, 'r') as f:
        hanghoaban = json.load(f)
        for data in hanghoaban["id"]:
            hanghoaban[data["idHang"]] = idHang
            if soluongnhap is not None: 
                hanghoaban[data["tongsoluong"]] = hanghoaban[data["tongsoluong"]] + soluongnhap
                hanghoaban[data["tonkho"]] = hanghoaban[data["tonkho"]]
                tao_phieunhapkho(idHang, hanghoaban)
            if soluongban is not None: 
                hanghoaban[data["tongsoluong"]] = hanghoaban[data["tongsoluong"]]
                hanghoaban[data["tonkho"]] = hanghoaban[data["tonkho"]] - soluongban
                capnhat_filenhapkho(idHang, hanghoaban)
    print('Nhap thanh cong hang hoa vao kho!!!')

def nhapkho(idHang = None):
    if idHang == None:
        idHang = input('Moi nhap ID hang hoa muon nhap: ')
        soluongnhap = input('Moi nhap so luong nhap: ')
        soluongnhap = int(soluongnhap)
        accept = False
        while not accept:
            if soluongnhap < 0:
                print('So luong nhap khong hop le. Moi nhap lai!!!')
                accept = False
            accept = True
        check = hanghoa.tim_hanghoa(idHang)
        if check == 1:
            capnhat_thongtin_trongkho(idHang)
        else :
            update_successful = False
            while not update_successful:
                ask = ('ID nay khong co trong kho. Ban co muon tao moi khong?')
                if ask == 'y':
                    tao_hanghoa_trongkho(idHang, soluongnhap)
                    update_successful = True
                else:
                    update_successful = True
nhapkho()

def laythongtin_hanghoa_tukho(idHang = None):
    thongtinhanghoa = {}
    idHang = str(idHang)
    filename = idHang + '.json'
    with open('../Data/kho/'+filename, "r") as f:
        thongtinhang = json.load(f)
        for data in thongtinhang:
            thongtinhanghoa["id"] = data
            print(data)

#laythongtin_hanghoa_tukho('DU01')
            
def tongsohang_trongkho():
    soluonghang = 0
    thongtin = {}
    for file in os.listdir('../Data/kho/'):
        pass
        
        
                

                
'''
def laythongtin_hanghoa_tukho(id = None):
    hanghoa = {}
    with open('../Data/hanghoa/'+id+'.csv', 'r') as f:
        line = f.readline()
        str_to_reads = line.split("#")
        hanghoa["id"] = str_to_reads[0]
        hanghoa["ten"] = str_to_reads[1]
        hanghoa["tonkho"] = str_to_reads[2]

        hanghoa["loaihanghoa_id"] = str_to_reads[3]  
    return hanghoa          

def tinh_tonghang_trongkho():
    tongsohang = 0
    for file in os.listdir('../Data/kho'):
        data = {}
        idHangHoa = file[0:len(file)-4]
        data = laythongtin_hanghoa_tukho(idHangHoa)
        tongsohang = tongsohang + data["tonkho"]
    return tongsohang

def tonkho():

def tao_filenhapkho(id = None, data=None):
    filename = id + '.csv'
    with open('../Data/kho/'+filename, 'w') as f:
        f.write(data)
    return 1

def luu_thongtin(id = None, data = None):
    data_to_save = data["id"] + '#' + data['ten'] + '#' + data['tonkho'] + '#' + data["loaihanghoa_id"]
    filename = id + '.csv'
    with open('../Data/kho/'+filename, 'w') as f:
        f.write(data_to_save)
    print('Da nhap thanh cong hang hoa')

def bosung_thongtin(idHang = None, soluongnhap = None):
    thongtinhang = {}
    thongtinhang = laythongtin_hanghoa_tukho(idHang)
    thongtinhang["tonkho"] = thongtinhang["tonkho"] + soluongnhap
    luu_thongtin(idHang, thongtinhang)
    
def them_hanghoa_vaokho(idHang=None, soluongthem = None):
    thongtinhang = {}
    hanghoa.tao_hanghoa(idHang)
    thongtinhang = hanghoa.laythongtin_hanghoa(idHang)
    del thongtinhang['gia']
    thongtinhang["tonkho"] = soluongthem
    luu_thongtin(idHang, thongtinhang)


def nhapkho():
    add_Successful = False
    while not add_Successful:
        idHang = input('Moi nhap ID hang hoa muon nhap kho: ')
        check = hanghoa.tim_hanghoa(idHang)
        if check == 1:
            soluongnhap = input('Moi ban nhap so luong nhap: ')
            bosung_thongtin(idHang, soluongnhap)
            add_Successful = True
        else: 
            print('Hang hoa nay chua co trong kho.')
            ask = input('Ban co muon them hang hoa nay vao kho khong ?')
            if ask == 'y':
                accept = False
                while not accept: 
                    hanghoa.tao_hanghoa(idHang)
                    soluongthem = input('Moi nhap so luong nhap: ')
                    soluongthem = int(soluongthem)
                    if soluongthem < 0:
                        print('So luong nhap khong duoc nho hon 0.Moi nhap lai!!')
                        accept = False
                    else: 
                        accept = True
                them_hanghoa_vaokho(idHang, soluongthem)



"""
Thong tin khach hang: Ten # So tien da mua do

Kho:
    -   Tao ra mot ban sao cua luong hang trong kho de tac dong len
    -   Tao them thuoc tinh cho hang hoa trong kho ["tongso"]
    -  
"""


'''