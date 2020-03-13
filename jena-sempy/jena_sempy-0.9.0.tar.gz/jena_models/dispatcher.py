#! /usr/bin/env python

'''
The purpose of the dispatcher is dynamic controllability. It ensures all plan constraints are satisfied
when assigning and scheduling plan activities.

'''
import time
import secrets
import threading

class Dispatcher(threading.Thread):

    def __init__(self, plan):
          threading.Thread.__init__(self)
          self.plan = plan
          self.lock = threading.Lock()
          self.paused_time = 0.0
          self.last_pause = False

    def run(self):
        """Dispatch a compiled plan.
            Assign and schedule the plan activities.

        Parameters
        ----------
        S : graph
                Compiled plan.

        L(T, C) : List
                The constraint changes that are necessary to represent each dispatchable component solution.
        """
        print("Dispatcher started")
        self.start_time = time.time()
        self.update_tactic()
        while self.plan.base_solution.available_steps():
            moves_r = [step for step in stn.available_steps() if self.tactic.step_assignments[step] == "Robot"]
            moves_h = [step for step in stn.available_steps() if self.tactic.step_assignments[step] == "Human"]
            print ("Moves available for the robot are :")
            for move in moves_r:
                print("{}".format(move[0]))
            print ("Moves available for the human are :")
            for move in moves_h:
                print("{}".format(move[0]))
            if moves_r:
                for step, subgraph in moves_r:
                    self.lock.acquire()
                    self.perform_action(list(subgraph.nodes(data=True))[0])
                    self.perform_action(list(subgraph.nodes(data=True))[1], step_completion=True )
                    self.lock.release()
                    time.sleep(1)
            else:
                print("WAITING FOR THE HUMAN...")
                time.sleep(1)

        print("The task has been completed in {}s".format(self.elapsed_time()))

    def perform_action(self, event, step_completion=False):
        #client(event)
        time.sleep(2)
        if step_completion:
            self.plan.base_solution.update_after_completion(event[1]['step'], self.elapsed_time())
            self.plan.set_of_differences.update(event[1]['step'], "Robot")

    def attribute_human(self, step_number):
        self.plan.set_of_differences.update('Step'+step_number, "Human")
        self.update_tactic()

    def update(self, step_number):
        self.plan.base_solution.update_after_completion('Step'+step_number, self.elapsed_time())
        self.plan.set_of_differences.update('Step'+step_number, "Human")

    def update_tactic(self):
        self.tactic = secrets.choice(self.plan.set_of_differences.valid_assignments)

    def elapsed_time(self):
        return time.time()-(self.start_time+self.paused_time)

    def start_pause(self):
        self.last_pause = time.time()

    def end_pause(self):
        self.paused_time += time.time()-self.last_pause
