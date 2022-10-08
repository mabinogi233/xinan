import random
import time
import sys
sys.setrecursionlimit(100000)

# Miller-Rabin算法判断素数，保证仅有不大于1/(2^15)的概率判断错误

def is_prime(num):
    # 循环次数m
    m = 15
    flag = 0
    for i in range(0, m):
        # a是2-P-1的随机数
        a = random.randint(2, num - 1)
        # 求幂取余
        tem2 = exp_multi(a, num - 1, num)
        if tem2 != 1:
            flag = 1
            break
    if flag == 0:
        return True
    elif flag == 1:
        return False
    else:
        return False


#随机生成一个素数，默认为1024bit
def random_prime(a=2**1023,b=2**(1024)-1):
    num = random.randint(a,b)
    while(not is_prime(num)):
        num += 1
    return num

#辗转相除法求最大公因数
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


#模逆元，即a*b mod m = 1，已知a，m求b
def _rmod(a, m):
    if m == 0:
        return 1, 0, a
    else:
        b, y, q = _rmod(m, a % m)
        b, y = y, (b - (a // m) * y)
        return b, y, q

def rmod(a,m):
    b, y, q = _rmod(a,m)
    if q != 1:
        return None
    else:
        return (b + m)%m

#密钥生成
def create_k():
    #随机生成p和q
    p = random_prime()
    print("p:",p)
    q = random_prime()
    print("q:", q)
    n = p*q
    phi_n = (p-1)*(q-1)
    if(phi_n>=2**(1024)-1):
        e = random_prime(a=2)
    else:
        e = random_prime(a=2,b=2**(1024)-1)
    print("e:",e)
    d = rmod(e,phi_n)
    #公钥，私钥
    return e,n,d,n

#计算大数 x^r mod n
#1. a=x; b=r; c=1;
#2. 若b=0,则输出结果c,结束
#3. 若b为奇数，跳转至5
#4. b<- b/2; a<-（a*a mod n）;跳转至3
#5. b<- b-1; c<-（c*a mod n）;跳转至2
def exp_multi(x,r,n):
    a = x
    b = r
    c = 1
    while(True):
        #若b=0,则输出结果c,结束
        if(b == 0):
            return c
        if(b%2 == 0):
            #b<- b/2; a<-（a*a mod n）转判断奇偶数
            b = b // 2
            a = (a * a) % n
        else:
            #b= b-1; c=（c*a mod n）下一次循环
            b = b - 1
            c = (c * a) % n


#加密
def deciphering(m,e,n):
    return exp_multi(m,e,n)

#解密
def encryption(c,d,n):
    return exp_multi(c,d,n)

#每个字符使用三位数字（ascii）表示
def string2ascii(_str):
    ascii_str=""
    for charx in _str:
        ascii_char = int(ord(charx))
        if(ascii_char<100):
            ascii_str += "0"
            ascii_str += str(ascii_char)
        else:
            ascii_str += str(ascii_char)
    return int(ascii_str)

if __name__ == '__main__':
    start = time.process_time()
    #文本字符串
    msg = "CQUINFORMATIONSECURITYEXP1"
    #明文ascii码串
    m = string2ascii(msg)
    print(m)
    #e，n为公钥，d，n为私钥
    e,n,d,_ = create_k()
    #加密，c为密文
    c = deciphering(m,e,n)
    print(c)
    #解密，_m为解密后的ascii码串
    _m = encryption(c,d,n)
    print(_m)
    end = time.process_time()
    #加密前与解密后对比，相同则成功
    if (m == _m):
        print("sucess")
        print("算法运行时间：",(end-start),"s")
    else:
        print("fail")










