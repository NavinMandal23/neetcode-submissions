class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        L, R = 0, len(people) - 1
        while L <= R:
            if people[L] + people[R] <= limit:
                print(people[L], people[R])
                L += 1
                R -= 1 
            else:
                print(people[R])
                R -= 1

            boats += 1
        return boats