# 雨课堂自动签到插件
## 由于已经没课了，没办法再进行测试，大概不会更新了，可以自行进行功能拓展
## 依赖
以下依赖需自行安装，请自行查阅教程，不安装会报错

playwright
## 配置文件
需要将以下信息写入env文件

1. username：你的雨课堂账号
2. password：你的雨课堂密码
3. superuser：（nb内置参数）你的qq号
   
## 说明
该插件通过playwright模拟浏览器登陆雨课堂，并在有课的时候向superuser私聊发送提醒。提醒会告知superuser是否有视频直播或者腾讯会议号。

检查时间：周一至周五，上午8点，十点8分，下午2点，下午4点8分

如需检查其他时间的课程请自行修改定时器部分代码

## 指令
ykt：检查现在是否正在上课