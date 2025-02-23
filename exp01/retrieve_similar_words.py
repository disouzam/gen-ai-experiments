import gensim.downloader

def get_similar_words(word: str):
    model = gensim.downloader.load(name="glove-wiki-gigaword-50")
    result: list[tuples] = model.most_similar(word)
    return result

if __name__ == "__main__":
    word = input("Enter a word: ")
    result = get_similar_words(word)

    for item in result:
        print(f"Word: {item[0]} - Probability(%): {item[1]*100:.2f}")