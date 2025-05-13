def get_book_text(path: str):
    with open(path) as f:
        contents = f.read()

    return contents

def count_words(text: str):
    return len([word for word in text.split()])

def count_char(text: str):
    text = text.lower()
    count_dict = {}
    
    for char in text:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1

    return count_dict
