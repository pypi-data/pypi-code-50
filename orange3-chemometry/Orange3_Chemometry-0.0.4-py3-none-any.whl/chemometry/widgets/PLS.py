from AnyQt import QtCore, QtGui
from AnyQt.QtCore import QThread, pyqtSlot
import Orange.data

import logging

from Orange.widgets.widget import OWWidget
from Orange.widgets.utils.widgetpreview import WidgetPreview
from Orange.widgets.utils.owlearnerwidget import OWBaseLearner
from Orange.base import Learner, Model, SklLearner, SklModel


from Orange.data import ContinuousVariable

from Orange.widgets import gui


from Orange.widgets import settings, gui

from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import LeaveOneOut

import Orange.evaluation

import pyqtgraph as pg

from collections import OrderedDict

from functools import partial


import numpy as np

import concurrent.futures
from Orange.widgets.utils.concurrent import (
    ThreadExecutor, FutureWatcher, methodinvoke
)


class PLSModel(SklModel):
    def predict(self, X):
        vals = self.skl_model.predict(X)
        #print(vals, X)
        if len(vals.shape) == 1:
            # Prevent IndexError for 1D array
            return vals
        elif vals.shape[1] == 1:
            return vals.ravel()
        else:
            return vals
        
    
class PLSLearner(SklLearner):
    __wraps__ = PLSRegression
    supports_weights = False
    
    def __init__(self,  n_components=1, preprocessors=None):
        super().__init__(preprocessors=preprocessors)
        self.params = vars()
        
    def fit(self, X, Y, W):
        model = super().fit(X, Y,W)
        return PLSModel(model.skl_model)




class PRESS_Calculator:
    
    def __init__(self, learner, method, data, W=None, test=None, settings=None, callback = None):
        self._learner = learner
        self._method = method
        self._settings = settings
        self._X = data.X
        self._Y = data.Y
        self._W = W
        self._callback = callback
        if self._callback is None:
            self._callback = lambda a1,a2,a3:None
        
    def calculate(self, params=None):
        if self._method == "leave one out":
            return self._calculate_leave_one_out(params)
        else:
            raise ArgumentError()
        
    def _calculate_leave_one_out(self, params=None):
        if params is None:
            params=dict()
        X = self._X
        Y = self._Y
        W = self._W
        loo = LeaveOneOut()
        errors = []
        for idx, (train_index, test_index) in enumerate(loo.split(X)):
            model = self._learner.fit(X[train_index], Y[train_index], None)
            error = (Y[test_index]-model.predict(X[test_index]))   
            self._callback(params, error, idx/len(X))
            errors.append(error)
        return errors
            
        

class PLSWidget(OWBaseLearner):
    # Widget needs a name, or it is considered an abstract widget
    # and not shown in the menu.
    name = "PLS"
    icon = "icons/mywidget.svg"
    want_main_area = True
    n_components = settings.Setting(1)
    LEARNER = PLSLearner
    max_press_N = settings.Setting(10)
    
    which_method = settings.Setting(0)
    
    
    def __init__(self):
        super().__init__()
        self._task = None
        self._executor = ThreadExecutor()
        #self._presscalculators = OrderedDict()
        self.results = OrderedDict()

        
    def create_learner(self, n_components = None):
        if n_components is None:
            n_components = self.n_components
        return self.LEARNER(n_components= n_components,preprocessors=self.preprocessors)
    
    def get_learner_parameters(self):
        return [self.n_components.value]
    
    def add_main_layout(self):
        want_main_area = True
        box = gui.widgetBox(self.controlArea, "PRESS calculation")
        self.max_press_spinner = gui.spin(box, self, 'max_press_N',
                 minv=0, maxv=90, step=1, label='Max. Components')
        self.radioMethod = gui.radioButtons(box,self, "which_method", btnLabels=("Leave one out"))#, "Split", "Test Data"))
        
        self.recalc_press = gui.button(box, self, "Calculate PRESS", callback=self._calculate_PRESS)
        
        self.component_spinner = gui.spin(self.controlArea, self, 'n_components',
                 minv=0, maxv=90, step=1, label='Number of Components')
        
        
        
        self.plotview = pg.GraphicsView(background="w")
        self.plot = pg.PlotItem(enableMenu=False)
        self.plotdataitem = self.plot.plot([],[])
        self.plot.setMouseEnabled(False, False)
        self.plot.hideButtons()
        
        axis = self.plot.getAxis("bottom")
        axis.setLabel("Components")

        axis = self.plot.getAxis("left")
        axis.setLabel("PRESS")
        
        #self.plot.setRange(xRange=(0.0, 1.0), yRange=(0.0, 1.0), padding=0.05)
        self.plot.enableAutoRange()
        self.plotview.setCentralItem(self.plot)
        self.mainArea.layout().addWidget(self.plotview)
        
        
    def handleNewSignals(self):
        self._update()
        
    
    
    
    @pyqtSlot(concurrent.futures.Future)
    def _task_finished(self, f):
        """
        Parameters
        ----------
        f : Future
            The future instance holding the result of learner evaluation.
        """
        assert self.thread() is QThread.currentThread()
        assert self._task is not None
        assert self._task.future is f
        assert f.done()

        self._task = None
        self.progressBarFinished()

        try:
            results = f.result()  # type: List[Results]
        except Exception as ex:
            # Log the exception with a traceback
            log = logging.getLogger()
            log.exception(__name__, exc_info=True)
            self.error("Exception occurred during evaluation: {!r}".format(ex))
            # clear all results
            for key in self.results.keys():
                self.results[key] = None
        else:
            # split the combined result into per learner/model results ...
            print(results)
            #import ipdb; ipdb.set_trace()
            self.results = results
            x = sorted(results.keys())
            y = [results[key]["PRESS"] for key in x]
            print(x,y)
            self.plotdataitem.setData(x=x,y=y)
    
    @pyqtSlot()
    def _calculate_PRESS(self):
        #print ("update")
        #print (self.data)
        if self._task is not None:
            # First make sure any pending tasks are cancelled.
            self.cancel()
        assert self._task is None
        
        
        
        def callback(finished):
            # check if the task has been cancelled and raise an exception
            # from within. This 'strategy' can only be used with code that
            # properly cleans up after itself in the case of an exception
            # (does not leave any global locks, opened file descriptors, ...)
            if task.cancelled:
                raise KeyboardInterrupt()
            set_progress(finished * 100)
            
        # setup the PRESS calculator evaluations as partial function capturing
        # the necessary arguments.
        
        #make cv selection
        cv = Orange.evaluation.LeaveOneOut()
        use_testdata = False 
        # setup the task state
        self._task = task = Task()
        # The learning_curve[_with_test_data] also takes a callback function
        # to report the progress. We instrument this callback to both invoke
        # the appropriate slots on this widget for reporting the progress
        # (in a thread safe manner) and to implement cooperative cancellation.
        set_progress = methodinvoke(self, "setProgressValue", (float,))
        
        
        
        
        def learning_curve(data, create_learner, Ns, callback=None, test_data=None):
            if callback is not None:
                total_parts = len(Ns)
                callback_wrapped = lambda value: lambda part: callback(
                part/total_parts + value
                )        
                

            else:
                callback_wrapped = lambda part: None
            if callback is None:
                callback = lambda:None
            results = dict()
            if use_testdata:
                pass
            else:
                for idx, N in enumerate(Ns):
                    learner = create_learner(N)
                    pc = PRESS_Calculator(data=data,learner=learner,  method="leave one out")
                    res = pc.calculate()
                    #import ipdb; ipdb.set_trace()
                    print(res, [r.shape for r in res])
                    results[N] = {"PRESS": np.sqrt(np.sum(np.vstack(res)**2))}
            return results
            
        
        Ns = list(range(1, self.max_press_N))
        # capture the callback in the partial function
        learning_curve_func = partial(learning_curve, data=self.data, create_learner= self.create_learner, callback=set_progress, Ns=Ns)
                                      #test_data = self.test_data)
        self.progressBarInit()
        # Submit the evaluation function to the executor and fill in the
        # task with the resultant Future.
        task.future = self._executor.submit(learning_curve_func)
        # Setup the FutureWatcher to notify us of completion
        task.watcher = FutureWatcher(task.future)
        # by using FutureWatcher we ensure `_task_finished` slot will be
        # called from the main GUI thread by the Qt's event loop
        task.watcher.done.connect(self._task_finished)
    
    def _update(self):
        
        if self.data is not None:
            self.max_press_spinner.setMaximum(self.data.X.shape[1])
            print(self.data, self.data.X.shape[1], self.max_press_spinner.maximum())
            if self.n_components > self.data.X.shape[1]:
                self.n_components = self.data.X.shape[1]
        self.learner = self.create_learner(self.n_components)
        if self.data is not None:
            self.model = self.learner.fit(self.data.X,self.data.Y, None)
        else:
            self.model = None
        
     
    #def progressBarSet(self, value):
    #    #print(value)
    #    pass
    
    @pyqtSlot(float)
    def setProgressValue(self, value):
        assert self.thread() is QThread.currentThread()
        self.progressBarSet(value)

    def onDeleteWidget(self):
        self.cancel()
        super().onDeleteWidget()
    
    def cancel(self):
        """
        Cancel the current task (if any).
        """
        if self._task is not None:
            self._task.cancel()
            assert self._task.future.done()
            # disconnect the `_task_finished` slot
            self._task.watcher.done.disconnect(self._task_finished)
            self._task = None


class Task:
    
    cancelled = False  # type: bool
    future = ...       # type: concurrent.futures.Future

    watcher = ...      # type: FutureWatcher
    
    def cancel(self):
        """
        Cancel the task.

        Set the `cancelled` field to True and block until the future is done.
        """
        # set cancelled state
        self.cancelled = True
        # cancel the future. Note this succeeds only if the execution has
        # not yet started (see `concurrent.futures.Future.cancel`) ..
        self.future.cancel()
        # ... and wait until computation finishes
        concurrent.futures.wait([self.future])


if __name__ == "__main__":
    t = np.arange(0,5,.1)
    X = np.vstack((t, t**2,t**3, t**4, np.cos(t), np.sin(t), t, t, t, t, t,t, t, t)).T
    print(X)
    Y = np.atleast_2d(t+ t**3+t**2+ np.cos(t)+t+np.random.randn(*t.shape)).T
    domain = Orange.data.Domain.from_numpy(X=X, Y=Y)
    dataset = Orange.data.Table.from_numpy(X=X, Y=Y, domain = domain)
    WidgetPreview(PLSWidget).run(dataset)
