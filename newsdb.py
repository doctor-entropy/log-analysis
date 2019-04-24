import psycopg2

class NewsDatabase:

    def __init__(self):
        self.db = psycopg2.connect(database='news')
        self.conn = self.db.cursor()

    def get_popular_articles(self, limit_number=3):

        sub_query = "\
            SELECT right(path, -9) as log_slug, count(*) \
            FROM log WHERE status = '200 OK' and path != '/' \
            GROUP BY log_slug ORDER BY count DESC"

        self.conn.execute("\
            SELECT art.title, proc.count \
            FROM articles AS art JOIN \
            ({}) AS proc\
            ON (art.slug = proc.log_slug)".format(sub_query))

        posts = self.conn.fetchall()
        
        for post in posts:
            print("\"{}\" - {} views".format(post[0], post[1]))

        return posts

    def get_popular_authors(self):

        sub_query = "\
            SELECT right(path, -9) as log_slug, count(*) \
            FROM log WHERE status = '200 OK' and path != '/' \
            GROUP BY log_slug ORDER BY count DESC"

        self.conn.execute("\
            SELECT authors.name as name, SUM(proc.count) as count \
            FROM authors \
            INNER JOIN articles ON (authors.id = articles.author) \
            INNER JOIN ({}) AS proc ON (articles.slug = proc.log_slug)\
            GROUP BY name ORDER BY count DESC".format(sub_query))

        posts = self.conn.fetchall()

        print(posts)

if __name__ == "__main__":
    news_database = NewsDatabase()
    news_database.get_popular_articles()
    news_database.get_popular_authors()