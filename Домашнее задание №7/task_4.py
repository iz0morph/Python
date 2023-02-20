class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(i,' ', end='')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + \
                                       other.my_list[i][i_2]
        return self


m = Matrix([[5, 2, 1], [4, -10, 1], [0, 2, -1]])
new_m = Matrix([[-5, -2, -1], [-6, 8, 2], [3, 5, -2]])
print(m)
print(new_m)
print(m + new_m)
