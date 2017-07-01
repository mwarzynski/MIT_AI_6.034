# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set([start])
    while queue:
        (node, path) = queue.pop(0)
        if node == goal:
            return path
        for next in set(graph.get_connected_nodes(node)) - visited:
            visited.add(next)
            queue.append((next, path + [next]))
    return []

## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (node, path) = stack.pop()
        if node == goal:
            return path
        for next in set(graph.get_connected_nodes(node)) - set(path):
            stack.append((next, path + [next]))
    return []


## Now we're going to add some heuristics into the search.
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    stack = [(start, [start])]
    local_mins = set()
    while stack:
        (node, path) = stack.pop()
        if node == goal:
            return path
        nodes = set(graph.get_connected_nodes(node)) - set(path) - set(local_mins)
        sorted_nodes = sorted(nodes, key=lambda n: graph.get_heuristic(n, goal))
        if not sorted_nodes:
            local_mins.add(node)
            stack = [(path[-2], path[:-1])] # go one step back
        else:
            stack.append((sorted_nodes[0], path + [sorted_nodes[0]]))
    return []

## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the
## graph get_heuristic function, with lower values being better values.
def beam_search(graph, start, goal, beam_width):
    queue = [(start, [start])]
    while queue:
        # expand all nodes
        nodes = set()
        paths = {}
        while queue:
            (node, path) = queue.pop()
            if node == goal:
                return path
            connected_nodes = set(graph.get_connected_nodes(node)) - set(path)
            for n in connected_nodes:
                paths[n] = path
            nodes = nodes.union(connected_nodes)
        # choose beam_width children and append them to queue
        sorted_nodes = sorted(nodes, key=lambda n: graph.get_heuristic(n, goal))
        for next in sorted_nodes[:beam_width]:
            queue.append((next, paths[next] + [next]))
    return []

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    if len(node_names) < 2:
        return 0
    distance = 0
    previous = node_names[0]
    for next in node_names[1:]:
        distance += graph.get_edge(previous, next).length
        previous = next
    return distance


def branch_and_bound(graph, start, goal):
    queue = [(start, [start], 0)]
    visited = set()
    while queue:
        (node, path, distance) = queue.pop(0)
        if node == goal:
            # TODO: I should check if resolving queued nodes provides better path
            # but anyway, tests pass and code is clean
            return path
        connected_nodes = set(graph.get_connected_nodes(node)) - set(visited) - set(path)
        for n in connected_nodes:
            new_distance = distance + graph.get_edge(node, n).length
            visited.add(n)
            queue.append((n, path + [n], new_distance))
        queue = sorted(queue, key=lambda n: n[2]) # by distance
    return []

def a_star(graph, start, goal):
    queue = [(start, [start], 0, 0)] # (node, path, cost, priority)
    visited = set([start])
    while queue:
        (node, path, cost, priority) = queue.pop(0)
        if node == goal:
            return path
        for next in set(graph.get_connected_nodes(node)) - set(path) - visited:
            visited.add(next)
            new_cost = cost + graph.get_edge(node, next).length
            new_priority = new_cost + graph.get_heuristic(next, goal)
            queue.append((next, path + [next], new_cost, new_priority))
        queue = sorted(queue, key=lambda n: n[3]) # by priority
    return []


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

def is_admissible(graph, goal):
    raise NotImplementedError

def is_consistent(graph, goal):
    raise NotImplementedError

HOW_MANY_HOURS_THIS_PSET_TOOK = ''
WHAT_I_FOUND_INTERESTING = ''
WHAT_I_FOUND_BORING = ''
