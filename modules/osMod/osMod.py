import os
from datetime import datetime

# print(os.getcwd())

os.chdir('E:\Python3')
# print(os.getcwd())
# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1')
# os.rmdir('OS-Demo-2/Sub-Dir-1')
# os.removedirs('OS-Demo-2/Sub-Dir-1')
# os.rename('text.txt', 'demo.txt')
# print(os.stat('demo.txt'))

# modtime = os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(modtime))
# print(os.listdir())

# for dirpath, dirnames, filename in os.walk('E:\Python3'):
# 	print('Current Path', dirpath)
# 	print('Directories', dirnames)
# 	print('Files', filename)
# 	print()

# print(os.environ)
# print(os.environ.get('HOMEPATH'))

# filepath = os.path.join(os.environ.get('HOMEPATH'), 'text.txt')
# print(filepath)

# print(os.path.basename('/tmp/test.txt'))
# print(os.path.dirname('/tmp/test.txt'))
# print(os.path.split('/tmp/test.txt'))
# print(os.path.exists('/tmp/test.txt'))

print(os.path.isdir('/tmp/test'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))