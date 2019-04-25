import newsdb as news

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
		print("\t{} - {}\% errors".format(error[0], error[1]))

if __name__ == '__main__':
	main()