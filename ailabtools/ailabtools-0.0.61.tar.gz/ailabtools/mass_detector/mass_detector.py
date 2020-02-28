import os
import time
import requests
import multiprocessing
from multiprocessing import Process, Queue, Lock, Value
from glob import glob
import numpy as np
from multiprocessing import Process, Queue, Value
import traceback
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

class mass_detector:
    def __init__(self, 
                 input_data, 
                 gpu_schedule, 
                 batch_size=1, 
                 num_producer=5, 
                 max_queue_batch_len=10, 
                 num_verbose=1000, 
                 show_warning=True):
        
        """Creat pipeline to use multiple model to predict inputs data

        Parameters
        ----------
        input_data: list
            list of input data to process
        gpu_schedule: list
            list of GPUs name for each model
        batch_size: int
            batch_size for model predict
        num_producer: int
            number of producer to process input data before feed to model
        max_queue_batch_len: int
            maximum queue len of batch between producers and consumers
        num_verbose: int
            show process after process num_verbose input
        show_warning: bool
            show warning if consumer is faster than producer

        Returns
        -------
        Class to inherit for specific demand
        To use must implement these functions:
        
        func get_item:
            Parameters
            ----------
            index: index of item in input_data
            Returns
            -------
            processed item
        
        func batch_from_items:
            Parameters
            ----------
            items: list of items get from function get_item
            Returns
            -------
            batch created by items to feed for model

        func load_model:
            Parameters
            ----------
            This function have no input
            Use this function to load model and config GPU usage
            Returns
            -------
            model to predict batch return by batch_from_items

        func predict:
            Parameters
            ----------
            model: output of load_model function
            batch: output of batch_from_items function
            Returns
            -------
            prediction of model to batch

        func save_prediction:
            Parameters
            ----------
            indexs: list of index
            predictions: list of predictions corresponding to indexes
            Use this function to save result
            Returns
            -------
            This function have no output
            
        Example
        class example_mass_detector(mass_detector):
            def get_item(self, index):
                item = self.input_data[index]
                item = preprocess(item)
                return img

            def batch_from_items(self, items):
                return np.array(items)

            def load_model(self):
                import tensorflow as tf
                from keras.backend.tensorflow_backend import set_session
                config = tf.ConfigProto()
                config.gpu_options.per_process_gpu_memory_fraction = 0.4
                set_session(tf.Session(config=config))
                model_path = "path_to_model"
                return load(model_path)

            def predict(self, model, batch):
                return model.predict(batch)

            def save_prediction(self, indexs, predictions):
                np.save("./save_dir/save_time_{}.npy".format(time.time()), {"indexes": indexs, "predictions": predictions})        
        """
        
        self.input_data = input_data
        self.num_input = len(self.input_data)
        self.batch_size = batch_size
        self.gpu_schedule = gpu_schedule
        
        self.num_producer = num_producer
        self.num_consumer = len(self.gpu_schedule)
        
        self.max_queue_batch_len = max_queue_batch_len

        self.data_queue = Queue(self.max_queue_batch_len)
        self.producer_lock = Lock()
        self.counter = Value('i', 0)
        self.producer_done = Value('i', 0)
        self.consumer_done = Value('i', 0)
        
        self.save_queue = Queue(self.max_queue_batch_len)
        
        self.num_verbose = num_verbose
        self.show_warning = show_warning
    #====================================================
    def produce(self):
        while True:
            counter_batch = 0
            items = []
            indexes = []
            current_producer_done = False
            while True:
                #get item index
                with self.producer_lock:
                    index = self.counter.value
                    if index == self.num_input:
                        print('Producer {} done!'.format(self.producer_done.value))
                        self.producer_done.value += 1
                        current_producer_done = True
                        break
                    else:
                        self.counter.value += 1

                if index != 0 and index % self.num_verbose == 0:
                    cur_queue_size = self.data_queue.qsize()
                    print('current index: {} \t current queue size: {}'.format(index, cur_queue_size))
                    
                    if self.show_warning and cur_queue_size < int(0.1 * self.max_queue_batch_len):
                        print("WARNING: current queue size is too low, consumers is faster producers!")
                
                #try get item by index
                try:
                    item = self.get_item(index)
                    indexes.append(index)
                    items.append(item)
                    counter_batch += 1
                except Exception as e:
                    print('producer error:', e)
                    traceback.print_exc()
                    
                #stop when enough batch size
                if counter_batch == self.batch_size:
                    break

            if len(items) > 0:
            
                #items to batch
                batch = self.batch_from_items(items)

                #put batch to queue include indexs to know input
                self.data_queue.put((indexes, batch))
            
            #print('current queue size:', self.data_queue.qsize())
            
            if current_producer_done:
                break
            
    def get_item(self, index):
        raise NotImplementedError
    
    def batch_from_items(self, items):
        raise NotImplementedError
    
    
    #====================================================
    def consum(self, gpu_index):
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = gpu_index
        print('start load model on GPU: {}'.format(gpu_index))
        model = self.load_model()
        print('load done')
        while True:
            get_batch_success = False
            try:
                indexes, batch = self.data_queue.get(timeout=1)
                get_batch_success = True
            except multiprocessing.queues.Empty:
                if self.producer_done.value == self.num_producer:
                    if gpu_index == "":
                        print('''Consumer use cpu done!''')
                    else:
                        print('''Consumer use gpu {} done!'''.format(gpu_index))
                    self.consumer_done.value += 1
                    break
                else:
                    continue
            except Exception as e:
                print('Unexpected dequeue problem:', e)
                traceback.print_exc()
            
            if get_batch_success:
                try:
                    predictions = self.predict(model, batch)
                    self.save_queue.put((indexes, predictions))
                except Exception as e:
                    print('Consumer error:', e)
                    traceback.print_exc()

    
    def load_model(self):
        raise NotImplementedError
    
    def save_prediction(self, indexs, predictions):
        s ='''Not implement function save_prediction(self, indexs, predictions) error
        function use to save result
        input:
            indexs: index of items in batch
            predictions: result predicted of item corresponding to indexs
        output:
            return prediction
        '''
        print(s)
        raise NotImplementedError
        
    def predict(self, model, batch):
        s ='''Not implement function predict(self, model, batch) error
        function describe how to use model predict batch of input
        input:
            model: model use to predict
            batch: batch of input 
        output:
            return prediction
        '''
        print(s)
        raise NotImplementedError
    
    #=====================================================
    def saver(self):
        while True:
            try:
                indexes, predictions = self.save_queue.get(timeout=1)
                self.save_prediction(indexes, predictions)
            except multiprocessing.queues.Empty:
                if self.consumer_done.value == self.num_consumer:
                    print('Saver done!')
                    break
                else:
                    continue
            except Exception as e:
                print('Saver error:', e)
                traceback.print_exc()
            
    
    #=====================================================
    def run(self):
        ps = []
        #init producer
        for _ in range(self.num_producer):
            p = Process(target=self.produce)
            ps.append(p)
            
        #init consumer
        for gpu_index in self.gpu_schedule:
            p = Process(target=self.consum, args=(gpu_index,))
            ps.append(p)
            
        p = Process(target=self.saver)
        ps.append(p)
        
        # start
        for p in ps:
            p.start()
            
        for p in ps:
            p.join()
            
        self.counter.value = 0
        self.producer_done.value = 0
