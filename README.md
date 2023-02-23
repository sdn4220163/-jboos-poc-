# jboss_poc

#### 介绍
利用fofa搜索关键字，批量检测网站中是否存在jboss的反序列化漏洞。

#### 安装教程

需要安装python模块：
pip3 install requests
pip3 install queue
pip3 install threading
pip3 install base64
pip3 install lxml
#### 使用说明
免责声明，本工具仅限学习使用，严禁用于违法犯罪，发生任何问题、违反任何法律都与发布者无关！
运行前请将以上模块安装好，打开host_collection.py  修改第25行代码，将自己的fofa的账号cookie复制到引号内，在用CMD执行host_collection.py
生成一个domains_CN.txt文件，然后运行jboss_poc.py