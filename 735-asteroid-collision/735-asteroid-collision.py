class Solution:
    def sameDirection(self, i,j):
        return (i < 0 and j < 0) or (i> 0 and j >0)
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # strategy 1: use 2 stacks
        stack1 = asteroids
        stack2 = []
        
        while stack1:
            if not stack2 or self.sameDirection(stack2[-1], stack1[-1]) or (stack1[-1]<0 and stack2[-1]>0):
                stack2.append(stack1.pop())
            else:
                x = stack1.pop()
                y = stack2.pop()
                
                
                if abs(x) > abs(y):
                    stack1.append(x)
                if abs(y) > abs(x):
                    stack1.append(y)
                else:
                    pass
                
                
                
        return reversed(stack2)
                        