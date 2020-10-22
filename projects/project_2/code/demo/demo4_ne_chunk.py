import nltk
from nltk import ne_chunk



if __name__ == '__main__':
    sent = "On Monday, September 17, 2018, John O'Malley promised his colleague Mary that he would put a replacement apple in the office fridge. O'Malley intended to share it with her on Tuesday at his desk and anticipated that the crunchy treat would delight them both. But she was sick that day."
    print(ne_chunk(nltk.tag.pos_tag(sent.split(' '))))

