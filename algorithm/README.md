## python 알고리즘용 문법 정리

- \<str\>.strip(\<str\>) <br>
  새로운 문자열을 반환하며, 파라미터로 문자를 주면 양 옆으로 해당 문자를 제거한다. default값은 공백이고, 오른쪽만, 왼쪽만 지울 수 있는 rstrip, lstrip함수도 있다.

- \<str\>.replace(\<str\>) <br>
  새로운 문자열을 반환한다. 파라미터로 기존 문자, 새로운 문자를 전달하면 기존 문자를 새로운 문자로 변환한 문자열을 리턴한다. replace("문자열", "")처럼 사용하면 해당 부분 문자열을 지울 수 있다.
  \*\<arr\>[A:B:C]
  extended slice는 A부터 B까지 C 간격으로 슬라이싱 하라는 의미이다. 주로 펠린드롬처럼 문자열을 뒤집을 때에 쓴다.
  ex)

```
print(["a","b","c"][::-1])

# ["c", "b", "a"]
```

- \<arr\>.sort(key=, reverse=) <br>
  배열을 정렬해준다. key 값에 값이 반환되는 일반 함수나 lamda 함수를 사용하면 해당 값 기준으로 정렬한다. ex)

```
a = [(1,3), (2,2), (3, 1)]
a.sort(key = lambda x : x[1])
# 두번째 원소 기준으로 오름차순 정렬
```

- set()함수 이용하여 중복 제거

```
arr = [1, 2, 3, 3, 2, 2, 4]
arr = list(set(arr))
print(arr)
#[1, 2, 3, 4]
```

- python에서 재귀깊이 제한풀기

```
import sys
sys.setrecursionlimit(10000)
```
