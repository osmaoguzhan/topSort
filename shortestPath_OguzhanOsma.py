#Code has been taken from Geeksforgeeks and updated
from collections import defaultdict
import time
class myGraph:
	def __init__(self,vertices):
		self.V = vertices
		self.graph = defaultdict(list)
	def edge(self,u,v,w):
		self.graph[u].append((v,w))
	def topologicalSortUtil(self,v,visited,stack):
		visited[v] = True
		if v in self.graph.keys():
			for node,weight in self.graph[v]:
				if visited[node] == False:
					self.topologicalSortUtil(node,visited,stack)
		stack.append(v)
	def shortestPath(self, s):
		visited = [False]*self.V
		stack =[]
		for i in range(self.V): # Sort starting from source vertice
			if visited[i] == False:
				self.topologicalSortUtil(s,visited,stack)
		dist = [float("Inf")] * (self.V)# Initialize distances to all vertices as infinite and distance to source as 0
		dist[s] = 0
		while stack:
			i = stack.pop()# Get the next vertex
			for node,weight in self.graph[i]:# Update distances
				if dist[node] > dist[i] + weight:
					print("\rCurrent Distances: " + str(dist),end="")
					dist[node] = dist[i] + weight
					time.sleep(2)
		print("\rResult: " +str(dist),end="")


g = myGraph(6)
g.edge(0, 1, 2)
g.edge(0, 2, 1)
g.edge(1, 2, 4)
g.edge(1, 4, 3)
g.edge(2, 3, 6)
g.edge(3, 4, 1)
g.edge(3, 5, 2)
g.edge(4, 5, 1)

s = 0 #For source 0
print("-------------------------------------")
print("Sorted")
print("-------------------------------------")
g.shortestPath(s)

