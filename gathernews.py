import webbrowser
import nltk
from newspaper import Article

userinput = input("Enter a keyword to filter:")


url = 'https://www.theverge.com/21277231/ps5-playstation-5-game-trailers-launch-release-dates-sony-event'
url2 = 'https://kotaku.com/the-hits-and-misses-of-the-ps5-reveal-event-1844006000'
url3 = 'https://www.ign.com/articles/the-last-of-us-part-2-review'


def article_scraper(string):
    article = Article(string)
    reader = open('news_summary.txt', 'a+')

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
        webbrowser.open(string)
    reader.close()


article_scraper(url)
article_scraper(url2)
article_scraper(url3)

print('success!')