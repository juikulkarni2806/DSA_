def get_max(*num):
    if len(num)==0:
        return None

    max_num=num[0]
    for n in num:
        if n>max_num:
            max_num=n
    return max_num
print(get_max(3,45,43,21,98))
print(get_max('jui','Zarina','zarina','lata'))
