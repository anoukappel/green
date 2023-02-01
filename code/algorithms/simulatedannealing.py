import random
import math

from code.algorithms.hillclimber import HillClimber

class SimulatedAnnealing(HillClimber):
    """
    The simulated annealing class switches houses. When the new solution is valid,
    it checks what the new number of cables is. When it is less than before, the
    change will be accepted. When it is more than it was before, it will check
    if this change is acceptable for the time being. The model with the lowest
    value will be saved.
    """
    def __init__(self, model, temperature=1, raise_temp=5, iterations_without_change=100):
        super().__init__(model)
        self.raise_temp = raise_temp
        self.model_temp = model
        self.t_now = temperature
        self.values = []
        self.counter = 0
        self.new_value = 0
        self.old_value = len(self.model_temp.cables)
        self.lowest_value = 100000
        self.best_model = None
        self.max_acceptable_value = 100000
        self.temps = []
        self.iterations_without_change = iterations_without_change

        # extra variable which was used for testing
        # self.t_begin = temperature


    def calculate_temp(self):
        """
        This formula will calculate the new temperature.
        """
        # the linear formula which is used for testing:
        # self.t_now = self.t_now - (self.t_begin / self.iterations)

        alpha = 0.99
        self.t_now = self.t_now * alpha

        # keeps track of the temperatures
        self.temps.append(self.t_now)


    def check_temp(self):
        """
        When the value stays the same for 500 iterations, the temperature
        will go up again.
        """
        if self.counter == self.iterations_without_change:
            self.t_now = self.raise_temp
            self.counter = 0

            # caculates the maximum acceptable value in case of higher value
            self.max_acceptable_value = self.old_value * 1.02


    def check_solution(self, new_model):
        """
        Caculates the new and old value of the models. Than caculates the
        probability. If the new model is a valid solution, the probability
        will be compared to a random number between 0 and 1. When it is lower and
        the new value is less than the maximum acceptable value, then the new
        model will be aceppeted and a new temperature will be calculated.
        """
        self.new_value = len(self.new_model.cables)
        self.old_value = len(self.model_temp.cables)

        try:
            probability = math.exp(-(self.new_value - self.old_value) / self.t_now)

            if self.new_model.is_solution():
                if random.random() < probability and self.new_value < self.max_acceptable_value:
                    self.model_temp = self.new_model
                    # the model with the lowest value will be saved as best model
                    if len(self.model_temp.cables) < self.lowest_value:
                        self.lowest_value = len(self.model_temp.cables)
                        self.best_model = self.model_temp
                    # keeps track of all the values in costs
                    self.values.append(int(self.model_temp.return_total_costs()))
                    counter = 0
                else:
                    # keeps track of all the values in costs
                    self.values.append(int(self.model_temp.return_total_costs()))
                    self.counter += 1

                self.check_temp()
                self.calculate_temp()

        except OverflowError:
            print("Mathematical calculation is too large")
