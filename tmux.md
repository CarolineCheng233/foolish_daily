* tmux ls                    列出所有tmux session

  tmux new -s xxx            创建session
  
  tmux at -t xxx             进入xxx session
  
  tmux kill-session -t xxx   关闭会话
  
  tmux kill-session          关闭上次打开的会话
  
  tmux rename -t s1 s2       重命名会话s1为s2
  
  同一个session新建窗口会复制旧窗口的环境
  
  新建session会复制bash环境


* ctrl+b c        创建同一个session的新窗口

  ctrl+b p        previous window

  ctrl+b n        next window

  ctrl+b <number> window number

* ctrl+b %        左右分屏

  ctrl+b "        上下分屏

  ctrl+b 方向键   切换panel

* ctrl+b d        退出session

  exit/ctrl+d     终止ssession