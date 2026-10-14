from collections import defaultdict
import heapq
from typing import List


class Twitter:

  def __init__(self):
    # Global time counter tweets ka order track karne ke liye
    # (har new tweet ke saath decrement karenge taaki min-heap ko max-heap ki tarah use kar sakein)
    self.count = 0

    # userId -> list of [count, tweetId]
    self.tweetMap = defaultdict(list)

    # userId -> set of followeeIds
    self.followMap = defaultdict(set)

  def postTweet(self, userId: int, tweetId: int) -> None:
    # Tweet ko user ki list mein add karte hain current count timestamp ke saath
    self.tweetMap[userId].append([self.count, tweetId])
    self.count -= 1  # Recent tweets ki value zyada negative (smaller) hogi

  def getNewsFeed(self, userId: int) -> List[int]:
    res = []
    minHeap = []

    # User hamesha khud ko follow karta hai taaki khud ke tweets bhi feed mein aayein
    self.followMap[userId].add(userId)

    # Har followee ka sabse recent tweet heap mein push karte hain
    for followeeId in self.followMap[userId]:
      if followeeId in self.tweetMap:
        index = len(self.tweetMap[followeeId]) - 1
        count, tweetId = self.tweetMap[followeeId][index]
        # format: (count, tweetId, followeeId, next_index_to_check)
        minHeap.append([count, tweetId, followeeId, index - 1])

    # Saare recent tweets ko heapify karte hain
    heapq.heapify(minHeap)

    # Top 10 most recent tweets nikaalte hain (Merge K Sorted Lists approach)
    while minHeap and len(res) < 10:
      count, tweetId, followeeId, index = heapq.heappop(minHeap)
      res.append(tweetId)

      # Agar usi user ka aur purana tweet available hai, toh heap mein agla tweet push karo
      if index >= 0:
        count, tweetId = self.tweetMap[followeeId][index]
        heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

    return res

  def follow(self, followerId: int, followeeId: int) -> None:
    # followeeId ko follower ke set mein add karte hain
    if followerId != followeeId:
      self.followMap[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    # Agar follow karta hai toh set se remove karte hain
    if followeeId in self.followMap[followerId]:
      self.followMap[followerId].remove(followeeId)