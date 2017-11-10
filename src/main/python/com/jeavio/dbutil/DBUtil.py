'''
Created on 03-Nov-2017

@author: karthikeyan
'''
from sqlalchemy import create_engine


class DBUtil(object):

    def create_engine(self):
        return create_engine('mysql://root:root@127.0.0.1:3307/system_analyzer', echo=False)
