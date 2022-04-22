import jieba
import math
txt = open("C:\\Users\\沈海健\\Desktop\\自然语言处理\\资本论_去停用词分词.txt", "r", encoding='utf-8').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

'''排序输出'''

for i in range(10):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))

'''计算信息熵'''

sum = 0
for num in counts.values():
    sum+=num
print(sum)
shannoEnt = 0.0
for word, freq in counts.items():
    prob = freq / sum
    shannoEnt -= prob*math.log(prob, 2)
print(shannoEnt)
