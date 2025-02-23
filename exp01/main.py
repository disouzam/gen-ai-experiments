import gensim.downloader

model = gensim.downloader.load(name="glove-wiki-gigaword-50")
result = model.most_similar("tower")
print(result)