## python 알고리즘용 문법 정리

- \<str\>.strip(\<str\>) <br>
  새로운 문자열을 반환하며, 파라미터로 문자를 주면 양 옆으로 해당 문자를 제거한다. default값은 공백이고, 오른쪽만, 왼쪽만 지울 수 있는 rstrip, lstrip함수도 있다.

- \<str\>.replace(\<str\>) <br>
  새로운 문자열을 반환한다. 파라미터로 기존 문자, 새로운 문자를 전달하면 기존 문자를 새로운 문자로 변환한 문자열을 리턴한다. replace("문자열", "")처럼 사용하면 해당 부분 문자열을 지울 수 있다.
- \<arr\>[A:B:C]
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

\+ 참고) max, min 함수에도 key값을 전달할 수 있다.

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

- list comprehension

```
# if문 사용 예시 -> 1부터 10중 짝수만 골라 배열로 만들기
a = [i for i in range(1, 11) if i%2 == 0]
#[2,4,6,8,10]
```

- set과 차집합을 이용하여 중복 없는 경우 배열 일부분 제외한 나머지 가져오기

```
b = [1,2,3,4,5,6]
a = [1,2,3]
# a에 있는 요소 제외한 나머지 모두를 가져오고 싶을 때
c = list(set(b) - set(a))
#[4,5,6]
```

- itertools 모듈

1. product() <br>
   여러개 배열을 넣고 중첩 for문을 사용한 것처럼 각 배열에서 하나씩 뽑아 경우의 수를 리턴한다.

```
A = [1,2,3]
list(itertools.product(A, repeat=2))
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

A = [1,2,3]
B = [4,5]
list(itertools.product(A,B))
# [(1, 4), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5)]
```

2. combination()<br>
   조합 경우의 수를 리턴

```
A = [1,2,3]
list(itertools.combination(A, 2))
#[(1, 2), (1, 3),(2,3)]
```

3. permutation()<br>
   사용법 조합과 동일. 순열 리턴

4. combination_with_replacement()<br>
   사용법 조합과 동일. 중복조합 리턴

- \<arr\>.index()의 시간복잡도는 O(N)이다. 시간 초과가 날 경우 딕셔너리를 이용하여 인덱스를 불러오자.

- 딕셔너리 관련 함수들

1. 삭제

```
dic = {a : 1, b : 2, c : 3}
del dic[b]
print(dic)
# {a : 1, c : 3}
```

2. key만, value만 각 각 리스트로 변환

```
#key
dic = {a : 1, b : 2, c : 3}
dic_keys = list(dic.keys())
print(dic_keys)
# [a, b, c]

#value
dic = {a : 1, b : 2, c : 3}
dic_vals = list(dic.values())
print(dic_vals)
# [1, 2, 3]
```

3. key-value쌍 얻기

```
dic = {a : 1, b : 2, c : 3}
dic_items = list(dic.items())
print(dic_items)
# [(a, 1), (b, 2), (c, 3)]
```

4. key값 유무 조사

```
dic = {a : 1, b : 2, c : 3}
print(a in dic)
# True
print(d in dic)
# False
```

- 집합 관련 함수들

1. 추가 (add, update)

```
# add 함수는 하나의 값만 추가 가능
a = set([1,2,3])
a.add(4)
print(a)
# {1,2,3,4}

```

```
#update 함수는 집합에 여러개 값 추가 가능
a = set([1,2,3])
b = set([4,5,6])
a.update(b)
print(a)
# {1,2,3,4,5,6}
```

2. 제거 (remove, discard)

```
#remove는 없는 값 제거 시 key error 발생, discard는 무시
a = set([1,2,3])
a.remove(1)
print(a)
# {2,3}
a.discard(2)
print(a)
{3}
a.remove(0)
# Key Error
a.discard(0)
# No Key Error
```

3. 집합의 연산

```
# 1. 합집합
a = {1,2,3,4,5}
b = {4,5,6}
print(a|b)
# {1,2,3,4,5,6}
print(union(a, b))
# {1,2,3,4,5,6}
```

```
# 2. 교집합
a = {1,2,3,4,5}
b = {4,5,6}
print(a&b)
# {4,5}
print(intersection(a, b))
# {4,5}
```

```
# 3. 차집합
a = {1,2,3,4,5}
b = {4,5,6}
print(a-b)
# {1,2,3}
print(difference(a, b))
# {1,2,3}
```

```
# 4. 대칭차집합
a = {1,2,3,4,5}
b = {4,5,6}
print(a^b)
# {1,2,3,6}
print(symmetric_difference(a, b))
# {1,2,3,6}
```

4. 그 외 함수

```
# 1. clear
# 집합안에 있는 모든 요소를 삭제
a = {1,2,3}
a.clear()
print(a)
# {}
```

```
# 2. copy
# 집합을 복사하여 리턴 ("="로 할당 시 원본이 변경된다.)
a = {1,2,3}
b = a.copy()
b.remove(1)
print(a)
print(b)
# {1,2,3}
# {2,3}
```

- math 모듈 (수학연산)

1. 올림, 내림, 반올림 연산

```
import math
a = 3.14

print(math.ceil(a))
# 4
print(math.floor(a))
# 3
print(round(a))
print(round(a, 1))
# 3
# 3.1
```

2. 조합/순열 경우의 수, 팩토리얼

```
import math
n = 5
m = 2
print(math.comb(n, m))
print(math.perm(n, m))
# 10
# 20
print(math.factorial(n))
# 120
```

3. 최대공약수, 최소공배수

```
import math
a = 2
b = 4
print(math.gcd(a, b))
# 2
a = 3
b = 5
print(math.lcm(a, b))
# 15
```

4. 제곱, 제곱근

```
a = 4
b = 2
print(math.pow(a, b))
print(math.sqrt(a, b))
# 16
# 2
```
