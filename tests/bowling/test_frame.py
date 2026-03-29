import pytest

from src.bowling.frame import Frame


def test_frame_has_2_rolls():
    frame = Frame()

    assert frame.roll_count == 2


def test_frame_stops_rolls():
    frame = Frame()

    frame.roll(8)
    frame.roll(2)

    with pytest.raises(FrameConcludedException):
        frame.roll(1)


def test_frame_allows_spares():
    frame = Frame()

    frame.roll(10)
    frame.roll(10)
    frame.roll(10)
    frame.roll(8)


def test_last_frame_allows_max_3_rolls():
    frame = Frame(is_last_frame=True)

    frame.roll(10)
    frame.roll(10)
    frame.roll(10)

    with pytest.raises(FrameConcludedException):
        frame.roll(1)
