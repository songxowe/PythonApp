import sys

print('The command line arguments are:')
# sys.argv 是一系列字符串的列表（List）
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')
