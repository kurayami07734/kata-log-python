class FrameConcludedException(Exception):
    """
    Indicates that a frame has exhausted its rolls
    """


class Frame:
    def __init__(self, is_last_frame=False) -> None:
        self.is_last_frame = is_last_frame
        self.roll_count = 2
        self.rolls: list[int] = []

    def __grant_spares(self):
        has_all_tens = all(r == 10 for r in self.rolls)
        should_limit_rolls = len(self.rolls) > 2 and self.is_last_frame

        if has_all_tens and not should_limit_rolls:
            self.roll_count += 1

    def roll(self, pin_count: int) -> None:
        if pin_count < 0 or pin_count > 10:
            raise ValueError(f"Illegal pin_count passed ({pin_count})")

        if not self.roll_count:
            raise FrameConcludedException()

        self.rolls.append(pin_count)
        self.roll_count -= 1

        if not self.roll_count:
            self.__grant_spares()

    def score(self) -> int:
        return sum(self.rolls)
