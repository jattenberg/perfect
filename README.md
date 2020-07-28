# perfect

A little investigation into the properties of integer factorization and perfect numbers. During a sleepless night I was wondering how often the aliquot sum of a number is greater than the number, how often it is less than the number. I also thought of a way to do integer factorization, though I'm sure there are more efficient ways than I came up with.

In number theory, a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. For instance, 6 has divisors 1, 2 and 3 (excluding itself), and 1 + 2 + 3 = 6, so 6 is a perfect number.

The sum of divisors of a number, excluding the number itself, is called its aliquot sum, so a perfect number is one that is equal to its aliquot sum. Equivalently, a perfect number is a number that is half the sum of all of its positive divisors including itself; in symbols, σ1(n) = 2n where σ1 is the sum-of-divisors function. For instance, 28 is perfect as 1 + 2 + 4 + 7 + 14 + 28 = 56 = 2 × 28.

```python
from perfect import factorization, aliquot_sum
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

%matplotlib inline
```


```python
aliquot_sum(999999)
```




    1042881




```python
def compare_sum_to_num(limit):
    x = list(range(1, limit))
    y = [aliquot_sum(n) for n in x]

    plt.plot(x, y)
    plt.xlabel("number")
    plt.ylabel("aliquot sum")
    plt.plot(x,x)
    plt.show()
```


```python
compare_sum_to_num(100)
```


![png](output_3_0.png)



```python
compare_sum_to_num(1000)
```


![png](output_4_0.png)



```python

```
