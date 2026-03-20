#!/usr/bin/env python
# coding: utf-8

# In[2]:


todos=[]
id_counter=1


# In[3]:


def add_task(task):
    global id_counter
    todos.append({'id':id_counter, 'task':task})
    id_counter+=1


# In[4]:


add_task("learn python")
add_task("build project")

print(todos)


# In[7]:


def delete_task(task_id):
    for item in todos:
        if item['id']==task_id:
            todos.remove(item)
            return "Deleted"
    return "Not Found"


# In[8]:


delete_task(1)
print(todos)


# In[9]:


add_task("Coding")


# In[10]:


print(todos)

