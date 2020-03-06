#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import platform
import shutil
from tempfile import mkdtemp
import unittest
import pickle

import symengine
import numpy

from jitcxde_common import jitcxde

y = symengine.Function("y")
f = [
		y(0),
		2*y(1)**3,
		y(0)+y(1)+y(2),
		symengine.exp(y(3)),
		5,
	]

def f_control(y):
	return [
		y[0],
		2*y[1]**3,
		y[0]+y[1]+y[2],
		numpy.exp(y[3]),
		5,
	]

class jitcxde_tester(jitcxde):
	dynvar = y
	
	def __init__(self,f_sym=(),omp=False):
		jitcxde.__init__(self,len(f),False)
		f_sym_wc = self._handle_input(f_sym)
		set_dy = symengine.Function("set_dy")
		self.omp = omp
		
		self.render_and_write_code(
			(set_dy(i,entry) for i,entry in enumerate(f_sym_wc())),
			name = "f",
			chunk_size = 1 if omp else 100,
			arguments = [
					("Y" , "PyArrayObject *__restrict const"),
					("dY", "PyArrayObject *__restrict const")
				]
			)
	
	def _compile_C(self):
		if self.jitced is None:
			self.compile_C()
	
	def compile_C(self,modulename=None):
		self._process_modulename(modulename)
		self._render_template(n=self.n)
		self._compile_and_load(False,None,None,self.omp)


name = ""
def get_unique_name():
	global name
	name += "x"
	return name

for omp in [True, False]:
	tester = jitcxde_tester(f,omp)
	tester.compile_C()
	arg = numpy.random.uniform(-2,2,5)
	numpy.testing.assert_allclose(
			tester.jitced.f(arg),
			f_control(arg)
		)



