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

G = nx.Graph()
G.add_edges_from(
    [("A", "B"), ("A", "C"), ("A", "E"), ("B", "D"), ("B", "E"), ("C", "F"), ("C", "G"), ("E", "D"), ("G", "C")])

nx.draw_networkx(G, with_labels=True)
plt.title('Example network #2')
#plt.show();

# Decision-making around the shortest path
print("Does a shortest path exist?", nx.has_path(G, source='F', target='B'))
print("---------------------------------")
print("Shortest path scenarios:", [p for p in nx.all_shortest_paths(G, source='F', target='B')])

print("The shortest path length is", nx.shortest_path_length(G, source='F', target='B'))
print("The average shortest path is:", nx.average_shortest_path_length(G))
pathLeangth=nx.average_shortest_path_length(G)
print(round(pathLeangth))
