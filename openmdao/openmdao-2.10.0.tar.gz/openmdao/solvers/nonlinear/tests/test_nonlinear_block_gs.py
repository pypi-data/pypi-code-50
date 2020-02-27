"""Test the Nonlinear Block Gauss Seidel solver. """

import unittest

import numpy as np

import openmdao.api as om
from openmdao.test_suite.components.paraboloid import Paraboloid
from openmdao.test_suite.components.double_sellar import DoubleSellar
from openmdao.test_suite.components.sellar import SellarDerivatives, \
    SellarDis1withDerivatives, SellarDis2withDerivatives, \
    SellarDis1, SellarDis2
from openmdao.utils.assert_utils import assert_rel_error, assert_warning

from openmdao.utils.mpi import MPI
try:
    from openmdao.api import PETScVector
except:
    PETScVector = None


class TestNLBGaussSeidel(unittest.TestCase):

    def test_reraise_error(self):

        prob = om.Problem(model=DoubleSellar())
        model = prob.model

        g1 = model.g1
        g1.nonlinear_solver = om.NonlinearBlockGS()
        g1.nonlinear_solver.options['maxiter'] = 1
        g1.nonlinear_solver.options['err_on_non_converge'] = True
        g1.linear_solver = om.DirectSolver(assemble_jac=True)

        g2 = model.g2
        g2.nonlinear_solver = om.NonlinearBlockGS()
        g2.nonlinear_solver.options['maxiter'] = 1
        g2.nonlinear_solver.options['err_on_non_converge'] = True
        g2.linear_solver = om.DirectSolver(assemble_jac=True)

        model.nonlinear_solver = om.NonlinearBlockGS()
        model.linear_solver = om.DirectSolver(assemble_jac=True)
        model.nonlinear_solver.options['err_on_non_converge'] = True
        model.nonlinear_solver.options['reraise_child_analysiserror'] = True

        prob.setup()

        with self.assertRaises(om.AnalysisError) as context:
            prob.run_model()

        msg = "Solver 'NL: NLBGS' on system 'g1' failed to converge in 1 iterations."
        self.assertEqual(str(context.exception), msg)

    def test_reraise_child_analysiserror_deprecation_warning(self):

        prob = om.Problem()
        model = prob.model

        model.nonlinear_solver = om.NonlinearBlockGS()
        model.linear_solver = om.ScipyKrylov(assemble_jac=True)
        model.nonlinear_solver.options['err_on_non_converge'] = True

        prob.setup()

        msg = "Deprecation warning: In V 3.x, reraise_child_analysiserror will default to False."
        with assert_warning(DeprecationWarning, msg):
            prob.run_model()

    def test_feature_set_options(self):
        import numpy as np

        import openmdao.api as om
        from openmdao.test_suite.components.sellar import SellarDis1withDerivatives, SellarDis2withDerivatives

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()

        nlgbs.options['maxiter'] = 20
        nlgbs.options['atol'] = 1e-6
        nlgbs.options['rtol'] = 1e-6

        prob.setup()

        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

    def test_feature_basic(self):
        import numpy as np

        import openmdao.api as om
        from openmdao.test_suite.components.sellar import SellarDis1withDerivatives, SellarDis2withDerivatives

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        model.nonlinear_solver = om.NonlinearBlockGS()

        prob.setup()

        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

    def test_feature_maxiter(self):
        import numpy as np

        import openmdao.api as om
        from openmdao.test_suite.components.sellar import SellarDis1withDerivatives, SellarDis2withDerivatives

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()
        nlgbs.options['maxiter'] = 2

        prob.setup()
        prob.set_solver_print()
        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58914915, .00001)
        assert_rel_error(self, prob['y2'], 12.05857185, .00001)

    def test_feature_rtol(self):
        import numpy as np

        import openmdao.api as om
        from openmdao.test_suite.components.sellar import SellarDis1withDerivatives, SellarDis2withDerivatives, SellarDerivatives

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()
        nlgbs.options['rtol'] = 1e-3

        prob.setup()

        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.5883027, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

    def test_feature_atol(self):
        import numpy as np

        import openmdao.api as om
        from openmdao.test_suite.components.sellar import SellarDis1withDerivatives, SellarDis2withDerivatives

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()
        nlgbs.options['atol'] = 1e-4

        prob.setup()

        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.5882856302, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

    def test_sellar(self):
        # Basic sellar test.

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()

        prob.setup()
        prob.set_solver_print(level=0)
        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

        # Make sure we aren't iterating like crazy
        self.assertEqual(model.nonlinear_solver._iter_count, 7)

        # Only one extra execution
        self.assertEqual(model.d1.execution_count, 8)

        # With run_apply_linear, we execute the components more times.

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                                promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()
        nlgbs.options['use_apply_nonlinear'] = True

        prob.setup()
        prob.set_solver_print(level=0)
        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

        # Make sure we aren't iterating like crazy
        self.assertEqual(model.nonlinear_solver._iter_count, 7)

        # Nearly double the executions.
        self.assertEqual(model.d1.execution_count, 15)

    def test_sellar_analysis_error(self):
        # Tests Sellar behavior when AnalysisError is raised.

        prob = om.Problem()
        model = prob.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

        model.add_subsystem('obj_cmp', om.ExecComp('obj = x**2 + z[1] + y1 + exp(-y2)',
                                                   z=np.array([0.0, 0.0]), x=0.0),
                            promotes=['obj', 'x', 'z', 'y1', 'y2'])

        model.add_subsystem('con_cmp1', om.ExecComp('con1 = 3.16 - y1'), promotes=['con1', 'y1'])
        model.add_subsystem('con_cmp2', om.ExecComp('con2 = y2 - 24.0'), promotes=['con2', 'y2'])

        nlgbs = model.nonlinear_solver = om.NonlinearBlockGS()
        nlgbs.options['maxiter'] = 2
        nlgbs.options['err_on_non_converge'] = True

        prob.setup()
        prob.set_solver_print(level=0)

        try:
            prob.run_model()
        except om.AnalysisError as err:
            self.assertEqual(str(err), "Solver 'NL: NLBGS' on system '' failed to converge in 2 iterations.")
        else:
            self.fail("expected AnalysisError")

    def test_sellar_group_nested(self):
        # This tests true nested gs. Subsolvers solve each Sellar system. Top
        # solver couples them together through variable x.

        # This version has the indepvarcomps removed so we can connect them together.
        class SellarModified(om.Group):
            """ Group containing the Sellar MDA. This version uses the disciplines
            with derivatives."""

            def __init__(self):
                super(SellarModified, self).__init__()

                self.add_subsystem('d1', SellarDis1withDerivatives(), promotes=['x', 'z', 'y1', 'y2'])
                self.add_subsystem('d2', SellarDis2withDerivatives(), promotes=['z', 'y1', 'y2'])

                self.nonlinear_solver = om.NonlinearBlockGS()
                self.linear_solver = om.ScipyKrylov()

        prob = om.Problem()
        root = prob.model
        root.nonlinear_solver = om.NonlinearBlockGS()
        root.nonlinear_solver.options['maxiter'] = 20
        root.add_subsystem('g1', SellarModified())
        root.add_subsystem('g2', SellarModified())

        root.connect('g1.y2', 'g2.x')
        root.connect('g2.y2', 'g1.x')

        prob.setup()
        prob.set_solver_print(level=0)

        prob.run_model()

        assert_rel_error(self, prob['g1.y1'], 0.64, .00001)
        assert_rel_error(self, prob['g1.y2'], 0.80, .00001)
        assert_rel_error(self, prob['g2.y1'], 0.64, .00001)
        assert_rel_error(self, prob['g2.y2'], 0.80, .00001)

    def test_NLBGS_Aitken(self):

        prob = om.Problem(model=SellarDerivatives())
        model = prob.model
        model.nonlinear_solver = om.NonlinearBlockGS()

        prob.setup()
        model.nonlinear_solver.options['use_aitken'] = True
        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)
        self.assertTrue(model.nonlinear_solver._iter_count == 5)

    def test_NLBGS_Aitken_cs(self):

        prob = om.Problem(model=SellarDerivatives())

        model = prob.model
        model.approx_totals(method='cs', step=1e-10)

        prob.setup()
        prob.set_solver_print(level=2)
        model.nonlinear_solver.options['use_aitken'] = True
        model.nonlinear_solver.options['atol'] = 1e-15
        model.nonlinear_solver.options['rtol'] = 1e-15

        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

        J = prob.compute_totals(of=['y1'], wrt=['x'])
        assert_rel_error(self, J['y1', 'x'][0][0], 0.98061448, 1e-6)

    def test_NLBGS_cs(self):

        prob = om.Problem(model=SellarDerivatives())

        model = prob.model
        model.approx_totals(method='cs')

        prob.setup()
        prob.set_solver_print(level=0)
        model.nonlinear_solver.options['atol'] = 1e-15
        model.nonlinear_solver.options['rtol'] = 1e-15

        prob.run_model()

        assert_rel_error(self, prob['y1'], 25.58830273, .00001)
        assert_rel_error(self, prob['y2'], 12.05848819, .00001)

        J = prob.compute_totals(of=['y1'], wrt=['x'])
        assert_rel_error(self, J['y1', 'x'][0][0], 0.98061448, 1e-6)

    def test_res_ref(self):

        class ContrivedSellarDis1(SellarDis1):

            def setup(self):
                super(ContrivedSellarDis1, self).setup()
                self.add_output('highly_nonlinear', val=1.0, res_ref=1e-4)
            def compute(self, inputs, outputs):
                super(ContrivedSellarDis1, self).compute(inputs, outputs)
                outputs['highly_nonlinear'] = 10*np.sin(10*inputs['y2'])

        p = om.Problem()
        model = p.model

        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        model.add_subsystem('d1', ContrivedSellarDis1(), promotes=['x', 'z', 'y1', 'y2'])
        model.add_subsystem('d2', SellarDis2(), promotes=['z', 'y1', 'y2'])

        nlbgs = model.nonlinear_solver = om.NonlinearBlockGS()

        nlbgs.options['maxiter'] = 20
        nlbgs.options['atol'] = 1e-6
        nlbgs.options['rtol'] = 1e-100

        p.setup()
        p.run_model()

        self.assertEqual(nlbgs._iter_count, 9, 'res_ref should make this take more iters.')


@unittest.skipUnless(MPI and PETScVector, "MPI and PETSc are required.")
class ProcTestCase1(unittest.TestCase):

    N_PROCS = 2

    def test_aitken(self):

        prob = om.Problem()
        model = prob.model
        model.add_subsystem('px', om.IndepVarComp('x', 1.0), promotes=['x'])
        model.add_subsystem('pz', om.IndepVarComp('z', np.array([5.0, 2.0])), promotes=['z'])

        p1 = model.add_subsystem('p1', om.ParallelGroup(), promotes=['*'])
        p1.add_subsystem('d1a', SellarDis1withDerivatives(), promotes=['x', 'z'])
        p1.add_subsystem('d1b', SellarDis1withDerivatives(), promotes=['x', 'z'])

        p2 = model.add_subsystem('p2', om.ParallelGroup(), promotes=['*'])
        p2.add_subsystem('d2a', SellarDis2withDerivatives(), promotes=['z'])
        p2.add_subsystem('d2b', SellarDis2withDerivatives(), promotes=['z'])

        model.connect('d1a.y1', 'd2a.y1')
        model.connect('d1b.y1', 'd2b.y1')
        model.connect('d2a.y2', 'd1a.y2')
        model.connect('d2b.y2', 'd1b.y2')

        model.nonlinear_solver = om.NonlinearBlockGS()

        prob.setup()
        prob.set_solver_print(level=2)
        model.nonlinear_solver.options['use_aitken'] = True

        # Set one branch of Sellar close to the solution.
        prob.set_val('d2b.y2', 12.05848815)
        prob.set_val('d1b.y1', 25.58830237)

        prob.run_model()

        print(prob.get_val('d1a.y1', get_remote=True))
        print(prob.get_val('d2a.y1', get_remote=True))
        print(prob.get_val('d1b.y2', get_remote=True))
        print(prob.get_val('d2b.y2', get_remote=True))

        assert_rel_error(self, prob.get_val('d1a.y1', get_remote=True), 25.58830273, .00001)
        assert_rel_error(self, prob.get_val('d1b.y1', get_remote=True), 25.58830273, .00001)
        assert_rel_error(self, prob.get_val('d2a.y2', get_remote=True), 12.05848819, .00001)
        assert_rel_error(self, prob.get_val('d2b.y2', get_remote=True), 12.05848819, .00001)

        # Test that Aitken accelerated the convergence, normally takes 7.
        self.assertTrue(model.nonlinear_solver._iter_count == 5)


if __name__ == "__main__":
    unittest.main()
