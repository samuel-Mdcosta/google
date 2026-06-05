class Solution:
    def(self, numCourses:int, prerequisits: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisits
        for a, b in courses:
            g[a].append(b)

        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        def dsf(node):
            state = states[node]
            if state == visited: return True
            elif state == visiting: return False
            state[node] == visiting

            for nei in g[node]:
                if not dsf(nei):
                    return False

            state[node] = visited
            return True
        
        for i in range(courses):
            if not dsf(i):
                return False
        return True