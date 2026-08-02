class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        x = len(asteroids)
        stack = []
        i = 0
        while i < x:
            num = asteroids[i]
            # append condition
            # first ast. or not colliding
            if len(stack) == 0 or (not (num < 0 and stack[-1] > 0)):
                stack.append(num)
                i+=1
            else:
                # while loop to handle collisions
                if abs(num) > stack[-1]:
                    stack.pop()
                elif abs(num) == stack[-1]:
                    stack.pop()
                    i += 1
                elif abs(num) < stack[-1]:
                    i += 1
                            
        return stack