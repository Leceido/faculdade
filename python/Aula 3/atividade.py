print("Questao 2")
x = "PaLaVrA"
for n in range(len(x)):
    print(x[(len(x)-1)-n].lower(), end="")

import numpy as np
mat = np.array([
    [[2, 14, 8, 1], [17, 4, 13, 9]],
    [[10, 5, 11, 18], [26, 19, 23, 16]],
    [[15, 6, 27, 3], [12, 20, 0, 21]],
])
print(mat[1, 0, 3] * 2)

conjunto = {"fusca", "gol", "brasilia"}
print("gol" in conjunto)

t1 = 1, 2, 3
t2 = (1, 2, 3)
print(t1==t2)

a = [[1,2],[3,4]]
print(a[1][0])