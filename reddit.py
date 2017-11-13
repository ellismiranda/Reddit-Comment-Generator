import praw
from secrets import client_secret, client_id, user_id, user_password

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     password=user_password,
                     user_agent='Language Scrapper',
                     username=user_id)


def get_hot_posts(sub_name):
    """Returns top posts for a subreddit. Filters out pinned posts."""
    return [post.id for post in reddit.subreddit(sub_name).hot() if not post.stickied]


def generate_post_reference(post_id):
    """Returns a post reference based on post id."""
    return reddit.submission(id=post_id)


def get_post_top_comments(post):
    """Returns a post's top comments."""
    return [comment.body for comment in post.comments if not bot_comment(comment.body)]


def get_post_all_comments(post):
    """Returns all the comments in a post."""
    post.comments.replace_more(limit=0)
    return [comment.body for comment in post.comments.list() if not bot_comment(comment.body)]


def bot_comment(comment):
    """Checks for the default message that bots will output."""
    return "Beep, I'm a bot." in comment

