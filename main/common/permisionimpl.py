#coding: utf-8
 
from flask import request,session
from functools import wraps

def check_session_id(session_id = None,remote_addr = None):    
    return True

def permision_allowed(func):
    @wraps(func)
    def wrapper(*arg,**kwargs):
        session_id = request.headers.get('Session-Id')
        status = check_session_id(session_id, request.remote_addr)
        
        if status:
            return func(*arg,**kwargs)
        else:
            return "missing session id, please login again!"
 
    return wrapper