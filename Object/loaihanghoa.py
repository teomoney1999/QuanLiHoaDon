import os



def laythongtin_loaihanghoa(id):
    with open('../Data/loaihanghoa/'+id+'.csv', 'r') as f:
        line = f.readline()
        str_to_reads = line.split("#")
        if len(str_to_reads) > 1:
            loaihanghoa = {}
            loaihanghoa["idloaihang"] = str_to_reads[0]
            loaihanghoa["ten"] = str_to_reads[1]
        return loaihanghoa
        
  

def tim_loaihanghoa(id=None):
    filename = id + ".csv"
    for file in os.listdir('../Data/loaihanghoa/'):
        if file == filename:
            return 1

    
            

def tao_loaihanghoa():
    data = {}
    create_successful = False
    while not create_successful:
        id = input("xin moi nhap id loai hang hoa:")
        tim_id_daco = tim_loaihanghoa(id)
        if tim_id_daco != 1:
            data["idloaihang"] = id
            data["ten"] = input("xin moi nhap ten loai hang hoa:")
            create_successful = True
        else: 
            print('Loai hang hoa da ton tai.')
            ask = input('Ban co muon nhap lai khong?')
            if ask == 'y':
                create_successful = False
                continue
            else: 
                break
        str_to_save = data["idloaihang"] + "#" + data["ten"]
        filename = id + '.csv'
        with open('../Data/loaihanghoa/'+filename, 'w') as f:
            f.write(str_to_save)
        print('Da tao thanh cong 1 loai hang hoa')


def xem_loaihanghoa():
    thongtinloaihanghoa = {}
    found = False
    while not found:
        id = input('Nhap ID loai hang hoa muon xem: ')
        id_daco = tim_loaihanghoa(id)
        if id_daco is None:
            print('Khong co ID loai hang hoa nay. Moi nhap lai!!!')
            ask = input('Ban co muon nhap lai khong?')
            if ask == 'y':
                found = False
                continue
            else: 
                break
        else:
            thongtinloaihanghoa = laythongtin_loaihanghoa(id)
            print(thongtinloaihanghoa)
            found = True



