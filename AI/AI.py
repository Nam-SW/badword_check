import pandas as pd
import matplotlib.pyplot as plt
import os
from tensorflow.keras.models import load_model

from utils import text


base_url = os.getcwd()
df = pd.read_excel(os.path.join(base_url, 'AI/dataset/dataset.xlsx'), encoding='utf-8-sig')
df.dropna(how='any', inplace=True)
df.to_excel(os.path.join(base_url, 'AI/dataset/dataset.xlsx'), encoding='utf-8-sig', index=None)
model = load_model(os.path.join(base_url, 'AI/model.h5'))


def show_graph():
    for i in range(len(df)):
        d = df.iloc[i]
        df.iloc[i] = [text.encode(d[0]) , d[1]]

    df['length'] = [len(df.iloc[i][0]) for i in range(len(df))]

    plt.hist(df['length'], bins=df['length'].max())
    plt.show()


def check_data_count():
    good_len = len(df[df['label'] == 0])
    bad_len = len(df[df['label'] == 1])
    print(len(df))
    print(f'goodword: {good_len}, badword: {bad_len}')


def predict(data):
    data = text.len_encode(data, 100)
    pred = model.predict(data)
    return pred