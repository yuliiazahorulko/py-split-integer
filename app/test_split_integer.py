from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    assert 32 == sum(split_integer(32, 6))


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    temp = split_integer(20, 20)
    assert all([i == temp[0] for i in temp])


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert 32 == split_integer(32, 1)[0]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    assert split_integer(122, 6)[0] == split_integer(122, 6)[-1] - 1


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(1, 3) == [0, 0, 1]
