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

        return posts

    def get_error_percentages(self, above_percentage=1.00):

        total_sub_query = "\
            SELECT DATE(time) AS date_tt, count(*) \
            FROM log GROUP BY date_tt"

        error_sub_query = "\
            SELECT DATE(time) as date_ss, count(*) \
            FROM log WHERE status != '200 OK' GROUP BY date_ss"

        error_percentage = "\
            SELECT date_tt as date, error.count * 100.00 / total.count as percentage\
            FROM ({}) AS total JOIN ({}) AS error \
            ON date_tt = date_ss".format(total_sub_query, error_sub_query)

        needed_date_error = "\
            SELECT * FROM ({}) AS error \
            WHERE error.percentage > {}".format(error_percentage, above_percentage)

        posts = self.conn.execute(needed_date_error)

        posts = self.conn.fetchall()

        return posts