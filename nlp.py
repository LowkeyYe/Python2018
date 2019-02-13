import os
import pandas as pd
import jieba.analyse

def read_txt(root):
    txt_list = os.listdir(root)
    doc = []
    label = [i.split('_')[0] for i in txt_list]
    for txt in txt_list:
        with open(root + '\\' + txt, 'r') as f:
            doc.append(f.readlines()[0])
    doc_df = pd.DataFrame({'doc':doc, 'label':label})
    return doc_df

def cut_doc(doc_df):
    jieba.analyse.set_stop_words()
if __name__ == "__main__":
    root = r'C:\Users\Administrator\Desktop\nlp_work\data'
    print(read_txt(root))