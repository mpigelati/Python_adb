import os
import  subprocess

class madb(object):
    __adbpath=None
    __output=None
    __error=None
    __devices=None

    def __init__(self,adbpath="adb"):
        self.__adbpath=adbpath

    def _clear_(self):
        self.__output = None
        self.__error  = None
        print("data cleased")

    def _build_cmd_(self,cmd):
        print("you are in build command {%s}" % cmd)
        a=list(cmd)
        print (type(a))
        a.insert(0,self.__adbpath)
        a.insert(1,cmd)
        print a
    def run_cmd(self,cmd):
        print("running {%s}" % cmd)
        self._clear_()
        self._build_cmd_(cmd)



    def adb_devices(self):
        print("adb devices")
        self.__devices=None
        self.run_cmd("devices")




#print(__data__)
#print(hellow())
#print(call_class())'''