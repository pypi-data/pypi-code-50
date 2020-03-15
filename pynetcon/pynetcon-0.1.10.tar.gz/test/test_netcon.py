from pynetcon.netcon import netcon

def test_netcon():
    # setup
    leg_links = (
        [-1, 1, 2, 3],
        [2, 4, 5, 6],
        [1, 5, 7, -3],
        [3, 8, 4, 9],
        [6, 9, 7, 10],
        [-2, 8, 11, 12],
        [10, 11, 12, -4]
    )
    verbosity = 0
    cost_type = 1
    mu_cap = 1
    allow_ops = True
    leg_costs = [[-1,2],[-2,2],[-3,2],[-4,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[10,2],[11,2],[12,2]]
    # calculate best sequence
    sequence = netcon(leg_links, verbosity, cost_type, mu_cap, allow_ops, leg_costs)
    # check result
    assert sequence == [11, 12, 2, 1, 5, 3, 4, 6, 7, 9, 8, 10]