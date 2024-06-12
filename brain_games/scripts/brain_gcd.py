#!/usr/bin/env python3

from brain_games.games.gcd import big_del
from brain_games.tools.engine import generate_game_data


def main():
    generate_game_data(big_del)


if __name__ == "__main__":
    main()
