# -*- coding: utf-8 -*-
import json
import requests
import webbrowser
from bs4 import BeautifulSoup
from wox import Wox,WoxAPI
from util import WoxEx, WoxAPI, load_module, Log # util for debug

with load_module():
    import pyperclip


class MovieSearch(WoxEx): # WoxEx instead of Wox
    def query(self, query):
        if not query:
            return ""

        apikey = "d1ef1559" # get valid apikey: http://www.omdbapi.com
        url = "http://www.omdbapi.com/?apikey=" + apikey + "&s=" + query
        r = requests.get(url)
        r = r.json()['Search']

        results = []
        for item in r:
            res = {}
            res["Title"] = item["Title"]
            res["SubTitle"] = "Year: " + item["Year"] + "    imdb: " + \
                              item["imdbID"] + "    Type: " + item["Type"]
            res["IcoPath"] = "Images\\movie.png"
            item_url = "https://www.imdb.com/title/" + item["imdbID"]
            res["JsonRPCAction"] = {"method": "openUrl", "parameters": [item_url], "dontHideAfterAction": False}
            results.append(res)
        return results

    def openUrl(self, url):
        webbrowser.open(url)


if __name__ == "__main__":
    MovieSearch()
