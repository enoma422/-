# [0]번째 인덱스에는 획수가 1인 자음/모음을 넣었다.
# 한글 자음 획수 리스트
han_ja_cnt = ['ㄱㄴㅇ','ㄷㅅㅈㅋㄲ','ㄹㅁㅊㅌㅎ', 'ㅂㅃㅉㄲㅉ']
# 한글 모음 획수
han_mo_cnt = ['ㅡㅣ','ㅏㅓㅗㅜㅢ','ㅐㅔㅚㅟㅕㅛㅟ','ㅘㅝㅒㅖ','ㅙㅞ']
# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

res_name1 = [0] * 3
res_name2 = [0] * 3
res_lst = []

# 글씨를 부수는 함수
def name_broke(korean_name):
    r_lst = []
    for w in list(korean_name.strip()):
            ## 588개 마다 초성이 바뀜. 
            ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
    return r_lst

# 자음/모음의 획수를 찾아주는 함수
def han_cnt(name):
    res = 0
    for i in name:
        for j in han_ja_cnt:
            if i in j:
                res = han_ja_cnt.index(j) + 1
        for k in han_mo_cnt:
            if i in k:
                res = han_mo_cnt.index(k) + 1
    return res            

# 리스트의 item값만 출력하는 함수
# 보기좋게... 띄어쓰기도 잘 했답니다
def lst_print(lst):
    print(" "*(6-len(lst)), end='')
    for i in range(len(lst)):
        print(lst[i], end='  ')
    print()

# 이름궁합에 필요한 더하기를 진행하는 함수 
# (양 옆의 숫자를 더해서 일의 자리만 남긴다)
def lst_add(lst):
    for i in range(len(lst)-1):
        lst[i] = (lst[i] + lst[i+1]) % 10
    del(lst[len(lst)-1])

# 이름 두개를 입력 받습니다
name1, name2 = map(str, input().split())

print("\n[", name1,"님과", name2, "님의 이름 궁합]")

for i in range(3):
    print(name1[i], name2[i], end=' ')

name1 = name_broke(name1)
name2 = name_broke(name2)

print()

# 각 이름 한 글자 안에서의 초/중/종성을 구분해 획수를 구하고 다시 각 글자당 획수로 합쳐준다
for i in range(3):
    tmp1 = 0
    tmp2 = 0
    for j in range(3):
        tmp1 += han_cnt(name1[i][j])
        tmp2 += han_cnt(name2[i][j])
    res_name1[i] = tmp1
    res_name2[i] = tmp2
    res_lst.append(res_name1[i])
    res_lst.append(res_name2[i])

# 이름의 획수를 한글자씩 출력
lst_print(res_lst)

# 이제 그 획수를 더해주는 중
for i in range(4):
    lst_add(res_lst)
    lst_print(res_lst)
    # 100점일 경우...
    if(i==2 and res_lst[0]==1 and res_lst[1]==0 and res_lst[2]==0):
        break

print("두분의 궁합은...", end=' ')
for i in range(len(res_lst)):
    print(res_lst[i], end='')
print("%")