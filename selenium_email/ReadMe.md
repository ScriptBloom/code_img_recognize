### 该方法使用selenium自动化测试框架，结合Chromedriver对网页中验证码进行截图并保存到本地，保存完成后通过smtp服务发送到你的邮箱，你查看后再爬虫程序运行中输入邮件中的验证码并继续爬虫，可能速率有一定影响


- 需要安装selenium模块

****

配置项：
- chromedriver_path 路径
- SAVE_CODE_PATH 保存路径
- email_username 163邮箱
- email_password 163邮箱密码
- target_email 接受验证码邮箱

***


- 下载Chromedriver并安装：https://blog.csdn.net/MenofGod/article/details/88421010
- pip安装需要的模块
- 注册一个163邮箱用于发送验证码（注册完成后记得开启客户端授权`入邮箱中心——客户端授权密码，选择开启`，打开smtp服务）
- 在程序中配置你的验证码存储路径、Chromedriver路径、邮箱账号密码、接收邮箱账号