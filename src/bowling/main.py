class Game:
    def __init__(self) -> None:
        self.frames = [[] for _ in range(10)]

    @property
    def frame_count(self):
        return len(self.frames)

    def roll(self, pin_count: int) -> None: ...

    def score(self) -> int: ...
