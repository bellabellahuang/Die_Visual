import pygal
from die import Die 

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(5000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

frequencies = []
sums = []
max_result = die_1.sides + die_2.sides + die_3.sides
for value in range(3, max_result+1):
	sums.append(value)
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 5,000 times."
hist.x_labels = sums
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('3 * D6', frequencies)
hist.render_to_file('three_D6_visual.svg')