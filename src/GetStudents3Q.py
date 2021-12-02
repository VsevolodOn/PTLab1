import numpy as np
from typing import Dict, List

RatingType = Dict[str, float]


class GetStudents3Q():

    def __init__(self, rating: RatingType) -> None:
        self.rating: RatingType = rating
        self.studetsq3: RatingType = {}

    def get(self) -> RatingType:
        rating_list = list(self.rating.values())
        third_quartile = np.quantile(rating_list, 0.75)
        median = np.quantile(rating_list, 0.5)
        for key in self.rating:
            if median <= self.rating[key] <= third_quartile:
                self.studetsq3[key] = float(self.rating[key])
        return self.studetsq3
