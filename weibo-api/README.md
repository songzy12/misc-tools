微博 API：<https://open.weibo.com/wiki/微博API>

新建 `config.py`， 并填入 `UID` 和 `access_token` 。

## 移除垃圾粉丝

运行如下命令：

```
python friendships.py
```

然后依次点击打印出的用户主页链接，确认后手动移除粉丝。

注意：这里不知道为什么在清除完垃圾粉丝后会有新的输出，所以在移除粉丝时要注意确认。

## 测试

```
python -m unittest -v utils_test
```

## 参考

<https://github.com/dataabc/weiboSpider>
