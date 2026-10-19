from collections import deque
from typing import List


class Solution:

  def findOrder(
      self, numCourses: int, prerequisites: List[List[int]]
  ) -> List[int]:
    # Step 1: Initialize adjacency list and in-degree tracking
    adj = {i: [] for i in range(numCourses)}
    in_degree = [0] * numCourses

    # prerequisites[i] = [course, prerequisite]
    # We must take 'prereq' before 'course' -> directed edge: prereq -> course
    for course, prereq in prerequisites:
      adj[prereq].append(course)
      in_degree[course] += 1

    # Step 2: Add all courses with 0 prerequisites to the queue
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []

    # Step 3: Process courses level by level
    while queue:
      node = queue.popleft()
      order.append(node)

      for neighbor in adj[node]:
        in_degree[neighbor] -= 1
        # When all prerequisites for this course are satisfied
        if in_degree[neighbor] == 0:
          queue.append(neighbor)

    # If all courses could be ordered, return the order; otherwise, a cycle exists
    return order if len(order) == numCourses else []