simple_list = ['huang', 123, 3.14, 'yi', 0, 'tong']

print(simple_list[1:-6])
# 输出完整列表
print(simple_list)
# 输出列表的第一个元素
print(simple_list[0])
# 输出第二个至第三个元素
print(simple_list[1:3])

# 输出第一个至第五个元素，并间隔2
print(simple_list[0:5:2])
# 输出列表两次
print(simple_list * 2)
# 打印列表连接
print(simple_list + [1, 'hello'])
# 修改
simple_list[1] = 789
print(simple_list)

