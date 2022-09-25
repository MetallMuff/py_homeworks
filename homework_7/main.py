import xlrd

while True:
    def sprav():
        rb = xlrd.open_workbook(r'E:\Учеба Gik\2 блок\Python\homework_7\Список телефонов.xls')
        sheet = rb.sheet_by_index(0)
        vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
        for kabinet, otdel, gorod, phone, doljnost, first_name in vals:
            first_name = first_name.strip()
            if a == first_name[:1] or a == first_name[:2] or a == first_name[:3]:
                kabinet = str(kabinet)
                kabinet = kabinet[:3]
                name = first_name, kabinet, otdel, gorod, int(phone), doljnost
                print('{} : каб. {} : {} : {} : {} : {}'.format(*name))
            elif a != first_name:
                pass


    a = input('Введите фамилию: ')
    a = a.title()

    if a != '':
        sprav()
    elif a == 0:
        sprav()
    else:
        pass
