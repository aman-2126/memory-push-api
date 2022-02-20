import threading
import ctypes
import time
import gc
class memory_thread(threading.Thread):
    def __init__(self, name, mode, arr):
        threading.Thread.__init__(self)
        self.name = name
        self.mode = mode
        self.arr = arr
             
    def run(self):
        arr = self.arr
        mode = self.mode
        arr_len = 0
        if mode == 'zero':
            arr_len = 0
        elif mode == 'low':
            arr_len = 2
        elif mode == 'med':
            arr_len = 15
        elif mode == 'high':
            arr_len = 40

        a = list()
        i = 0
        try:
            while (len(a) < arr_len*1024*1024):
                a.append(i)
                i += 1
        except Exception as error:
            print("ran out of memory")
        finally:
            while(len(arr) > 0):
                arr.pop(0)
            gc.collect()
            arr.append(a)
          
    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
 