# [Lecture 5: Floats and Approximation Methods](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/mit6_100l_f22_lec05_pdf/)

## Floats

```
x = 0
for i in range(10):
    x += 0.1
print(x == 1, x)

y = 0
for i in range(10):
    y += 0.125
print(y == 1.25, y)

output:
False 0.9999999999999999
True 1.25
```
0.1은 2로 나누어 떨어지지 않아 approximation이 들어가고

0.125는 2로 나누어 떨어지기에 exact하다.

따라서 designing algorithm 시에 float 사용을 조심.

**Because they can't be represented in memory exactly**

## EFFECT of APPROXIMATION on our ALGORITHMS?
- **Exact** answer may not be **accessible**
- Need to find ways to get "**good enough**"(or **close enough**) answer -> Therefore, let's use epsilon-delta.
