from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    w = [[1] + ([0] * final_score)] * len(individual_play_scores)

    for i, play_score in enumerate(individual_play_scores):
        for j in range(1, final_score + 1):
            with_play, without_play = 0, 0

            if j - play_score >= 0:
                with_play = w[i][j - play_score]

            if i > 0:
                without_play = w[i - 1][j]
            w[i][j] = with_play + without_play
    return w[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
