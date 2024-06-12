#!/usr/bin/env python3

from brain_games.games.calc import calc
from brain_games.tools.engine import generate_game_data


def main():
    generate_game_data(calc)


if __name__ == "__main__":
    main()
