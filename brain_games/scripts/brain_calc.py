#!/usr/bin/env python3

import brain_games.games.calc
from brain_games.tools.engine import generate_game_data


def main():
    generate_game_data(brain_games.games.calc)


if __name__ == "__main__":
    main()
