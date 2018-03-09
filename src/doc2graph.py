
# coding: utf-8

# In[33]:


import doc_tool
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec


# In[34]:


# not works on jupyter
#import sys,os
#PATH = os.path.dirname(os.path.abspath(__file__))
#print(PATH)
#sys.path.insert(PATH)


# In[35]:


docContent = doc_tool.readFile("/home/hmenn/Workspace/doc2graph/dataset/turkishText1.txt")


# In[36]:


pureSentences = doc_tool.text2sentences(docContent)


# In[37]:


print("Sentences:",pureSentences)


# In[38]:


stopwords = doc_tool.load_stop_words("/home/hmenn/Workspace/doc2graph/dataset/tr_stopwords.txt")


# In[39]:


words = doc_tool.sentences2Words(pureSentences,stopwords)


# In[40]:


print("Words:",words)


# In[12]:


textGraph = nx.Graph()


# In[41]:


# trace all text and extract simple graph. Each node/word connected with it's prev. word
    
textGraph.add_node(words[0]) 
for i in range(1,len(words)): 
    textGraph.add_node(words[i]) 
    textGraph.add_edge(words[i-1],words[i],weight=1)


# In[42]:


print("Nodes[",textGraph.number_of_nodes(),"]:",textGraph.nodes())


# In[43]:


print("Edges[",textGraph.number_of_edges(),"]:",textGraph.edges())


# In[44]:


nx.draw(textGraph,width=0.5,node_size=80,font_size=8,with_labels=True)


# In[45]:


plt.savefig("/home/hmenn/Workspace/doc2graph/outputs/textGraph.pdf") # save graph to pdf file


# In[19]:


graphN2V = Node2Vec(textGraph, dimensions=64, walk_length=30, num_walks=200, workers=4) 


# In[20]:


model = graphN2V.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)


# In[22]:


testWord = "zaman"
similarities = model.wv.most_similar(testWord)  # Output node names are always strings

#save and print results
with open("/home/hmenn/Workspace/doc2graph/outputs/similarity.txt","w") as f:
    f.write("Word:"+testWord+"\n")
    f.write(str(similarities))

print("Similarities of",testWord)
print(similarities)
    


# In[24]:


model.wv.save_word2vec_format("/home/hmenn/Workspace/doc2graph/outputs/node2vec_output.txt")

