from flask import Flask, request
import gc
from memory_thread import memory_thread

app = Flask('__name__')
arr = list()
mem_thread = None

   
@app.route('/')
def index():
    return "Hello world"

@app.route('/push-memory')
def push_memory():
    mode = request.args.get('mode', type = str, default = 'zero')
    
    global mem_thread
    if mem_thread:
        mem_thread.raise_exception()
        mem_thread.join()
        mem_thread = None

    mem_thread = memory_thread('mem_thread', mode, arr)
    mem_thread.start()

    
    return f"pushing memory in mode {mode}"
    



if __name__ == '__main__':
    app.run()
    