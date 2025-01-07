from dataclasses import dataclass
from enum import Enum
from typing import List


class Color(Enum):
    GREEN = 1
    RED = 2
    YELLOW = 3
    BLUE = 4
    WHITE = 5
    BLACK = 6

class AnswerColor(Enum):
    WHITE = 1
    BLACK = 2

@dataclass
class Mastermind:
    answer: List[Color]

    def get_black_indices(self, pegs: List[Color]) -> List[AnswerColor]:
        answer_indices = list()
        for index, peg in enumerate(pegs):
            if peg == self.answer[index]:
                answer_indices.append(index)
        return answer_indices

    def get_white_indices(self, black_indices, pegs):
        white_indices = list()

        filtered_answer = [peg for index, peg in enumerate(self.answer) if index not in black_indices ]

        for index in range(4):
            if index not in black_indices and pegs[index] in filtered_answer:
                white_indices.append(index)
                index_to_remove = filtered_answer.index(pegs[index])
                filtered_answer.pop(index_to_remove)
        return white_indices


    def guess(self, pegs: List[Color]) -> List[AnswerColor]:
        black_indices = self.get_black_indices(pegs)
        white_indices = self.get_white_indices(black_indices, pegs)

        guess_result = []

        for i in range(4):
            if i in black_indices:
                guess_result.append(AnswerColor.BLACK)
            elif i in white_indices:
                guess_result.append(AnswerColor.WHITE)
            else:
                guess_result.append(None)

        print(guess_result)
        return guess_result




m = Mastermind(answer=[Color.RED, Color.RED, Color.RED, Color.RED])
assert m.guess([Color.RED, Color.RED, Color.RED, Color.RED]) == [AnswerColor.BLACK,
                                                                 AnswerColor.BLACK,
                                                                 AnswerColor.BLACK,
                                                                 AnswerColor.BLACK]



assert m.guess([Color.GREEN, Color.RED, Color.GREEN, Color.RED]) == [None,
                                                                 AnswerColor.BLACK,
                                                                 None,
                                                                 AnswerColor.BLACK]


m = Mastermind(answer=[Color.RED, Color.GREEN, Color.BLUE, Color.BLUE])
assert m.guess([Color.BLUE, Color.BLUE, Color.GREEN, Color.GREEN]) == [AnswerColor.WHITE,
                                                                 AnswerColor.WHITE,
                                                                 AnswerColor.WHITE,
                                                                 None]

assert m.guess([Color.RED, Color.BLUE, Color.GREEN, Color.GREEN]) == [AnswerColor.BLACK,
                                                                 AnswerColor.WHITE,
                                                                 AnswerColor.WHITE,
                                                                 None]

assert m.guess([Color.YELLOW, Color.YELLOW, Color.YELLOW, Color.YELLOW]) == [None,
                                                                 None,
                                                                 None,
                                                                 None]



