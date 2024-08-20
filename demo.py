# 142. Readline & Readlines


# 141. Opening Files Using With
# with se koristi za otvraanje fileova i zatvaranje da ne moramo koristiti file.close svaki put
# with open('data.txt', 'r') as file:
#     contents = file.read()
#     print(contents)

"""# 140. Writing & Appending Data To A File
file = open('data.txt', 'a')
content = ('\n5. Novi sadrzaji u fileu')
file.write(content)
file.close()"""

#
"""# Opening A File
file = open('data.txt', 'r')
# 139. Reading Data From A File
# content = file.read()
content = file.readline()
print(content)
file.close()
"""
