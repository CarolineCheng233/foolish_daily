tar -[parameter]：打包/压缩文件

* -c  创建打包文件
* -x 解压缩/解打包
* -j 通过bzip2的支持进行压缩/解压缩，文件后缀为.tar.bz2
* -z 通过gzip的支持进行压缩/解压缩，文件后缀为.tar.gz
* -v 压缩/解压缩过程中，将正在处理的文件名显示出来
* -f 其后跟压缩文件名称
* -C 解压缩到指定目录



e.g.

```shell
tar -czvf test.tar.gz cur_dir   压缩成gzip的格式，显示处理过程中的文件名

tar -xzvf test.tar.gz 解压缩文件到当前目录

tar -xzvf test.tar.gz -C /etc 解压缩到/etc目录

tar -xzvf test.tar.gz etc/udev 仅解压缩tar文件里的etc/udev目录
```
