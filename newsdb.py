import psycopg2

class NewsDatabase:

    def __init__(self):
        self.db = psycopg2.connect(database='news')
        self.conn = self.db.cursor()

    def get_popular_articles(self, limit_number=3):
        self.conn.execute("\
            SELECT right(path, -9) as log_slug, count(*) \
            FROM log WHERE status = '200 OK' and path != '/' \
            GROUP BY log_slug ORDER BY count DESC")

        posts = self.conn.fetchall()
        print(posts)

if __name__ == "__main__":
    news_database = NewsDatabase()
    news_database.get_popular_articles()