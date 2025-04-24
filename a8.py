from neural import *

print("<<<<<<<<<<<<<< XOR >>>>>>>>>>>>>>\n")


train_data_raw = "|0.9|0.6|0.8|0.3|0.1|1.0|;|0.8|0.8|0.4|0.6|0.4|1.0|;|0.7|0.2|0.4|0.6|0.3|1.0|;|0.5|0.5|0.8|0.4|0.8|0.0|;|0.3|0.1|0.6|0.8|0.8|0.0|;|0.6|0.3|0.4|0.3|0.6|0.0|"

test_raw_data = "|1.0|1.0|1.0|0.1|0.1|;|0.5|0.2|0.1|0.7|0.7|;|0.8|0.3|0.3|0.3|0.8|;|0.8|0.3|0.3|0.8|0.3|;|0.9|0.8|0.8|0.3|0.6|"

def proccess_raw_data(data):
    proccessed_data = []
    t = data.split(";")
    for item in t:
        x = item.split("|")
        tempy = []
        for y in x:
            if y != "":
                tempy.append(float(y))
        proccessed_data.append(tempy)
    return proccessed_data

train_data = proccess_raw_data(train_data_raw)
test_data = proccess_raw_data(test_raw_data)

train_data = [(i[:5], [i[5]]) for i in train_data]




neural_net = NeuralNet(5, 15, 1)


neural_net.train(train_data)

print(neural_net.test(test_data))
