import pickle

test_data = ['Save me!', 123.456, True]

f = file('test.data','w')
pickle.dump(test_data,f)
f.close()
