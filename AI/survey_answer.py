import pandas as pd

df = pd.read_excel('./dataset/욕설 구분 모델용 데이터셋 수집(응답).xlsx', 
                   encoding='utf-8-sig', 
                   names=['제출시간', '동의여부', '욕설답변'], 
                   )

df = df.dropna(how='any')

print('df_len:', len(df))

bad_word_list = []

for i, answer in enumerate(df['욕설답변']):
    print(answer)
    split_word = input(f'{i}번째글 기준 단어: ')
    if not split_word:
        split_word = '\n'
    
    bad_word_list += answer.split(split_word)

print(len(bad_word_list))
save_df = pd.DataFrame({'data': bad_word_list, 'label':[1 for _ in range(len(bad_word_list))]}).dropna(how='any')

save_df.to_excel('./dataset/badword.xlsx', encoding='utf-8-sig', index=False)