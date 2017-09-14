man = []
other = []

try:
    # with 语句使用了一种上下文管理协议(context management protocol)的 Python 技术
    # with 不再需要操作关闭打开的文件,因为 Python 解释器会自动关闭文件
    with open("sketch.txt") as data:
        for each_line in data:
            try:
                (role, line_spoken) = each_line.split(":", 1)
                # 去除空白符
                line_spoken = line_spoken.strip()
                if role == "Man":
                    man.append(line_spoken)
                elif role == "Other Man":
                    other.append(line_spoken)
            except ValueError:
                pass
except IOError as error:
    print("The datafile is missing!" + str(error))

# ----------------------------------------------------
try:
    with open("man_data.txt", "w") as man_file, open("other_data.txt", "w") as other_file:
        print(man, file=man_file)
        print(other, file=other_file)

        print("write file success. :)")
except IOError as error:
    print("write file error." + str(error))
