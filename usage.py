from flask import Flask, request
import gc
import multiprocessing


app = Flask('__name__')
arr = list()
memoryProcess = None

   

def use_memory(mode, arr):
    
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

    manipulating_arr = [False]
    while(True):
        a = 1


@app.route('/')
def index():
    return "Hello world"
@app.route('/push-memory')
def push_memory():
    mode = request.args.get('mode', type = str, default = 'zero')
    global memoryProcess
    if(memoryProcess):
        memoryProcess.terminate()
        memoryProcess = None
    memoryProcess = multiprocessing.Process(target = use_memory, args = (mode, arr))
    memoryProcess.start()
    
    return f"pushing memory in mode {mode}"
    



if __name__ == '__main__':
    memoryProcess = None
    app.run()
    if(memoryProcess):
        memoryProcess.terminate()




