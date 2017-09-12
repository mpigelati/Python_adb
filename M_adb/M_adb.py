import os
import  subprocess

class I_adb :

    __output=None
    __error=None

    def __clear__(self):
        self.__output = None
        self.__error  = None
        print("data cleasrd")

    def __data__(self):
        self.__output = 1
        self.__error  = 1
        print("you are in data ")


def hellow()

    print("hellow world)