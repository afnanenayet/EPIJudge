from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    """ Given a final score, and a list of valid point values, figure out the
    total number of combinations that lead to the final score using any
    combination of the aforementioned point values.

    This approach using dynamic programming to yield valid point values.
    Each row of the DP table corresponds to a series of valid point values.
    For example, if we have a set of point values (2, 3, 7), then the first
    row will correspond to only 2, the second row (2, 3), and so on.

    The column corresponds to the final score. Thus dp[1][12] corresponds to
    the total number of ways you can yield the score 12 using the points (2, 3).

    We define the solution as the answer to the subproblem: how many ways can
    we generate the final score excluding the current valid point + how many
    ways can we generate the final score using this method for the final score
    minus the current point value.

    We iteratively construct the DP table with nested for loops.

    Complexity:
        - runtime: O(sn) where s is the final score and n is the number of
          individual scores
        - space: O(sn)
    """
    # construct the dp array
    # dp[1][12] is the number of ways the score 12 can be generated with 2
    # (1 + 1) score combinations
    dp = [[1] + [0] * final_score] * len(individual_play_scores)
    individual_play_scores = sorted(individual_play_scores)

    for i, points in enumerate(individual_play_scores):
        for index in range(1, final_score + 1):
            ways = 0

            if i >= 1:
                ways += dp[i - 1][index]

            if index - points >= 0:
                ways += dp[i][index - points]
            dp[i][index] = ways
    return dp[-1][-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )
