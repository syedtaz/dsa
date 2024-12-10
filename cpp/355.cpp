#include <vector>

class Twitter {
public:
  Twitter() {}

  void postTweet(int userId, int tweetId) {}

  std::vector<int> getNewsFeed(int userId) {}

  void follow(int followerId, int followeeId) {}

  void unfollow(int followerId, int followeeId) {}
};