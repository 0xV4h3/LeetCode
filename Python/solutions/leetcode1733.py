# 1733. Minimum Number of People to Teach
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]

        problem_users = set()
        for u, v in friendships:
            if langs[u - 1].isdisjoint(langs[v - 1]):
                problem_users.add(u)
                problem_users.add(v)

        if not problem_users:
            return 0

        known_count = [0] * (n + 1)
        for user in problem_users:
            for lang in langs[user - 1]:
                known_count[lang] += 1

        return len(problem_users) - max(known_count)

        # problem_users = set()
        # for friends in friendships:
        #     u = friends[0]
        #     v = friends[1]
        #     if not (set(languages[u - 1]) & set(languages[v - 1])):
        #         problem_users.add(u)
        #         problem_users.add(v)
        #
        # if not problem_users:
        #     return 0
        #
        # lang_count = [0] * n
        #
        # for lang in range(1, n + 1):
        #     for user in problem_users:
        #         if lang not in languages[user - 1]:
        #             lang_count[lang - 1] += 1
        #
        # return min(lang_count)

if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]))  # 1
    print(sol.minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]))  # 2