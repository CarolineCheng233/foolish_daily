* conda create -n name python=3.8          创建环境并制定python版本

* conda remove -n name --all               删除环境
* conda create -n new_name --clone name    复制环境

* 重命名环境 先复制再删除

* 更新conda:\
  conda update -n [name] conda

* conda remove package          移除当前环境下的package包
* conda remove -n name package  移除name环境下的package包