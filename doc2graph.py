
# coding: utf-8

# In[15]:


from doc_tool import DocTool
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec


# In[16]:


dt = DocTool()
docContent = dt.readFile("dataset/englishText1.txt")


# In[3]:


pureSentences = dt.getPureSentences(docContent)


# In[4]:


print("Sentences:",pureSentences)


# In[5]:


words = dt.sentences2Words(pureSentences)


# In[6]:


print("Words:",words)


# In[7]:


textGraph = nx.Graph()


# In[8]:


# trace all text and extract simple graph. Each node/word connected with it's prev. word
textGraph.add_node(words[0])
for i in range(1,len(words)):
    textGraph.add_node(words[i])
    textGraph.add_edge(words[i-1],words[i],weight=1)


# In[11]:


print("Nodes[",textGraph.number_of_nodes(),"]:",textGraph.nodes())


# In[12]:


print("Edges[",textGraph.number_of_edges(),"]:",textGraph.edges())


# In[ ]:


nx.draw_circular(textGraph,node_size=100,font_size=8,with_labels=True)


# In[ ]:


plt.savefig("textGraph.pdf") # save graph to pdf file


# In[ ]:


graphN2V = Node2Vec(textGraph, dimensions=64, walk_length=30, num_walks=200, workers=4) 


# In[ ]:


model = graphN2V.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)


# In[ ]:


model.wv.most_similar("model")  # Output node names are always strings


# In[ ]:


model.wv.save_word2vec_format("save.txt")

