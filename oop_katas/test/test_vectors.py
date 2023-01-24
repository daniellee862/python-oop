from oop_katas.src.vectors import Vector


vector_one = Vector([1, 2, 3])
vector_two = Vector([2, 3, 4])


def test_vector_add_method_returns_sum_off_two_vectors():
    sample_vector = Vector([3, 5, 7])
    created_vector = vector_one.add(vector_two)

    assert sample_vector == created_vector


def test_vector_subtract_methods_returns_subtraction_of_two_vectors():
    sample_vector = Vector([-1, -1, -1])
    created_vector = vector_one.subtract(vector_two)
    assert sample_vector == created_vector


def test_multiply_and_sum():
    result = 20
    expected = vector_one.multiply_and_sum(vector_two)
    assert expected == result


'''multipy Should return a new Vector
list_one = Vector([1,2,3])
list_two = Vector([2,3,4])
list_one.dot(list_two) # Should return (1*2 + 2*3 + 3*4) = 20'''
