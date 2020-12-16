* 添加快捷键ctrl+s保存文件

  在~/.bashrc里加入

  ```
  stty stop ''
  ```

  在~/.vimrc里加入

  ```
  map <C-s> :w<CR>
  imap <C-s> <C-o>:w<CR>
  ```