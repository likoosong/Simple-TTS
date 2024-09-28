# Simple-TTS

Simple-TTS 是一个简单的将文本转换成语音的小工具，方便在小视频中增加“台词”......

## 功能介绍

- 太简单，啥也不是......


## 基本操作

- 输入需要转换成语音的文本。
- 选择一位voicer，下拉列表中默认自带两个voicer,可以在下拉列表中选择voicer。如果需要增加voicer，请在main.py中增加。voicer存放在/voice目录下的voice.json文件中。也可以通过如下命令查看支持的voicer：
```
edge-tts --list-voices
```
- 选择要保存的文件路径及文件名（默认保存为mp3格式），文件路径支持中文。
- 点击“生成MP3”按钮，开始转换。
- 转换完成后，会在文件路径中生成一个mp3文件。
- 点击“试听MP3”按钮，可以试听生成的MP3文件。
- 退出直接X掉窗口。:DDD

## 使用方法

1. 下载并安装Python 3.8及以上版本。
2. 下载并安装edge-tts库。
3. 下载并安装pyinstaller库，用于打包成exe文件。

```
# 安装edge-tts库
pip install edge-tts
# 安装pyinstaller库
pip install pyinstaller

# 打包成exe文件
pyinstaller -F -i likoosong.ico main.py -w

# 环境下直接运行
python main.py

```

