from flask import Flask, request
import gc
app = Flask('__name__')

arr = list()


@app.route('/')
def index():
    return "Hello world"


@app.route('/low')
def low():
    a = list()
    i = 0
    try:
        while(len(a) < 1024*1024*4):
            i += 1
            a.append(i)
    except Exception as error:
        print("ran out of memory")
    finally:
        while(len(arr) > 0):
            arr.pop(0)
        gc.collect()
        arr.append(a)

    return "low"


@app.route('/med')
def mid():
    # arr = list()
    a = list()
    i = 0
    try:
        while(len(a) < 1024*1024*10):
            i += 1
            a.append(i)
    except Exception as error:
        print("ran out of memory")
    finally:
        while(len(arr) > 0):
            arr.pop(0)
        gc.collect()
        arr.append(a)

    return "mid"


@app.route('/high')
def high():
    # arr = list()
    a = list()
    i = 0
    try:
        while(len(a) < 1024*1024*40):
            i += 1
            a.append(i)
    except Exception as error:
        print("ran out of memory")
    finally:
        while(len(arr) > 0):
            arr.pop(0)
        gc.collect()
        arr.append(a)
    return "high"


@app.route('/no')
def no():

    print(len(arr))
    try:
        while(len(arr) > 0):
            arr.pop(0)
    except Exception as error:
        print("empty array")
    gc.collect()

    return "no"


if __name__ == '__main__':
    # try:
    #     while(len(arr) < 1024*1024*50):
    #         arr.append(1)
    # except Exception as error:
    #     print("ran out of memory")

    app.run()
