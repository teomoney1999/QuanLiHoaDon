filename = "IN" + sohoadon +".json"
 with open('../HoaDon/' + filename, 'w') as f:
    json.dump(hoadon, f)
data = open("../HoaDon/id_invoice.txt", "a")
data.write("IN" + sohoadon +"\n")
