def read_file(filename):
    '''
    用来读取文件内容
    :param filename: 文件名
    '''
    with open(filename,'a+') as fr:
        fr.seek(0) # 移动文件指针
        content = fr.read() # content 类型是字符串
        print('content:',content)


read_file('users') # 调用函数


def write_file(filename,content):
    '''
    用来读取文件内容的
    :param filename: 文件名
    '''
    with open(filename,'a+') as fw:
        fw.seek(0) # 移动文件指针
        fw.truncate() # 清空文件内容
        fw.write(str(content))

        
write_file('a','hello world') # 调用函数