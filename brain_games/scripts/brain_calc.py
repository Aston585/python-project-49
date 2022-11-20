#!/usr/bin/env python3

import brain_games.engin
from brain_games.games.calc import rules, question, correct_answer


def main():
    brain_games.engin.game_engin(rules, question, correct_answer)


if __name__ == '__main__':
    main()
