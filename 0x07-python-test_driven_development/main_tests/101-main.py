#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print('\n')
print(lazy_matrix_mul([[1, 2]], [[3, 4], [5, 'k']]))
#print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4], [5, 6]]))
print(lazy_matrix_mul([],[]))
#print(lazy_matrix_mul([[]],[[]]))
