sample_space = {'Heads','Tails'}
probaility_heads = 1 / len(sample_space)
print()

# an event is the subset of those elements within the sample
# that satisfy some event condition.
# an event condition is a simple boolean function whose input 
# is a single Boolean function whose input is a single element in 
# the sample.

# defining event conditions
def is_heads_or_tails(outcome): return outcome in { 'Heads', 'Tails'}
def is_neither(outcome): return not is_heads_or_tails(outcome)

# defining additional event conditions
def is_heads(outcome): return outcome == 'Heads'
def is_tails(outcome): return outcome == 'Tails'

# defining an event-detection function
def get_matching_event (event_condition, sample_space):
    return set([outcome for outcome in sample_space if event_condition(outcome)])

event_conditions = [is_heads_or_tails, is_heads, is_tails, is_neither]

for event_condition in event_conditions:
    print(f"Event Condition: {event_condition.__name__}")
    event = get_matching_event(event_condition, sample_space)
    print(f'Event: {event}\n')

'''
Event Condition: is_heads_or_tails
Event: {'Tails', 'Heads'}

Event Condition: is_heads
Event: {'Heads'}

Event Condition: is_tails
Event: {'Tails'}

Event Condition: is_neither
Event: set()
'''

# Computing Event probabilities
def compute_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    return len(event) / len(generic_sample_space)

for event_condition in event_conditions:
    prob = compute_probability(event_condition, sample_space)
    name = event_condition.__name__
    print(f"Probability of event arising from '{name}' is {prob}")


# 1.1.1 Analyzing a Biased Coin

# representing a weighted sample space
weighted_sample_space = {'Heads':4, 'Tails':1}

# check the weighted sample space size
sample_space_size = sum(weighted_sample_space.values())
assert sample_space_size == 5

# checking the weighted event size
event = get_matching_event(is_heads_or_tails, weighted_sample_space)
event_size = sum(weighted_sample_space[outcome] for outcome in event)
assert event_size == 5

# defining a generalized event probability function
def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()): # checks whether generic_event_space is set
        return len(event) / len(generic_sample_space)
    
    event

# 1.1.1 Analyzing a biased coin

# representing a weighted sample space
weighted_sample_space = {'Heads':4, 'Tails':1}

# check the weighted sample space size
sample_space_size = sum(weighted_sample_space.values())
assert sample_space_size == 5

# checking the weighted event size
event = get_matching_event(is_heads_or_tails, weighted_sample_space)
# the above function iterates over each outcome in the inputted sample space
# thus it works as expected as Pything iterates over dictionary keys, not ke-value pairs
# as in many other popular programming languages
event_size = sum(weighted_sample_space[outcome] for outcome in event)
assert event_size == 5

# our generalized definition of sample space size and event size
# permit us to create compute_event_probability function. This function 
# takes as input a generic_sample_space variable that can be either 
# a weighted dictionary or an unwheighted set

def compute_event_probability(event_condition, generic_sample_space):
    event = get_matching_event(event_condition, generic_sample_space)
    if type(generic_sample_space) == type(set()): # checks whether generic_event_space is a set
        return len(event) / len(generic_sample_space)
    
    event_size = sum(generic_sample_space[outcome] for outcome in event)
    return event_size / sum(generic_sample_space.values())

for event_condition in event_conditions:
    prob = compute_event_probability(event_condition, weighted_sample_space)
    name = event_condition.__name__
    print(f"Probabiliy of event arising from '{name}' is {prob}")



# 1.2 Computing nontrivail probabilities

#  analyzing a family of 4 children
possible_children = ['Boy', 'Girl']
sample_space = set()
for child1 in possible_children:
    for child2 in possible_children:
        for child3 in possible_children:
            for child4 in possible_children:
                # each possible sequence of 4 children is represented by a 4-element tuple
                outcome = (child1, child2, child3, child4)
                sample_space.add(outcome)

# an alternative to this code above can be made more efficient by
# using the tertools.product function
from itertools import product
all_combinations = product(*(4 * [possible_children]))
#print(set(all_combinations)) #  this makes some kind of change on the variable all_combinations
assert set(all_combinations) == sample_space
sample_space_efficient = set(product(possible_children, repeat=4))
assert sample_space == sample_space_efficient

# compute the probability of 2 boys
def has_two_boys(outcome): return len([child for child in outcome if child == 'Boy']) == 2
prob = compute_event_probability(has_two_boys, sample_space)
print(f"Probability of 2 boys is {prob}")


# Problem 2 : Analyzing multiple die rolls
# suppose we have a fair six sided die whose faces are numbered
# 1 to 6. The die is rolled size times. What is the probability that 
# these six die rolls add up to 21?

# we begin by defining the possible valies of any single roll. 
possible_rolls = list(range(1,7))
print(possible_rolls)

# next we create a sample space for six consecutive rolls using the product function
sample_space = set(product(possible_rolls, repeat=6))

# define has_sum_of_21 event condition that we'll subsequentnly pass into compute_event_probability
def has_sum_of_21(outcome): return sum(outcome) == 21
prob = compute_event_probability(has_sum_of_21, sample_space)
# conceptually rolling a singe die six times is equivalent to rolling six dice simulataneously
print(f"6 rolls sum to 21 with a probability if {prob}")

# Lambda expressions allow us to define short functions in a single line of code
# coding lambda x: is functionally equivalent to coding func(x):
# this, lambda x: sum(x) == 21 us functionally equivalent to has_sum_of_21
prob = compute_event_probability(lambda x: sum(x) == 21, sample_space)
assert prob == compute_event_probability(has_sum_of_21, sample_space)

# 1.2.3 Computing die-roll probabilities using weighted sample spaces

from collections import defaultdict
weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    total = sum(outcome)
    weighted_sample_space[total] +=1

assert weighted_sample_space[6] == 1
assert weighted_sample_space[36] == 1

num_combinations = weighted_sample_space[21]
print(f"There are {num_combinations} ways for 6 die rolls to sum 21")

# exploring different ways of summing 21
assert sum([4, 4, 4, 4, 3, 2]) == 21
assert sum([4, 4, 4, 5, 3, 1]) == 21

event = get_matching_event(lambda x: sum(x) == 21, sample_space)
assert weighted_sample_space[21] == len(event)
assert sum(weighted_sample_space.values()) == len(sample_space)
prob = compute_event_probability(lambda x: x == 21, weighted_sample_space)
assert prob == compute_event_probability(has_sum_of_21, sample_space)
print(f"6 rolls sum to 21 with a probability of {prob}")
print('Number of Elements in Unweighted Sample Space:')
print(len(sample_space))
print('Number of Elements in Weighted Sample Space:')
print(len(weighted_sample_space))

# 1.3 computing probabilities over interval ranges

# define a closed interval in which the min/max boundaries
# are included, however it's also possible to define open 
# intervals when needed. In open intervals, at least one 
# boudary is excluded
def is_in_interval(number, minimum, maximum):
    return minimum <= number <= maximum

# lambda function takes input x ad returns True if
# x falls in an interval between 10 and 21
# this one line lambda function servers as our event condition
prob = compute_event_probability(lambda x: is_in_interval(x, 10, 21), weighted_sample_space)
print(f"Probability of interval is {prob}")

# Probability of interval is 0.5446244855967078
# the six die rolls will fall between that interval range more than
# 54% of the time. Thus if a roll sum of 13 or 20 comes up, we should not be surprised

# Interval analysis is critical to solving a whole class of very important problems in 
# probability and statistics. One such problem involves the evaluation of extremes: 
# the problem boils down to whether observed data is too extreme to be believable

# computing the sample space of 10 coin flips
def generate_coin_sample_space(num_flips=10):
    weighted_sample_space = defaultdict(int)
    for coin_flips in product(['Heads','Tails'], repeat=num_flips):
        heads_count = len([outcome for outcome in coin_flips if outcome =='Heads'])
        weighted_sample_space[heads_count] +=1
    return weighted_sample_space

weighted_sample_space = generate_coin_sample_space()
assert weighted_sample_space[10] == 1
assert weighted_sample_space[9] == 10

# compute an extreme head-count probability
prob = compute_event_probability(lambda x: is_in_interval(x, 8, 10), weighted_sample_space)
print(f"Probability of observing more than 7 heads is {prob}")
# Probability of observing more than 7 heads is 0.0546875

# computing an extreme interval probability
prob = compute_event_probability(lambda x: not is_in_interval(x, 3, 7), weighted_sample_space)
print(f"Probability of observing more than 7 heads or 7 tails is {prob}")
# Probability of observing more than 7 heads or 7 tails is 0.109375

# analyzing extreme head count for 20 fair coin flips
weighted_sample_space_20_flips = generate_coin_sample_space(num_flips=20)
prob = compute_event_probability(lambda x: not is_in_interval(x, 5, 15), weighted_sample_space_20_flips)
print(f"Probability of observing more than 15 heads or 15 tails is {prob}")
# Probability of observing more than 15 heads or 15 tails is 0.01181793212890625
