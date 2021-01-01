1. 查看系统中有无zsh\
    cat /etc/shells

2. 若无，安装zsh  \
    sudo apt-get install zsh

3. 更改默认shell为zsh  \
    sudo chsh -s $(which zsh)  \
    退出登录使修改生效

4. 查看默认shell  \
    echo $SHELL

5. 安装oh my zsh  \
   wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh  \
    -O - 表示在终端展示文件内容

6. (option)修改oh-my-zsh的主题 \
   查看已有主题 ls \~/.oh-my-zsh/themes  \
    在~/.zshrc中修改 ZSH_THEME=“ys”  或其他主题\
     source ~/.zshrc 使其生效

7. 安装oh-my-zsh插件

   cd ~/.oh-my-zsh/custom/plugins/

   * zsh-syntax-highlighting  使语法高亮 \
     git clone https://github.com/zsh-users/zsh-syntax-highlighting \
      在~/.zshrc里找到 plugins=(git) ，在括号里加入zsh-syntax-highlighting

   * autojump 不用输入完整路径即能跳转到文件目录 j dir \
     必须是之前cd过才能自动跳转 \
     git clone https://github.com/wting/autojump  \
     cd autojump; sh install.py \
     重启终端 \
     在~/.zshrc里加入如下命令 \
     [[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh

   * zsh-autosuggestions  命令自动补全 \
     git clone https://github.com/zsh-users/zsh-autosuggestions \
     在~/.zshrc里加入 plugins=(* zsh-autosuggestions)

     

#### 安装完以后别忘记将~/.bashrc里的各种环境变量迁移过来，例如anaconda初始化

