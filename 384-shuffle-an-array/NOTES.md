# Random

```
random.sample(list, int)
```

returns multiple random elements from the list without replacement.


```
import random

l = [0, 1, 2, 3, 4]

print(random.sample(l, 3))
# [1, 3, 2]

random.sample(l, len(l)) -> shuffle a list

```
