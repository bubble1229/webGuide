欢迎使用个人导航网站

概述：
  适用于小团队建立自己的导航，利于新同学，也方便知识库的引导与分享。
  python开发，200行代码。
  搭建的一个网站：测试人导航 http://nobug.sinaapp.com/

一、需要安装的软件：
  1.python,下载地址：http://www.python.org/ftp
   下python2.x的版本，web.py还不支持python3。加环境变量。
  2.web.py,安装指南：http://webpy.org/install
   下载解压后安装：python setup.py install
  3.下载webGuide代码
  4.sqlite3数据库
二、替换LOGO图片：static\images\logo.jpg 和 favicon.ico
三、启动
  1.python webGuide.py 80
  2.http://localhost/
四、添加导航分组和地址(添加后只能编辑/删除，不支持调整顺序)
五、如果手动修改数据库，需要在页面上点刷新内存。
六、sqlite3数据库工具下载：http://www.sqliteexpert.com/SQLiteExpertPersSetup.exe