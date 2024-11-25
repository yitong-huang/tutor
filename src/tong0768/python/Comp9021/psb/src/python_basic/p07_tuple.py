print()

simple_tuple = ('huang', 123, 3.14, 'yi', 0, 'tong')
# 输出完整列表
print(simple_tuple)
# 输出列表的第一个元素
print(simple_tuple[0])
# 输出第二个至第三个元素
print(simple_tuple[1:3])
# 输出第一个至第五个元素，并间隔2
print(simple_tuple[0:5:2])
# 输出列表两次
print(simple_tuple * 2)
# 修改（不允许）
simple_tuple[1] = 789
print(simple_tuple)