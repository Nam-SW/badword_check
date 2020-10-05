# badword_check
입력한 글(한글)이 욕설인지 아닌지를 딥러닝을 통해 판별하는 모델입니다.  
`tensorflow 2.0`을 원활하게 구동할 수 있는 Python 3.5 - 3.7 의 환경에서 원활하게 작동합니다.

## 설치
```
$ git clone https://github.com/Nam-SW/badword_check.git
$ cd 클론한_디렉토리
$ pip install -r requirements.txt
```

## 사용방법
```py
from badword_check import BadWord

model = BadWord.load_badword_model()
data = BadWord.preprocessing("그게 뭔데 씹덕아...")
print(model.predict(data))
```

## 변경내역
+ **버전 1.0:** 첫 버전 릴리즈

## 참고자료
+ [[NDC] 딥러닝으로 욕설 탐지하기][욕설탐지]
+ [Notion 프로젝트 정리 페이지][notion]

## 참고사항
현재 본 프로젝트는 지속적으로 보완중인 프로젝트입니다. 아직 모델이 걸러낼 수 없는 말들이 다수 존재합니다.
만약 라이브러리에 오류가 있거나 모델이 잘못 예측하는 경우엔 이슈나 [메일][Gmail]로 연락 주시면 감사하겠습니다.

[욕설탐지]: https://www.youtube.com/watch?v=K4nU7yXy7R8
[notion]: https://www.notion.so/namseungwoo/1c380d64fd374b8fb54b08c6a0be1440
[Gmail]: https://gmail.com/
