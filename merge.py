import pandas as pd
import json

data = pd.read_csv("reuters_out.csv", header=None, sep='\t')
sentences=[]
labels=[]
for sentence, label in zip(data[2], data[1]):
    sentences.append(sentence)
    labels.append(label)

for sentence, label in zip(sentences, labels):
    jsonobj={'sentence':sentence, 'label':label}
    print json.dumps(jsonobj)

