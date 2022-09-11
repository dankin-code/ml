import numpy as np

# simulate random die roll
die_roll = np.random.randint(1, 7)
assert 1 <= die_roll <= 6

# seeding reproducible random die rolls
np.random.seed(0)
die_rolls = [np.random.randint(1, 7) for _ in range(3)]
assert die_rolls == [5, 6, 1]
