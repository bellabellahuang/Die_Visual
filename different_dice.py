import pygal
from die import Die 

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []
sums = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result+1):
	sums.append(value)
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = sums
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('D6_D10_visual.svg')