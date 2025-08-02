from enum import Enum


class InvalidDeterminant(ValueError):
    pass


class InvalidParameter(ValueError):
    pass


class InvalidCharacter(ValueError):
    pass


class InvalidPairings(ValueError):
    pass


class ErrorCategory(Enum):
    SELF_PAIRING = "character mapped to itself"
    REPEATED_CHARS = "characters used more than once"
    NOT_ALL_CHARS_PAIRED = "not all characters have a corresponding pair"
    NOT_A_PAIR = "found sequence that is not a pair"
    NO_ERROR = "valid pairings"
