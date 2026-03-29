from src.bowling.frame import Frame, FrameConcludedException


class GameConcludedException(Exception):
    """
    Indicates that game has concluded
    """


class Game:
    def __init__(self) -> None:
        self.frames: list[Frame] = [Frame(is_last_frame=(i == 9)) for i in range(10)]
        self.current_frame = 0

    @property
    def frame_count(self):
        return len(self.frames)

    def roll(self, pin_count: int) -> None:
        if self.current_frame > 9:
            raise GameConcludedException()

        frame = self.frames[self.current_frame]

        try:
            frame.roll(pin_count)
        except FrameConcludedException:
            self.current_frame += 1
            self.roll(pin_count)

    def score(self) -> int:
        return sum(f.score() for f in self.frames)
