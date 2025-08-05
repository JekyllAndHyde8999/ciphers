from typing import Sequence

from ..base import Cipher
from ..exceptions import InvalidPairings


class Vatsyayana(Cipher):
    def __init__(self, pairings: Sequence[tuple[str, str]]) -> None:
        super().__init__()

        is_valid, error_message = self.validate_pairings(pairings)
        if not is_valid:
            raise InvalidPairings(error_message.value)

        reverse_pairings = {val: key for key, val in pairings}
        self.pairings = {**dict(pairings), **reverse_pairings}

    def validate_pairings(
        self, pairings: Sequence[tuple[str, str]]
    ) -> tuple[bool, InvalidPairings.ErrorCategory]:
        seen = set()

        for pair in pairings:
            if not isinstance(pair, (list, tuple)) or len(pair) != 2:
                return False, InvalidPairings.ErrorCategory.NOT_A_PAIR

            a, b = pair

            if a == b:
                # character cannnot be mapped to itself
                return False, InvalidPairings.ErrorCategory.SELF_PAIRING

            if a in seen or b in seen:
                # characters cannot be repeated in pairings
                return False, InvalidPairings.ErrorCategory.REPEATED_CHARS

            seen.update([a, b])

        # all characters must be used
        remaining_chars = set(self.letters) - seen
        if len(remaining_chars):  # if there are characters left
            return False, InvalidPairings.ErrorCategory.NOT_ALL_CHARS_PAIRED
        else:
            return True, InvalidPairings.ErrorCategory.NO_ERROR

    def encode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        out = []

        for char in message_wo_puncts:
            out.append(self.pairings[char])

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)

    def decode(self, message: str) -> str:
        message_wo_puncts, puncts = self.separate(message)
        out = []

        for char in message_wo_puncts:
            out.append(self.pairings[char])

        for punct, index in puncts:
            out.insert(index, punct)

        return "".join(out)
