import pymem
import re
import win32api
import win32con
from time import sleep


wh_is_on = False


pm = pymem.Pymem('csgo.exe')
client = pymem.process.module_from_name(pm.process_handle,
                                        'client.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                         clientModule).start() + 2


while True:
    if win32api.GetAsyncKeyState(90): # 90 - Z
        pm.write_uchar(address, 1 if wh_is_on else 2)
        wh_is_on = not wh_is_on
        sleep(1)
    elif win32api.GetAsyncKeyState(win32con.VK_DELETE):
        break

pm.write_uchar(address, 1 if wh_is_on else 2)
pm.close_process()
