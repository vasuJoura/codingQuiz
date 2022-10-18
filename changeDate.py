import datetime

def changedate(d):
    d = str(d)
    lst_d = d.split('/')
    # print(lst_d)
    if len(lst_d[0]) == 1:
        lst_d[0] = f'{0}{lst_d[0]}'
    if len(lst_d[1]) == 1:
        lst_d[1] = f'{0}{lst_d[1]}'
    lst_d[2] = f'{20}{lst_d[2]}'
    d = f'{lst_d[2]}-{lst_d[0]}-{lst_d[1]}'
    d = datetime.datetime.strptime(d, '%Y-%m-%d')
    # print(d)
    return d