
# coding: utf-8

# In[1]:


text = """Roberto Baggio (born 18 February 1967) is a retired Italian footballer. He is widely regarded as one of the finest footballers of all time (4th at a Fifa internet poll; member of the Fifa World Cup Dream Team). Baggio won both the Ballon d’Or and the FIFA World Player of the Year in 1993. He is the only Italian player ever scoring in three World Cups. He is also one of the top 5 all-time goalscorers for Italy. Baggio is known as Il Divin Codino (The Divine Ponytail), for the hairstyle he wore for most of his career and his Buddhist background. """


# In[2]:


text = text.lower()


# In[3]:


from nltk import tokenize
sentences = tokenize.sent_tokenize(text)
print(sentences[:5])


# In[4]:


import re
pureSentences = [re.sub(r'[^\w\s]','',x) for x in sentences]
print(pureSentences[:5])


# In[5]:


pureText = " ".join(pureSentences)
print(pureText)


# In[6]:


splitText  = pureText.split(" ")
print("SplittedPureText:",splitText)


# In[7]:


import networkx as nx
graph = nx.Graph()


# In[8]:


graph.add_node(splitText[0])
for i in range(1,len(splitText)):
    graph.add_node(splitText[i])
    graph.add_edge(splitText[i-1],splitText[i],weight=1)


# In[9]:


print("NumberOfNodes:",graph.number_of_nodes())
print("NumberOfEdges:",graph.number_of_edges())


# In[10]:


print("Nodes:",graph.nodes())
print("Edges:",graph.edges())


# In[13]:


nx.draw_circular(graph,node_size=60,font_size=6,with_labels=True)


# In[14]:


import matplotlib.pyplot as plt 
plt.savefig("a.pdf") # save graph to pdf file


# In[16]:


from node2vec import Node2Vec


# In[17]:


node2vec = Node2Vec(graph, dimensions=64, walk_length=30, num_walks=200, workers=4) 


# In[18]:


model = node2vec.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)


# In[21]:


model.wv.most_similar("roberto")  # Output node names are always strings


# In[20]:


model.wv.save_word2vec_format("save.txt")

