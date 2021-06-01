# pip install watchdog
# more events on_deleted, on_created_ on_moved

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for file_name in os.listdir(src_dir):

            # Get file extension
            ext = os.path.splitext(file_name)[1][1:].lower()

            src = src_dir + file_name

            # Create new folder if not exists e.g pdf, jpeg, png
            dst = os.path.join(dst_dir, ext)

            # If file/folder already exists
            try:
                os.mkdir(dst)
            except WindowsError:
                print("already exists")
            
            # Move File
            print("moving file to =",dst)
            shutil.move(src, os.path.join(dst, os.path.basename(src)))

    

src_dir = "D:\\test\\"
dst_dir = "D:\\Lab\\"


event_handler = MyHandler()
obeserver = Observer()
obeserver.schedule(event_handler, src_dir, recursive=True)
obeserver.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    obeserver.stop()
obeserver.join()
