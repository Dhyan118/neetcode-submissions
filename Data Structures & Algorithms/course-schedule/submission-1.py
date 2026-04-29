class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        # map each course to its prerequisite list
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visitSet = all courses along the current DFS path
        visitSet = set()

        def dfs(crs):
            # if course already in current path, cycle detected
            if crs in visitSet:
                return False
            # if no prerequisites, course can be finished
            if preMap[crs] == []:
                return True

            # mark current course as being visited
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            # remove from current path after exploring
            visitSet.remove(crs)
            # mark course as completed (no more prerequisites)
            preMap[crs] = []
            return True

        # check all courses
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
