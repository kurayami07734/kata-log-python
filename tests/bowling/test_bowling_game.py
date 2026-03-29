import pytest

from src.bowling.main import Game, GameConcludedException


def test_game_has_10_frames():
    game = Game()

    assert game.frame_count == 10


def test_game_scenario():
    game = Game()

    # Frame 1
    game.roll(10)
    game.roll(10)
    game.roll(2)

    assert game.score() == 22

    # Frame 2
    game.roll(8)
    game.roll(2)

    assert game.score() == 32

    # Frame 3
    game.roll(7)
    game.roll(3)

    assert game.score() == 42

    # Frame 4
    game.roll(5)
    game.roll(5)

    assert game.score() == 52

    # Frame 5
    game.roll(7)
    game.roll(3)

    assert game.score() == 62

    # Frame 6
    game.roll(7)
    game.roll(3)

    assert game.score() == 72
    # Frame 7
    game.roll(7)
    game.roll(3)

    assert game.score() == 82
    # Frame 8
    game.roll(7)
    game.roll(3)

    assert game.score() == 92
    # Frame 9
    game.roll(7)
    game.roll(3)

    assert game.score() == 102

    # Frame 10
    game.roll(7)
    game.roll(3)

    assert game.score() == 112

    with pytest.raises(GameConcludedException):
        game.roll(7)
