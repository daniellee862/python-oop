
# make sure to import your class
from oop_katas.src.build_a_northcoder import Northcoder

alex = Northcoder('Alex', 'Stockport', 'Software Engineering', 'March 2020')

def test_northcoder_has_name_assertion():
    expected = 'Alex'
    result = alex.name
    assert result == expected

def test_northcoder_has_location_assertion():
    expected = 'Stockport'
    result = alex.location
    assert result == expected

def test_northcoder_has_course_assertion():
    expected = 'Software Engineering'
    result = alex.course
    assert result == expected

def test_northcoder_has_graduation_assertion():
    expected = 'March 2020'
    result = alex.graduation_date
    assert result == expected

def test_northcoder_greet_method_returns_correct_string():
    expected = 'Hello Joe, my name is Alex'
    result = alex.greet('Joe')
    print(f'Result is: {result}')
    assert result == expected

def test_northcoder_greet_method_returns_a_string():
    result = alex.greet('Joe')
    print(f'Result is: {result}')
    assert isinstance(result, str)

def test_graduation_date_returns_true():
    expected = True
    result = alex.alumni() 
    assert result == expected