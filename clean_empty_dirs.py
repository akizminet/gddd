import os

book_dir = '/home/phamnv/dev/gddd/book'

deleted_dirs = 0
for root, dirs, files in os.walk(book_dir, topdown=False):
    for d in dirs:
        dir_path = os.path.join(root, d)
        if not os.listdir(dir_path):
            print("Removing empty directory:", os.path.relpath(dir_path, book_dir))
            os.rmdir(dir_path)
            deleted_dirs += 1

print("Total empty directories removed:", deleted_dirs)
