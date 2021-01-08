* 压缩
```shell script
zip -r <zip_file_name>.zip <to_be_zip_directory>  -r 表示递归压缩
zip -m <zip_file_name>.zip <to_add_file>          -m 表示向压缩文件里添加文件
```
* 解压缩
```shell script
unzip -d <to_unzip_directory> <zip_file_name>.zip   -d 指定解压缩文件目录
unzip <zip_file_name>.zip                              解压到当前目录
```