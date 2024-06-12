#!/usr/bin/env python3

from brain_games.games.progression import progress
from brain_games.tools.engine import generate_game_data


def main():
    generate_game_data(progress)


if __name__ == "__main__":
    main()
