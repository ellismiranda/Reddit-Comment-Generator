from reddit import get_hot_posts, generate_post_reference, get_post_top_comments

a = get_hot_posts('runescape')[0]
post = generate_post_reference(a)
print(get_post_top_comments(post))
print(post.title)