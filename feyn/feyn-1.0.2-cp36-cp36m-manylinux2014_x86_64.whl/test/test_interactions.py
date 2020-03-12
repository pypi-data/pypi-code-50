import unittest
import pandas as pd
import numpy as np

import _feyn

# This is a test to implement all interaction state logic. 
# It is not meant to test, at least for now, the logic of the interations.
class TestInteractions(unittest.TestCase):

    def test_lr_interaction_state(self):
        lr_interaction = _feyn.Interaction('lr')
        state = {
            'w0': 1.0,
            'w1': 0.3,
            'bias': 3.2
        }
        lr_interaction.state = state

        self.assertAlmostEqual(state['w0'], lr_interaction.state['w0'])
        self.assertAlmostEqual(state['w1'], lr_interaction.state['w1'])
        self.assertAlmostEqual(state['bias'], lr_interaction.state['bias'])
        
        with self.assertRaises(KeyError):
            lr_interaction.state['missing_key']
    
    def test_sine_interaction_state(self):
        sine_interaction = _feyn.Interaction('sine')
        state = {
            'x0': 0,
            'k': 1.0
        }
        sine_interaction.state = state

        self.assertAlmostEqual(state['x0'], sine_interaction.state['x0'])
        self.assertAlmostEqual(state['k'], sine_interaction.state['k'])

        with self.assertRaises(KeyError):
            sine_interaction.state['missing_key']
    
    def test_gaussian_interaction_state(self):
        gaussian_interaction = _feyn.Interaction('gaussian')
        state = {
            'center0': 0,
            'center1': 1.0,
            'w0': 0.2,
            'w1': 0.3
        }
        gaussian_interaction.state = state

        self.assertAlmostEqual(state['center0'], gaussian_interaction.state['center0'])
        self.assertAlmostEqual(state['center1'], gaussian_interaction.state['center1'])
        self.assertAlmostEqual(state['w0'], gaussian_interaction.state['w0'])
        self.assertAlmostEqual(state['w1'], gaussian_interaction.state['w1'])
        
        with self.assertRaises(KeyError):
            gaussian_interaction.state['missing_key']
    
    def test_multiply_interaction_state(self):
        multiply_interaction = _feyn.Interaction('multiply')
        
        state = {
            'random_prop': 0
        }

        multiply_interaction.state = state

        self.assertEqual({}, multiply_interaction.state)

        with self.assertRaises(KeyError):
            multiply_interaction.state['missing_key']
    

    def test_continous_register_interaction_state(self):
        register_cat_interaction = _feyn.Interaction('cont')
        state = {
            'variance': 0,
            'absmax': 1.0,
            'iabsmax': 0.2
        }
        register_cat_interaction.state = state

        self.assertAlmostEqual(state['variance'], register_cat_interaction.state['variance'])
        self.assertAlmostEqual(state['absmax'], register_cat_interaction.state['absmax'])
        self.assertAlmostEqual(state['iabsmax'], register_cat_interaction.state['iabsmax'])
        
        with self.assertRaises(KeyError):
            register_cat_interaction.state['missing_key']
    
    def test_category_register_interaction_state(self):
        register_cat_interaction = _feyn.Interaction('cat')
        state = [
            ('red', 0.1),
            ('blue', 0.15),
            ('none', 0.001)
        ]

        register_cat_interaction.state = state

        self.assertListEqual(state, register_cat_interaction.state)
        

    def test_category_register_interaction_update(self):
        register_cat = _feyn.Interaction('cat', label='myinput')
        register_cat.state = [
            ('red', 0.1),
            ('blue', 0.15),
        ]

        register_cat.set_source(0, -1)

        out = _feyn.Interaction("cont", label="out")
        out.set_source(0,0)

        g = _feyn.Graph(2)
        g.set_interaction(0,register_cat)
        g.set_interaction(1,out)
        o = g.query({"myinput": np.array(["red", "blue", "purple", 42])})
        
        self.assertAlmostEqual(o[0],0.1)
        self.assertAlmostEqual(o[1],0.15)
        self.assertAlmostEqual(o[2],0.0)
        self.assertAlmostEqual(o[3],0.0)

        newstate = {i[0]: i[1] for i in register_cat.state}
        self.assertAlmostEqual(newstate["purple"], 0.0)
        self.assertAlmostEqual(newstate["42"], 0.0)