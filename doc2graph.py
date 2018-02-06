
# coding: utf-8

# In[100]:


text = """Roberto Baggio (born 18 February 1967) is a retired Italian footballer. He is widely regarded as one of the finest footballers of all time (4th at a Fifa internet poll; member of the Fifa World Cup Dream Team). Baggio won both the Ballon d’Or and the FIFA World Player of the Year in 1993. He is the only Italian player ever scoring in three World Cups. He is also one of the top 5 all-time goalscorers for Italy. Baggio is known as Il Divin Codino (The Divine Ponytail), for the hairstyle he wore for most of his career and his Buddhist background. """


# In[101]:


text = text.lower()


# In[102]:


from nltk import tokenize
sentences = tokenize.sent_tokenize(text)
print(sentences[:5])


# In[103]:


import re
pureSentences = [re.sub(r'[^\w\s]','',x) for x in sentences]
print(pureSentences[:5])


# In[104]:


pureText = " ".join(pureSentences)
print(pureText)


# In[105]:


splitText  = pureText.split(" ")
print("SplittedPureText:",splitText)


# In[106]:


import networkx as nx
graph = nx.Graph()


# In[107]:


graph.add_node(splitText[0])
for i in range(1,len(splitText)):
    graph.add_node(splitText[i])
    graph.add_edge(splitText[i-1],splitText[i])


# In[108]:


print("NumberOfNodes:",graph.number_of_nodes())
print("NumberOfEdges:",graph.number_of_edges())


# In[109]:


print("Nodes:",graph.nodes())
print("Edges:",graph.edges())


# In[110]:


import matplotlib.pyplot as plt


# In[122]:


nx.draw(graph,pos=nx.spring_layout(graph),node_size=60,font_size=6)
nx.draw_networkx_labels(graph,pos=nx.spring_layout(graph))


# In[124]:


plt.figure(3,figsize=(12,12)) 
plt.savefig("test.png",format="PNG")
plt.show()

