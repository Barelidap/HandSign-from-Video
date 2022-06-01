import os

def get_all_videos(rootdir):
    topics = []
    words = []
    langs = []
    videos = []

    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            topics.append(d)

    for word in topics:
        for file in os.listdir(word):
            d = os.path.join(word, file)
            if os.path.isdir(d):
                words.append(d)

    for lang in words:
        for file in os.listdir(lang):
            d = os.path.join(lang, file)
            if os.path.isdir(d):
                langs.append(d)


    return langs
