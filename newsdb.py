import psycopg2

class NewsDatabase:

    def __init__(self):
        self.db = psycopg2.connect(database='news')
        self.conn = self.db.cursor()

if __name__ == "__main__":
    news_database = NewsDatabase()