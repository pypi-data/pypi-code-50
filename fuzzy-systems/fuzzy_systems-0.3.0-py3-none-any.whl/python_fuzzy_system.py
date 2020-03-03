import numpy as np

###################################################
#           Fuzzy libary for python3
###################################################
# Written by Magnus Sörensen GitHub:byteofsoren
###################################################
# The fuzzy rule-based system created in this
# library is based on Ning Xiongs lecturs
#
# The thought is you have an input then the
# following:
# 1.Fuzzy fication
#   Compute the membership degrees of each input
#   to the system with respect to linguistic
#   terms.
# 2. Rule Matching:
#   Calculate the firing strength (degrees of
#   satification) of the induvidual rules.
# 3. Fuzzy Implication:
#   determine the suggestions of rules according
#   to firing strengths and rule conclusions
# 4. Fuzzy Aggregation:
#   combine suggestions from individual rules into
#   an overall output fuzzy set.
# 5. Defuzzification:determine a crisp value
#   from the output membership function
#   as the final result or solution.
#
###################################################


class fuzzy_member():
    """ The member is the part of a set"""
    def __init__(self):
        self.points = None
        self._shape = None
        self._linear= None
        pass

    def fire(x:float):
        """ Calculates the membership from the input
            Needs to be implemented in the sub class.

        """
        return 0


class fuzzy_member_pointlist(fuzzy_member):
    """ Creates an fuzzy memmber using a point list such:
        member = fuzzy_member_pointlist([[1,0],[3,1],[5,1],[7,0]])
        Will create a Trapezoid ass follow:
             _______
        ___ /       \____
            1 3   5 7
    """

    def __init__(self, points:list, filename:str=None, endpoints=[-10e10,10e10]):
        #super(fuzzy_member_Trapezoid, self).__init__()
        self.points = np.array(points)
        self._shape = np.shape(self.points)
        if filename == None:
            # No file to load use the points list
            try:
                if (self._shape[0] == 2 or self._shape[1] == 2) and (np.min(self._shape) > 2):
                    # its a point list with [[x1,y1],[x2,y2]..] or [[x1, x2, x3],[y1,y2,y3]]
                    # Is transposed to the first version [[x1,y1],[x2,y2]...]
                    if self._shape[0] < self._shape[1]:
                        self.points = self.points.T

            except Exception as e:
                    raise ValueError('ERROR: wrong shape on list')
            # Adding points to infinity to the self.points
            self._poitstoinf = np.array([[endpoints[0], self.points[0,1]]])
            self._poitstoinf = np.vstack((self._poitstoinf, self.points))
            self._poitstoinf = np.vstack((self._poitstoinf, np.array((endpoints[0], self.points[-1,1]))))
            # Calculating the y=k*x + m for all lines
            A = np.vstack((self._poitstoinf[:,0],np.ones(len(self._poitstoinf)))).T
            km = None
            for index in np.arange(len(self._poitstoinf)-1):
                y = self._poitstoinf[index:index+2,1]
                params = np.linalg.lstsq(A[index:index+2,:],y,rcond=None)[0]
                # print(f'params={params}')
                if km is None:
                    km = np.array(params)
                else:
                    km = np.vstack((km, params))

            # print(km)
            xlim = np.array([self._poitstoinf[:-1,0]])
            # print(f'xlim={xlim}')
            limconf = np.vstack([xlim, km.T]).T
            # print(f'stack xlim km.T = \n{np.round(limconf,2)}')
            #test2 = [endpoints[1],0,0]
            pampering = [endpoints[1],0,0]
            self._linear = np.vstack([limconf,pampering])
            # The _linear contains an matrix that definse the
            # linear functions in the class such
            # [xlimit,k,m]


    def __str__(self):
        return f'Fuzzy member with the points\n{self.points}'

    def fire(self, x:float):
        # Interval like a<x<b is calculated by tu retrieving a
        # compound Boolean array for the functions that could be used.
        # print(f'f({x}) in\n{self._linear[:,0].T}')
        self._boollimit = np.vstack((self._linear[:,0] <= x, self._linear[:,0] > x ))
        # print(self._boollimit)
        # Find index in boollimit where it transfers form Ture to False

        kernel = np.array([[True,False],[False,True]])
        index = None
        for i in np.arange(len(self._boollimit.T - 1)):
            if np.all(self._boollimit[:,i:i+2] == kernel):
                index = i
                break
        # Now whe now wich function to calculate
        # print(self._linear)
        return  np.array([x,1]) @ self._linear[index,1:]


class fuzzy_set():
    """ calculating firing strengths (degrees of satisfaction) of the
        individual rules
        First add_fuzzy_members()
        Then call fire() to calculate the rules
    """
    def __init__(self):
        self.fuzzy_members = list()
        self.points = None

    def add_fuzzy_member(self, fuzzy:fuzzy_member):
        self.fuzzy_members.append(fuzzy)
        if self.points is None:
            self.points = np.array(fuzzy.points)
        else:
            self.points = np.vstack((self.points, fuzzy.points))

    def fire(self, x):
        return np.array([member.fire(x) for member in self.fuzzy_members])







def plot_data(fuzzy:fuzzy_member, xaxis, label:str='No label', color=''):
    plt.plot(fuzzy.points[:,0], fuzzy.points[:,1], f'o{color}', label=f'{label} points', markersize=10)
    plt.plot(xaxis,np.array(list(map(lambda i: fuzzy.fire(i), xaxis))), f'{color}', label=f'{label} set')


def test():
    x = np.arange(-10,20)
    plot_data(cold,x,'Cold','b')
    plot_data(warm,x,'Warm','g')
    plot_data(hot,x,'Warm','r')
    # plot_data(temp,'tem','r')
    plt.title('Fuzzy sets')
    # print(temp.fire(1.5))

def plot_points_from_set(fuzzy:fuzzy_set, x:float):
    list_of_fire = np.array([fuzzy.fire(x)]).T
    xaxis = np.full((1,len(list_of_fire)),x).T
    print(list_of_fire)
    print(xaxis)
    plt.plot(xaxis, list_of_fire, 'xr', markersize=10)


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    cold =  fuzzy_member_pointlist([[0,1],[3,0]])
    warm =  fuzzy_member_pointlist([[1,0],[3,1],[5,1],[7,0]])
    hot = fuzzy_member_pointlist([[3,0],[6,1]])
    temp = fuzzy_set()
    temp.add_fuzzy_member(cold)
    temp.add_fuzzy_member(warm)
    temp.add_fuzzy_member(hot)
    plot_points_from_set(temp,1.5)
    test()
    plt.legend()
    plt.show()

















