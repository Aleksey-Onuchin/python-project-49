#!/usr/bin/env python3

import brain_games.game_engine
import brain_games.games.game_gcd


def main():
    brain_games.game_engine.main(brain_games.games.game_gcd.gcd,
                                 brain_games.games.game_gcd.task)
