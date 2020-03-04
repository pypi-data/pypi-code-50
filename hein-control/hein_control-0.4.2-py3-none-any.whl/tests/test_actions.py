import unittest
from hein_control.scheduler.action import Action, TrackedAction
from .imported_methods import *


class TestSchedulerAction(unittest.TestCase):
    def setUp(self) -> None:
        # register all actions
        Action.register_action(one_second)
        Action.register_action(fifty_ms)
        Action.register_action(user_time)

    def test_registry(self):
        """tests registry functionality of SchedulerAction"""
        self.assertTrue(
            Action.action_is_registered(one_second)
        )
        self.assertTrue(
            Action.action_is_registered(fifty_ms)
        )

    def test_scheduler_action(self):
        """test functionality of action calling and return"""
        action = Action.register_action(one_second)
        self.assertEqual(  # test name attribute
            action.name,
            one_second.__name__
        )
        ret = action()  # execute action, test return
        self.assertEqual(
            one_second_return,
            ret
        )

    def test_argument_passthrough(self):
        """tests argument and kwarg passthrough"""
        action = Action.register_action(passthrough)
        args = (0.123, 123, 456)
        kwargs = {'asdf': 'qwerty'}
        ret = action(
            *args,
            **kwargs
        )
        self.assertEqual(
            (args, kwargs),
            ret
        )

    def test_arg_kwarg(self):
        """tests argument and kwarg specification and passthrough"""
        args = (0.123, 123, 456)
        kwargs = {'asdf': 'qwerty'}
        # test argument updating
        action = TrackedAction(
            passthrough,
            *args,
            **kwargs
        )
        self.assertEqual(
            action.args,
            args
        )
        self.assertEqual(
            action.kwargs,
            kwargs
        )
        action(
            789,
            asdf='al;skdjf;'
        )
        self.assertEqual(
            action.args,
            (789, 123, 456)
        )
        self.assertEqual(
            action.kwargs,
            {'asdf': 'al;skdjf;'}
        )

    def test_error_catching(self):
        action = Action.register_action(erronious)
        self.assertRaises(
            ValueError,
            action
        )
        self.assertTrue(action.error)
        self.assertIsNotNone(action.error_details)


class TestTrackedAction(unittest.TestCase):
    def test(self):
        tracked_action = TrackedAction(
            one_second
        )
        start_time = time.time()
        tracked_action()
        end_time = time.time()
        self.assertAlmostEqual(
            start_time,
            tracked_action.time_started
        )
        self.assertAlmostEqual(
            end_time,
            tracked_action.time_completed
        )
        self.assertAlmostEqual(
            end_time - start_time,
            tracked_action.action_duration
        )
        self.assertEqual(
            tracked_action.name,
            one_second.__name__
        )
        self.assertEqual(
            tracked_action.method_return,
            one_second_return
        )
        dct = tracked_action.as_dict()  # todo more elaborate test for dict testing
