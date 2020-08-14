"""
Usage of heapq module
#SE officiel python documentation for smarte anvendelser
#https://docs.python.org/2/library/heapq.html

Se her for tips til ,hvordan heapq bruges som max-heap:
 https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
"""

import heapq

q=[]

heapq.heappush(q, (5, 'data5'))

print heapq.heappop(q)
print q

heapq.heappush(q, (5, 'data5'))
heapq.heappush(q, (4, 'data5'))
print q
heapq.heappush(q, (3, 'data5'))
heapq.heappush(q, (2, 'data5'))

heapq.heappush(q, (6, 'data5'))
heapq.heappush(q, (10, 'data5'))
print q
print heapq.heappop(q)



pq=[]

heapq.heappush(pq, 5)

a=[4,6,8,2,1]
heapq.heapify(a)
print a
a.pop()
print a


b= [4,6,8,2]
print "hex"
print heapq.heappush(b, 1)
