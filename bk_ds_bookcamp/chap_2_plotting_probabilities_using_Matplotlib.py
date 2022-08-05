import matplotlib.pyplot as plt

from chap_1_computing_probabilities_using_python import get_matching_event, compute_event_probability, is_in_interval, weighted_sample_space
from chap_1_computing_probabilities_using_python import generate_coin_sample_space



# plotting a linear relationship
x = range(0, 10)
y = [ 2 * value for value in x]

# plot linear relationship
# plt.plot(x, y)

# plot individual data points
# plt.scatter(x, y)


# shading an interval beneath a connected plot
plt.plot(x, y)
where = [is_in_interval(value, 2, 6) for value in x]
plt.fill_between(x, y, where = where)


# adding axis and labels
plt.xlabel('Values between {} and {}'. format(0, 10))
plt.ylabel('Twice the values of x')
plt.show()


# plotting the coin-flip weighted sample space
x_10_flips = list(weighted_sample_space.keys())
y_10_flips = [weighted_sample_space[key] for key in x_10_flips]
plt.scatter(x_10_flips, y_10_flips)
plt.xlabel('Head-cound')
plt.ylabel('Number of coin-flip combinations with x heads')
plt.show()


# plotting the coin-flip porbabilities
sample_space_size = sum(weighted_sample_space.values())
prob_x_10_flips = [value / sample_space_size for value in y_10_flips]
plt.scatter(x_10_flips, prob_x_10_flips)
plt.xlabel('Head-count')
plt.ylabel('Probability')
plt.show()

# the total area below the probability distribution is 1.0
# this holds for any distribution, including our head-count plot
assert sum(prob_x_10_flips) == 1.0

# shading the interval under the probalility curve
plt.plot(x_10_flips, prob_x_10_flips)
plt.scatter(x_10_flips, prob_x_10_flips)
where = [is_in_interval(value, 8, 19) for value in x_10_flips]
plt.fill_between(x_10_flips, prob_x_10_flips, where=where)
plt.xlabel('Head-count')
plt.ylabel('Probability')
plt.show()

# shading the interval under the extremes of a probability curve
plt.plot(x_10_flips, prob_x_10_flips)
plt.scatter(x_10_flips, prob_x_10_flips)
where = [not is_in_interval(value, 3, 7) for value in x_10_flips]
plt.fill_between(x_10_flips, prob_x_10_flips, where = where)
plt.xlabel('Head-count')
plt.ylabel('Probability')
plt.show()

# comparing multiple con-flip probability distributions
# computing probabilities for a 20 coin flip distribution
weighted_sample_space_20_flips = generate_coin_sample_space(20)
x_20_flips = list(weighted_sample_space_20_flips.keys())
y_20_flips = [weighted_sample_space_20_flips[key] for key in x_20_flips]
sample_space_size = sum(weighted_sample_space_20_flips.values())
prob_x_20_flips = [value / sample_space_size for value in y_20_flips]


# ploting 2 simultaneous distributions
plt.plot(x_10_flips, prob_x_10_flips, label='A: 10 coin-flips')
plt.scatter(x_10_flips, prob_x_10_flips)
plt.plot(x_20_flips, prob_x_20_flips, color='black', linestyle='--', label='B: 20 coin-flips')
plt.scatter(x_20_flips, prob_x_20_flips, color='k', marker='x')
plt.xlabel('Head-count')
plt.ylabel('Probability')
plt.legend()
plt.show()


# highlighting intervals beneath two plotted distributions
plt.plot(x_10_flips, prob_x_10_flips, label='A: 10 coin-flips')
plt.plot(x_20_flips, prob_x_20_flips, color='k', linestyle=':', label='B: 20 coin-flips')

where_10 = [not is_in_interval(value, 3, 7) for value in x_10_flips]
plt.fill_between(x_10_flips, prob_x_10_flips, where=where_10)
where_20 = [not is_in_interval(value, 5, 15) for value in x_20_flips]
plt.fill_between(x_20_flips, prob_x_20_flips, where=where_20)

plt.xlabel('Head-count')
plt.ylabel('Probability')
plt.legend()
plt.show()

