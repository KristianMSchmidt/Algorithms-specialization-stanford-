"""
Implementation of two multiplication algorithms: The standard school algorithm and Karatsuba's algorithm
Krms 28/12
"""
import math
import matplotlib.pyplot as plt
import time
import random

number_of_calls=0

def karatsuba(x, y):
    """
    This is multiplication by Karatsuba's algorithm.
    Recursive - divide and conquer.
    NB: Requires to numbers of same length

    Divide x into a(first half of digits) and b (second half of digits)
    Divide y into c(first half of digits) and d (sec. half of digits)
    """
    global number_of_calls
    number_of_calls +=1
    #base case:
    if x < 10 or y < 10:
        return x*y

    if len(str(x)) >= len(str(y)):
        max_len = len(str(x))
        if max_len%2:
            n_half = int(math.ceil(max_len/2))
        else:
            n_half = int(max_len/2)
        #print (n_half)

        num = len(str(x))-n_half

        a = int(str(x)[:num])
        b = int(str(x)[num:])

        if len(str(y)) <= n_half:
            c = 0
            d = y
        else:
            num = len(str(y))-n_half
            c = int(str(y)[:num])
            d = int(str(y)[num:])

    else:
        max_len = len(str(y))
        if max_len%2:
            n_half = int(math.ceil(max_len/2))
        else:
            n_half = int(max_len/2)

        num = len(str(y))-n_half

        c = int(str(y)[:num])
        d = int(str(y)[num:])

        if len(str(x)) <= n_half:
            a = 0
            b = x
        else:
            num = len(str(x))-n_half
            a = int(str(x)[:num])
            b = int(str(x)[num:])
    #print (x, a, b)
    #print (y, c, d)

    first_term = karatsuba(a,c)
    second_term = karatsuba(b,d)
    third_term = karatsuba(a + b, c + d)

    return 10**(n_half+n_half) * first_term + 10**n_half *(third_term - first_term - second_term) + second_term

def test():
    tal3 = 3141592653589793238462643383279502884197169399375105820974944592
    tal4 = 2718281828459045235360287471352662497757247093699959574966967627
    tal1 = 12345344444444444444444444444444444444444444444444444444444444444444444444444444444444444
    tal2 = 67844333333333333333333333333333333333333333333333333333333333333333333333333333333333333
    #print ("answer to exercise is:", karatsuba(tal3, tal4))
    karatsuba(tal3, tal4)
    tal1*tal2
    print number_of_calls
test()


def standard_algo(n, m):
    """
    This is the standard school algorithm.
    """
    n_list = list(str(n))
    n_list.reverse()
    m_list = list(str(m))
    m_list.reverse()
    numbers_to_add = []

    num_zeros = -1

    for num1 in n_list:
        #print("num1:{}".format(num1))
        surplus = 0
        powers_of_ten = 0
        number_to_add = 0
        num_zeros +=1
        for num2 in m_list[:-1]:
            #print("num2: {}".format(num2))
            prod = int(num1)*int(num2) + surplus
            #print ("prod {}".format(prod))
            rest = prod%10
            surplus = (prod-rest)//10
            number_to_add += rest*(10**powers_of_ten)
            powers_of_ten += 1
            #print (number_to_add)
        last_num = m_list[-1]
        prod = int(num1)*int(last_num) + surplus
        number_to_add += prod*(10**powers_of_ten)
        number_to_add *= 10**num_zeros
        numbers_to_add.append(number_to_add)

#    print(numbers_to_add)
    return sum(numbers_to_add)

#print ("numbers to add", 7*823, 60*823,500*823)
# n_list =  7 6 5
# m 1 2 3 = 1 2 3
def test():
    print standard_algo(567119999,823569)
    print 567119999*823569
    print "Mere tekst"

#test()



def plot_running_time(number):

    x_vals = []
    y_vals = []
    current_x_val = 0
    current_y_val = 0

    for n in range(number):
        x_ran = random.randrange(10)
        y_ran = random.randrange(10)
        current_x_val = current_x_val*10+x_ran
        current_y_val = current_y_val*10+y_ran
        x_vals.append(current_x_val)
        y_vals.append(current_y_val)
    #print x_vals
    #print y_vals

    plot_x = []
    plot_y = []
    plot_y2 = []
    plot_y3 = []

    for n in range(number):
        plot_x.append(n)

        num1=x_vals[n]
        num2=y_vals[n]

        t0 = time.clock()
        num1*num2
        plot_y.append(time.clock() - t0)

        t0 = time.clock()
        standard_algo(num1,num2)
        plot_y2.append(time.clock() - t0)

        t0 = time.clock()
        karatsuba(num1,num2)
        plot_y3.append(time.clock() - t0)

    plt.plot(plot_x, plot_y, label = "Standard python multiplication")
    plt.plot(plot_x, plot_y2, label = "Grundskole algoritme")
    plt.plot(plot_x, plot_y3, label = "Karatsuba algoritme")

    plt.xlabel("Size of numbers (number of digits)")
    plt.ylabel('CPU running time (sec.)')

    #tegner
    plt.legend()

    plt.title("Comparison of running times for integer multiplication(desktop Python)")

    #goer det hele synligt
    plt.show()


plot_running_time(200)
