微博 API：<https://open.weibo.com/wiki/微博API>

## 功能1：查询已失效转发微博

新建 `config.py`， 并填入 

1. `UID`: 通过查看个人主页 url 获得
2. `COOKIE`: 通过访问 http://weibo.com/ 并 F12 查看网络请求头文件获得。

运行如下命令：

```
python -m statuses
```

运行完成后结果会被写入本地文件以供查看。

## 功能2：查询垃圾粉丝

新建 `config.py`， 并填入 

1. `UID`: 通过查看个人主页 url 获得
2. `ACCESS_TOKEN`: 通过访问 https://open.weibo.com/tools/console 获得。

运行如下命令：

```
python -m friendships
```

然后依次点击打印出的用户主页链接，确认后手动移除粉丝。

注意：这里不知道为什么在清除完垃圾粉丝后会有正常粉丝的url输出，所以在移除之前时要注意确认是否确实为垃圾粉丝。

## 功能3：获取某条微博的点赞用户列表

新建 `config.py`， 并填入 

1. `STATUS_ID`: 感兴趣的微博状态ID
2. `COOKIE`: 通过访问 http://m.weibo.cn/ 并 F12 查看网络请求头文件获得。

运行如下命令：

```
python -m attitudes
```

## 功能4：对于点赞用户列表里的每一个用户，获取用户信息

新建 `config.py`， 并填入 

1. `ATTITUDES_FILENAME`: 点赞用户列表输出文件。
2. `COOKIE`: 通过访问 http://m.weibo.cn/ 并 F12 查看网络请求头文件获得。

运行如下命令：

```
python -m user_info
```
