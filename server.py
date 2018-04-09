import Pyro4
import os


@Pyro4.expose
class Media(object):

    def media_list(self, type_operation=None, file_name=None):
        print(os.name)
        print(os.uname())
        print(os.getcwd())
        media_tech = "/home/malachite/PycharmProjects/untitled/media"
        print(os.listdir(media_tech))
        files = os.listdir(media_tech)
        if type_operation == 'list':
            return files
        if type_operation == 'get':
            for file in files:
                if file_name == file:
                    return file


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Media)
ns.register("ftp.media", uri)

print('start server')
daemon.requestLoop()

