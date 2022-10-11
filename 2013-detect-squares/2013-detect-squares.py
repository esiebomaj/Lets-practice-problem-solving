from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.x = {}
        self.y = {}
        self.counts = defaultdict(int)
        

    def add(self, point: List[int]) -> None:
        # print("ADD")
        self.counts[tuple(point)] += 1
        if point[0] in self.x:
            self.x[point[0]].add(tuple(point))
        else:
            self.x[point[0]] = set([tuple(point)])
            
        if point[1] in self.y:
            self.y[point[1]].add(tuple(point))
        else:
            self.y[point[1]] = set([tuple(point)])
        

    def count(self, point: List[int]) -> int:
        if point[0] not in self.x or point[1] not in self.y:
            return 0
        
        count = 0
        for x,y in self.x[point[0]]:
            for x1,y1 in self.y[point[1]]:
                if ( x1,y in self.x[x1]) and (abs(point[0]-x1) == abs(y-point[1])) and [x1,y] != point:
                    count += self.counts[tuple([x1,y])] * self.counts[tuple([x1,y1])] * self.counts[tuple([x,y])]
        return count
                    
        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)