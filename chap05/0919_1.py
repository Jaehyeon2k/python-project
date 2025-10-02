# p26 re.search() 함수

import re

txt1 = "Hello World, Hi python"
txt2 = "Nice to meet you"

print(re.search("Hi", txt1))
print(re.search("To", txt2))

# p28 메타 문자 : 앵커

print(re.search("^Hi", txt1))
print(re.search("^Nice", txt2))
print(re.search("python$", txt1))
print(re.search("to$", txt2))

# p30 메타 문자 : 도트, 이스케이프문자, 대괄호

print(re.search("H..L", "HTML5"))
print(re.search("CSS\d", "CSS3"))
print(re.search("[hH]ello", "hello"))
print(re.search("\w\w[1-9]", "ID9"))
print(re.search("[A-F][A-F]\s\d", "AB 7"))
print(re.search("[^ABCD].[1-9]", "E72"))

# 문제 YJU-학년, 학년은 1, 2, 3만 가능

txt = "YJU-1"
txt2 = "YJU-4"
pattern = "^YJU-[1-3]"
print(re.search(pattern,txt))
print(re.search(pattern,txt2))

# p32 확장 정규식의 메타 문자
print(re.search("hello|hello", "Hello"))
print(re.search("\+?\d\d", "10"))
print(re.search("-[1-9][0-9]", "-10"))
print(re.search("\+[1-9]\d+", "+39"))

# {} 한정자
print(re.search("'0\d{2}-[1-9]\d{2}-\d{4}", "053-940-5297"))
# {n,m} 한정자
print(re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", "127.0.0.1"))

# 문제 4자리수 출생 년도 패턴

txt = "2000"
txt2 = "01"
txt3 = "1999"
pattern= "[12][0-9]{3}"
print(re.search(pattern, txt))
print(re.search(pattern, txt2))
print(re.search(pattern, txt3))

# p33 실습. 정규표현식 : 행 추출
f = open("test1.txt")

for line in f:
    line = line.rstrip()
    if re.search("^\([0-9]+\)", line) :
        print(line)

# p34 re.findall()메소드

text="""101 COM PythonProgramming
102 MAT LinearAlgebra
103 ENG ComputerEnglish"""

s = re.findall("\d+", text)
print(s)

# p35 실습. 정규표현식 : 이메일 추출
f = open("test1.txt")
txt = f.read()

output = re.findall("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", txt)

print("추출된 이메일 개수 : ", len(output))
print("추출된 이메일 목록 :\n", output)