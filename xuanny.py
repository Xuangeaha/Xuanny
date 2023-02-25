import sys
import time
import getopt

version: str = 'Beta 0.0.1'

def Exception(location: any, name: str, discripton: str):
    print("--------------------------------------------------")
    print("  出了点小问题（" + time.strftime("%H:%M:%S", time.localtime()) + "）：")
    print("    在", location, "中")
    print("  " + name + "：" + discripton)
    print("--------------------------------------------------")
    sys.exit()

try:
    arg = getopt.getopt(sys.argv[1:],'',['help','version'])
except getopt.GetoptError:
    Exception(sys.argv[0:], "参数错误", "未知的参数：" + str(sys.argv[1:]))

print(arg)