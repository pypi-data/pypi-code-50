# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2020

from .bundleresthandler.wmlbundleresthandler import WmlBundleRestHandler
import pickle
import logging
   
tracer = logging.getLogger(__name__) 




#################################################
# output class
# given to WmlBundleRestHandler to write results
# to any destionation
#################################################
class DefaultOutput():
    def __init__(self, output_object, single_output):
        self._output_object = output_object
        self._single_output = single_output
        pass
    def __call__(self, results):
        tracer.debug("Start output_function")
        for index,result_list in enumerate(results):
            tracer.debug("Start result submission ")
            ###############################################################################
            # 1st list is the result list being generated anyway
            # contains either successful results only or successful results and error tuple
            # depends on _single_output
            ###############################################################################
            if index == 0:
                for list_element in result_list:
                    #self._output_object.submit('result_port',{'__spl_po':memoryview(pickle.dumps(list_element))})
                    # print store writeToFile whatever
                    pass
            ##############################################################################
            # 2nd list is the error list being generated only if _single_output = False
            ##############################################################################
            elif index == 1:
                if not self._single_output:
                    for list_element in result_list:
                        #self._output_object.submit('error_port',{'__spl_po':memoryview(pickle.dumps(list_element))})
                        # print store writeToFile whatever
                        pass
                else:
                    tracer.error("Internal error: Single output configured but error_list generated. ")
            else:
                tracer.error("Internal error: More result lists generated than supported. ")



#################################################
# define callable source generator class
#################################################
class SourceGeneartor():
    def __init__(self):
        pass
        
    def __call__(self):
    
        yield None
    




#################################################
# WmlPerformanceTester class
# 
# 
#################################################
class WmlPerformanceTester():

    #################################################
    # Set WmlBundlerResthandler class variables
    #################################################
    
    
    #################################################
    # define input data list and its lock
    #################################################
    


    #################################################
    # define thread control variables
    #################################################


    
    #################################################
    # __init__
    #################################################
    def __init__(self):
        #create input thread
        
        #create starting handler threads
                      
        pass
    


    #################################################
    # thread source function using the source generator
    #################################################
    
    
    
    #################################################
    # thread handler function using WmlBundleResthandler
    #################################################
    
    
    
    
#################################################
# Jupyter notebook GUI for WmlPerformanceTester
#
# it just uses the interfaces of WmlPerformanceTester
# for control and gettings results back
#################################################
class WmlPerformanceTesterGui(WmlPerformanceTester):

    #################################################
    # 
    #################################################

    
