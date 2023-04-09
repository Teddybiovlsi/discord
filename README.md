[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-3716/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


## ⚡ Introduction 簡介

### **Discord Python MapleStory 琉德-挑食怪公會用機器人**

**Discord Pyhon Bot 骨架**

<br>

## 📥 Installation 安裝指南
> 運行環境 建議 `Python 3.7` 以上 / `discord.py 1.7` 以上<br>當前環境為`Python 3.7`/ `discord.py 1.7.3`

1. 下載整個專案  
2.  解壓後將 `example_setting.json` 重新命名為 `setting.json` ; 自行修改設定檔裡的資料  
3. 運行 `bot.py` 即可

<br>

## 🔩 Folder structure 資料夾結構
```
/ # 根目錄
------------------------------------
- bot.py # bot 啟動主文件
- example_setting.json # 設定檔


/cmds # 放置所有 Cog 指令
------------------------------------
- main.py  #主要指令區(舉凡需要加上!號的在這檔案進行編寫)(可自行設定)
- event.py # 所有 event 觸發性事件指令區
- mod.py # 管理、控制類指令區
- owner.py # 擁有者權限指令區


/core  #放置類別、核心通用功能
------------------------------------
- classes.py # 主要類別區
- check.py # 自定全域指令檢查器
- error.py # 預設、自訂 錯誤管理器
```
