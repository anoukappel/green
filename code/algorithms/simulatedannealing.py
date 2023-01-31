import random
import math

from code.algorithms.hillclimber import HillClimber

class SimulatedAnnealing(HillClimber):

    def __init__(self, model, temperature=1):
        super().__init__(model)
        # self.t_begin = temperature
        self.model_temp = model
        self.t_now = temperature
        self.y = []
        self.counter = 0
        self.new_value = 0
        self.old_value = len(self.model_temp.cables)
        self.lowest_value = 100000
        self.best_model = None



    def calculate_temp(self):
        # self.t_now = self.t_now - (self.t_begin / self.iterations)
        # print(f"temp: {self.t_now}")

        alpha = 0.99
        self.t_now = self.t_now * alpha

        # beta = 0.01
        # self.t_now = (self.t_now/ (1 + beta * self.t_now))

    def check_temp(self):
        if self.counter == 200:
            print(self.t_now)
            self.t_now = 10
            self.counter = 0


    def check_solution(self, new_model):
        self.new_value = len(self.new_model.cables)

        self.old_value = len(self.model_temp.cables)


        try:
            probability = math.exp(-(self.new_value - self.old_value) / self.t_now)

            if self.new_model.is_solution():
                if random.random() < probability:
                    self.model_temp = self.new_model
                    if len(self.model_temp.cables) < self.lowest_value:
                        self.lowest_value = len(self.model_temp.cables)
                        self.best_model = self.model_temp
                    # print("the model is changed")
                    # print(self.new_value)
                    self.y.append(int(self.model_temp.return_total_costs()))
                    counter = 0
                else:
                    self.y.append(int(self.model_temp.return_total_costs()))
                    self.counter += 1
                self.check_temp()
                self.calculate_temp()

        except OverflowError:
            print("Mathematical calculation is too large")
