import os
import pickle
from string import ascii_lowercase, ascii_uppercase
from collections.abc import Iterable

import numpy as np
from hgtk.text import compose, decompose
from tensorflow import reduce_sum
from tensorflow.keras import callbacks, layers, metrics
from tensorflow.keras.utils import plot_model, to_categorical
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.preprocessing.sequence import pad_sequences


directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(directory, 'model')

def get_path(filename):
    return os.path.join(path, filename)

if os.path.isfile(get_path('chardict.pkl')):
    with open(get_path('chardict.pkl'), 'rb') as f:
        char_dict = pickle.load(f)

else:
    jaem = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ']
    moem = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
    english = list(ascii_lowercase) + list(ascii_uppercase)
    sign = [s for s in ''' `~!@#$%^&*()+-/=_,.?;:'"[]{}<>\|''']

    link_list = sign + jaem + moem + english + [str(i) for i in range(10)]
    char_dict = {k: code + 2 for code, k in enumerate(link_list)} # 0은 padding, 1은 oov

    with open(get_path('chardict.pkl'), 'wb') as f:
        pickle.dump(char_dict, f, pickle.HIGHEST_PROTOCOL)

vocab_size = len(char_dict) + 2 # padding, OOV 포함!
maxlen = 60


def encode(text: str) -> list:
    """
    하나의 str을 받아와 인코딩합니다. 단, padding 작업은 진행하지 않습니다.

    argument
    text: 인코딩할 문자열입니다.

    return: 인코딩된 리스트를 반환합니다.
    """
    assert isinstance(text, str), "text argument must be str."

    text = decompose(str(text)).replace('ᴥ', '')
    code = [char_dict.get(t, 1) for t in text]
    return code


def preprocessing(data: Iterable) -> np.ndarray:
    """
    하나의 str 또는 str로 구성된 iterable한 객체을 받아와 인코딩합니다.
    padding 작업과 one-hot-encoding 작업도 진행합니다.

    argument
    text: 인코딩할 문자열 또는 문자열이 담긴 순회가능한 객체입니다.

    return: 인코딩, padding, one-hot-encoding 작업을 거친 3차원 numpy 배열입니다.
    """
    if isinstance(data, str):
        data = [encode(data)]
    elif isinstance(data, Iterable):
        data = [encode(t) for t in data]
    else:
        assert True, "data argument must be str or Iterable object."
    
    data = pad_sequences(data, maxlen)
    
    return to_categorical(data, vocab_size)


def load_badword_model() -> Model:
    """
    학습된 모델을 불러옵니다. 불러온 모델은 compile 작업을 마친 상태입니다.
    
    return: 사전학습된 tf.keras.Model 객체가 compile된 상태로 반환됩니다.
    """
    model = load_model(get_path('model.h5'))
    model.compile(
        loss="binary_crossentropy", 
        optimizer="adam", 
        metrics=[
                 metrics.BinaryAccuracy(name="acc"), 
                 metrics.Recall(name="recall"), 
                 metrics.Precision(name="prec"),
                 ]
                  )
    
    return model