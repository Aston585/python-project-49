#!/usr/bin/env python3

import brain_games.engin
from brain_games.games.calc import rules, game


def main():
    brain_games.engin.game_engin(rules, game)


if __name__ == '__main__':
    main()
