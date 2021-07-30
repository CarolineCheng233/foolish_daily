* 全局换源

```shell script
中科大(比较快速)
pip config set global.index-url http://mirrors.ustc.edu.cn/pypi/simple/
阿里云
pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
清华(推荐,不过也经常出现网络连接问题)
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
```

* 临时使用源
```shell script
pip install xxx -i https://pypi.mirrors.ustc.edu.cn/simple/
```

* 更新源

```shell script

```