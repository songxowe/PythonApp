data = open('sketch.txt')

for each_line in data:
    # 避免 (pause)
    if not each_line.find(":") == -1:
        # 截取一行数据中第一个 :
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

data.close()
