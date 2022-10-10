import os


current_path = os.path.abspath (__file__)

config_dir = os.path.dirname (current_path)

root_dir = os.path.dirname (config_dir)

data_dir = os.path.join (root_dir, 'data')

case_file =  os.path.join (data_dir, 'cases.xlsx')
# case_file=case_file.replace ('\\\\', '\\')

host = 'http://api.lemonban.com:8766/'

# print (case_file)
#  需要  D:\自动化测试学习\Study_unittest\Lesson_21\data\cases.xlsx