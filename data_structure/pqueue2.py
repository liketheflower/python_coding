try:     
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put((10,'ten','adf'))
q.put((10,'one'))
q.put((5,'five'))
while not q.empty():
    print q.get(),
