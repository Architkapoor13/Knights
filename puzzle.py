from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # game logic
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # Puzzle 0 logic
    Implication(AKnight, And(AKnight, AKnave)), # if A is Knight then the what A says must be correct!
    Implication(AKnave, Not(And(AKnight, AKnave))) # if A is Knave then the what A says must not be correct!
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # game logic
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # puzzle 1 logic
    Implication(AKnave, Not(And(AKnave, BKnave))),
    Implication(AKnight, And(AKnave, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
Asays = And(Biconditional(AKnight, BKnight), Biconditional(AKnave, BKnave))
Bsays = And(Biconditional(AKnight, BKnave), Biconditional(AKnave, BKnight))
knowledge2 = And(
    # game logic
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # puzzle 2 logic
    Implication(AKnight, Asays),
    Implication(AKnave, Not(Asays)),
    Implication(BKnight, Bsays),
    Implication(BKnave, Not(Bsays))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
Asays3 = And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))
Bsays3 = And(AKnave, CKnave)
Csays3 = AKnight
knowledge3 = And(
    # game logic
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # puzzle 3 logic
    Implication(AKnight, Asays3),
    Implication(AKnave, Not(Asays3)),
    Implication(CKnight, Csays3),
    Implication(CKnave, Not(Csays3)),
    Implication(BKnight, Bsays3),
    Implication(BKnave, Not(Bsays3))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
