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
# the justification for these is that we know we will get more feed requests than any other type of request
# computing the feeds everytime a user requests is going to be resource expensive
# also users dont want to wait that long everytime they want to see their feeds
# to give a great user experience the getFeeds endpoint needs to be as fast as posible



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
        

        
        

        
        
# these is a much more easier to understand solution
# we compute the user feeds on demand
# this is less perfomant beuase the getFeeds has a complexity of Time: O(m*n*log(m*n)) where
# m=number of following
# n=avg number of post per per following user

# class Twitter:

#     def __init__(self):
#         self.db = defaultdict(lambda:{"tweets": [], "following": set()})
#         self.date = 0
        
#     def postTweet(self, userId: int, tweetId: int) -> None: # Time: O(1)
            
#         self.db[userId]["tweets"].append((self.date, tweetId))
#         self.date -= 1
        
#     def getNewsFeed(self, userId: int) -> List[int]: 
#         #Time: O(m*n*log(m*n))  
#         # m=number of following
#         # n=number of post per per following user
        
#         # max heap
#         heap = []
#         feeds = []
        
#         self.db[userId]["following"].add(userId)
        
#         for user in self.db[userId]["following"]:
#             for tweet in self.db[user]["tweets"]:
#                 heapq.heappush(heap, tweet)

#         for i in range(10):
#             if heap:
#                 feeds.append(heapq.heappop(heap)[1]) 
        
#         return feeds
        

#     def follow(self, followerId: int, followeeId: int) -> None: #Time: O(1)
#         self.db[followerId]["following"].add(followeeId)    

#     def unfollow(self, followerId: int, followeeId: int) -> None: #Time: O(1)
#         self.db[followerId]["following"].discard(followeeId)

        
# # Your Twitter object will be instantiated and called as such:
# # obj = Twitter()
# # obj.postTweet(userId,tweetId)
# # param_2 = obj.getNewsFeed(userId)
# # obj.follow(followerId,followeeId)
# # obj.unfollow(followerId,followeeId)