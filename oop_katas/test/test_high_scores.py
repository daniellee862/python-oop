from oop_katas.src.high_scores import HighScores

# Creat instance of highschool and define limit
first_high_scores = HighScores(3)


def test_for_score_property():
    assert first_high_scores.score_list == []  # Should return True


def test_for_limit_property():
    expected = 3
    result = first_high_scores.limit
    assert result == expected


def test_score_is_added():
    expected = [{"name": "daniel", "score": 10}]
    result = first_high_scores.update_list("daniel", 10)
    assert result == expected


def test_multiple_scores_added():
    expected = [{"name": "rachel", "score": 15},
                {"name": "daniel", "score": 10},
                ]
    result = first_high_scores.update_list("rachel", 15)
    assert result == expected


def test_three_scores_added():
    expected = [{"name": "rachel", "score": 15},
                {"name": "daniel", "score": 10},
                {"name": "timmy", "score": 5}]
    result = first_high_scores.update_list("timmy", 5)

    assert result == expected


def test_if_limit_has_been_reached_if_score_is_higher_add_score():
    expected = [{"name": "rachel", "score": 15},
                {"name": "daniel", "score": 10},
                {"name": "barley", "score": 8}]
    result = (first_high_scores.update_list("barley", 8))

    assert result == expected


def test_if_limit_has_been_reached_and_score_is_lower_and_not_added():
    expected = [{"name": "rachel", "score": 15},
                {"name": "daniel", "score": 10},
                {"name": "barley", "score": 8}]
    result = (first_high_scores.update_list("bill", 3))

    assert result == expected


def test_average_score_value():
    expected = 11
    result = first_high_scores.average_score()
    assert result == expected


def test_highest_scorer_name_is_returned():
    expected = "rachel"
    result = first_high_scores.highest_scorer()
    assert expected == result


def test_lowest_scorer_name_is_returned():
    expect = "barley"
    result = first_high_scores.lowest_scorer()
    assert expect == result


def test_scores_table_is_resest():
    expect = []
    result = first_high_scores.reset()
    assert expect == result
