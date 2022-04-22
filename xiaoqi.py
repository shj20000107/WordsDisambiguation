import logging
import os.path
import sys
import multiprocessing
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
from gensim.models import Word2Vec
import numpy as np

program = os.path.basename(sys.argv[0])  # 读取当前文件的文件名
logger = logging.getLogger(program)
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))
# inp为输入语料, outp1为输出模型, outp2为vector格式的模型
inp = 'C:\\Users\\沈海健\\Desktop\\自然语言处理\\资本论_去停用词分词.txt'
out_model = 'corpusSegDone_1.model'
out_vector = 'corpusSegDone_1.vector'
# 训练模型
model = word2vec.Word2Vec(LineSentence(inp), vector_size=50, window=5, min_count=5, workers=multiprocessing.cpu_count())
# 保存模型
model.save(out_model)
# 保存词向量
model.wv.save_word2vec_format(out_vector, binary=False)

model = Word2Vec.load('corpusSegDone_1.model')
model.wv.most_similar(u'斗争')
content = ['无产阶级', '反对', '资本主义', '斗争']
des1 = ['矛盾', '双方', '激烈', '冲突']
des2 = ['群众', '当面', '批判', '打击']
des3 = ['努力', '奋斗', '努力奋斗']

def w2v_mean(essay, model):
    ls = np.zeros(50)
    for unit in essay:
        try:
            ls += np.array(model.wv[unit])
        except:
            pass
    return ls / len(essay)

content = w2v_mean(content, model)
d1 = w2v_mean(des1, model)
d2 = w2v_mean(des2, model)
d3 = w2v_mean(des3, model)
print(np.dot(d1, content) / (np.linalg.norm(d1) * (np.linalg.norm(content))))
print(np.dot(d2, content) / (np.linalg.norm(d2) * (np.linalg.norm(content))))
print(np.dot(d3, content) / (np.linalg.norm(d3) * (np.linalg.norm(content))))
