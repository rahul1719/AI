# %%time
# View the run time for the script to see the processing time after the script runs
# --- Start Python Libraries for Assignment --- #

# --- 🖥 Data analysis packages 🖥 --- #
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import collections
from collections import deque
import time

# --- 📃 Web scraping packages 📃 --- #
import requests
from bs4 import BeautifulSoup
import re

# --- 📅 Search algorithms and network analysis package 📅 --- #
import networkx as nx

# --- Finish Python Libraries for Assignment --- #
seed_url = "https://en.wikipedia.org/wiki/Machine_learning"

# result set
result_urls = []
queue = deque([])

# store title of each page
title_list = []


# Customize attributes for print statements
class color:
    blue = '\033[94m'
    bold = '\033[1m'
    end = '\033[0m'


def BFS_crawler(seed_url):
    depth = 1
    queue.append(seed_url)
    while (len(queue)) != 0 and len(result_urls) < 100 and depth < 6:
        # dequeue a url
        # level = []
        size = len(queue)
        for i in range(0, size):
            current_url = queue.popleft()
            # level.append(current_url)
            time.sleep(1)
            source_code = requests.get(current_url).text
            soup = BeautifulSoup(source_code, "html.parser")
            content = soup.find('div', {'id': 'mw-content-text'})
            # title = soup.find('h1', {'id': 'firstHeading'} and {'class': 'firstHeading'})

            for item in content.findAll('a', {'title': True} and {'class': False}):
                if ('#' not in item.get('href')) and item.get('href').startswith('/wiki/') \
                        and not item.get('href').startswith('/wiki/Category:') \
                        and not item.get('href').startswith('/wiki/File:') \
                        and not item.get('href').startswith('/wiki/Template:') \
                        and not item.get('href').startswith('/wiki/Book:') \
                        and not item.get('href').startswith('/wiki/Portal:') \
                        and not item.get('href').startswith('/wiki/Help:') \
                        and not item.get('href').startswith('/wiki/Template_talk:') \
                        and not item.get('href').startswith('/wiki/Talk:'):

                    url = "https://en.wikipedia.org" + item.get('href')
                    keyword = "Machine"
                    if re.search(keyword, url, re.IGNORECASE):
                        if len(result_urls) < 100 and url not in result_urls:
                            result_urls.append(url)
                            queue.append(url)
                            if len(result_urls) % 10 == 0:
                                print("URL is", color.bold + url + color.end)
                                print("This is URL #", len(result_urls))
                        if len(result_urls) == 100:
                            output_urls(result_urls)
                            return 0
        depth += 1


# write url into text output file.  You can change this as you change the URLs
def output_urls(urls):
    file_loc = r'output/ML_URLs.txt'
    fx = open(file_loc, "w")
    for url in urls:
        fx.write(url + '\n')
    fx.write('\n' + "Num of Urls: " + str(len(urls)) + '\n')
    fx.close()


# The function here to solve the problem, different urls point to the same page, is to check the title of each page
# correspond to each URL.
def isVisited_url(arg_url):
    time.sleep(1)
    source_code = requests.get(arg_url).text
    soup = BeautifulSoup(source_code, "html.parser")
    title = soup.find('h1', {'id': 'firstHeading'})
    if title in title_list:
        return 1
    else:
        title_list.append(title)
        return 0


BFS_crawler(seed_url)
