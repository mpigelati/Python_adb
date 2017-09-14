import os
import  subprocess

class madb(object):

    __adbpath=None
    __output=None
    __error=None
    __devices=None
    __cmd=None

    def __init__(self,adbpath="adb"):
        self.__adbpath=adbpath

    def _clear_(self):
        self.__output = None
        self.__error  = None

    def _build_cmd_(self,cmd):
        #print("you are in build command {%s}" % cmd)
        cmd_list=[]
        #print(type(cmd))
        cmd_list.insert(0,self.__adbpath)
        cmd_list.insert(1,cmd)
        #print(cmd_list)
        print("generated build and returning from __build_cmd_ "," ".join(cmd_list))
        return " ".join(cmd_list)

    def run_cmd(self,cmd):
        print("start_run_cmd {%s}" % cmd)
        self._clear_()
        #self._build_cmd_(cmd)
        #print(self._build_cmd_(cmd))
        self.__cmd=self._build_cmd_(cmd)
        print("[cmd]",self.__cmd)

        command=subprocess.check_output(self.__cmd,shell=True)
        print ("type",type(command))
        print(command)
        data = command.split(" ")[0]
        print data
        data = command.split(" ")[1]
        print data
        data = command.split(" ")[2]
        print data
        data = command.split(" ")[3]
        print data
        data = command.split(" ")[4]
        print ("data",data)
        #data = command.split(" ")[5]
        #print data

    def adb_devices(self):
        #print("adb devices")
        self.__devices=None
        self.run_cmd("devices")

    def adb_root(self):
        #print("adb devices")
        self.__devices = None
        self.run_cmd("root")




        #print(__data__)
#print(hellow())
#print(call_class())'''