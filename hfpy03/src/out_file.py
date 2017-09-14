man = []
other = []

try:
    data = open("sketch.txt")
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
except IOError:
    print("The datafile is missing!")
finally:
    data.close()

# ----------------------------------------------------
try:
    # 以写模式打开文件
    man_file = open("man_data.txt", "w")
    other_file = open("other_data.txt", "w")

    print(man, file=man_file)
    print(other, file=other_file)

    print("write file success. :)")
except IOError:
    print("write file error.")
finally:
    man_file.close()
    other_file.close()
