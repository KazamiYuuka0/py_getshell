import threading
import subprocess
def thread_(path):
    subprocess.call(path)
    print('over')
    return 0
thread1 = threading.Thread(target=thread_,args=('gamedata.dll',))
thread1.start()
