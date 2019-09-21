def confirm():
    confirm = False
   


def enterAgain(do_again = False):
    do_again = False

    while not do_again:
        ask = input('Ban co muon nhap lai khong?')
        if ask == 'y':
            do_again = True
        else:
            do_again = False
