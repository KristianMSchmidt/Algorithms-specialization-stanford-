"""
Naive experiment in implementing a hash table using a (bad) hash function.
"""
import random

input_data = (("Adam", 12), ("Cat", 34), ("Bob",50), ("Sadnam",61), ("Kirsten",37))

def hash(name):
    """
    hash functions has to be deterministic, but a more "random" function would be better
    """
    return len(name)

def make_hash_table(data):
    buckets = []
    for dummy in range(len(data)*2):
        buckets.append(None)
    for x in input_data:
        name, age = x
        key = hash(name)
        if buckets[key] is None:
            buckets[key] = [x]
        else:
            buckets[key].append(x)
    return buckets

hash_table = make_hash_table(input_data)

#How old is Adam?
def get_age(name):
    bucket = hash_table[hash(name)]
    if len(bucket) == 1:
        print bucket[0][1]
    else:
        for element in bucket:
            if element[0] == name:
                print element[1]

get_age("Adam")
get_age("Cat")
