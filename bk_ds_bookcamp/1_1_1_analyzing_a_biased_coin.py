# representing a weighted sample space
weighted_sample_space = {'Heads':4, 'Tails':1}

# check the weighted sample space size
sample_space_size = sum(weighted_sample_space.value())
assert sample_space_size == 5

# checking the weighted event size
event = get_matching_event()