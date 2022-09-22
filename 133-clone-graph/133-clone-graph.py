"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        newNode = Node(node.val)
        q  = [(node, newNode)]
        seen = {node:newNode}
        
        while q:
            old, new = q.pop()
            for nei in old.neighbors:
                if nei not in seen:
                    newNei = Node(nei.val)
                    new.neighbors.append(newNei)
                    q.insert(0, (nei, newNei))
                    seen[nei] = newNei
                else:
                    newNei = seen[nei]
                    new.neighbors.append(newNei)
                    
        return newNode
                    
                    
                
            