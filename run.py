import newsdb as news

def convert_datetime_to_string(dt):
    month_string = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }

    return '{} {}, {}'.format(dt.day, month_string[dt.month], dt.year)

def main():

    news_db = news.NewsDatabase()

    print("1. The three most popular articles of all time are...")
    popular_articles = news_db.get_popular_articles(
                                limit_number=3)
    for article in popular_articles:
        print("\t\"{}\" - {} views".format(article[0], article[1]))

    print("\n2. The most popular article authors of all time are...")
    popular_authors = news_db.get_popular_authors()
    for author in popular_authors:
        print("\t\"{}\" - {} views".format(author[0], author[1]))

    print("\n3. The days that lead to more than 1% errors are...")
    high_error_rate = news_db.get_error_percentages(
                                above_percentage=1.00)
    for error in high_error_rate:
        error_rate = error[1]
        date_time = convert_datetime_to_string(error[0])
        print("\t{} - {}% errors".format(date_time, round(error_rate,1)))

    print("\nPlease run \'bash delete_views.sh\' file to delete views")

if __name__ == '__main__':
    main()