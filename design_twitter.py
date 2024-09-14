from collections import defaultdict
import heapq

class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1 # This decrement is because in python we have only MinHeap
        # and the count itself is here to record which is the latest tweet.The more 
        # Negative count means the more recent tweet 

        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        result = [] # To store the 10 ids with the most negative count means the most
        # Recent tweet ids
        min_heap = []
        # A person also follows himself so
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                last_value_index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][last_value_index]
                min_heap.append([count, tweetId, followeeId, last_value_index - 1])
        heapq.heapify(min_heap)  # to convert a list into a heap
        while min_heap and len(result) < 10:
            count, tweetId, followeeId, last_value_index = heapq.heappop(min_heap)
            result.append(tweetId)
            if last_value_index >= 0:
                count, tweetId = self.tweetMap[followeeId][last_value_index]
                heapq.heappush(min_heap, [count, tweetId, followeeId, last_value_index - 1])
        return result

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId != followeeId and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        # self.followMap[followerId].discard(followeeId) # This will not throw exception
        # if the followeeId is already not in follower's followList


        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
