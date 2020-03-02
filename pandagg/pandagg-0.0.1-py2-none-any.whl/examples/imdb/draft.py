#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pandagg.agg import Agg


# In[62]:


agg = Agg({
    "genres": {
        "terms": {
            "field": "genres",
            "size": 3
        },
        "aggs": {
            "release_decade": {
                "date_histogram": {
                    "field": "year",
                    "fixed_interval": "3655d"
                },
                "aggs": {
                    "avg_nb_directors": {
                        "avg" : {
                            "field" : "nb_directors"
                        }
                    },
                    "avg_nb_roles": {
                        "avg" : {
                            "field" : "nb_roles"
                        }
                    },
                    "avg_rank": {
                        "avg": {
                            "field": "rank"
                        }
                    }
                }
            }
        }
    }
})


# In[63]:


agg


# In[64]:


from elasticsearch import Elasticsearch

client = Elasticsearch(hosts=['localhost:9300'])

agg.bind(client=client, index_name='movies')


# In[67]:


df = agg    .query({'range': {'year': {'gte': '1950'}}})    .execute()


# In[68]:


df


# In[85]:


df.unstack('genres').avg_nb_roles.plot(figsize=(12,12), ylim=[0, 20])


# In[ ]:


df.plot()


# ## Query

# In[ ]:


from pandagg.utils import equal_queries
from pandagg.query import Nested, Bool, Query, Range, Term, Terms

q = Query()    .query({'terms': {'genres': ['Action', 'Thriller']}})    .nested(path='roles', _name='nested_roles', query=Term('roles.gender', value='F'))    .query(Range('rank', gte=7))    .query(Term('roles.role', value='Reporter'), parent='nested_roles')

q


# # Mapping

# In[38]:


from pandagg.client import Elasticsearch

client = Elasticsearch('localhost:9300')
indices = client.fetch_indices()


# In[39]:


movies = indices.movies


# In[40]:


movies.mapping


# In[ ]:




