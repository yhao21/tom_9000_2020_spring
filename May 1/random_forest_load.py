import pickle


with open('serialized_random_forest.pkl', 'rb') as f:
    machine = pickle.load(f)

new_data = [
	[0.9,2.15,-1.0,-4.0,-6.7,-0.12,3.40,3.64,1.75,11.9,15.2,-15,1.24,4,-8.0,9.62,14.1,-9.0,15.3,22.1,-0.52,4.91,-7.5,2.70,-3.2,0.947,1.90,-7.9,12,0.312],
	[0.011,1.08,0.8964,3.225,-.885,1.487,2.596,-14.8,-1.04,4.566,-10.0,9.141,-0.923,1.006,-2.87,1.994,3.103,-4.51,1.984,0.4903,3.534,11.03,0.0957,-3.89,12.13,9.445,5.488,5.631,-3.14,7.871],
	[0.980,0.380,0.852,0.344,2.41,2.16,5.93,-20,2.14,2.01,13.9,-.5,.310,-6.9,1.75,.455,-12,32.3,-3.8,1.27,-0.79,-0.08,-4.9,6.95,0.561,25.0,-1.2,0.676,13.5,2.32]
	]

print(machine.predict(new_data))
"""[3 2 2]"""
"""now, even if we do not import sklean, we can run this machine. and run it super fast"""