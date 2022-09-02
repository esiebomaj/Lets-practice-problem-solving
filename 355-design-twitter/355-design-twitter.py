class NewsFeed():
    def __init__(self):
        self.feeds = []
        
    def add(self, tweetId, user):
        self.feeds.insert(0, (user, tweetId))
        
    def getFeeds(self,):
        return [i[1] for i in self.feeds[:10]]
    
    def removeTweetsByUser(self, userId):
        self.feeds = [i for i in self.feeds if i[0] != userId]

class Twitter:

    def __init__(self):
        self.db = {} 
        
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if  userId not in self.db:
            self.db[userId] = {
                "tweets":[],
                "newsFeed":NewsFeed(),
                "followers":set()
            }
            
        self.db[userId]["tweets"].append(tweetId)
        self.db[userId]["newsFeed"].add(tweetId, userId)
        
        for follower in self.db[userId]["followers"]:
            self.db[follower]["newsFeed"].add(tweetId, userId)            
            
        
    def getNewsFeed(self, userId: int) -> List[int]:
        return self.db[userId]["newsFeed"].getFeeds()
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if  followerId not in self.db:
            self.db[followerId] = {
                "tweets":[],
                "newsFeed":NewsFeed(),
                "followers":set()
            }
            
        if  followeeId not in self.db:
            self.db[followeeId] = {
                "tweets":[],
                "newsFeed":NewsFeed(),
                "followers":set()
            }
            
        self.db[followeeId]["followers"].add(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.db[followeeId]["followers"].remove(followerId)
        self.db[followerId]["newsFeed"].removeTweetsByUser(followeeId)
        

        
        

        
        
import heapq   
from collections import defaultdict
        
def newUser():
    return {"tweets": [], "following": set()}
        
        
class Twitter:

    def __init__(self):
        self.db = defaultdict(newUser)
        self.date = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
            
        self.db[userId]["tweets"].append((self.date, tweetId))
        self.date += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        feeds = [None]*10
        heap = []
        
        self.db[userId]["following"].add(userId)
        
        print("following",self.db[userId]["following"] )
        for user in self.db[userId]["following"]:
            # print(user)
            for tweet in self.db[user]["tweets"]:
                heapq.heappush(heap, tweet)
        # print(heap)
        while len(heap) > 10:
            heapq.heappop(heap)
        
        for i in range(10-1, -1, -1):
            if heap:
                feeds[i] = heapq.heappop(heap)[1] 
            else:
                break
        
        return [i for i in feeds if i]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        self.db[followerId]["following"].add(followeeId)
        # print("after follow", self.db[followerId]["following"])
    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.db[followerId]["following"].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)