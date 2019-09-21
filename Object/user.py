import os

class User():
    loginID = None
    password = None
    def __init__(self, loginID, password):
        self.loginID = loginID
        self.password = password
  


def tao_fileuser(loginID=None, data=None):
    filename = loginID + '.csv'
    with open('../Data/user/'+filename, 'w') as f:
        f.write(data)

def laythongtin_user(loginID=None):
    data = {}
    filename = loginID + '.csv'
    with open('../Data/user/'+filename, 'r') as f:
        line = f.readline()
        str_to_read = line.split('#')
        data["loginID"] = str_to_read[0]
        data["password"] = str_to_read[1]
    return data



def tao_user():
        thongtin_user = {}
        create_successful = False
        while not create_successful:
            loginID = input("Moi nhap loginID: ")
            checkID = tim_user(loginID)
            if checkID == 1:
                print('Da co loginID nay!!')
                ask = input('Ban co muon nhap lai khong?')
                if ask == 'y':
                    create_successful = False
                    continue
            password = input("Moi nhap mat khau: ")
            confirm_password = input("Moi nhap lai de xac nhan mat khau: ")
            if password == confirm_password:
                thongtin_user["loginID"] = loginID
                thongtin_user["password"] = password
                str_to_save = thongtin_user["loginID"] + '#' + thongtin_user['password']
                tao_fileuser(thongtin_user["loginID"], str_to_save)
                print('Tao thanh cong 1 user')
                create_successful = True


def sua_user():
    found = False
    while not found:
        loginID_muonsua = input('Nhap loginID muon sua: ')
        checkID = tim_user(loginID_muonsua)
        if checkID is None:
            print('User khong ton tai.')
            ask = input('Ban co muon nhap lai khong?')
            if ask == 'y':
                found = False
                continue
        else:
            found = True
    filename = loginID_muonsua + '.csv'
    old_data = {}
    new_password = None
    for file in os.listdir('../Data/user'):
        if filename == file:
            old_data = laythongtin_user(loginID_muonsua)
            confirm = False
            while not confirm:
                old_password = input('Moi nhap mat khau truoc do: ')
                if old_password == old_data["password"]:
                    create_success = False
                    while not create_success:
                        password = input('Moi nhap mat khau moi: ')
                        confirm_password = input('Moi nhap lai de xac nhan mat khau: ')
                        if password == confirm_password:
                            new_password = confirm_password
                            str_to_save = old_data["loginID"] + '#' + new_password
                            with open('../Data/user/'+filename, 'w') as f:
                                f.write(str_to_save)
                            print('Da sua thanh cong user ', old_data["loginID"])
                            create_success = True 
                              
                        else: 
                            print('Nhap lai mat khau khong dung. Moi nhap lai!!!')
                            create_success = False
                    confirm = True
                else: 
                    confirm = False

def tim_user(loginID=None):
    filename = loginID + '.csv'
    for file in os.listdir('../Data/user/'):
        if filename == file:
            return 1

def xoa_user(loginID = None):
    delete_Successful = False
    while not delete_Successful:
        loginID_muonxoa = input('Moi nhap login ID muon xoa: ')
        checkID = tim_user(loginID_muonxoa)
        if checkID != 1:
            print('User khong ton tai.')
            ask = input('Ban co muon nhap lai khong?')
            if ask == 'y':
                delete_Successful = False
        else:
            correct = False
            user_info = laythongtin_user(loginID_muonxoa)
            while not correct:
                old_password = input('Moi nhap mat khau ban dau: ')
                if old_password == user_info["password"]:
                    fileDelete = loginID_muonxoa + '.csv'
                    # Phan nay chua chay duoc do khong tim duoc file
                    if os.path.exists('../Data/user/'+fileDelete):
                        os.remove(fileDelete)
                        
                else:
                    print('Nhap mat khau khong dung. Moi nhap lai')
                    correct = False

        

def login():
    success = False
    while not success:
        loginID = input('Moi nhap loginID: ')
        password = input('Moi nhap mat khau: ')
        #Nho Hai giai thich logic phan tim_user()
        kiemtra = tim_user(loginID)
        if kiemtra == 1: 
            user_info = laythongtin_user(loginID)
            confirm_password = user_info["password"]
            if password == confirm_password:
                success = True
        else:
            print('Tai khoan khong ton tai. Moi nhap lai!!!')
            success = False
       
    return success

def logout():
    pass
        

    




                    








        




