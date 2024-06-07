#!/usr/bin/env python3

from brain_games.games.calc import calco1
from brain_games.tools.data import generate_game_data
from brain_games.tools.round_tools import RULES


def main():
    generate_game_data(calco1, RULES["calc"])


if __name__ == "__main__":
    main()
