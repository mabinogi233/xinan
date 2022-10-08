from PIL import Image
import numpy as np

def read_png(path):
    pic = Image.open(path)
    out_m = pic.convert("RGBA")
    m = np.array(out_m)
    return m

def write_png(path,rgba_bits,w,h):
    pic = Image.new("RGBA", (w, h))
    for i in range(h):
        for j in range(w):
            pic.putpixel((j,i), (int(rgba_bits[i][j][0]), int(rgba_bits[i][j][1]), int(rgba_bits[i][j][2]),int(rgba_bits[i][j][3])))
    pic.save(path)

def LSB(rgba_bits,w,h,str_bits):
    peek = 0
    #m为哪个通道（RGBA）
    for m in range(3):
        for i in range(h):
            for j in range(w):
                #判断最后一位是0还是1
                if(rgba_bits[i][j][m] &1 == 1):
                    #是1则变成0
                    rgba_bits[i][j][m]-=1
                #写入第peek位的二进制信息
                rgba_bits[i][j][m] += int(str_bits[peek])
                peek+=1
                if(peek==len(str_bits)):
                    #返回写入后图片，写入数据量，操作成功
                    return rgba_bits,peek,True
    # 返回写入后图片，写入数据量，操作失败
    return rgba_bits,len(str_bits),False

def reLSB(rgba_bits,w,h,peek_n):
    peek = 0
    str_bits = ""
    #m为哪个通道（RGBA）
    for m in range(3):
        for i in range(h):
            for j in range(w):
                #获取最后一位
                str_bits += str(rgba_bits[i][j][m] & 1)
                peek+=1
                if(peek==peek_n):
                    #返回字符串，操作成功
                    return str_bits,True
    # 返回字符串操作失败
    return str_bits,False

#每个字符使用8位二进制表示
def string2ascii(_str):
    ascii_str=""
    for charx in _str:
        ascii_char = int(ord(charx))
        #转二进制
        b_ascii_char = bin(int(str(ascii_char),10)).replace("0b","")
        for i in range(8 - len(b_ascii_char)):
            ascii_str+="0"
        ascii_str+=b_ascii_char
    return ascii_str

#每个字符使用8位二进制表示
def ascii2str(_ascii):
    _str=""
    _char = ""
    for charx in _ascii:
        _char += charx
        if(len(_char)==8):
            _str += chr(int(_char,2))
            _char = ""
    return _str

if __name__ == "__main__":
    #图片
    pic = read_png(r"E:\文件\信息安全\test.png")
    #待加密到图片的字符串
    _str = "CQUWATERMASKEXP"
    #字符串转ascii码串
    ascii_str = string2ascii(_str)
    #加密
    lsb_pic,key,op = LSB(pic,pic.shape[1],pic.shape[0],ascii_str)
    write_png(r"E:\文件\信息安全\加密后.png",lsb_pic,lsb_pic.shape[1],lsb_pic.shape[0])
    if(op):
        print("加密成功")
        print("加密的信息量为：",key)
    else:
        print("加密失败，待加密字符过多")
    #解密
    ascii_str_de,op = reLSB(lsb_pic,lsb_pic.shape[1],lsb_pic.shape[0],key)
    _str_de = ascii2str(ascii_str_de)
    if (op and ascii_str==ascii_str_de):
        print("解密成功")
        print("加密前：",ascii_str)
        print("加密前：", _str)
        print("解密后：",ascii_str_de)
        print("加密前：", _str_de)
    else:
        print("解密失败")