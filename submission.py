import csv
from queue import PriorityQueue
#import networkx as nx
#import matplotlib.pyplot as plt

class CityNotFoundError(Exception):
    def __init__(self, city):
        self.city = city
        print("%s does not exist" % city)

class PathNotFoundError(Exception):
    def __init__(self, path):
        self.path = path
        print("%s does not exist" % path)

class GraphNode:
	def __init__(self, name):
		self.name = name
		self.neighbors = []
	def add_neighbor(self, node, weight):
		self.neighbors.append({"neighbor":node,"weight":weight})

class Graph:
	def __init__(self):
		self.nodes = {}
		self.edges = {}
	def __contains__(self, key):
		return key in self.nodes
	def add_vertex(self, node_name):
		new_node = GraphNode(node_name)
		self.nodes[node_name] = new_node
	def add_edge(self, node_name_1, node_name_2, weight=1000000):
		if node_name_1 not in self.nodes:
			self.add_vertex(node_name_1)
		if node_name_2 not in self.nodes:
			self.add_vertex(node_name_2)
		self.nodes[node_name_1].add_neighbor(self.nodes[node_name_2], weight)
		self.nodes[node_name_2].add_neighbor(self.nodes[node_name_1], weight)
		if (node_name_1, node_name_2) not in self.edges and (node_name_2, node_name_1) not in self.edges:
			self.edges[(node_name_1, node_name_2)]={"weight":weight}

	def neighbors(self, node_name):
		the_neighbors = []
		if node_name in self.nodes:
			for n in self.nodes[node_name].neighbors:
				the_neighbors.append(n["neighbor"].name)
		return the_neighbors

	def get_edge_data(self, node_name_1, node_name_2):
		if (node_name_1, node_name_2) in self.edges:
			return self.edges[(node_name_1, node_name_2)]
		elif (node_name_2, node_name_1) in self.edges:
			return self.edges[(node_name_2, node_name_1)]
		else:
			return None

def check_file(path):
    file_found=True
    try:
      f = open(path)
    except IOError:
        file_found=False
    finally:
        return file_found

def check_city_existance(city,G):
    if city not in G:
        raise  CityNotFoundError(city)

# Implement this function to read data into an appropriate data structure.
def build_graph(path):
    fields = []
    rows = []
    if not check_file(path):
        raise PathNotFoundError(path)
    with open(path, 'r',encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
    #my own graph implementation
    G = Graph()
    for i in range(len(rows)):
        G.add_edge(rows[i][0], rows[i][1],weight=rows[i][2])
    #networkx implementation
    '''G = nx.Graph()
    for i in range(len(rows)):
        G.add_edge(rows[i][0], rows[i][1],weight=rows[i][2])'''
    #to draw the graph with netowrkx
    '''pos = nx.spring_layout(G)
    nx.draw(G, pos, font_size=10, with_labels=True)
    nx.draw_networkx_edge_labels(G,pos,font_size=8,edge_labels = nx.get_edge_attributes(G,'weight'))
    plt.show()'''
    return G

# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
    explored = set()
    queue = PriorityQueue()
    queue.put((0, start))
    parents = {start:None}
    while queue:
        cost, node = queue.get()
        if node not in explored:
            explored.add(node)
            if node == end:
                path_to_goal = [node]
                prev_node = node
                while prev_node != start:
                    parent = parents[prev_node]
                    path_to_goal.append(parent)
                    prev_node = parent
                return {"path":path_to_goal,"cost":cost}
            for i in graph.neighbors(node):
            	if i not in explored:
                    m = graph.get_edge_data(node, i)
                    total_cost = cost + int(m["weight"])
                    queue.put((total_cost, i))
                    if i and node is not None:
                        if i in parents:
                           n =graph.get_edge_data(parents[i], i)
                           if int(m["weight"]) >int(n["weight"]):
                               pass
                           else:
                               if i == end:
                                  parents[i]
                               else:
                                   if node in parents:
                                      pass
                                   else:
                                      parents[i] = node
                        else:
                             parents[i] = node

# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    try:
        path = input("Enter your file path: ")
        G= build_graph(path)
        start = input("Enter starting city: ")
        check_city_existance(start,G)
        end = input("Enter target city: ")
        check_city_existance(end,G)
        result = uniform_cost_search(G, start,end)
        print(start,"is", result["cost"],"far away from", end)
        print(result["path"][::-1])
    except :
        pass
