import os
import loaihanghoa



def laythongtin_hanghoa(id = None):
    hanghoa = {}
    with open('../Data/hanghoa/'+id+'.csv', 'r') as f:
        line = f.readline()
        str_to_reads = line.split("#")
        hanghoa["id"] = str_to_reads[0]
        hanghoa["ten"] = str_to_reads[1]
        hanghoa["giaban"] = str_to_reads[2]
        hanghoa["loaihanghoa_id"] = str_to_reads[3]  
    return hanghoa          

def tim_hanghoa(id = None):
    filename = id + '.csv'
    for file in os.listdir('/Users/teomoney1999/QuanLiHoaDon/Data/hanghoa'):
        if file == filename:
            return 1




def tao_hanghoa(id = None):
    data = {}
    create_successful = False
    while not create_successful:
        if id is None: 
            id = input("xin moi nhap id hang hoa:")
            tim_id_daco = tim_hanghoa(id)
            if tim_id_daco == 1:
                print('Hang hoa da ton tai.')
                ask = input('Ban co muon nhap lai khong?')
                if ask == 'y':
                    create_successful = False
                    continue
                else: 
                    break
            data["id"] = id
            data["ten"] = input("xin moi nhap ten hang hoa:")
            data["giaban"] = input("xin moi nhap gia ban:")
            id_loaihanghoa = input("xin moi nhap ma loai hang hoa:")
            if loaihanghoa.tim_loaihanghoa(id_loaihanghoa) is None:
                print('Loai hang hoa khong ton tai!!!')
                hoi = input('Co muon tao moi khong?')
                if hoi is 'y':
                    loaihanghoa.tao_loaihanghoa()
                elif hoi is 'n':
                    return
            data["idloaihanghoa"] = id_loaihanghoa
            str_to_save = data["id"] +'#'+data['ten']+'#'+data['giaban']+'#'+data['idloaihanghoa']
            filename = id + '.csv'
            with open('../Data/hanghoa/'+filename, 'w') as f:
                f.write(str_to_save)
            print('Da tao thanh cong hang hoa!!!')
            return data
            
            

def xem_hanghoa():
    thongtinhanghoa = {}
    found = False
    while not found:
        id = input('Nhap ID hang hoa muon xem: ')
        id_daco = tim_hanghoa(id)
        if id_daco is None:
            print('Khong co ID hang hoa nay. Moi nhap lai!!!')
            found = False
        else:
            thongtinhanghoa = laythongtin_hanghoa(id)
            print(thongtinhanghoa)
            found = True

'''
def sua_hanghoa():
    data = {}
    add_successful = False
    while not add_successful:
        thongtinhang = {}
        id = input("xin moi nhap id hang hoa:")
        tim_id_daco = tim_hanghoa(id)
        if tim_id_daco == 1:
            thongtinhang = laythongtin_hanghoa(id)

'''



