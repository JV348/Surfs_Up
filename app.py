#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import the Flask dependency
from flask import Flask


# In[3]:


# Create a new Flask instance called app
app = Flask(__name__)


# In[4]:


## Create Flask Routes

# First flask route 
@app.route('/')
def hello_world():
    return 'Hello world'


# In[ ]:


## Run a Flask App

# Set the FLASK_APP environment variable to the name of our Flask file, app.py
export FLASK_APP=app.py

