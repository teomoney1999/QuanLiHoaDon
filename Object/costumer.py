import os
import hanghoa


"""
lay ten khach hang, so tien mua ho mua tu hoa don
dung file csv
"""

def laythongtin_khachhang_tuhoadon(id=None):
    thongtinkhachhang = {}
    data = {}
    filename = id + '.csv'
    with open('..Data/HoaDon/'+filename,'r') as f:
        data = f.readline()
        str_to_reads = data.split('#')
        if len(str_to_reads) > 1:
            thongtinkhachhang["tenkhach"] = str_to_reads[0]
            thongtinkhachhang["sotienmua"] = str_to_reads[1]
        return thongtinkhachhang
                

def bosung_khach(tenkhach=None, thongtinbosung=None):
    filename = tenkhach + ".csv"
    thongtinsaubosung = {}
    thongtinsaubosung["tenkhach"] = tenkhach
    thongtinsaubosung["sotienmua"] = thongtinsaubosung["sotienmua"] + thongtinbosung 
    str_to_save = thongtinsaubosung["tenkhach"] + '#' + thongtinsaubosung["sotienmua"]
    with open("../Data/khachhang/"+filename, 'a') as f:
        f.write(str_to_save)
    print("Da tao thanh cong file thong tin khach!!!")
    

def tao_thongtinkhachmoi(tenkhach=None, thongtinkhach=None):
    filename = tenkhach + ".json"
    data = {}
    data["tenkhach"] = tenkhach
    data["sotienmua"] = 0
    str_to_save = data["tenkhach"] + '#' + data["sotien"]
    with open("../Data/khachhang/"+filename, 'w') as f:
        f.write(str_to_save)
    print("Da tao thanh cong file thong tin khach!!!")