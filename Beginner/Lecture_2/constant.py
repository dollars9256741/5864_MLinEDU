#!/usr/bin/env python
# coding: utf-8

# In[1]:


PI = 3.14
GRAVITY = 9.8


# In[2]:


class constant:
    class ConstError(TypeError) : pass
    class ConstCaseError(ConstError):pass

    def __setattr__(self, name, value):
            if name in self.__dict__:
                raise Exception(self.ConstError, "Can't change const value!")
            if not name.isupper():
                raise Exception(self.ConstCaseError, 'const "%s" is not all letters are capitalized' %name)
            self.__dict__[name] = value

import sys
sys.modules[__name__] = constant()


# In[ ]:




