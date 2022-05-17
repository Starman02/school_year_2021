import pickle

d_dict = {'name': 'Shaymin', 'health': 90, 'power': 28, 'filename': 'shaymin.png'}

dunsp_data = open('003.dat', 'wb')
pickle.dump(d_dict, dunsp_data)
