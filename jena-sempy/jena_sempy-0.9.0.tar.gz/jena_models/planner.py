from jena_models.base_solution import BaseSolution
from jena_models.set_of_differences import SetOfDifferences

class Planner(object):
    """Compile a plan.

    Converts the information retrieved from the knowledge base into a
    Multi-agent Disjunctive Temporal Constraint Network With Uncertainty
    """

    def __init__(self, policy=None):
        self.base_solution = BaseSolution()
        self.set_of_differences = SetOfDifferences()
        self.planning_policy = policy

    def create_plan(self, task):
        """ Model a temporal plan .

        Model a plan and instantiate a dispatcher to perform the plan
        """
        self.base_solution.model_temporal_problem(task)
        self._ica_map_u()
        #nx.write_graphml(self.base_solution._graph, "base_solution.graphml")
        return True if (self.set_of_differences.count_valid_assignments() > 0) else False

    def _ica_map_u(self):
        ''' Return a compact dispatchable form of a temporal problem '''
        ### Compute the Base Solution
        ## Retrieve info from self.stn instead of args now
        self.base_solution.relax_network()
        self.base_solution.transform_dispatchable_graph()
        self.set_of_differences.initialize_set_of_differences(self.base_solution, self.planning_policy)
        # self.export_data()
        for full_assignment in self.set_of_differences.valid_assignments:
            constraints = [asg[0] for asg in full_assignment.task_assignments]
            temporally_consistent = self.set_of_differences.backpropagate_task_assign(constraints, self.base_solution, full_assignment)
            if not temporally_consistent:
                full_assignment.feasible = False

    def export_data(self):
        with open(os.path.join("./", self.planning_policy.name + '.csv'), mode='w') as working_times:
            data_csv = csv.writer(working_times, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for full_assignment in self.planning_policy.data:
                data_csv.writerow(full_assignment)
