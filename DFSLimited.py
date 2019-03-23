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
# Create a new graph for the next problems
G = nx.Graph()
nx.add_path(G, [0, 1, 2, 3, 4, 5, 6])
nx.add_path(G, [2, 7, 8, 9, 10])
# Customize the depth_limit below 🔍
print(dict(nx.bfs_successors(G, source=1, depth_limit=5)))
# With the graph path as a reference
G = nx.path_graph(5)
# Why does this code break? For practice, see if you can discover the reason.🔬
print(list(nx.dfs_edges(G, source=0)))