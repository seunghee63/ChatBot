# 챗봇
- 간단하게 만든 Seq2Seq 모델을 이용하여 챗봇을 만들어봅니다.
- 'konlpy패키지 > 꼬꼬마 형태소분석기' 이용하여 문장의 형태소를 분석합니다. http://konlpy.org/ko/v0.4.3/#
- Seq2Seq 모델 자체는 크게 변경하지 않았으며, 모델을 이용하기 위해 단어 임베딩을 만들고, 이를 이용하는 전처리/후처리 코드가 많이 추가되었습니다.


### 데이터

국립국어원 언어정보나눔터 > 데이터 베이스 자료 > 말뭉치자료

- 8CT_0045.txt : 주제대화_취업
- 8CT_0044.txt : 주제대화_대학진학

### 사용방법

기본적으로 다음 데이터를 사용합니다. config.py 파일에서 추가 옵션들을 확인해보세요.

- data/chat.log : 대화 데이터
- data/chat.voc : 어휘 데이터


# 채팅해보기

```
python3 chat.py
```

<img src="screenshot.png" width="480">

### 데이터 전처리 > chat.log 생성

```
python preproc.py
```

### 어휘 데이터 생성 > chat.voc

토크나이저를 바꿨거나 새로운 데이터를 이용하기를 원하는 경우, 다음과 같은 방법으로 먼저 어휘 데이터를 생성해야 합니다.
기본 토크나이저는 공백과 특수문자로 구분합니다.

```
python dialog.py --voc_build
```

### 학습 > 모델 생성

``` 
python train.py --train
```
>정확도 조절을 위해 epoch,batch_size 값을 변경합니다.


학습된 모델이 있으면 새로 생성하지 않고 추가학습을 합니다.

다음과 같이 텐서보드를 통해 cost 를 확인할 수 있습니다.

```
tensorboard --logdir=./logs
```

### 테스트

```
python train.py --test
```


