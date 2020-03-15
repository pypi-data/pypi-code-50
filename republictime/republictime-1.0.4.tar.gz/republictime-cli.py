from argparse import ArgumentParser
from republictime.articles import Article
import apikey


parser = ArgumentParser()
parser.add_argument("--apikey", help="Enter your unique api key..")
parser.add_argument("--url", help="Enter the url address of host.")
parser.add_argument("--address", help="Set news access address.")
parser.add_argument("--promoted", help="Set True for promoted news.")
parser.add_argument("--trending", help="Set True for trending news.")
args = parser.parse_args()


args.apikey = apikey.APIKEY
args.url = apikey.ALLOWED_HOST


if args.apikey and args.url and args.address:
    articles = Article(args.address, args.apikey, args.url)

    if args.promoted == "True" and args.trending == "True":
        articles = articles.get_article(promoted=True, trending=True)
        for article in articles:
            print(str(article["title"][0:50]) + "..." + " | " + str(article["is_promote"]) + " | " + str(article["is_trend"]))

    elif args.promoted == "True" and args.trending == "None":
        articles = articles.get_article(promoted=True, trending=None)
        for article in articles:
            print(str(article["title"][0:50]) + "..." + " | " + str(article["is_promote"]) + " | " + str(article["is_trend"]))

    elif args.promoted == "False" and args.trending == "None":
        articles = articles.get_article(promoted=False, trending=None)
        for article in articles:
            print(str(article["title"][0:50]) + "..." + " | " + str(article["is_promote"]) + " | " + str(article["is_trend"]))

    elif args.promoted == "None" and args.trending == "True":
        articles = articles.get_article(promoted=None, trending=True)
        for article in articles:
            print(str(article["title"][0:50]) + "..." + " | " + str(article["is_promote"]) + " | " + str(article["is_trend"]))

    else:
        articles = articles.get_article()
        for article in articles:
            print(str(article["title"][0:50]) + "..." + " | " + str(article["is_promote"]) + " | " + str(article["is_trend"]))

else:
    print(dict(error="In order to use republictime module, Address and APIKEY are required."))
