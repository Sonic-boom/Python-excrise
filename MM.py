def text_create(name, msg):
    desktop_path = 'C://Users/akuma/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


i = 0
while i < 10:
    i = i + 1
    text_create(str(i), 'i')
