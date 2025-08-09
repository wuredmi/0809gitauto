~~~~ 【YML語法】 ~~~~
參考講義6「YML & Github Actions.pdf」
0809gitauto
https://github.com/wuredmi/0809gitauto.git

先clone下來：git clone https://github.com/wuredmi/0809gitauto.git

測試自動hello.yml
------------------
# 檔名：.github/workflows/hello.yml

name: Hello World Workflow

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - name: 顯示問候
      run: echo "Hello, GitHub Actions!"
------------------

然後把這個檔，上傳到github
用UI (TortoiseGit)
>滑鼠右鍵 → TortoiseGit> 加入... >選擇全部的檔案
>滑鼠右鍵 → Git提交 -> main
>滑鼠右鍵 → Git同步 選擇 「推送」
------------------
GitHub的啟動方式
選單「Actions」
