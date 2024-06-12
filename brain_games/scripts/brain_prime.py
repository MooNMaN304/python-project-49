#!/usr/bin/env python3

from brain_games.games.prime import prime
from brain_games.tools.engine import generate_game_data


def main():
    generate_game_data(prime)


if __name__ == "__main__":
    main()
