# 1
str = '2 + 2 = 4'
str = str.replace('2', 'two')
print(str)

# 2
a = '123 + (d + (a + b) + 12) = 223'
a = a.replace('(', '*(', 1)
ind = a.rfind(')')
a = a[:ind] + ')*' + a[ind+1:]
print(a)