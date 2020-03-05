# encoding: utf-8

class RL(object):


    def __init__(self, world, n):

        """
        Parameters
        ----------
        n : int
            num of iterations
        """

        self.world = world
        self.n     = n


    def choose_state(self, states):

        pass


    def choose_action(self, state):

        pass


    def update(self):

        pass


    def finish_iteration(self):

        pass


    def finish_fit(self):

        pass



    def iter(self, fitting=True):

        self.state_current = self.choose_state(self.world.starts)

        while(True):
            self.action_current = self.choose_action(self.state_current)
            self.state_next     = self.world.take(self.state_current, self.action_current)

            print(self.state_current, '-->', self.state_next)

            if fitting:
                self.update()

            self.state_current = self.state_next

            if self.finish_iteration():
                break



    def fit(self):

        # iterations
        for i in range(self.n):
            print('iter: %s' % i)
            self.iter()
            print()

            if self.finish_fit():
                break


    def predict(self):

        return self.iter(fitting=False)
