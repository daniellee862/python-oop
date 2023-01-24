from operator import itemgetter


class HighScores:
    score_list = []

    def __init__(self, limit):
        self.limit = limit

    def update_list(self, name, score):
        person_score = {}
        person_score["name"] = name
        person_score["score"] = score

        list_length = len(self.score_list)

        if list_length >= self.limit:
            if self.score_list[list_length - 1]["score"] < score:
                del self.score_list[list_length - 1]
                self.score_list.append(person_score)

        else:
            self.score_list.append(person_score)

        self.score_list.sort(
            key=itemgetter('score'), reverse=True)

        return self.score_list

    def average_score(self):
        return (sum(person['score'] for person in self.score_list)) / len(self.score_list)

    def highest_scorer(self):
        return self.score_list[0]["name"]

    def lowest_scorer(self):
        last_player_index = len(self.score_list) - 1
        return self.score_list[last_player_index]["name"]

    def reset(self):
        self.score_list = []
        return self.score_list
