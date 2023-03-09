import pandas as pd
import numpy as np
from itertools import product

# Заданное множество
A = [1,2,3,4]

# Вспомогательная матрица
m = pd.DataFrame(np.array(list(A) * len(A)).reshape(len(A), -1),
                columns = list(A), index = list(A))
print(m)

# Делим каждую строку вспомогательной матрицы на вектор А и проверяем остаток от деления на 1
res = (m.div(list(A), axis = 0) % 1 == 0).astype('int8')
print(res)

# Множество пар
pred = lambda a, b: b % a == 0
rel = [(a, b) for (a, b) in product(list(A), repeat = 2) if pred(a, b)]
print(rel)

# Тест на транзитивность
second_elements = [b for (a, b) in rel]
for (a, b) in rel:
    for c in second_elements:
        if (b, c) in rel and (a, c) not in rel:
            print('No')
print('Yes')