"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.
"""
class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edges = []
    
    def get_coords(self):
        return self.x, self.y
    
    def add_edge(self, edge):
        self.edges.append(edge)

    def check_lowest_weight(self, weight):
        for edge in self.edges:
            if edge.weight < weight:
                return False
        return True

    def get_min_edge(self, seen_nodes, cost):
        min_val = float("inf")
        min_edge = None
        seen_node = None
        for edge in self.edges:
            other_node = edge.get_other_node(self)
            weight = edge.compute_manhattan()
            #print(str(seen_nodes.keys()))
            # for key in seen_nodes.keys():
            #     print("keys: ", key.get_coords())
            # print("current node: ", self.get_coords())
            # print("other node: ", other_node.get_coords())
            if (self not in seen_nodes or other_node not in seen_nodes) and weight < min_val:
                #if other_node.check_lowest_weight(weight):
                min_val = weight
                min_edge = edge 
                seen_node = other_node
                    # 
                # print("    min val: ", min_val)
                # print("    seen node: ", seen_node.get_coords())
            elif self in seen_nodes and weight < seen_nodes[self]:
                min_val = weight
                min_edge = edge 
                cost -= seen_nodes[self]
                seen_nodes[self] = weight
                
        #print("=========================END OF MIN EDGE CALL============================")
        if min_val == float("inf"):
            min_val = 0
        seen_nodes[self] = True
        cost += min_val
        return min_edge, min_val, seen_node, seen_nodes, cost

class Edge(object):
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.weight = self.compute_manhattan()
    
    def compute_manhattan(self):
        x1, y1 = self.node1.get_coords()
        x2, y2 = self.node2.get_coords()
        return abs(x1 - x2) + abs(y1 - y2)
    
    def get_other_node(self, node):
        if self.node1.get_coords() == node.get_coords():
            return self.node2
        return self.node1 

class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cost = 0
        if len(points) <= 1:
            return cost
        nodes = []
        for point in points:
            node = Node(point[0], point[1])
            nodes.append(node)
        
        edges = []
        i = 1
        for node in nodes:
            for n in nodes[i:]:
                if node.get_coords() != n.get_coords():
                    edge = Edge(node, n)
                    node.add_edge(edge)
                    n.add_edge(edge)
                    edges.append(edge)

        seen_nodes = {} #nodes[0]: True
        for node in nodes:
            min_edge, min_val, seen_node, seen_nodes, new_cost = node.get_min_edge(seen_nodes, cost) 
            cost = new_cost
            #print("COST DURING LOOP: ", cost)
            if seen_node is not None:
                seen_nodes[seen_node] = min_val
            
        return cost
            
sol = Solution()
print(sol.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(sol.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
print(sol.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]]))