import os.path
# 파일 입출력
'''
파일: 보조기억장치(HDD)에 데이터 영구저장
텍스트 파일: 텍스트, 연속적인 줄
파일입출력과정: 열기 > 읽기, 쓰기 > 닫기
'''

# 파일 사용
'''
파일객체 = open(파일명, 모드) 
    모드: r(기본), w, a

'''

f = open('py_ai/name.txt')
data = f.read()
print(data)
f.close()

f = open('py_ai/name.txt')
data = f.readline()
print(data)
f.close()

f = open('py_ai/name.txt')
data = f.readlines()
print(data)
f.close()


f = open('py_ai/name.txt')
while True:
    data = f.readline()
    if not data:break
    print(data, end='')

f.close()

f = open('py_ai/name.txt')
data = f.readlines()
for line in data:
    print(line)
f.close()

ff = 'py_ai/club.txt'


if os.path.exists(ff):
    f = open('py_ai/club.txt', 'w')
    while True:
        name = input("이름: ")
        if not name:break
        f.write(name+'\n')
    f.close()
else:
    print(f"{ff} 파일이 없습니다.")


try:
    f = open('py_ai/club.txt', 'w')
    while True:
        name = input("이름: ")
        if not name:break
        f.write(name+'\n')
    f.close()
except:
    print(f"{ff} 파일이 없습니다.")


# 엑셀 파일 
'''
# pandas 파일 입출력 핵심 코드

## 1. CSV 읽기
```python
import pandas as pd

df = pd.read_csv('my_file.csv')
df.head()
```

---

## 2. Excel 읽기
```python
import pandas as pd

df = pd.read_excel('my_addr.xlsx')
df.head()
```

---

## 3. CSV 저장
```python
df.to_csv('my_file.csv')
```

옵션
```python
df.to_csv('my_file.csv', index=False)
```

---

## 4. Excel 저장
```python
df.to_excel('my_addr.xlsx')
```

옵션
```python
df.to_excel('my_addr.xlsx', index=False)
```

---

## 5. CSV 추가 저장 (append)
```python
df.to_csv('my_file.csv', mode='a', header=False, index=False)
```

---

## 6. 데이터프레임 생성
```python
import pandas as pd

df = pd.DataFrame([
    ['루비', 80, 80, 75, 90, 'B+', 0]
])
```

---

## 7. 데이터 추가 (append)
```python
df = df.append({
    '이름': '유관순',
    '연락처': '010-3333-3333',
    '이메일': 'you@test.com'
}, ignore_index=True)
```

---

## 핵심 함수 정리

- pd.read_csv()
- pd.read_excel()
- df.to_csv()
- df.to_excel()
- df.head()
- pd.DataFrame()
- df.append()

'''