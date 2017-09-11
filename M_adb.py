import os
import  subprocess

class I_adb :

    __output=None
    __error=None

    def __clear__(self):

        self.__output = None
        self.__error  = None