import sys
import time
import getopt

version: str = 'Beta 0.1.1'

name = []
value = []
type = []

STR, INT, BOOL = "文字", "数字", "bool"

def Exception(location: any, name: str, discripton: str):
    print("---------------------------------------------------------------------------")
    print("  出了点小问题（" + time.strftime("%H:%M:%S", time.localtime()) + "）：")
    print("    在", location, "中：")
    print("  " + name + "：" + discripton)
    print("---------------------------------------------------------------------------")
    sys.exit()

def _define(_name, _value):
    try:
        _nameTran = int(_name)
        Exception(sentences,"变量错误","不支持的变量名 " + sentence[0])
    except ValueError:
        pass

    try:
        _valueTran = int(_value)
        _type = INT
        try:
            if sentence[3] == "文字":
                _type = STR
        except IndexError:
            pass
    except ValueError:
        _valueTran = str(_value)
        _type = STR
        try:
            if sentence[3] == "数字":
                Exception(sentences,"类型错误",sentence[0] + "的类型应为 '文字'，实际为 '数字'")
        except IndexError:
            pass

    for _key_define in range(0,len(name)):
        if name[_key_define] == _name:
            value[_key_define] = _valueTran
            type[_key_define] = _type
            print(name,value,type)
            return
    name.append(_name)
    value.append(_value)
    type.append(_type)
    print(name,value,type)
    return

def _print(_word):
    if _word in name:
        for _key_print in range(0,len(name)):
            if name[_key_print] == _word:
                print(value[_key_print])
    else:
        Exception(sentences,"变量错误","未定义的变量 " + sentence[1])

def run(sentence: str):
    try:
        if sentence[1] == "=":
            _define(sentence[0],sentence[2])
        if sentence[0] == "输出":
            _print(sentence[1])
    except IndexError:
        pass

try:
    args = getopt.getopt(sys.argv[1:],'',['help','version'])
except getopt.GetoptError:
    Exception(sys.argv[0:], "参数错误", "未知的参数 " + str(sys.argv[1:]))

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
        with open(filename) as file_obj:
            for sentences in file_obj:
                sentence = sentences.replace("\n","").split(" ")
                print(sentence)
                run(sentence)
    except FileNotFoundError:
        Exception(sys.argv[0:], "文件读取错误", "找不到文件 " + str(sys.argv[1:]))
