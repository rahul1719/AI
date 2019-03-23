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
G.add_edges_from([("A","B"),("A","S"),("B","A"),("C","D"),("C","E"),("C","F"),("C","S"),("D","C"),("E","C"),("E","H"),("F","C"),("F","G"),("H","E"),("H","G"),("S","A"),("S","C"),("S","G")])

nx.draw_networkx(G, with_labels=True)
plt.title('A more complex graph')
#plt.show();
print(nx.dfs_predecessors(G, source='C'))
print("The average shortest path is:", round(nx.average_shortest_path_length(G)))
print("Shortest path scenarios:", [p for p in nx.all_shortest_paths(G, source='A', target='H')])
print("The shortest path length is", nx.shortest_path_length(G, source='A', target='H'))