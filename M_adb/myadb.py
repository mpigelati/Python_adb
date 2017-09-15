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
        print(cmd_list)
        #print("generating build command and returning from __build_cmd_() function  "," ".join(cmd_list))
        return " ".join(cmd_list)

    def run_cmd(self,cmd):
        print("start_run_cmd {%s}" % cmd)
        self._clear_()
        #self._build_cmd_(cmd)
        #print(self._build_cmd_(cmd))
        try:
            self.__cmd = self._build_cmd_(cmd)
            # print("[cmd]",self.__cmd)
            command = subprocess.check_output(self.__cmd,shell=True)
            #print ("type",type(command))
            print ("command",command)
            #print ("successfully executed build command",self.__cmd)
            return  command
        except OSError, e:
           self.__error = str(e)
            #self.__error = str(e)
           print (self.__error)
           print ("Failed to execute",self.__cmd)

    def device_filter(self,cmd):
        #print ("device_filter",cmd) #Output :- ('device_filter', 'List of devices attached \n7dab6ce3\tdevice\n\n')
        dev = cmd.split(" ")[4]
        dev = dev.split("\t")[0].strip("\n"),
        #dev=dev.rstrip("\n")
        #print dev
        self.__devices= dev

    def adb_devices(self):
        #print("adb devices")

        try:
            self.__devices=None
            cmd=self.run_cmd("devices")
            #print cmd
            self.device_filter(cmd)
            print("cc",self.__devices)

        except :
            self.__devices-=None
            print (self.__devices)
    def adb_root(self):
        #print(a devices")
        #self.__devices = None
        try:
            self.adb_devices()
            if self.__devices !=None:
               data = self.run_cmd("root")
               print("root fun",data)
        except OSError,e:
            

            self.__devices=None



        #print(__data__)
#print(hellow())
#print(call_class())'''