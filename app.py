from models.reddit import get_hot_posts, generate_post_reference, get_post_top_comments
from models.language_model import LanguageModel
from models.utils import format_comment

'''
BEST COMMENT GENERATED ABOUT 'Dogs waiting to enter the hospital rooms of sick children for animal therapy.' from R/AWW:

"I bet he licked his dick right before ? Shows what I actually give my life . Edit : This is my asshole !"

'''

new = True
another = True

print('\nTop Comment Generator')
print('@ellismiranda, 2018')

while another:
    if new:
        subreddit = input('\nWhat subreddit are we getting the top post from? r/')
        new = False
        a = get_hot_posts(subreddit)[0]
        post = generate_post_reference(a)
        tops = get_post_top_comments(post)
        model = LanguageModel()
        model.train(tops)
    example_sentence = model.generate_sentence()
    print('\nPost this and enjoy the free karma!:', format_comment(example_sentence))
    another = True if input('Generate another top comment for the top post of r/{}? [y/n] '.format(subreddit)) == 'y' else False
    if not another:
        new = True if input('Generate top comments for another subreddit? [y/n]') == 'y' else False
        another = True if new else False

