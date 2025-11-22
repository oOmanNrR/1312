from typing import List

class RatingService:

    MIN_RATING = 1
    MAX_RATING = 5
 
    def _validate_rating(self, rating: int) -> None:
        if not isinstance(rating, int):
            raise ValueError("Rating must be an integer")
        if not (self.MIN_RATING <= rating <= self.MAX_RATING):
            raise ValueError("Invalid rating value")

    def calculate_average(self, ratings: List[int]) -> float:
        if not ratings:
            raise ValueError("Cannot calculate average of an empty list")
        for r in ratings:
            self._validate_rating(r)
        return round(sum(ratings) / len(ratings), 1)