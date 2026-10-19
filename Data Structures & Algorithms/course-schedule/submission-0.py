from typing import List


class Solution:

  def canFinish(
      self, numCourses: int, prerequisites: List[List[int]]
  ) -> bool:
    # Step 1: Map each course to its prerequisite list
    # crs -> [prereqs]
    preMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
      preMap[crs].append(pre)

    # Track all courses currently on the current DFS path to detect cycles
    visiting = set()

    def dfs(crs: int) -> bool:
      # Cycle detected: this course is already being visited in the current path
      if crs in visiting:
        return False

      # Base case: course has no prerequisites left (already verified safe)
      if preMap[crs] == []:
        return True

      # Add to path
      visiting.add(crs)

      # Check all prerequisites for the current course
      for pre in preMap[crs]:
        if not dfs(pre):
          return False

      # Backtrack: remove from current path
      visiting.remove(crs)

      # Optimization: mark as completed so we don't repeat DFS for this node
      preMap[crs] = []

      return True

    # Step 2: Check each course (handling disconnected components)
    for crs in range(numCourses):
      if not dfs(crs):
        return False

    return True