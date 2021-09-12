* 列出所有tmux session
```shell
   tmux ls
```

* 创建session
```shell
   tmux new -s xxx            
```

* 进入xxx session
```shell
   tmux at -t xxx             
```

* 关闭会话
```shell
   tmux kill-session -t xxx   
```

* 关闭上次打开的会话
```shell
   tmux kill-session          
```

* 重命名会话s1为s2
```shell
   tmux rename -t s1 s2       
```


  同一个session新建窗口会复制旧窗口的环境
  
  新建session会复制bash环境


* 创建同一个session的新窗口
```shell
   ctrl+b c
```

* previous window
```shell
   ctrl+b p
```

* next window
```shell
   ctrl+b n        
```

* window number
```shell
   ctrl+b <number> 
```

* 左右分屏
```shell
   ctrl+b %        
```

* 上下分屏
```shell
   ctrl+b "        
```

* 切换panel
```shell
   ctrl+b 方向键    
```

* 退出session
```shell
   ctrl+b d        
```

* 终止session
```shell
   exit/ctrl+d     
```
* 启用鼠标
1. 编辑文件 ~/.tmux.conf，在其中加入以下内容 \
(for tmux -V > 2.1)
```shell
set-option -g mouse on
```
(for tmux -V <= 2.1)
```shell
setw -g mouse-resize-pane on
setw -g mouse-select-pane on
setw -g mouse-select-window on
setw -g mode-mouse on
```
2. 
```shell
tmux source-file ~/.tmux.conf
```

* zsh autosuggestions提示浅色显示
```shell script
编辑~/.tmux.conf文件 set -g default-terminal "screen-256color"
```

* 取消窗口自动命名，在~/.tmux.conf文件中添加以下内容
```shell script
set-option -g allow-rename off
set -g status-keys vi
set -g history-limit 10000
```