
#형태소 태깅
from konlpy.tag import Kkma, Mecab
from konlpy.utils import pprint

mecab = Mecab()
kkma = Kkma()

inputstr = kkma.pos("안녕, 반가워 나는 승희라고 해! 니 이름은 뭐야?", 9 ,True)

print(inputstr)