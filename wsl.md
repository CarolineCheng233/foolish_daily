* 迁移硬盘
1. 在设置中打开开发人员模式
2. 管理员权限打开PowerShell, 运行
```shell script
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```
3. 下载LxRunOffline, 选择mingw.zip后缀的压缩文件
https://github.com/DDoSolitary/LxRunOffline/releases
4. 解压后用PowerShell运行查看子系统名称
```shell script
LxRunOffline.exe list
```
5. 关闭wsl
```shell script
wsl --shutdown
```
6. 运行命令
```shell script
LxRunOffline.exe move -n <WSL name> -d <file_path>
```

似乎迁移磁盘之后能够解除wsl挂载磁盘的写保护==之前碰到一个问题是wsl原来的挂载盘在C盘，C盘快满了的时候wsl磁盘被写保护，一直解决不了这个问题，索性迁移了磁盘之后写保护被自动解除了==


* 使用主机vpn
1. 设置https_proxy, http_proxy为windows的ip地址
```shell script
export hostip=$(ip route | grep default | awk '{print $3}')
export https_proxy="http://${hostip}:7890"
export http_proxy="http://${hostip}:7890"
export all_proxy="socks5://${hostip}:7890"
```
2. 主机vpn打开"允许局域网连接"
3. windows防火墙设置入站规则-端口-允许7890连接
