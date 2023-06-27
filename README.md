# ws-clipboard
A simple python websocket server that copies received messages into system clipboard.

This uses [`pyperclip`](https://pypi.org/project/pyperclip/) under the hood, which should work out of box for Windows and MacOS. For Linux, you may need to install `xclip` or `xsel` depending on your distro.

## Install requirements
```bash
pip install -r requirements.txt
```

## Start server
```bash
python server.py [PORT]
```
If `[PORT]` is ommited, the default port is 8881

## Why
I use this on my headless dev VM so I can yank from neovim to host
```lua
-- save yanked text to host
-- this uses websocat and a websocket server running on the host machine
vim.cmd([[
augroup YankToScript
  autocmd!
  autocmd TextYankPost * if v:register == '+' | call writefile([getreg('+')], '/tmp/yank') | silent! execute '!bash -c "source ~/.bashrc && cat /tmp/yank | websocat -1 -t -u ws://$HOST_MACHINE_IP:8881"' | redraw! | endif
augroup END
]])
noremap('v', '<leader>y', '"+y')
```
This requires `export HOST_MACHINE_IP=<IP>` in your `~/.bashrc` and `cargo install websocat` in the system
