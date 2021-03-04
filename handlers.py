import os
import time
from minio import Minio
import tornado.web
import sqlite3

import minio_config

conn = sqlite3.connect('db/app.db')
c = conn.cursor()

client = Minio(
    minio_config.ENDPOINT,
    access_key=minio_config.ACCESS_KEY,
    secret_key=minio_config.SECRET_KEY,
)

try:
    c.execute(
        '''CREATE TABLE feedbacks (name text, rating text, feedback text)''')
except sqlite3.OperationalError:
    pass

# Handler to work with feedback
class BaseHandler(tornado.web.RequestHandler):
    def get(self):
        c.execute('select * from feedbacks')
        res = c.fetchall()
        feedbacks = []
        for i in res:
            feedbacks.append(i)
        self.render('home.html', feedbacks=feedbacks)

    def post(self):
        name = self.get_argument('name')
        rating = self.get_argument('rating')
        feedback = self.get_argument('feedback')
        c.execute("insert into feedbacks values (?, ?, ?)",
                  (name, rating, feedback))
        conn.commit()
        self.redirect('/?msg=feedback_updated')

# Handler to work with Log file upload
class LogUpload(tornado.web.RequestHandler):
    def get(self):
        bucket_name = "logs"
        f = open("logs/app.log", "r")
        found = client.bucket_exists(bucket_name)
        if not found:
            client.make_bucket(bucket_name)
        size = os.fstat("logs/app.log").st_size
        client.put_object(
            bucket_name, str(time.time()) + "app.log", f, size
        )
        self.redirect('/?msg=file_stored')
