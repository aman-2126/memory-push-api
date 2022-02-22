import multiprocessing
import time
from flask import Flask, request
import numpy as np

app = Flask(__name__)
processList = list()
def processing():
	while True:
		x = 1000
		A = np.random.rand(200,1000)
		B = np.random.rand(1000,200)

		result = np.random.rand(len(A), len(B[0]))
		for i in range(len(A)):
			for j in range(len(B[0])):
				for k in range(len(B)):
					result[i][j] += A[i][k] * B[k][j]
		time.sleep(0.2)

@app.route('/')
def index():
	mode = request.args.get('mode', type=str, default='low')
	if(mode=='low'):
		while len(processList) > 0:
			processList[0].terminate()
			processList.pop(0)
		process = multiprocessing.Process(target=processing)
		processList.append(process)
		process.start()

	elif(mode=='med'):
		while len(processList) > 0:
			processList[0].terminate()
			processList.pop(0)
		while len(processList) < 3:
			process = multiprocessing.Process(target=processing)
			processList.append(process)
			process.start()
	elif(mode=='high'):
		while len(processList) > 0:
			processList[0].terminate()
			processList.pop(0)
		while len(processList) < 7:
			process = multiprocessing.Process(target=processing)
			processList.append(process)
			process.start()

	return f"pushing cpu in mode {mode}"


if __name__ == '__main__':
	app.run()