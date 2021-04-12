
def dot_to_bin(x):
    bins=[]
    s=float(x)
    while s:
        s*=2
        if s>=1:
            ss=1
            s-=1
        else :
            ss=0
        bins.append(ss)
    stra =''
    for aa in range(len(bins)):
        stra += str(bins[aa])
    return  stra
#获得去掉小数点后从第二位到最后一位数字
def get_dot_num(a):
    if '.' in str(a):
        result=str(a).split('.',1)
        re_num = len(result[0])
        num1 = str(result[0])
        num2 = str(result[1])
        if re_num > 1:
            new_num=num1[1:re_num]+num2
        else:
            new_num=num2
        return new_num
    else:
        new_num=a
        return new_num
#获得小数点前数字的位数
def exp_num(a):
    if '.' in str(a):
        result=str(a).split('.',1)
        re_num = len(result[0])
        if re_num > 1:
            exp=re_num-1
        else :
            exp=re_num
        return exp
    else :
        result = str(a)
        re_num=len(result)
        if re_num>1:
            exp=re_num-1
        else :
            exp=0
        return exp

#实数转小数
def num_to_bin(n):
    if '.' in str(n):
        result = str(n).split('.', 1)
        int1=str(result[0])
        int2=bin(int(int1))
        dot='0.'+str(result[1])
        dot1=dot_to_bin(dot)
        final=int2[2:]+'.'+dot1
    else :
        int1=n
        int2=bin(int1)
        final=int2[2:]
    return final
#实数转浮点二进制数
def num_to_float(x):
    mid_num=abs(float(x))
    binary=num_to_bin(mid_num)
    num2=get_dot_num(binary) #小数点后的数
    num1=binary[0] #小数点前的数
    final_num=num2
    last_num = abs(23 - len(num2))
    if last_num > 23:
        final_num = str(final_num)[:23]
    else:
        for i in range(last_num):
            final_num += "0"  # 尾数
    exp=exp_num(num1)
    e=int(exp)+127
    eb=str(bin(e)[2:]) #指数
    if len(eb)<8:
        eb0='0'+eb
    else :
        eb0=eb
    if float(x)>=0:
        first=0
    else :
        first=1
    float_num=str(first)+'_'+eb0+'_'+final_num
    return float_num
#test=num_to_float()

total_num=input('请输入需要转换的数据总数：')
list1=[]
for i in range(1,int(total_num)+1):
    data_in=input('输入第%d个数据：'%i)
    list1.append(data_in)

#向.mif文件进行写入
headfile='''
WIDTH = 32;
DEPTH = 4096;
ADDRESS_RADIX = UNS;
DATA_RADIX = BIN;
CONTENT BEGIN
'''
mif=open('test.mif','w')
mif.truncate()
mif.writelines(headfile)
for i in range(int(total_num)):
    this_num=list1[i]
    test = num_to_float(this_num)
    mif.write(str(i)+":"+test+";\n")
mif.write('END;')

mif.close()