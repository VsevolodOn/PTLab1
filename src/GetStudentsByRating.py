from typing import Dict, List
from Types import DataType

RatingType = Dict[str, float]
StudentType = List[str]


class GetStudentsByRating():

    def __init__(self, data: DataType) -> None:
        self.rating: DataType = data
        self.did: StudentType = []

    def getStudents(self):
        return 0
