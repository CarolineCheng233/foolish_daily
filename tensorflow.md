全程使用conda安装
注意版本匹配,见官网
```shell
https://www.tensorflow.org/install/source
```

从中可以找到在linux上安装gpu版本的tensorflow
```shell
https://www.tensorflow.org/install/source#gpu
```

要注意 python 和 CUDA 一定要满足相应的版本要求,并且也需要安装cudnn

cudnn的安装,可以使用国内源,具体有哪些版本可以查看源列出的list,如果没有相应版本conda会提示下列url中找不到相应的版本
```shell
conda install cudnn==7.6.0
```


最后,安装tensorflow
2.x以上的版本是gpu和cpu合在一起安装,如果没有相应的CUDA支持则会安装cpu版本
```shell
conda install tensorflow==2.0.0  # 依个人情况而定
```

如果python的版本不满足要求,也请使用conda升级或者降级