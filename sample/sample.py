import sys


#sys.path.append('/home/mohansai/python/Python_adb/M_adb')
sys.path.append("/home/mohansai/python/Python_adb/M_adb")
#from M_adb import myadb as adb
#import M_fastboot
import myadb
#from myadb import myadb


def main():
    #print(myadb.hellow())
    adb = myadb.madb()

    adb._data_()
    adb.run_cmd("adb devices")
    print(adb.run_cmd)









if __name__ == "__main__":
    main()