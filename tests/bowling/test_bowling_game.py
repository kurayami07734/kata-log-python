from src.bowling.main import Game


def test_game_has_10_frames():
    game = Game()

    assert game.frame_count == 10
