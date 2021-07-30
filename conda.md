* conda安装
```shell script
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh
conda init
```

* 使用官网上最新的安装包
```shell script
https://www.anaconda.com/products/individual#Downloads
```

```shell script
conda create -n name python=3.8          创建环境并制定python版本
conda remove -n name --all               删除环境
conda create -n new_name --clone name    复制环境
conda update -n [name] conda             更新conda
conda remove package                     移除当前环境下的package包
conda remove -n name package             移除name环境下的package包
```

* 重命名环境 先复制再删除

* conda 查看源
```shell script
conda config --show-sources
```

* conda 添加中科大源
```shell script
cconda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
```

* 更新库
```shell script
conda update --all
```

