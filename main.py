#!/usr/bin/env python3

"""
Example of edge_tts usage with a tkinter GUI.
"""

import asyncio
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import edge_tts
import os  # 添加这行导入

class EdgeTTSApp:
    def __init__(self, master):
        self.master = master
        master.title("SimpleTTS v0.0.1 by likoo")
        master.geometry("300x500")
        
        # 添加这行来设置图标
        master.iconbitmap('./assets/likoosong.ico')

        self.text_label = ttk.Label(master, text="输入要转换的文本:")
        self.text_label.pack(pady=5)

        # self.text_entry = ttk.Entry(master, width=40)
        self.text_entry = tk.Text(master, width=40, height=10)
        self.text_entry.pack(pady=5)

        self.voice_label = ttk.Label(master, text="选择配音员(默认云希):")
        self.voice_label.pack(pady=5)

        self.voice_combobox = ttk.Combobox(master, values=["zh-CN-YunxiNeural", "en-US-AriaNeural","zh-CN-XiaoxiaoNeural"])
        self.voice_combobox.set("zh-CN-YunxiNeural")
        self.voice_combobox.pack(pady=5)

        self.output_button = ttk.Button(master, text="创建输出文件", command=self.select_output_file)
        self.output_button.pack(pady=10)

        self.generate_button = ttk.Button(master, text="生成语音 MP3", command=self.generate_mp3)
        self.generate_button.pack(pady=5)  # 减少一些垂直间距

        self.play_button = ttk.Button(master, text="试听 MP3", command=self.play_mp3)
        self.play_button.pack(pady=5)
        self.play_button.config(state=tk.DISABLED)  # 初始状态为禁用

        self.status_label = ttk.Label(master, text="")
        self.status_label.pack(pady=30)

    def select_output_file(self):
        self.output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if self.output_file:
            self.status_label.config(text=self.output_file)

    def generate_mp3(self):
        text = self.text_entry.get("1.0", tk.END)
        voice = self.voice_combobox.get()
        if not hasattr(self, 'output_file'):
            self.status_label.config(text="请先选择或创建要输出的文件！")
            return
        asyncio.run(self.generate_mp3_async(text, voice, self.output_file))
        self.play_button.config(state=tk.NORMAL)  # 生成成功后启用播放按钮

    async def generate_mp3_async(self, text, voice, output_file):
        try:
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(output_file)
            self.status_label.config(text="MP3 generated successfully!")
            self.play_button.config(state=tk.NORMAL)  # 生成成功后启用播放按钮
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            self.play_button.config(state=tk.DISABLED)  # 生成失败时禁用播放按钮

    def play_mp3(self):
        if hasattr(self, 'output_file') and os.path.exists(self.output_file):
            os.startfile(self.output_file)  # 在 Windows 上使用系统默认应用打开文件
        else:
            self.status_label.config(text="No MP3 file available to play.")

def main():
    root = tk.Tk()
    app = EdgeTTSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()