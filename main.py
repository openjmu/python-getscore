# -*- coding: utf-8 -*-
import os
import func

os.system("title 集美大学教务系统获取成绩 v20180121 - Author : https://blog.alexv525.com/")
temp_dir = (os.environ["TMP"])+'\\scoreTemp'
try:
    func.cleanDir(temp_dir)
except FileNotFoundError:
    pass
os.mkdir(temp_dir)

# 登录过程
username = input('输入用户名： ')
password = input('输入密码： ')
flag = func.userLogin(func.predictCheckCode(func.getCheckCode()), username, password)

# 登录后执行抓取评测列表，进行逐个评测
if flag == 1:
    term = input("输入学年学期：")
    print("获得成绩列表中...")
    score_url = 'http://jwgls.jmu.edu.cn/Student/ScoreCourse/ScoreAll.aspx'
    viewstate = func.getViewstate()
    score_list = str(func.getPage(score_url, term, viewstate))
    course_name, course_score = func.scoreRead(score_list)
    print(' ')
    print(' ', '课程名称'.ljust(20, " "), ' ', '课程成绩'.ljust(5, ' '), ' ')
    for i in range(0, len(course_name)):
        print(' ', course_name[i].ljust(12, "　"), ' ', course_score[i].ljust(5, '　'), ' ')
    print(' ')
    
os.system('pause')
