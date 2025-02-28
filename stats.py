def get_num_words(file_path):
    with open(file_path) as f:
        readfile = f.read()
        file_array = readfile.split()
        return len(file_array)

def get_num_chars(file_path):
    with open(file_path) as f:
        readfile = f.read()
        readfile = readfile.lower()
        char_dict = {}
        for char in readfile:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
        return char_dict
    
def sorted_list(dict):
    char_list = list(dict.items())
    char_list.sort(key=lambda x: x[1], reverse=True)
    return char_list