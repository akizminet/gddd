import os
import re

book_dir = '/home/phamnv/dev/gddd/book'
summary_file = os.path.join(book_dir, 'SUMMARY.md')

with open(summary_file, 'r') as f:
    content = f.read()

pattern = re.compile(r'\[.*?\]\((.*?\.md)\)')
referenced = set(pattern.findall(content))
referenced.add('SUMMARY.md')

print("Referenced files from SUMMARY.md:")
for ref in sorted(referenced):
    print("  -", ref)

deleted_count = 0
for root, dirs, files in os.walk(book_dir):
    for file in files:
        if file.endswith('.md'):
            rel_path = os.path.relpath(os.path.join(root, file), book_dir)
            if rel_path not in referenced:
                file_to_delete = os.path.join(root, file)
                print("Deleting:", rel_path)
                os.remove(file_to_delete)
                deleted_count += 1

print("Total files deleted:", deleted_count)
