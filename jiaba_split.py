import jieba

def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word != '\t':
            outstr += word
            outstr += " "
    return outstr

# 给出文档路径
filename = "D:\\复试\\自然语言处理\\自然语言处理18074305沈海健\\源代码\\资本论.txt"
outfilename = "D:\\复试\\自然语言处理\\自然语言处理18074305沈海健\\源代码\\资本论_普通分词.txt"
inputs = open(filename, 'rb')
outputs = open(outfilename, 'w')

# 将输出结果写入ou.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
    print("-------------------正在分词---------------------")
outputs.close()
inputs.close()
print("普通分词成功！！！")
