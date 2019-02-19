# -*- coding:utf-8 -*-
import re  # 정규 표현식 모듈

from konlpy.tag import Kkma

fp = open('7CM00044.txt', 'r', encoding='utf-16')
ff = open('chat.log', 'w', encoding='utf-8')

Nstr = re.compile("\/[\W].*?")

isText = 0;
cnt = 0;
kkma = Kkma()

while True:
    line = fp.readline()

    # 대화 문장만 추출
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
        #print(line[8:10] + ": ", end='')
        tagging_cnt = 0

    personEnd = re.search('</u>', line, re.I | re.S)
    line = re.sub('<.*?>', '', line, 0, re.I | re.S)
    line = re.sub(',', '', line, 0, re.I | re.S)
    line = re.sub('\n', '', line, 0, re.I | re.S)
    line = re.sub('::', '', line, 0, re.I | re.S)
    line = re.sub('<trunc>.*</trunc>', '', line, 0, re.I | re.S)
    line = re.sub('<phon>.*</phon>', '', line, 0, re.I | re.S)

    # 한 사람이 말 한 내용이 없으면(한숨 같은 효과음) 없애기
    # line = re.sub('  ',' ',line ,0, re.I|re.S)

    " ".join(line.split())

#
    #if (line == ""):
        #continue

    dialog = kkma.pos(line, 22, True)

    print_dialog = ""
    for data in dialog:
        data += " "
        print_dialog += data

    # personEnd 나오기 전 까지 /cnt 세기

    if (personEnd is not None):  # 한사람 말 끝나면 줄넘김

        cnt = cnt + 1
        tagging_cnt = print_dialog.count('/')

        #너무 짧은 문장 지움
        if (tagging_cnt <= 2):
            continue
        else :
            #print(print_dialog)
            ff.write(print_dialog + "\n")

    elif (line == ""):
        continue
    else:  # 말 이어서 하는중이면 줄넘김 없음
        print_dialog = re.sub('.*?/SF ', '', print_dialog, 0, re.I | re.S)

        tagging_cnt = print_dialog.count('/')

        #너무 짧은 문장 지움
        if (tagging_cnt == 1):
            continue
        #print(print_dialog, end='')
        #print(" ", end='')
        ff.write(print_dialog)


    #if cnt == 2:
    #    print("")
    #    cnt = 0


fp.close()
ff.close()
