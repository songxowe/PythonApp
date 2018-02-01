import random
import jieba

# pip3 install jieba

dataset_file = ["我喜欢吃苹果。", "你吃橘子。"]
print("\n分词前：", dataset_file)

for i, each_sentence in enumerate(dataset_file):
    dataset_file[i] = " ".join(jieba.cut(each_sentence))

print("\n分词后：", dataset_file)

model = {}

for line in dataset_file:
    line = line.lower().split()
    for i, word in enumerate(line):
        if i == len(line) - 1:
            model['END'] = model.get('END', []) + [word]
        else:
            if i == 0:
                model['START'] = model.get('START', []) + [word]
            model[word] = model.get(word, []) + [line[i + 1]]

print("\n模型：", model)

generated = []
while True:
    if not generated:
        words = model['START']
    elif generated[-1] in model['END']:
        break
    else:
        words = model[generated[-1]]
    generated.append(random.choice(words))

print("\n生成的一个结果：" + "".join(generated))
