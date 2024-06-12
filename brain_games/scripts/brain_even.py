#!/usr/bin/env python3

from brain_games.games.even import del_of_two
from brain_games.tools.engine import generate_game_data


def main():
    generate_game_data(del_of_two)


if __name__ == "__main__":
    main()
