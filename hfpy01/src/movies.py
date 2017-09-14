# 声明列表
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
          ["Graham Chapman", ["Michael Palin", "John Cleese",
                              "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

# 输出列表对象
print(movies)
# 输出列表长度
print(len(movies))

# 循环
for each_item in movies:
    print(each_item)

print("-- 嵌套循环 ----------------")
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            print(nested_item)
    else:
        print(each_item)

print("-- 多重嵌套循环 ----------------")
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)

# 通过函数解决
print("-- 函数 ---------------------------------")


def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            # 递归
            print_lol(each_item)
        else:
            print(each_item)


# 调用函数
print_lol(movies)
