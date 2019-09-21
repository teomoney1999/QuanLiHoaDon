import user
import hanghoa
import loaihanghoa
import costumer
import hoadon


print('+------------DANG NHAP------------+')
login_success = user.login()

while login_success is True:
    print('+-----------------MENU-----------------+')
    print('| - Chon HH de quan li hang hoa        |')
    print('| - Chon LHH de quan li loai hang hoa  |')
    print('| - Chon HD de quan li hoa don         |')
    print('| - Chon KH de quan li khach hang      |')
    print('| - Chon KHO de quan li kho            |')
    print('| - Chon KHACH de quan li khach        |')
    print('| - Chon USER de quan li nhan vien     |')
    print('| - Chon OUT de dang xuat              |')
    print('| - Chon T de thoat khoi chuong trinh  |')
    print('+--------------------------------------+')

    userChoice = input('Moi chon chuc nang: ')
    if userChoice == 't':
        print('Hen gap lai!!!')

        break
    if userChoice == 'hh':
        outOfFunction = False
        while not outOfFunction:
            print('+-----------------MENU-----------------+')
            print('| - Chon C de tao hang hoa moi         |')
            print('| - Chon XTT de xem thong tin hang hoa |')
            print('| - Chon S de sua thong tin hang hoa   |')
            print('| - Chon X de xoa thong tin hang hoa   |')
            print('| - Chon O de ra MENU chinh            |')
            print('+--------------------------------------+')
            userChoice = input('Moi chon chuc nang: ')
            if userChoice == 'c':
                hanghoa.tao_hanghoa()
            elif userChoice == 'xtt':
                hanghoa.xem_hanghoa()
            elif userChoice == 's':
                pass

            elif userChoice == 'x':
                pass
            elif userChoice == 'o':
                outOfFunction = True
        
    if userChoice == 'lhh':
        outOfFunction = False
        while not outOfFunction:
            print('+----------------------MENU----------------------+')
            print('| - Chon C de tao loai hang hoa moi              |')
            print('| - Chon XTT de xem thong tin loai hang hoa      |')
            print('| - Chon S de sua thong tin loai hang hoa        |')
            print('| - Chon X de xoa thong tin loai hang hoa        |')
            print('| - Chon O de ra MENU chinh                      |')
            print('+------------------------------------------------+')

            userChoice = input("Moi chon chuc nang: ")
            if userChoice == 'c':
                loaihanghoa.tao_loaihanghoa()
            elif userChoice == 'xtt':
                loaihanghoa.xem_loaihanghoa()
            elif userChoice == 's':
                pass
            elif userChoice == 'x':
                pass
            elif userChoice == 'o':
                outOfFunction = True
    if userChoice == 'hd':
        outOfFunction = False
        while not outOfFunction:
            print('+----------------------MENU----------------------+')
            print('| - Chon C de tao loai hoa don moi               |')
            print('| - Chon XTT de xem thong tin hoa don            |')
            print('| - Chon O de ra MENU chinh                      |')
            print('+------------------------------------------------+')

            userChoice = input('Moi chon chuc nang: ')
            if userChoice == 'c':
                hoadon.tao_hoadon()
            elif userChoice == 'xtt':
                hoadon.xem_hoadon()
            elif userChoice == 'o':
                outOfFunction = True
    

    if userChoice == 'user':
        outOfFunction = False
        while not outOfFunction:
            print('+----------------------MENU----------------------+')
            print('| - Chon C de tao USER moi                       |')
            print('| - Chon S de sua thong tin USER                 |')
            print('| - Chon X de xoa thong tin USER                 |')
            print('| - Chon O de ra MENU chinh                      |')
            print('+------------------------------------------------+')

            userChoice = input("Moi chon chuc nang: ")
            if userChoice == 'c':
                user.tao_user()
            elif userChoice == 's':
                user.sua_user()
            elif userChoice == 'x':
                user.xoa_user()
            else: 
                outOfFunction = True
    
    


            
