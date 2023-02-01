import random
import math

from code.algorithms.hillclimber import HillClimber

class SimulatedAnnealing(HillClimber):
    """
    The simulated annealing class switches houses to 
    """
    def __init__(self, model, temperature=1, raise_temp=10):
        super().__init__(model)
        self.t_begin = temperature
        self.raise_temp = raise_temp
        self.model_temp = model
        self.t_now = temperature
        self.values = []
        self.counter = 0
        self.new_value = 0
        self.old_value = len(self.model_temp.cables)
        self.lowest_value = 100000
        self.best_model = None
        self.max_difference = 100000
        self.temps = []



    def calculate_temp(self):
        self.t_now = self.t_now - (self.t_begin / self.iterations)
        # print(f"temp: {self.t_now}")

        # alpha = 0.99
        # self.t_now = self.t_now * alpha

        self.temps.append(self.t_now)


    def check_temp(self):
        if self.counter == 500:
            print(self.t_now)
            self.t_now = self.raise_temp
            self.counter = 0
            self.max_difference = self.old_value * 1.01


    def check_solution(self, new_model):
        self.new_value = len(self.new_model.cables)

        self.old_value = len(self.model_temp.cables)

        try:
            probability = math.exp(-(self.new_value - self.old_value) / self.t_now)


            if self.new_model.is_solution():
                if random.random() < probability and self.new_value < self.max_difference:
                    self.model_temp = self.new_model
                    if len(self.model_temp.cables) < self.lowest_value:
                        self.lowest_value = len(self.model_temp.cables)
                        self.best_model = self.model_temp
                    # print("the model is changed")
                    # print(self.new_value)
                    self.values.append(int(self.model_temp.return_total_costs()))
                    counter = 0
                else:
                    self.values.append(int(self.model_temp.return_total_costs()))
                    self.counter += 1
                self.check_temp()
                self.calculate_temp()

        except OverflowError:
            print("Mathematical calculation is too large")
