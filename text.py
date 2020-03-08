import re
from hgtk.text import compose, decompose
from string import ascii_lowercase



jaem = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㄲ', 'ㄸ', 'ㅃ', 'ㅆ', 'ㅉ', 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ']
moem = ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅐ', 'ㅒ', 'ㅔ', 'ㅖ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ']
english = list(ascii_lowercase)

link_list = [' ', ',', '.', '?', '!', '^', '%'] + jaem + moem + english + [str(i) for i in range(10)]
encoding_dict = {k:code+1 for code, k in enumerate(link_list)}
decoding_dict = {v:k for k, v in encoding_dict.items()}
pattern = re.compile('[ㄱ-ㅣa-z0-9 ,.?!^%]')


def Decompose(text):
    text = ' '.join(list(text.lower())) # 아   시 발   이 건   좀   아 니 지
    text = ''.join(decompose(text)) # ㅇㅏ   ㅅㅣ ㅂㅏㄹ   ㅇㅣ ㄱㅓㄴ   ㅈㅗㅁ   ㅇㅏ ㄴㅣ ㅈㅣ
    text = ''.join(pattern.findall(text)) # ㅇㅏ   ㅅㅣ ㅂㅏㄹ   ㅇㅣ ㄱㅓㄴ   ㅈㅗㅁ   ㅇㅏ ㄴㅣ ㅈㅣ
    return text

def Compose(text):
    text = compose(text + ' ')[:-1]
    text_list = text.split('   ') # ['아', '시 발', '이 건', '좀', '아 니 지']
    text_list = [t.replace(' ', '') for t in text_list] # ['아', '시발', '이건', '좀', '아니지']
    text = ' '.join(text_list)
    return text

def encode(text):
    # t_l = Decompose(text).split('   ')
    # text = ' '.join([t.replace(' ', '') for t in t_l])

    # encoding = [encoding_dict[t] for t in text]
    code = [encoding_dict[t] for t in Decompose(text)]
    return code

def decode(code):
    text = ''.join([decoding_dict[c] for c in code])
    text = Compose(text)
    return text


if __name__ == "__main__":
    while True:
        s = input()
        # dec = Decompose(s)
        # com = Compose(dec)
        # print(f"{dec}     {com}\n")
        enc = encode(s)
        dec = decode(enc)
        print(f"{enc}     {dec}\n")