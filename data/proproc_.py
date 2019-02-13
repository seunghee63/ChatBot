#-*- coding:utf-8 -*-
import re #정규 표현식 모듈

from konlpy.tag import Kkma

fp=open('7CM00044.txt', 'r', encoding='utf-16')
ff=open('chat.log','w',encoding='utf-8')

Nstr = re.compile("\/[\W].*?")

isText = 0;
cnt = 0;
kkma = Kkma()

while True:
    line = fp.readline()

    # 대화 문장만 추출 해 냄
    if not line:
        break
    elif (line == "<text>\n"):
        isText = 1
    elif (line == "</text>\n"):
        isText = 0

    if (isText != 1):
        continue

    #
    person = re.search('<u who="P\d">', line, re.I | re.S)
    if (person is not None):
        print(line[8:10] + ": ", end='')

    personEnd = re.search('</u>', line, re.I | re.S)
    line = re.sub('<.*?>', '', line, 0, re.I | re.S)
    line = re.sub(',', '', line, 0, re.I | re.S)
    line = re.sub('\n', '', line, 0, re.I | re.S)
    line = re.sub('::', '', line, 0, re.I | re.S)
    line = re.sub('<trunc>.*</trunc>', '', line, 0, re.I | re.S)

    # 한 사람이 말 한 내용이 없으면(한숨 같은 효과음) 없애기
    # line = re.sub('  ',' ',line ,0, re.I|re.S)

    " ".join(line.split())

    dialog = kkma.pos(line, 22, True)

    print_dialog = ""
    for data in dialog:
        data += " "
        print_dialog += data

    if (personEnd is not None):  # 한사람 말 끝나면 줄넘김
        print(print_dialog)
        ff.write(print_dialog + "\n")
        cnt = cnt + 1
    else:  # 말 이어서 하는중이면 줄넘김 없음
        print(print_dialog, end='')
        print(" ", end='')
        ff.write(print_dialog)

    if cnt == 2:
        print("")
        cnt = 0

fp.close()
ff.close()
