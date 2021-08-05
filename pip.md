* 全局换源

```shell script
中科大(比较快速)
pip config set global.index-url http://mirrors.ustc.edu.cn/pypi/simple/
阿里云
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
清华(推荐,不过也经常出现网络连接问题)
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
豆瓣
pip config set global.index-url http://pypi.douban.com/simple/
```

* 临时使用源
```shell script
pip install xxx -i https://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.doubanio.com(添加信任,此目的是为了)
```

写入~/.config/pip/pip.conf文件
```shell script
[global]
index-url = http://pypi.douban.com/simple/
trusted-host = pypi.douban.com
```

by the way,我因为tensorflow的安装需要将python版本从3.8降到3.7之后,使用pip出了问题.
目前还不清楚是什么原因,可能是urllib3的版本太高导致的,要降到1.25.8及以下
pip安装的时候还得使用豆瓣源以及加上--trusted-host参数