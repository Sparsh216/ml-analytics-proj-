# import requests
import pickle
# url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# response=requests.get(url)
# response_text=response.text
# data=response_text.splitlines()
# red=[[i] for i in data]

# fileobj=open('iris.pkl','wb')
# pickle.dump(red,fileobj)
# fileobj.close()

fileobj=open('iris.pkl','rb')
print(pickle.load(fileobj))
fileobj.close()