import jieba

# 创建停用词列表
def stopwordslist():
    stopwords = [line.strip() for line in open('C:\\Users\\沈海健\\Desktop\\自然语言处理\\hit_stopwords.txt', encoding='UTF-8').readlines()]
    return stopwords


# 对句子进行中文分词
def seg_depart(sentence):
    # 对文档中的每一行进行中文分词
    print("正在分词")
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    stopwords = stopwordslist()
    # 输出结果为outstr
    outstr = ''
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

# 给出文档路径
filename = "C:\\Users\\沈海健\\Desktop\\自然语言处理\\资本论.txt"
outfilename = "C:\\Users\\沈海健\\Desktop\\自然语言处理\\资本论_去停用词分词.txt"
inputs = open(filename, 'rb')
outputs = open(outfilename, 'w')

# 将输出结果写入ou.txt中
for line in inputs:
    line_seg = seg_depart(line)
    outputs.write(line_seg + '\n')
    print("-------------------正在去停用词分词-----------")
outputs.close()
inputs.close()
print("删除停用词和分词成功！！！")
