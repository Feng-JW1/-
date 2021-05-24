def perms(s=''):
    if len(s) <= 1:  # 长度为1的字符串，排列组合就是自己
        return [s]
    sl = []  # 放结果
    for i in range(len(s)):  # 第一个数的可能取值
        for j in perms(s[0:i] + s[i + 1:]):  # 排除第一个数
            sl.append(s[i] + j)
    return (list(set(sl)))
perm_nums = perms('111111111')
print('no_repeat_nums', len(perm_nums), perm_nums)

filename='新建文本文档.txt'
with open(filename,'w') as f:
    f.truncate()
    for i in range(len(perm_nums)):
        sr=perm_nums[i]
        f.write("9'b" +sr[0]+"_"+sr[1:5]+"_"+sr[5:9]+",\n")



