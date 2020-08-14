"""
Tallene i opgaven er ligeligt fordelt i intervallet
"""
import matplotlib.pyplot as plt

def make_list_from_data():
    fh = open('million_integers.txt')
    data = fh.read()
    data_lines = data.split('\n')
    data_lines = data_lines[:-1]
    return [int(num) for num in data_lines]

integers = make_list_from_data()

def plot_data():
    interval = (max(integers) - min(integers))/30

    freqs = {}
    for integer in integers:
        klynge = integer/interval
        freqs[klynge] = freqs.get(klynge, 0) + 1
    #print freqs
    x_vals =[]
    y_vals = []
    for key, val in freqs.items():
        x_vals.append(key)
        y_vals.append(val)
    plt.bar(x_vals, y_vals)

    plt.show()

plot_data()

#print "Average number of integers in each bucket:", float(20000)/(max(integers) - min(integers))*len(integers)
