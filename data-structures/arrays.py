import numpy as np

array = np.array([[1, 2, 3, 4, 5]])

print(array)
print("Boyut :", array.shape)

array2D = np.array([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10]])

print(array2D)
print("Boyut : ", array2D.shape)
print("2.satır 4.sütun : ", array2D[1, 3])


