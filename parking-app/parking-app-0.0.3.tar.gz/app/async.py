import json
import requests
from requests.auth import *
from _datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import numpy as np
import cv2
import time
import traceback, sys
import mimetypes

from mpipes.common import AuthenticatedConn
from app.utils import local_job_dir, get_job_step_configuration_value

ASYNC = None

class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.

    Supported signals are:

    finished
        No data

    error
        `tuple` (exctype, value, traceback.format_exc() )

    result
        `object` data returned from processing, anything

    progress
        `int` indicating % progress

    '''
    finished = pyqtSignal(str)
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)


class Worker(QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self,  name, fn,  *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        # self.kwargs['progress_callback'] = self.signals.progress

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''

        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            # traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((self.name, exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit(self.name)  # Done


def initAsync( status_widget, log_window):
    global ASYNC
    ASYNC = AsyncComunicator(status_widget, log_window)

def getAsync():
    global ASYNC
    return ASYNC

class AsyncComunicator:

    def __init__(self, status_widget, log_window):
        self.status_widget = status_widget
        self.log_window = log_window
        self.threadpool = QThreadPool()
        self.con = None
        self.mime = mimetypes.MimeTypes()
        # print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

    def getCon(self):
        if not self.con:
            self.con = AuthenticatedConn()
        return self.con

    def reloadCon(self):
        self.con = AuthenticatedConn()

    def addLogText(self, text):
        if self.log_window:
            self.log_window.insertPlainText(text)
            self.log_window.verticalScrollBar().setValue(
            self.log_window.verticalScrollBar().maximum())

    def format_err_response(self, resp):
        status = "Error:"
        try:
            data = json.loads(resp.data.decode())
            status = "{} Http status {} error {}\n".format( str(datetime.now()), data['_status'], str(data['_error']).replace('\n',' '))
        except:
            status = "{} - {}\n".format(str(datetime.now()), resp.reason)
        self.addLogText(status)
        if self.status_widget:
            self.status_widget.showMessage(status)

    def start_info(self, name ):
        msg = "{} - {} - {}\n".format(str(datetime.now()),name, "request starting")
        self.addLogText(msg)
        if self.status_widget:
            self.status_widget.showMessage(msg)

    def finish_info(self, name):
        msg = "{} - {} - {}\n".format(str(datetime.now()), name, "request finished")
        self.addLogText(msg)
        if self.status_widget:
            self.status_widget.showMessage(msg)

    def error_info(self, err_tuple):
        name, exctype, value, formated = err_tuple
        msg = "{} - {} - {}\n".format(str(datetime.now()), name,  formated)
        self.addLogText(msg)
        if self.status_widget:
            self.status_widget.showMessage(msg)


    def communicate(self, name, execute_this_fn, result_fn,  *args, **kwargs):
        self.start_info(name)
        worker = Worker(name, execute_this_fn,  *args, **kwargs)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(result_fn)
        worker.signals.finished.connect(self.finish_info)
        worker.signals.error.connect(self.error_info)
        # Execute
        self.threadpool.start(worker)


    def _list_jobs(self, offset=0, count=-1, page_size=10):
        con = self.getCon()
        rt_items = []
        if count != -1 and page_size > count:
            page_size = count
        while True:
            fileds = {
                'count': page_size,
                'offset': offset
            }
            resp = con.get_request('/api/micropipes/jobs/', fields=fileds)
            if resp.status != 200:
                self.format_err_response(resp)
                return None
            data = json.loads(resp.data.decode())
            items = data['_items']
            if len(items) == 0:
                return rt_items
            rt_items.extend(items)
            offset += len(items)
            if count != -1 and len(rt_items) + page_size > count:
                page_size = count - len(rt_items)
                if page_size == 0:
                    return rt_items

    def list_jobs(self,  result_fn):
        self.communicate("Load jobs",  self._list_jobs, result_fn)

    def _loadLastJobImage(self, job_id):
        con = self.getCon()
        fileds = {
            'from': '-3',
        }
        resp = con.get_request('/api/micropipes/jobs/{}/runtime/files/{}{}'.format(job_id,
                                                                                   'd', '/parking/'),
                               fields=fileds)
        if resp.status != 200:
            self.format_err_response(resp)
            return (None, None, None)
        data = json.loads(resp.data.decode())
        items = data['_items']
        if len(items) == 0:
            return (None, None, None)
        for item in reversed(items):
            if 'entry' in item and str(item['entry']).endswith('checked.jpg'):
                resp = con.get_request(
                    '/api/micropipes/jobs/{}/runtime/files/{}{}{}'.format(job_id,
                                                                          'd', '/parking/',
                                                                          item['entry']))
                if resp.status != 200:
                    self.format_err_response(resp)
                    return (None, None, None)
                arr = np.asarray(bytearray(resp.data), dtype=np.uint8)
                if (arr is None or arr.size == 0):
                    return (None, None, None)
                img = cv2.imdecode(arr, -1)
                return (img, item['entry'], item['time'])

    def loadLastJobImage(self, result_fn, job_id):
        self.communicate("Last job {} image".format(job_id), self._loadLastJobImage, result_fn, job_id)

    def _loadJobStats(self, job_id, prec, vals):
        con = self.getCon()
        fields = {
            'from': -1 * int(vals),
        }
        resp = con.get_request('/api/micropipes/jobs/{}/runtime/stats/{}'.format(job_id, prec),
                               fields=fields)
        if resp.status != 200:
            self.format_err_response(resp)
            return None
        data = json.loads(resp.data.decode())
        return data['_items']

    def loadJobStats(self, result_fn, job_id, prec, vals):
        self.communicate("Load job {} stats".format(job_id), self._loadJobStats, result_fn, job_id, prec, vals)


    def _loadJobLogs(self, job_id, level, vals):
        con = self.getCon()
        fields = {
            'start': -1 * int(vals),
        }
        resp = con.get_request('/api/micropipes/jobs/{}/runtime/logs/{}'.format(job_id, level),
                               fields=fields)
        if resp.status != 200:
            self.format_err_response(resp)
            return None
        data = json.loads(resp.data.decode())
        return data['_items']

    def loadJobLogs(self, result_fn, job_id, level, vals):
        self.communicate("Load job {} {} logs".format(job_id, level), self._loadJobLogs, result_fn, job_id, level, vals)


    def _jobStartStop(self, job_id, operation):
        con = self.getCon()
        resp = con.post_request('/api/micropipes/jobs/{}/{}'.format(job_id, operation), None)
        if resp.status != 200:
            self.format_err_response(resp)
            return False
        return True

    def jobStartStop(self, result_fn, job_id, operation):
        self.communicate("Job {} {} ".format(job_id, operation), self._jobStartStop, result_fn, job_id, operation)

    def _jobAdd(self, job_data):
        con = self.getCon()
        resp = con.post_request('/api/micropipes/jobs/', job_data)
        if resp.status != 201:
            self.format_err_response(resp)
            return False
        data = json.loads(resp.data.decode())
        job_id = data['_id']
        job = json.loads(job_data)
        temp_job_id = job['id']
        mapfile = get_job_step_configuration_value(job, 'parking_checker', 'map')
        if self._upload_if_not_exists(job_id, mapfile, temp_job_id=temp_job_id):
            return True
        return False

    def jobAdd(self, result_fn, job_data):
        self.communicate("Creating job", self._jobAdd, result_fn, job_data)

    def _jobEdit(self, job_id, job_data):
        con = self.getCon()
        stopEnsured = False
        retries = 0
        while not stopEnsured and retries < 10:
            self.addLogText('Get status of job {}\n'.format(job_id))
            resp = con.get_request('/api/micropipes/jobs/{}'.format(job_id))
            if resp.status != 200:
                self.format_err_response(resp)
                return False
            data = json.loads(resp.data.decode())
            ojob =  data['_items']
            if ojob['status'] == 'status.stop':
                stopEnsured = True
                continue
            if ojob['status']  == 'status.started':
                # stop it now
                self.addLogText('Will stop job {}\n'.format(job_id))
                resp = con.post_request('/api/micropipes/jobs/{}/stop'.format(job_id), None)
                if resp.status != 200:
                    self.format_err_response(resp)
                    return False
                time.sleep(1)
            retries += 1

        if not stopEnsured:
            self.addLogText('Failed to stop job {}\n'.format(job_id))
            return False
        self.addLogText('Sending job data {}\n'.format(job_id))
        resp = con.put_request('/api/micropipes/jobs/{}'.format(job_id), job_data)
        if resp.status != 200:
            self.format_err_response(resp)
            return False
        # background map fixture
        mapfile = get_job_step_configuration_value(json.loads(job_data), 'parking_checker', 'map')
        if self._upload_if_not_exists(job_id, mapfile):
            return True
        return False

    def jobEdit(self, result_fn, job_id, job_data):
        self.communicate("Edit job", self._jobEdit, result_fn, job_id, job_data)


    def _jobDelete(self, job_id):
        con = self.getCon()
        stopEnsured = False
        retries = 0
        while not stopEnsured and retries < 10:
            self.addLogText('Get status of job {}\n'.format(job_id))
            resp = con.get_request('/api/micropipes/jobs/{}'.format(job_id))
            if resp.status != 200:
                self.format_err_response(resp)
                return False
            data = json.loads(resp.data.decode())
            ojob =  data['_items']
            if ojob['status'] == 'status.stop':
                stopEnsured = True
                continue
            if ojob['status']  == 'status.started':
                # stop it now
                self.addLogText('Will stop job {}\n'.format(job_id))
                resp = con.post_request('/api/micropipes/jobs/{}/stop'.format(job_id), None)
                if resp.status != 200:
                    self.format_err_response(resp)
                    return False
                time.sleep(1)
            retries += 1

        if not stopEnsured:
            self.addLogText('Failed to stop job {}\n'.format(job_id))
            return False
        resp = con.delete_request('/api/micropipes/jobs/{}'.format(job_id))
        if resp.status != 200:
            self.format_err_response(resp)
            return False
        return True

    def jobDelete(self, result_fn, job_id):
        self.communicate("Delete job", self._jobDelete, result_fn, job_id)


    def _grab_data(self, img_url, img_url_user, img_url_pass ):
        self.addLogText('{} Connecting to {} as {} with {}\n'.format(str(datetime.now()), img_url, img_url_user, img_url_pass))
        response = requests.get(img_url, auth=HTTPDigestAuth(img_url_user, img_url_pass), verify=False)
        self.addLogText('{} Response status is {} - {}\n'.format(str(datetime.now()), response.status_code, response.reason))
        rt_n = None
        rt_len = 0
        if response.status_code == 200:
            btra = bytearray(response.content)
            rt_n = cv2.imdecode(np.asarray(btra), 1)
            rt_len = len(btra)
        self.addLogText('{} Read {} bytes\n'.format(str(datetime.now()), rt_len))
        return (rt_n, rt_len)

    def grabData(self, result_fn, img_url, img_url_user, img_url_pass):
        self.communicate("Grabbing image", self._grab_data, result_fn, img_url, img_url_user, img_url_pass)


    def _download_used_map(self, job_id, mapfile):
        jdir = local_job_dir(job_id)
        ffname = os.path.join(jdir, mapfile)
        con = self.getCon()
        resp = con.get_request(
            '/api/micropipes/jobs/{}/runtime/files/{}{}{}'.format(job_id,
                                                                  'p', '/parking/',
                                                                  mapfile))
        if resp.status != 200:
            self.format_err_response(resp)
            return None
        else:
            with open(ffname, 'wb') as f:
                f.write(resp.data)
            self.addLogText('Downloaded map {} for job {}\n'.format(mapfile, job_id))
            return ffname

    def download_used_map(self, result_fn, job_id, mapfile):
        self.communicate("Map {} for job {}".format(mapfile, job_id), self._download_used_map, result_fn, job_id, mapfile)

    def _upload_if_not_exists(self, job_id, mapfile, temp_job_id = None):
        if not mapfile or not job_id:
            return False
        con = self.getCon()
        fileds = {
            'from': '0',
        }
        resp = con.get_request('/api/micropipes/jobs/{}/runtime/files/{}{}'.format(job_id,
                                                                                   'p', '/parking/'),
                               fields=fileds)
        if resp.status != 200:
            self.format_err_response(resp)
            return False
        data = json.loads(resp.data.decode())
        items = data['_items']
        if len(items) > 0:
            for item in reversed(items):
                if 'entry' in item and str(item['entry']) == mapfile:
                    self.addLogText('Map {} for job {} already on server\n'.format(mapfile, job_id))
                    return True

        if temp_job_id:
            jdir = local_job_dir(temp_job_id)
        else:
            jdir = local_job_dir(job_id)
        ffname = os.path.join(jdir, mapfile)
        basename = mapfile
        with open(ffname, 'rb') as f:
            binary_data = f.read()
        mime_type = self.mime.guess_type(basename)[0]
        if not mime_type:
            mime_type = 'application/octet-stream'
        headers = {'content-type': mime_type}
        resp = con.post_request(
            '/api/micropipes/jobs/{}/runtime/files/{}{}{}'.format(job_id,
                                            'p','/parking/', basename),
                                        headerz=headers,
                                        payload=binary_data
                                )
        if resp.status != 201:
            self.format_err_response(resp)
            return False
        else:
            self.addLogText('Uploaded map {} for job {}\n'.format(mapfile, job_id))
            return True


    def _loadJobFiles(self, job_id):
        con = self.getCon()
        fileds = {
            'from': '0',
        }
        resp = con.get_request('/api/micropipes/jobs/{}/runtime/files/{}{}'.format(job_id,
                                                                                   'd', '/parking/'),
                               fields=fileds)
        if resp.status != 200:
            self.format_err_response(resp)
            return None
        data = json.loads(resp.data.decode())
        return data['_items']

    def loadJobFiles(self, result_fn, job_id):
        self.communicate("Job {} files".format(job_id), self._loadJobFiles, result_fn, job_id)

    def _download_file(self, job_id, duration, filename):
        jdir = local_job_dir(job_id)
        ffname = os.path.join(jdir, filename)
        con = self.getCon()
        resp = con.get_request(
            '/api/micropipes/jobs/{}/runtime/files/{}{}{}'.format(job_id,
                                                                  duration, '/parking/',
                                                                  filename))
        if resp.status != 200:
            self.format_err_response(resp)
            return None
        else:
            with open(ffname, 'wb') as f:
                f.write(resp.data)
            self.addLogText('Downloaded file {} for job {}\n'.format(filename, job_id))
            return ffname

    def download_file(self, result_fn, job_id,  duration, filename):
        self.communicate("Downloading {} with duration {} for job {}".format(filename, duration, job_id),
                         self._download_file, result_fn, job_id, duration, filename)