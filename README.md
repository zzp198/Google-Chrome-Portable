屠龙者终成恶龙，再见了Edge. 此项目在前人的肩膀上，加入了自己喜欢的定制。

# 功能

- ~~双击关闭标签页~~
- ~~保留最后标签页（防止关闭最后一个标签页时关闭浏览器，点X不行）~~
- 根据个人习惯取消了双击关闭，避免误触带来的麻烦
- 鼠标悬停标签栏滚动
- 按住右键时滚轮滚动标签栏
- ~~便携设计，程序放在App目录，数据放在Data目录（不兼容原版数据，可以重装系统换电脑不丢数据）~~
- 便携设计，程序放在Chrome目录，数据和缓存放在同级目录Data\Cache下，不会在%User%/AppData中建立目录（不兼容原版数据，可以重装系统换电脑不丢数据）
- 移除更新错误警告，移除不必要的显示（因为是绿色版没有自动更新功能）

# 获取

全自动无人管理项目，每周定时拉取最新Chrome离线包，并封装为便携版。

采用GitHub
Actions自动编译发布，下载地址：[https://nightly.link/zzp198/Google-Chrome-Portable/workflows/build/main](https://nightly.link/zzp198/Google-Chrome-Portable/workflows/build/main)

[![build status](https://github.com/zzp198/Google-Chrome-Portable/actions/workflows/build.yml/badge.svg)](https://github.com/zzp198/Google-Chrome-Portable/actions/workflows/build.yml)

# 安装

**解压Chrome文件夹，为Chrome.exe建立桌面快捷方式即可**

# 更新

无法自动更新，未来可以建立独立的绿色升级软件，原Chrome每4周发布一次新版本，定时为每周，会出现最新的版本相同的情况，平时不需要频繁升级。

**保留Chrome文件夹中的Data和Cache,其他文件删除后解压新压缩包即可，单纯的文件替换。**

# 卸载

删除Chrome文件夹，删除快捷方式即可，无残留。**注意提前保存Data，避免自己的个人浏览数据清空（可谷歌账号同步，但不如Data全面）。**
