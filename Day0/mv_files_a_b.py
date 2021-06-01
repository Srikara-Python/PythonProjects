import shutil
import os

src = "D:\\test\\"
dst = "D:\\Lab\\"

files = os.listdir(src)

# count total files in source
list      = os.listdir(src)
src_count = len(list)


# Move files
for f in files:
    shutil.move(src + f, dst)

# count files in destination
list      = os.listdir(dst)
dst_count =  len(list)

print("src count was ", src_count, " dst count is ",dst_count)

