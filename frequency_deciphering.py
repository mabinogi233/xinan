

#统计字符出现频率
def acc_f(_str):
    dict_f = {}
    n = 0
    for _char in _str:
        if(not _char.isalpha()):
            continue
        n+=1
        if(_char not in dict_f):
            dict_f[_char] = 1
        else:
            dict_f[_char] += 1
    for key in dict_f.keys():
        dict_f[key] = dict_f[key]/n
    l = sorted(dict_f.items(), key=lambda kv: (kv[1], kv[0]))
    l.reverse()
    for i in range(len(l)):
        if (i % 5 == 0):
            print()
        print(l[i], end='')
    return l


#统计二字母对出现频率
def acc_f_2(_str):
    dict_f = {}
    n = 0
    for i in range(len(_str)-1):
        if(_str[i].isalpha() and _str[i+1].isalpha()):
            n += 1
            _char = _str[i]+_str[i+1]
            if (_char not in dict_f):
                dict_f[_char] = 1
            else:
                dict_f[_char] += 1
    for key in dict_f.keys():
        dict_f[key] = dict_f[key]/n
    l = sorted(dict_f.items(), key=lambda kv: (kv[1], kv[0]))
    l.reverse()
    for i in range(len(l)):
        if (i % 5 == 0):
            print()
        print(l[i],end='')
    return l


#统计三字母对出现频率
def acc_f_3(_str):
    dict_f = {}
    n = 0
    for i in range(len(_str)-2):
        if(_str[i].isalpha() and _str[i+1].isalpha() and _str[i+2].isalpha()):
            n += 1
            _char = _str[i]+_str[i+1]+_str[i+2]
            if (_char not in dict_f):
                dict_f[_char] = 1
            else:
                dict_f[_char] += 1
    for key in dict_f.keys():
        dict_f[key] = dict_f[key]/n
    l = sorted(dict_f.items(), key=lambda kv: (kv[1], kv[0]))
    l.reverse()
    for i in range(len(l)):
        if (i % 5 == 0):
            print()
        print(l[i], end='')
    return l

if __name__ == '__main__':
    msg = "UZ QSO VUOHXMOPV GPOZPEVSG ZWSZ OPFPESX UDBMETSX AIZ VUEPHZ HMDZSHZO WSFP APPD TSVP QUZW YMXUZUHSX EPYEPOPDZSZUFPO MB ZWP FUPZ HMDJ UD TMOHMQ"
    l = acc_f(msg)
    l2 = acc_f_2(msg)
    l3 = acc_f_3(msg)



