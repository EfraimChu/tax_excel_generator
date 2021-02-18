# -*- coding: utf-8 -*-
# author: YF
import json
import web
from txt_current_model import TaxCurrentData

# todo  使用 Bottle: Python Web Framework¶
urls = (
    '/', 'index',
    '/js/(.*)', 'js',
    '/css/fonts/(.*)', 'font',
    '/css/(.*)', 'css',

    '/list', 'list',
    '/add', 'TaxRow',
    '/.*', 'null',
)
app = web.application(urls, globals())


class null:
    def GET(self):
        return 1


class css:
    def GET(self, css_file):
        return open("./resource/" + css_file)


class font:
    def GET(self, css_file):
        return open("./resource/" + css_file)


class js:
    def GET(self, js_file):
        return open("./resource/" + js_file)


class index:
    def GET(self):
        return open("ui.html")


class list:
    def GET(self):
        taxList = TaxCurrentData.select().dicts()
        row_list = []
        for row in taxList:
            row_list.append(row)
        web.header('Content-Type', "application/json")
        return json.dumps(row_list)


class TaxRow:
    def POST(self):
        i = web.input()
        row = TaxCurrentData()
        row.good = i.good
        row.price = i.price
        row.quantity = i.quantity
        row.save()
        print(i)
        return "ok"


class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'


if __name__ == "__main__":
    app.run()
