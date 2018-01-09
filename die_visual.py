import pygal
from die import Die 

die = Die()

results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

frequencies = []
sides = []
for value in range(1, die.sides+1):
	sides.append(value)
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = sides
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')