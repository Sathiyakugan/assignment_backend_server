#!/usr/bin/env python
import sys

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado.options import define, options
import handlers
import os

define("port", default=8000, type=int)

urls = [
    (r"/", handlers.BaseHandler),
    (r"/log_upload", handlers.LogUpload),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": r"{0}".format(os.path.dirname(__file__))})
]

settings = dict({
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "cookie_secret": str(os.urandom(45)),
    "xsrf_cookies": True,
    "debug": False,
    "gzip": True,
})

application = tornado.web.Application(urls, **settings)


if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    args = sys.argv
    args.append("--log_file_prefix=logs/app.log")
    tornado.options.parse_command_line(args)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()