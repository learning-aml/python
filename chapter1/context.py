#获取模块,文件名,行号,函数名

import sys  
import inspect  
import os  
  
def get_current_function_name():
    return inspect.stack()[1][3]
 
def get_attrs():  
    print('Module:', __name__)  
    print('File Path: ', __file__)  
    print('File Name: ', os.path.basename(__file__))  
    print('Line No.: ', sys._getframe().f_lineno)  
    print('Func: ', sys._getframe().f_code.co_name)
    
get_attrs()  
