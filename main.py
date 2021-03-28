from csv import reader

def cleaning():
    # remove stop words
    # remove numbers and Symbols
    # group words with the same base word
    pass

def main():
    with open('netflix_titles.csv', encoding='utf-8', newline='') as netflix_data:
        data = list(reader(netflix_data))
        data.pop()

    for i in data:
        print(i[1], i[11])

if __name__ == '__main__':
    main()
