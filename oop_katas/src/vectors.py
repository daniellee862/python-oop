import numpy as np


class Vector:
    def __init__(self, list_int, ):
        self.list_int = list_int

    def __eq__(self, otherVector):
        if isinstance(otherVector, Vector):
            if otherVector.list_int == self.list_int:
                return True
        return False

    def add(self, class_to_add):
        list_one = self.list_int
        list_two = class_to_add.list_int

        sum_of_lists = [list_one[i] + list_two[i]
                        for i in range(len(list_one))]
        return Vector(sum_of_lists)

    def subtract(self, class_to_subract):
        list_one = self.list_int
        list_two = class_to_subract.list_int

        lists_subtracted = [list_one[i] - list_two[i]
                            for i in range(len(list_one))]
        return Vector(lists_subtracted)

    def multiply_and_sum(self, class_to_mutltiply):
        list_one = self.list_int
        list_two = class_to_mutltiply.list_int
        result = np.dot(list_one, list_two)
        return result
