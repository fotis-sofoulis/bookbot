def get_book_text(path: str):
    with open(path) as f:
        contents = f.read()

    return contents

def count_words(text: str):
    return len([word for word in text.split()])

