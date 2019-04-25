import newsdb as news
import helpers as hp

def main():

    news_db = news.NewsDatabase()

    print("1. The three most popular articles of all time are...")
    popular_articles = news_db.get_popular_articles(limit_number=3)
    for article in popular_articles:
        print("\t\"{}\" - {} views".format(article[0], article[1]))

    print("\n2. The most popular article authors of all time are...")
    popular_authors = news_db.get_popular_authors()
    for author in popular_authors:
        print("\t\"{}\" - {} views".format(author[0], author[1]))

    print("\n3. The days that lead to more than 1% errors are...")
    high_error_rate = news_db.get_error_percentages(above_percentage=1.00)
    for error in high_error_rate:
        error_rate = error[1]
        date_time = hp.convert_datetime_to_string(error[0])
        print("\t{} - {}% errors".format(date_time, round(error_rate, 1)))

    print("\nPlease run \'bash delete_views.sh\' file to delete views")

if __name__ == '__main__':
    main()
