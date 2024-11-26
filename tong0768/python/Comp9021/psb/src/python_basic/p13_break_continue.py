i = 0
break_target = 10
continue_target = 5
print("break")
while True:
    i += 1
    if i == break_target:
        break
    print(i)


i = 0
print("continue")
while True:
    i += 1
    if i == break_target:
        break
    if i == continue_target:
        continue
    print(i)

print("out of while")
