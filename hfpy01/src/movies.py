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
