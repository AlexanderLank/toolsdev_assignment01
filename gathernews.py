import webbrowser
import nltk
import newspaper
from newspaper import Article

userinput = input("Enter a keyword to filter:")


url = 'https://www.gamesradar.com/uk/search/?searchTerm='
url2 = 'https://www.ign.com/search?q='
url3 = 'https://www.theverge.com/search?q='







def article_filter(string):
    collection = newspaper.build(string, memoize_articles = False)
    reader = open('news_summary.txt', 'a+')


    ender = 0
    for article in collection.articles:
        article.download()
        article.parse()
        nltk.download('punkt')
        article.nlp()
        if userinput in article.keywords or userinput == '':
            reader.write(article.title)
            reader.write(' - ')
            reader.writelines(article.authors)
            reader.write('\n')
            reader.write(article.summary + '\n')
            reader.write('\n')
            webbrowser.open(article.url)
        if ender > 8:
            break
        ender = ender + 1
    reader.close()


article_filter(url)
article_filter(url2)
article_filter(url3)

print('success!')