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