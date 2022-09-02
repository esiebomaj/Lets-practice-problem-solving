import heapq   
from collections import defaultdict
            

# an attempt to solve this question and reduce complexity for  getFeeds by caching newsfeed
# i.e when a user makes a tweet, we add the tweet to all his folowers newsfeed 
# the problems with this solution are
# 1. how do we update a users feeds with the previous post of a person he just followed?
# 2. how do we update a users feeds when after he unfolowed another user 
# (we need to remove the unfollowed users post from his feeds)

# Proposed solutions
# problem 1: we can merge the newly followed users posts with the current user feeds
#            We know that both feeds and followed users posts are sorted so our task here is to merge 2 sorted arrays
# problem 2: filter out all tweets made by unfollowed user from user feeds

# once we can solve all these problems we have a feed system that is supperfast (constant time)
# the justification for these is that we know we will get more feed requests that any other type of request
# and to give a great user experience these endpoint needs to be as fast as posible



class NewsFeed():
    def __init__(self):
        self.feeds = []
        
    def add(self, tweetId, user, date):
        self.feeds.insert(0, (date, user, tweetId))
        
    def getFeeds(self,):
        return [i[2] for i in self.feeds[:10]]
    
    def removeTweetsByUser(self, userId):
        self.feeds = [i for i in self.feeds if i[1] != userId]
        
    def merge(self, tweets):
        i,j = 0,0
        merged = []
        # we use these set to avoid duplicates
        seen = set()
        while i < len(self.feeds) and j < len(tweets):
            if self.feeds[i][0] >= tweets[j][0]:
                if self.feeds[i][0] not in seen:
                    merged.append(self.feeds[i])
                    seen.add(self.feeds[i][0])
                i+=1
            else:
                if tweets[j][0] not in seen:
                    merged.append(tweets[j])
                    seen.add(tweets[j][0])
                j += 1
            
                
        while  j < len(tweets):
            if tweets[j][0] not in seen:
                merged.append(tweets[j])
                seen.add(tweets[j][0])
            j += 1
            
        while i < len(self.feeds):
            if self.feeds[i][0] not in seen:
                merged.append(self.feeds[i])
                seen.add(self.feeds[i][0])
            i+=1
            
        self.feeds = merged
        

def newUser():
    return  {"tweets":[], "newsFeed":NewsFeed(), "followers":set()}

    
class Twitter:

    def __init__(self):
        self.db = defaultdict(newUser)
        self.date = 0
        
        
    def postTweet(self, userId: int, tweetId: int) -> None:   
        print("post tweet")
        self.db[userId]["tweets"].append((self.date, userId, tweetId))
        self.db[userId]["newsFeed"].add(tweetId, userId, self.date)
        
        for follower in self.db[userId]["followers"]:
            self.db[follower]["newsFeed"].add(tweetId, userId, self.date)  
            
        self.date+=1
            
        
    def getNewsFeed(self, userId: int) -> List[int]:
        print("get feeds")
        return self.db[userId]["newsFeed"].getFeeds()
        

    def follow(self, followerId: int, followeeId: int) -> None:
        print("follow")
        self.db[followeeId]["followers"].add(followerId)
        followeeTweets = list(reversed(self.db[followeeId]["tweets"]))
        self.db[followerId]["newsFeed"].merge(followeeTweets)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        print("unfollow")
        self.db[followeeId]["followers"].discard(followerId)
        self.db[followerId]["newsFeed"].removeTweetsByUser(followeeId)
        

        
        

        
        

# class Twitter:

#     def __init__(self):
#         self.db = defaultdict(lambda:{"tweets": [], "following": set()})
#         self.date = 0
        
#     def postTweet(self, userId: int, tweetId: int) -> None:
            
#         self.db[userId]["tweets"].append((self.date, tweetId))
#         self.date += 1
        
#     def getNewsFeed(self, userId: int) -> List[int]:
#         feeds = [None]*10
#         heap = []
        
#         self.db[userId]["following"].add(userId)
        
#         for user in self.db[userId]["following"]:
#             for tweet in self.db[user]["tweets"]:
#                 heapq.heappush(heap, tweet)

#         while len(heap) > 10:
#             heapq.heappop(heap)
        
#         for i in range(10-1, -1, -1):
#             if heap:
#                 feeds[i] = heapq.heappop(heap)[1] 
#             else:
#                 break
        
#         return [i for i in feeds if i]
        

#     def follow(self, followerId: int, followeeId: int) -> None:
#         self.db[followerId]["following"].add(followeeId)    

#     def unfollow(self, followerId: int, followeeId: int) -> None:
#         self.db[followerId]["following"].discard(followeeId)

        
# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)