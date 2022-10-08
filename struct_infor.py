import re

#提取形如（xxxx年xx月xx日的日期格式，x可为0）
def find_data(str):
    regex = "[0-9]{1,4}年[0-9]{1,2}月[0-9]{1,2}日"
    return re.findall(regex,str)

#提取18位身份证号
def find_idcardnumber(str):
    regex = "[0-9]{17}[0-9Xx]"
    return re.findall(regex,str)

#人民币金额提取
def find_money(str):
    regex = "￥([0-9]+.?[0-9]+)"
    return re.findall(regex,str)

if __name__ == '__main__':
    print(find_data("新华社北京2021年11月10日电中共中央将于2021年11月12日上午10时举行新闻发布会，介绍党的十九届六中全会精神。"))
    print(find_idcardnumber("身份证号码形如：11111111111111111x"))
    print(find_money("待支付的金额为￥8000.02"))







