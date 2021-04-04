import csv
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt
import sys


class CityNotFoundError(Exception):
    def __init__(self, city):
        print("%s does not exist" % city)


# Implement this function to read data into an appropriate data structure.
def build_graph():
   pass

# Implement this function to perform uniform cost search on the graph.
def uniform_cost_search(graph, start, end):
    visited = set()
    queue = PriorityQueue()
    queue.put((0, start))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == end:
                print(end,"is",cost,"km away from",start)
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    m =graph.get_edge_data(node,i )
                    #s=nx.convert.to_edgelist(graph)
                    
                    #s=nx.shortest_path(G,"Antalya","Ankara")
                    #if(k[1].len>5):
                        #p = k[1]
                    #print(m)
                    total_cost = cost + int(m["weight"])
                    
                   #print(i)
                    #print(node)
                    queue.put((total_cost, i))
                    print(total_cost,i)
                       
                    
                    

# Implement main to call functions with appropriate try-except blocks
if __name__ == "__main__":
    filename = "cities.csv"
    fields = []
    rows = []
    try:
        with open(filename, 'r',encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
        # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
          
        # get total number of rows
        n = csvreader.line_num   
       #print(n)
       #print("Total no. of rows: %d"%(csvreader.line_num))
       #print(rows[0][1])
            
        G = nx.Graph()
        for i in range(len(rows)):
            G.add_edge(rows[i][0], rows[i][1],weight=rows[i][2] )
              
            #print(rows[i][2])
               
        #☻G.add_edge(1, 2, weight=4.7 )
            
    
            
       # print(list(G.nodes()))
            
        pos = nx.spring_layout(G)
            
        nx.draw(G, pos, font_size=10, with_labels=True)
             
            
        nx.draw_networkx_edge_labels(G,pos,font_size=8,edge_labels = nx.get_edge_attributes(G,'weight')) 
          # nx.draw_networkx_labels(G, pos)
        plt.show()
        uniform_cost_search(G, "Ankara","Antalya")
    except:
          print("An exception occurred")
#main(sys.argv)
    
