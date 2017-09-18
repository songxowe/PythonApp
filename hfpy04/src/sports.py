def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string

    (mins, secs) = time_string.split(splitter)
    return mins + "." + secs


with open("james.txt") as jaf:
    # 读取数据行
    data = jaf.readline()
# 将数据转换为一个列表 [方法串链 method chaining]
james = data.strip().split(",")

with open("julie.txt") as juf:
    data = juf.readline()
julie = data.strip().split(",")

with open("mikey.txt") as mif:
    data = mif.readline()
mikey = data.strip().split(",")

with open("sarah.txt") as saf:
    data = saf.readline()
sarah = data.strip().split(",")

print(james)
print(julie)
print(mikey)
print(sarah)

# 原地排序
# print(james.sort())
# 复制排序
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

# 处理 - : 后排序
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for earch_item in james:
    clean_james.append(sanitize(earch_item))
for earch_item in julie:
    clean_julie.append(sanitize(earch_item))
for earch_item in mikey:
    clean_mikey.append(sanitize(earch_item))
for earch_item in sarah:
    clean_sarah.append(sanitize(earch_item))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))
