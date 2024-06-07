#!/usr/bin/env python3

from brain_games.games.even import del_of_two1
from brain_games.tools.data import generate_game_data
from brain_games.tools.round_tools import RULES


def main():
    generate_game_data(del_of_two1, RULES["even"])


if __name__ == "__main__":
    main()
