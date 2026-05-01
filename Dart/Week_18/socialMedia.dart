void main() {
  SocialMediaFeed feed = SocialMediaFeed();
  Post p1 = Post('Gym', 'Dylan', 01052026);
  feed.addPost(p1);
  feed.displayFeed();
}

class Post {
  String content;
  String author;
  int date;
  int likes = 0;

  Post(this.content, this.author, this.date);

  void like() {
    likes++;
  }

  String toString() {
    return '$content by $author ($date) - Likes: $likes';
  }
}

class SocialMediaFeed {
  List<Post> feed = [];

  void addPost(Post post) {
    feed.add(post);
  }

  void removePost(Post post) {
    feed.remove(post);
  }

  void likePost(Post post) {
    post.like();
  }

  void displayFeed() {
    feed.sort((a, b) => a.date.compareTo(b.date));

    for (Post post in feed) {
      print(post);
    }
  }
}
