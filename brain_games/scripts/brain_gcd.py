#!/usr/bin/env python3

from brain_games.games.gcd import big_del1
from brain_games.tools.data import generate_game_data
from brain_games.tools.round_tools import RULES


def main():
    generate_game_data(big_del1, RULES["gcd"])


if __name__ == "__main__":
    main()
