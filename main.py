from collections import Counter, OrderedDict


class Names:
    @staticmethod
    def unique_names(first_list: list, second_list: list) -> list:
        return list(set(([*first_list, *second_list])))


def group_by_owners(files: dict) -> dict:
    result = {}
    for file, owner in files.items():
        result[owner] = result.get(owner, []) + [file]
    return result


class LeagueTable:
    def __init__(self, gamers: list):
        self.standings = OrderedDict([(gamer, Counter()) for gamer in gamers])

    def record_result(self, gamer: str, score: int):
        self.standings[gamer]['games_counter'] += 1
        self.standings[gamer]['score'] += score

    def player_rank(self, result: int) -> str:
        return sorted(self.standings, key=lambda p: (-self.standings[p]['score'], self.standings[p]['games_counter']))[result-1]
