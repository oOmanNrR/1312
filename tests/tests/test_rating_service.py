# tests/test_rating_service.py

import pytest
from services import RatingService


def test_calculate_average_rating():
    ratings = [1, 3, 5, 5, 2]
    service = RatingService()
    result = service.calculate_average(ratings)
    assert result == 3.2


def test_average_with_single_rating():
    service = RatingService()
    assert service.calculate_average([4]) == 4.0


def test_average_with_all_same_values():
    service = RatingService()
    assert service.calculate_average([5, 5, 5]) == 5.0


def test_average_with_empty_list():
    service = RatingService()
    with pytest.raises(ValueError, match="Cannot calculate average of an empty list"):
        service.calculate_average([])


def test_average_with_invalid_rating_values():
    service = RatingService()
    # Допустим, рейтинг должен быть от 1 до 5
    with pytest.raises(ValueError, match="Invalid rating value"):
        service.calculate_average([1, 6])  # 6 — недопустимо

    with pytest.raises(ValueError, match="Invalid rating value"):
        service.calculate_average([0, 3])  # 0 — недопустимо

    with pytest.raises(ValueError, match="Invalid rating value"):
        service.calculate_average([1, -2])