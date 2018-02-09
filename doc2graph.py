
# coding: utf-8

# In[42]:


from doc_tool import DocTool
import networkx as nx
import matplotlib.pyplot as plt
from node2vec import Node2Vec


# In[43]:


dt = DocTool()
docContent = dt.readFile("dataset/englishText1.txt")


# In[44]:


pureSentences = dt.getPureSentences(docContent)


# In[45]:


print("Sentences:",pureSentences)


# In[46]:


words = dt.sentences2Words(pureSentences)


# In[47]:


print("Words:",words)


# In[48]:


textGraph = nx.Graph()


# In[49]:


# trace all text and extract simple graph. Each node/word connected with it's prev. word
textGraph.add_node(words[0])
for i in range(1,len(words)):
    textGraph.add_node(words[i])
    textGraph.add_edge(words[i-1],words[i],weight=1)


# In[54]:


print("Nodes[",textGraph.number_of_nodes(),"]:",textGraph.nodes())


# In[55]:


print("Edges[",textGraph.number_of_edges(),"]:",textGraph.edges())


# In[76]:


nx.draw_circular(textGraph,width=0.5,node_size=80,font_size=8,with_labels=True)


# In[77]:


plt.savefig("outputs/textGraph.pdf") # save graph to pdf file


# In[78]:


graphN2V = Node2Vec(textGraph, dimensions=64, walk_length=30, num_walks=200, workers=4) 


# In[79]:


model = graphN2V.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)


# In[80]:


testWord = "document"
similarities = model.wv.most_similar(testWord)  # Output node names are always strings

#save and print results
with open("outputs/similarity.txt","w") as f:
    f.write("Word:"+testWord+"\n")
    f.write(str(similarities))

print("Similarities of",testWord)
print(similarities)
    


# In[81]:


model.wv.save_word2vec_format("outputs/node2vec_output.txt")

