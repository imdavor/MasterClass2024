# 140. Writing & Appending Data To A File
file = open('data.txt', 'w')
file.write('Novi sadrzaj u fileu')
file.close()

#
"""# Opening A File
file = open('data.txt', 'r')
# 139. Reading Data From A File
# content = file.read()
content = file.readline()
print(content)
file.close()
"""
