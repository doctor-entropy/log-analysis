import psycopg2

class NewsDatabase:

    def __init__(self):

        try:
            self.db = psycopg2.connect(database='news')
        except psycopg2.OperationalError:
            print("Can't connect to news database. Please check if the database exists")
            exit(1)

        self.conn = self.db.cursor()

        self.conn.execute("\
            SELECT EXISTS(SELECT * FROM information_schema.tables \
            WHERE table_name = \'proc\')")

        proc_views_exists = self.conn.fetchone()[0]

        if not proc_views_exists:
            print("Please run \'create_views.sh\' file before running this script")
            exit(1)

    def get_popular_articles(self, limit_number=3):

        self.conn.execute("\
            SELECT art.title, proc.count \
            FROM articles AS art JOIN \
            proc AS proc\
            ON (art.slug = proc.log_slug) LIMIT {}".format(
                                                limit_number))

        posts = self.conn.fetchall()

        return posts

    def get_popular_authors(self):

        self.conn.execute("\
            SELECT authors.name as name, SUM(proc.count) as count \
            FROM authors \
            INNER JOIN articles ON (authors.id = articles.author) \
            INNER JOIN proc AS proc ON (articles.slug = proc.log_slug)\
            GROUP BY name ORDER BY count DESC")

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