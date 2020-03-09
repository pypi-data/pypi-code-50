"""
Created on Thu Oct 31 16:50:17 2019

pyCICY - A python CICY toolkit. It allows for computation of 
line bundle cohomologies over Complete Intersection
Calabi Yau manifolds.

This class includes functions related to fibration structures in CICYs.


Authors
-------
Magdalena Larfors (magdalena.larfors@physics.uu.se)
Robin Schneider (robin.schneider@physics.uu.se)
"""

# libraries
import itertools
import numpy as np
import sympy as sp
import random
from random import randint
import scipy as sc
import scipy.special
import math
import time
from texttable import Texttable
import os
# for documentation
import logging
from pyCICY.pyCICY import CICY
from sympy.solvers.diophantine  import diophantine, diop_linear


class fCICY(CICY):

    def __init__(self, conf, log=3):
        """
        The fCICY class. It includes fibration related functions,
        such as finding obvius genus one fibrations and putative sections.
        
        Parameters
        ----------
        conf : array[nProj, K+1]
            The CICY configuration matrix, including the first col for the
            projective spaces.
        log : int, optional
            Documentation level. 1 - DEBUG, 2 - INFO, 3 - WARNING, by default 3.

        Examples
        --------
        The manifold #7833 of the CICYlist:

        >>> M = fCICY([[2,2,1],[3,1,3]])
        """
        super().__init__(conf, log)

        self.active_fibration = np.array([])
        self.active_base = np.array([])


    def set_base(self, base, fibrations):
        self.active_fibration = np.array(fibrations)
        self.active_base = np.array(base)
        self._sort_configuration_matrix()

    def _sort_configuration_matrix(self):
        self.M = self.M

    def clear_fibration(self):
        self.active_fibration = np.array([])
        self.active_base = np.array([])

    def find_ogf(self):
        """
        returns a list of ogf in the format
        [base_indices, [list of all fibration coloumns]]
        e.g.: the CICY

        """
        #fill with all combinations and track the positions at the same time.
        all_ambient = [list(itertools.combinations(self.M[:,0], i)) for i in range(1,self.len)]
        all_position = [list(itertools.combinations(range(self.len), i)) for i in range(1,self.len)]

        ogf = []
        for i in range(self.len-1):
            for j in range(len(all_ambient[i])):
                # special case of P1 x P1 or other 
                # trivial base product. for n.folds
                n_zeroes = sum(all_ambient[i][j])-self.nfold+1
                if n_zeroes == 0:
                    #trivial fibration where the base is just a product of two ambient spaces
                    ogf += [all_position[i][j], []]
                else:
                    if n_zeroes > 0:        
                        # bring in block form with zeroes sorted to top
                        # and rows to bottom.
                        fibration_col = self._find_cols(all_position[i][j], n_zeroes)
                        if fibration_col != []:
                            # adding the base and all its possible fibrations to the list
                            ogf += [[all_position[i][j], fibration_col]]
        return ogf

    def _find_cols(self, base, nzeros):
        """
        Brings the conf matrix in a positon such that we have
        Zeros in the top left corner and the base at the bottom.
        Needs the base rows and number of zeroes.
        """
        # put all the base elements at the bottom
        base_matrix = [0 for i in range(self.len)]
        j = 0
        for i in range(self.len):
            in_base = False
            for x in base:
                if i == x:
                    in_base = True
            if in_base:
                base_matrix[self.len-1-j] = self.M[i]
                j += 1
            else:
                base_matrix[i-j] = self.M[i]

        # Next we need to make a zero block in the right corner
        # This is easiest achieved by looking for all zero sums up to the base
        zero_row = []
        for i in range(1, self.K+1):
            row = 0
            for j in range(self.len-len(base)):
                row += base_matrix[j][i]
            if row == 0:
                zero_row += [i]

        #check whether there are sufficient possibilities to make a zero block
        #we need at least nzeros
        if len(zero_row) < nzeros:
            return []
        else:
            fibration_col = itertools.combinations(zero_row, nzeros)
            return list(fibration_col)

    def find_putative_section(self, fibration):

        """
        finds putative sections, by solving the constraints coming from
        oguiso and birational.
        """
        if not self.fav:
            logging.warning('Analysis is only valid for favourable CICYs.')
            logging.warning('Check: http://www1.phys.vt.edu/cicydata/ for a list of favourable CICYs.')

        om, ov = self.oguiso_constraint(fibration)
        bm, bv = self.birational_constraint(fibration)
        # order is important
        vars = sp.symbols('a0:'+str(self.len), integer=True) #, order=lex

        oguiso = [0 for i in range(len(om))]
        for i in range(len(om)):
            oguiso[i] = (-1)*ov[i][0]
            for j in range(len(om[i])):
                oguiso[i] += om[i][j]*vars[j]
        
        birational = [0 for i in range(len(bm))]
        for i in range(len(bm)):
            for j in range(len(bm[i])):
                birational[i] += (-1)*bv[i][0][j]*vars[j]
                for k in range(len(bm[i][j])):
                    birational[i] += bm[i][j][k]*vars[j]*vars[k]

        if self.doc:
            print('We find the following constraints:')
            for a in oguiso:
                print(a, '= 0')
            for a in birational:
                print(a, '= 0')
            #print('Next we calculate Groebner basis and find some solutions.')
        
        m = sp.symbols('m', integer=True)
        ogu_degrees = [sp.degree(oguiso[0], variable) for variable in vars]
        l_vars = [variable for variable in vars]
        all_parametrizations = []

        # run through all constraints
        for i in range(len(oguiso)):
            # find parametrization
            parametrization = diop_linear(oguiso[i], m)
            count = 0
            # substitute all parametrizations into the other expressions
            for para in parametrization:
                if para == None:
                    if self.doc:
                        print('There is no solution to the constraints.')
                    return False
                # add the new parameters to variable list
                new_variables = para.free_symbols
                for v in new_variables:
                    # but only if they are really new
                    if v not in l_vars:
                        l_vars += [v]
                # run through each variable and replace it with ne parametrization
                for k in range(count, len(ogu_degrees)):
                    if ogu_degrees[k] == 1:
                        count = k+1
                        # add said parametrization to parameter list
                        all_parametrizations += [[l_vars[k],para]]
                        # replace in other ogu constraints
                        for l in range(i+1, len(oguiso)):
                            oguiso[l] = oguiso[l].subs(l_vars[k], para)
                        #replace in birational constraints
                        for l in range(len(birational)):
                            birational[l] = birational[l].subs(l_vars[k], para)
                        break
            # include new variables in higher ogu_degrees
            if len(oguiso)-i > 1:
                ogu_degrees = [sp.degree(oguiso[i+1], variable) for variable in l_vars]

        # do the same analysis for birational; Note the diophantine equations are
        # quadratic now and can only be solved for less than three variables
        #bir_degrees = [[sp.degree(entry, variable) for variable in l_vars] for entry in birational]
        contribution = [[1 if sp.degree(entry, variable) > 0 else 0 for variable in l_vars] for entry in birational]
        # Hence it is important that we sort the equations in such a way that the ones with
        # 3 variables come first and hopefully parametrize the later ones in such a way that we are good.
        # This might not cover all cases yet, but most. Since the ordering can still be improved.
        # raise an exception if we run into bad ordering?
        sorted = np.argsort([sum(entry) for entry in contribution])
        bir_sort = [birational[i] for i in sorted]
        cont_sort = [contribution[i] for i in sorted]
        
        #to many but better save than sorry
        t = sp.symbols('b0:'+str(len(sorted)), integer=True)

        for i in range(len(sorted)):
            parametrization = list(diophantine(bir_sort[i], t[i]))
            if parametrization == []:
                new_variables = bir_sort[i].free_symbols
                resolve = False
                if len(new_variables) < 3:
                    # then it might still be possible to solve,
                    #as there are some problems in in the build function with new parametrizations
                    # and minus signs
                    for x in new_variables:
                        if x not in vars:
                            # do the same thing with flipped sign
                            test = list(diophantine(bir_sort[i].subs(x,-x), t[i]))
                            if test != []:
                                resolve = True
                                #fix all the rest
                                parametrization = test
                                # resubstitute in all parametrizations
                                for entry in all_parametrizations:
                                    entry[1] = entry[1].subs(x, -x)
                                # in all following constraints
                                for j in range(i, len(sorted)):
                                    bir_sort[j] = bir_sort[j].subs(x,-x)
                                #break the loop since we managed to resolve
                                break
                if not resolve:
                    if self.doc:
                        print('There is no solution to the constraints.')
                    return False
                #else continue buisness as if nothing happened ;)
            count = 0
            for para in parametrization[0]:
                new_variables = para.free_symbols
                for v in new_variables:
                    if v not in l_vars:
                        l_vars += [v]
                for k in range(count, len(cont_sort[i])):
                    if cont_sort[i][k] == 1:
                        count = k+1
                        all_parametrizations += [[l_vars[k],para]]
                        for l in range(i+1,len(sorted)):
                            bir_sort[l] = bir_sort[l].subs(l_vars[k], para)
                        break
            if len(sorted)-i > 1:
                cont_sort[i+1] = [1 if sp.degree(bir_sort[i+1], variable) > 0 else 0 for variable in l_vars]

        if self.doc:
            print(all_parametrizations)

        """
        Next, we should solve the parametrization (if not unique for any values)
        and return some examples.
        """
        for entry in all_parametrizations:
            if entry[0] not in vars:
                for b_entry in all_parametrizations:
                    b_entry[1] = b_entry[1].subs(entry[0], entry[1])

        #next sort them
        paramet_sorted = [0 for i in range(len(vars))]
        count = 0
        for variable in vars:
            for entry in all_parametrizations:
                if variable == entry[0]:
                    paramet_sorted[count] = entry[1]
                    count += 1

        if self.doc:
            print('And the final parametrization:')
            print(paramet_sorted)     

        return paramet_sorted


    def fill_psec(self, psec, x=0):
        """
        Takes a psec and returns possible line bundles.
        Takes as additional argument a range for the parametrization.
        """
        #last we parametrize for all undetermined variables.
        if not psec:
            if self.doc:
                print('The putative section was empty.')
            return False
        parameters = []
        parameter_list = [[] for i in range(len(psec))]
        for i in range(len(psec)):
            par = psec[i].free_symbols
            for y in par:
                contains = False
                position = 0
                for j in range(len(parameters)):
                    if y == parameters[j]:
                        contains = True
                        position = j
                if not contains:
                    parameters += [y]
                    parameter_list[i] += [len(parameters)-1]
                else:
                    parameter_list[i] += [position]
                
        all_combinations = list(itertools.permutations(range(-x,x+1), len(parameters)))
        solutions = [[0 for i in range(len(psec))] for a in range(len(all_combinations))]
        count = 0
        for entry in all_combinations:
            for i in range(len(psec)):
                for z in parameter_list[i]:
                    solutions[count][i] = psec[i].subs(parameters[z], entry[z])
            count += 1

        if self.doc:
            print('Solutions for the specified range of', [-x,x] , 'are:')
            print(solutions)

        return solutions
        
    def oguiso_constraint(self, fibration):
        """
        Determines the oguiso constraints for a given fibration.
        e.g.:
        
        """
        #First we determine all alpha_tuples
        alpha_tuples = np.array(list(itertools.product(fibration[0], repeat=self.nfold-1)), dtype=np.int8)

        mu_base = np.array([[self.M[i][j] for j in fibration[1]] for i in fibration[0]], dtype=np.int8)
        #dim_base = sum([self.M[x][0] for x in fibration[0]])
        mu_top = np.transpose(np.array(self.N, dtype=np.int8))

        solutions = []
        #Next we go and find the constraints coming from all alpha
        for alpha in alpha_tuples:

            constraints = [0 for i in range(self.len)]
            sol = 0

            # Only permutations in the mu_base allowed.
            # check if nontrivial solution
            ambient = [a[0] for a in self.M]
            sol_nontriv = True
            for entry in alpha:
                ambient[entry] -= 1
                if ambient[entry] < 0:
                    sol_nontriv = False

            if sol_nontriv:
                # determine base tuples
                base_tuple = []
                for i in range(len(fibration[0])):
                    base_tuple += [i]*ambient[fibration[0][i]]

                #check for trivial case
                if base_tuple == []:
                    sol = 1
                else:
                    base_tuples = itertools.permutations(base_tuple, len(mu_base))                
                    # fill sol
                    for x in base_tuples:
                        value = 1
                        for i in range(len(mu_base)):
                            #there is probably some python way to make this nicer
                            value = value*mu_base[i][x[i]]
                        sol += value

                #determine top tuples
                top_tuple = []
                for i in range(self.len):
                    top_tuple += [i]*ambient[i]
                
                top_tuples = np.array(list(itertools.permutations(top_tuple, len(mu_top)+1)), dtype=np.int8)
                top_tuples = np.unique(top_tuples, axis=0) #+1 for sheav S

                # fill contraints
                for x in top_tuples:
                    value = 1
                    for j in range(len(mu_top)):
                        value = value*mu_top[j][x[j+1]]
                    #if value != 0:
                    #    print(x)
                    constraints[x[0]] += value
                # removing any identical constraints
                if [constraints, [sol]] not in solutions: 
                    solutions += [[constraints, [sol]]]
        matrix = np.array([x[0] for x in solutions], dtype=np.int8)
        vector = np.array([x[1] for x in solutions], dtype=np.int8)
        return matrix, vector

    def birational_constraint(self, fibration):
        """
        determines the birational constraint for a given fibration,
        e.g.
        """
        if self.nfold > 3:
            logging.warning('Note that the birational criterion has only been proven for 2,3-folds.')
        
        #First we determine all alpha_tuples
        alpha_tuples = np.array(list(itertools.product(fibration[0], repeat=self.nfold-2)), dtype=np.int8)

        first_chern_base = [self.M[i][0]+1-sum([self.M[i][j] for j in fibration[1]]) for i in fibration[0]]
        chern_ambient = np.array([0 for i in range(self.len)], dtype=np.int8)
        for i in range(len(fibration[0])):
            chern_ambient[fibration[0][i]] = first_chern_base[i]
        mu_top = np.transpose(np.array(self.N, dtype=np.int8))
        base_extended = np.append(mu_top, [chern_ambient], axis=0)

        solutions = []
        #Next we go and find the constraints coming from all alpha
        #Note this time there will be quadratic ones
        for alpha in alpha_tuples:

            constraints = [[0 for i in range(self.len)] for j in range(self.len)]
            sol = [0 for i in range(self.len)]

            # Only permutations in the mu_base allowed.
            # check if nontrivial solution
            ambient = [a[0] for a in self.M]
            sol_nontriv = True
            for entry in alpha:
                ambient[entry] -= 1
                if ambient[entry] < 0:
                    sol_nontriv = False

            if sol_nontriv:

                # determine all top tuples
                top_tuple = []
                for i in range(self.len):
                    top_tuple += [i]*ambient[i]
                top_tuples = np.array(list(itertools.permutations(top_tuple, len(top_tuple))), dtype=np.int8)
                top_tuples = np.unique(top_tuples, axis=0)

                # fill sol
                for x in top_tuples:
                    value_1 = -1
                    value_2 = 1
                    for i in range(len(base_extended)):
                        #there is probably some python way to make this nicer
                        value_1 = value_1*base_extended[i][x[i+1]]
                        if i != len(base_extended)-1:
                            value_2 = value_2*base_extended[i][x[i+2]]
                    sol[x[0]] += value_1
                    constraints[x[0]][x[1]] += value_2
                if [constraints, [sol]] not in solutions: 
                    solutions += [[constraints, [sol]]]
        matrix = np.array([x[0] for x in solutions], dtype=np.int8)
        vector = np.array([x[1] for x in solutions], dtype=np.int8)
        return matrix, vector

    def is_ghs(self, psec):
        #N = [a if a > 0 else 0 for a in psec]
        #D = [-a if a < 0 else 0 for a in psec]
        """
        determines whether a putative section is a global holomorphic section

        """
        logging.warning('Has not been implemnted yet.')
        return None

if __name__ == '__main__':
    print('done')