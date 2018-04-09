import Pyro4

media = Pyro4.Proxy("PYRONAME:ftp.media")
while 1:
    print(media.media_list(type_operation='list'))

    name = input("choose file: ")
    print(media.media_list(type_operation='get', file_name=str(name)))
