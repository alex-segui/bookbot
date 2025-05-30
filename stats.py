def get_num_words(text):
    # takes a string as input and returns the number of words
    num_words = 0
    text_list = text.split()

    for word in text_list:
        num_words += 1

    return num_words


def get_num_char(text):
    # takes a string as input and returns the number of times that each character appears
    low_case_text = text.lower()
    char_dict = {}

    for char in low_case_text:
        if (char in char_dict) == False:
            char_dict[char] = 1
        else:
            char_dict[char] +=1

    return char_dict


def sort_on(dict):
    return dict['num']

def sort_list(dict):
    # takes a dictionay of characters and their counts and returns a sorted list of dictionaries
    dict_list = []

    for key in dict:
        dict_key = {'char': key, 'num': dict[key]}
        dict_list.append(dict_key)

    dict_list.sort(reverse=True, key=sort_on)
    
    return dict_list