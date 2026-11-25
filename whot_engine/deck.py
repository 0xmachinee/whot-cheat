"""The Whot deck. A card is a tuple: (shape, number), ("circle", 5)."""

from collections import Counter

# Number each shape has in a standard Nigerian Whot deck
SHAPES = {
    "circles":      [1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14],
    "triangles":    [1, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14],
    "crosses":      [1, 2, 3, 5, 7, 10, 11, 13, 14],
    "squares":      [1, 2, 3, 5, 7, 10, 11, 13, 14],
    "stars":        [1, 2, 3, 4, 5, 7, 8],
}

WHOT_SHAPE = "whot"
WHOT_NUMBER = 20
WHOT_COPIES = 5
DECK_SIZE = 54

# Order of shapes in menus (Whot last)
SHAPE_MENU = list(SHAPES) + [WHOT_SHAPE]

def build_deck():
    """Return a Counter of the full 54-card deck, with each card as a tuple (shape, number)."""
    deck = Counter()
    for shape, numbers in SHAPES.items():
        for number in numbers:
            deck[(shape, number)] += 1
    deck[(WHOT_SHAPE, WHOT_NUMBER)] += WHOT_COPIES
    return deck
