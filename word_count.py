from csv import reader

def gather_desc_words(input_data):
    # two dimentional list with sub lists as each description of netflix show
    all_words = []  # where all the words will be saved as individual strings
    for desc in input_data:
        all_words.extend(desc[10].split())

    return all_words

def create_dict(input_data):
    # if word is not in dictionary, add word
    # if word in dictionary, increment word number
    word_counter = {}
    for word in input_data:
        try:
            word_counter[word] += 1
        except KeyError:
            word_counter[word] = 1

    return word_counter


def navigate_dict(word_dict):
    while True:
        word_name = input('put word: ')
        if word_name == 'stop':
            break
        else:
            try:
                print(str(word_dict[word_name]) + '\n')
            except KeyError:
                print('word not in dict\n')

def main():
    with open('netflix_titles.csv', encoding='utf-8', newline='') as netflix_data:
        data = list(reader(netflix_data))
        data.pop(0)

    word_list = gather_desc_words(data)

    word_dict = create_dict(word_list)

    timer = 0

    for i in word_dict:
        if timer == 30:
            break
        print(i, word_dict[i])
        timer += 1




if __name__ == '__main__':
    main()
