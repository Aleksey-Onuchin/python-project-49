#!/usr/bin/env python3

import brain_games.game_engine
import brain_games.games.game_calc


def main():
    brain_games.game_engine.main(brain_games.games.game_calc.calc,
                                 brain_games.games.game_calc.task)
