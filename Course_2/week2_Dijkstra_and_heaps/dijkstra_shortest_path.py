"""
Dijkstra's shortest path algorith for weighted paths with non-negative edge lengths.
3/1 2018.
"""


def build_graph_from_file():
    """
    Load data and build undirected weighted graph with desired data_structure.
    graph = {1: {2:1, 3:4}, 2:{3:2, 4:6}, 3:{4:3}, 4:{}}
            {tail1: {head1: dist_from_tail_to_head1, head2: ... }, tail2:....}
    """

    fh = open('dijkstraData.txt')
    data = fh.read()
    print "Read data from file"
    data_lines = data.split('\n')
    data_lines =  data_lines[:-1]

    graph = {}

    for line in data_lines:
        line = line.split()
        head = int(line[0])
        tail_dict = {}
        for edge_str in line[1:]:
            edge = edge_str.split(',')
            tail_dict[int(edge[0])] = int(edge[1])
        graph[head] = tail_dict

    return graph

real_graph = build_graph_from_file()

#graph1 = {1: {2:1, 3:4}, 2:{3:2, 4:6}, 3:{4:3}, 4:{}}
#print graph1[1]
#expected = {1:0, 2:1, 3:3, 4:6}

def naive_dijkstra1(graph, source):
    """
    Takes a weighted graph and a source node and returns a dictionary with shortest paths from
    the source to each node in the graph.
    answer = {node: length_of_shortest_path_from_source_to node, ....}.
    I want the algorithm to work on graphs with/without parallel edges
    I may assume that the graph is undirected - if convinient
    If there is no path between source and node, then distance is 1000000
    """

    answer = {source: 0}
    max_num_iterations = len(graph)
    indx = 1

    while indx < max_num_iterations:
        min_score = float('inf')
        selected_head = None
        for node, dijkstra_score in answer.items():
            for head in graph[node]:
                if head not in answer:
                    pot_score = dijkstra_score + graph[node][head]
                    if pot_score < min_score:
                        min_score = pot_score
                        selected_head = head

        if selected_head is None:
            break

        if selected_head != None:
            answer[selected_head] = min_score
        indx += 1

    for node in graph:
        if node not in answer:
            answer[node] = 1000000

    return answer

def naive_dijkstra2(graph, source):
    """
    Takes a weighted graph and a source node and returns a dictionary with shortest paths from
    the source to each node in the graph.
    answer = {node: length_of_shortest_path_from_source_to node, ....}.
    I want the algorithm to work on graphs with/without parallel edges
    I may assume that the graph is undirected - if convinient
    If there is no path between source and node, then distance is 1000000
    """

    answer = {source: 0}
    max_num_iterations = len(graph)
    indx = 1

    while indx < max_num_iterations:
        min_score = float('inf')
        selected_head = None
        for tail, heads in graph.items():
            if tail in answer:
                for head in heads:
                    if head not in answer:
                        pot_score = answer[tail] + graph[tail][head]
                        if pot_score < min_score:
                            min_score = pot_score
                            selected_head = head

        if selected_head is None:
            break
        else:
            answer[selected_head] = min_score
        indx += 1

    for node in graph:
        if node not in answer:
            answer[node] = 1000000

    return answer

graph1 = {2:{3:2, 4:6}, 3:{4:3}, 4:{},1: {2:1, 3:4}}
#print graph1[1]
#print dijkstra(graph1,1)

def dijkstra2(graph, source):
    """
    Fast implementation using heaps.
    Or, actually, this implementation is slower on my dataset, since heapq does not suppert O(log(n)) removal
    of arbitrary elements from heap (which I need).
    But it works.

    """
    import heapq
    heap = []
    heap_elements = [node for node in graph.keys() if node != source]
    answer = {source: 0}

    #Nedenstaaende kunne goeres hurtigere, hvis jeg med det samme havde genmt alle in-arrows til alle elementer
    for x in heap_elements:
        score = float('inf')
        for node, dist in answer.items():
            for head in graph[node]:
                if head == x:
                    gready_dijkstra_score_of_edge = dist + graph[node][head]
                    score = min(score, gready_dijkstra_score_of_edge)
        heapq.heappush(heap, (score, x))

    #Now both invariants are satisfied

    max_num_iterations = len(graph)

    indx = 1

    while indx < max_num_iterations:
        #print "looop number:", indx
        #print "Heap before loop", heap
        score, next_node = heapq.heappop(heap)
        #print "Next node: {} with score {}".format(next_node, score)
        answer[next_node] = score
        #print "Answer after above result got added", answer
        for head in graph[next_node]:
            if head not in answer: ##i.e. head is in the heap
                #print "Maintaining head number:", head
                #print "current heap", heap
                #Nedenstaeende er langsomt: Det tager lineaer tid at finde det rigtige sted i heapen...boer kunne goeres hurtigere. Hvad er tricket?
                for indx2 in range(len(heap)):
                    if heap[indx2][1] == head:
                        #print "the case"
                        old_score_of_head = heap[indx2][0]
                        #The next to lines are not optimal, timewise. heapq does not support the operation I need - namely removal
                        #arbitrary elements from the heap.
                        # Maybe -I could use HeapDict instead for better performance
                        heap.pop(indx2)
                        heapq.heapify(heap)
                        score_head = min(old_score_of_head, answer[next_node] + graph[next_node][head])
                        heapq.heappush(heap, (score_head, head))
                        #print heap
        #print "Heap after maintanance ", heap
        indx +=1
        #print ""
        #print ""
        #print heap, indx
    for node in answer:
        if answer[node] == float('inf'):
            answer[node] = 1000000

    return answer

#print dijkstra(graph1, 3)


def dijkstra(graph, source):
    """
    Fast implementation using heaps.
    This version solves two of the problem in the above implemtation: I simply don't remove elements - I just
    push new elements with same value (but possible different key) into heap. This is okay as long as make a check
    when extracting min.
    """
    import heapq
    heap = []
    heap_elements = (node for node in graph if node != source)
    answer = {source: 0}
    #not_in_answer = set(graph)
    #not_in_answer.remove(source)

    # Initialize heap (could be done faster using heapify)
    for x in heap_elements:
        score = float('inf')
        for node in answer:
            for head in graph[node]:
                if head == x:
                    gready_dijkstra_score_of_edge = answer[node] + graph[node][head]
                    score = min(score, gready_dijkstra_score_of_edge)
        heapq.heappush(heap, (score, x))
    #Now both invariants are satisfied

    max_num_iterations = len(graph)

    indx = 1

    while indx < max_num_iterations:
        next_node = source
        while next_node in answer:
            score, next_node = heapq.heappop(heap)
        answer[next_node] = score
        #not_in_answer.remove(next_node)
        for head in graph[next_node]:
            #if head in not_in_answer
            if head not in answer: ##i.e. head is in the heap
                score_head = answer[next_node] + graph[next_node][head]
                heapq.heappush(heap, (score_head, head))
        indx +=1

    for node in answer:
        if answer[node] == float('inf'):
            answer[node] = 1000000
    return answer




def answer_assignment():
    # d = naive_dijkstra1(real_graph, 1)
    # print d[7], d[37], d[59], d[82], d[99], d[115], d[133], d[165], d[188], d[197]
    # d = naive_dijkstra2(real_graph, 1)
    # print d[7], d[37], d[59], d[82], d[99], d[115], d[133], d[165], d[188], d[197]
    d = dijkstra(real_graph, 1)
    print d[7], d[37], d[59], d[82], d[99], d[115], d[133], d[165], d[188], d[197]

    # nodes = [7,37,59,82,99,115,133,165,188,197]
    #
    # filehandle = open('results.txt', 'w')
    #
    # s = ""
    # for node in nodes:
    #     s += str(d[node])+" "
    # #print s
    # filehandle.write(s)
    # filehandle.close()

answer_assignment()
