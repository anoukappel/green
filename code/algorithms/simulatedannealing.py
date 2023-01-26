import random
import math

from code.algorithms.hillclimber import HillClimber

class SimulatedAnnealing(HillClimber):

    def __init__(self, model, temperature=1):
        super().__init__(model)
        # self.t_begin = temperature
        self.model_temp = model
        self.t_now = temperature
        self.x = []
        self.y = []
        self.counter = 0



    def calculate_temp(self):
        # self.t_now = self.t_now - (self.t_begin / self.iterations)
        # print(f"temp: {self.t_now}")

        alpha = 0.99
        self.t_now = self.t_now * alpha

        # beta = 0.01
        # self.t_now = (self.t_now/ (1 + beta * self.t_now))


    def check_solution(self, new_model):
        new_value = len(self.new_model.cables)
        print(f"New: {new_value}")
        old_value = len(self.model_temp.cables)
        print(f"Old: {old_value}")

        try:
            probability = math.exp(-(new_value - old_value) / self.t_now)
            print(f"temp2: {self.t_now}")
            print(f"Kans: {probability}")
            self.counter += 1

            if self.new_model.is_solution():
                self.x.append(self.counter)
                if random.random() < probability:
                    self.model_temp = self.new_model
                    print("the model is changed")
                    print(new_value)
                    self.y.append(new_value)
                else:
                    self.y.append(old_value)
                self.calculate_temp()

        except OverflowError:
            print("Mathematical calculation is too large")




            # self.value = new_value






# import random
# import math
#
# from .hillclimber import HillClimber
#
#
# class SimulatedAnnealing(HillClimber):
#
#
#        def __init__(self, model, temperature=1):
#         # Use the init of the Hillclimber class
#         super().__init__(model)
#
#         # Starting temperature and current temperature
#         # self.model = model.copy()
#         # self.new_model = None
#         self.t_begin = temperature
#         self.t_now = temperature
#
# def update_temperature(self):
#         """
#         This function implements a *linear* cooling scheme.
#         Temperature will become zero after all iterations passed to the run()
#         method have passed.
#         """
#         self.t_now = self.t_now - (self.t_begin / self.iterations)
#
#         # Exponential would look like this:
#         # alpha = 0.99
#         # self.T = self.T * alpha
#
#         # where alpha can be any value below 1 but above 0
#
#     def check_solution(self, new_model):
#         new_value = len(self.new_model.cables)
#         old_value = len(self.model.cables)
#
#         delta = new_value - old_value
#         probability = math.exp(-delta / self.t_now)
#
#         if random.random() < probability:
#             self.model = new_model
#             # self.value = new_value
#
#         self.update_temperature()
