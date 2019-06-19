class School(object):
  def __init__(self, subject1):
    self.subject1=subject1
    self.subject2="cpp"
    
  #重写属性访问拦截器
  def __getattribute__(self, obj):
    if "subject1" == obj:
        return "redict python"
    else:#注意，如果注释后面的两行，其他属性会不能正常访问
        return object.__getattribute__(self, obj)
      
s = School("s1")
print(s.subject1)
print(s.subject2)
