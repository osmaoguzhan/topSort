#Code has been taken from Geeksforgeeks
from collections import defaultdict
import time
class myGraph:
	def __init__(self,verts):
		self.graph = defaultdict(list)
		self.V = verts
	def edge(self,u,v): # adding an edge
		self.graph[u].append(v)
	def topSortSub(self,v,visited,queue):
		visited[v] = True #set v's index as visited
		for i in self.graph[v]: # Recursion for all the v's adjacent to this vertex
			if visited[i] == False:
				self.topSortSub(i,visited,queue)
				time.sleep(2)
		#Pushing current vertex to queue
		queue.insert(0,v)
		print("\rCurrent Queue: " + str(queue), end='')
	def topsort(self):
		visited = [False]*self.V #setting all visited nodes False
		queue =[]
		for i in range(self.V):
			if visited[i] == False:#if the node isn't visited yet
				self.topSortSub(i,visited,queue) #run topSortSub func.
		print("\rResult: "+str(queue))
graph = myGraph(5)
graph.edge(0, 1);
graph.edge(0, 4);
graph.edge(1, 2);
graph.edge(3, 1);
graph.edge(3, 2);
graph.edge(4, 1);
graph.edge(4, 3);
print("-------------------------")
print("Sorted")
print("-------------------------")
graph.topsort()
