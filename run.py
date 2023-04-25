from airplane import Airplane
from simulation import Simulation
from queues import Steffen
from functools import partial

ROWS = 30
SEATS_PER_ROW = 6
NUMBER_OF_PASSENGERS = 167

airplane = Airplane(number_of_rows = ROWS, seats_per_row = SEATS_PER_ROW,
                    total_passengers = NUMBER_OF_PASSENGERS)
sim = Simulation(airplane, partial(Steffen, perfect = True), max_iter = 1000)
results = sim.run()
print(results)