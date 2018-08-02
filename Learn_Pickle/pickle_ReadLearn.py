import pickle

f=file('test.data')
test_data=pickle.load(f)
f.close()
print test_data