import sys
import time
import getopt

version: str = 'Beta 0.0.2'

def Exception(location: any, name: str, discripton: str):
    print("---------------------------------------------------------------------------")
    print("  出了点小问题（" + time.strftime("%H:%M:%S", time.localtime()) + "）：")
    print("    在", location, "中")
    print("  " + name + "：" + discripton)
    print("---------------------------------------------------------------------------")
    sys.exit()

def run(sentence: str):
    pass

try:
    args = getopt.getopt(sys.argv[1:],'',['help','version'])
except getopt.GetoptError:
    Exception(sys.argv[0:], "参数错误", "未知的参数：" + str(sys.argv[1:]))

if len(args[0]) > 0:
    if "--help" in args[0][0]:
        print("Xuanny", version)
        print("Copyright (c) 2023 轩哥啊哈OvO")
        print("An interpreted, object-oriented, high-level chinese programming language with dynamic semantics.\n一种具有动态语义的解释型、面向对象的高级中文编程语言。\n")
        print("Usage/用法: \n")
        print("    xuanny [filename] <options>\n")
        print("其中, 可能的选项包括:\n")
        print("    --help  查看帮助")
        print("    --version  查看 Xuanny 版本\n")

    if "--version" in args[0][0]:
        print("Xuanny", version)

if len(args[1]) > 0:
    filename = args[1][0]
    try:
        with open(filename, encoding='utf-8') as file_obj:
            sentence = file_obj.read()
            run(sentence)
    except FileNotFoundError:
        Exception(sys.argv[0:], "文件读取错误", "找不到文件：" + str(sys.argv[1:]))
