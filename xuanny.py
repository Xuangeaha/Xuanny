print("""Xuanny 0.0.4 (tags/v0.0.4:9d38120, Oct 14 2022, 07:06:00) [MSC v.1929 64 bit (AMD64)] on win32
输入 “帮助”、“版权” 或 “作者” 以查看更多信息.""")

key = []
answer = []

def raise_exception(name:str,description:str):
    print("--------------------------------------------------")
    print("出了点儿问题：")
    print("   在",sentence_get,"中：")
    print(name+"："+description)
    print("--------------------------------------------------")

while True:
    sentence_get = input(">>> ").split("、")
    for each_sentence in range(len(sentence_get)):
        sentence = sentence_get[each_sentence].split(" ")

        is_help = sentence[0] == "帮助"
        is_printword = sentence[0] == "输出文字"
        is_print = sentence[0] == "输出"
        is_raise = sentence[0] == "抛出"
        if len(sentence) <= 1:
            pass
        else:
            is_def = sentence[1] == "="

        if is_help:
            print("""Xuanny 编程语言现已支持的关键字与用法：
        
            帮助 --> 查看帮助
            [*变量名] = [*值] --> 定义变量的值
            输出 [*变量名1] [*变量名2] [*变量名3] ... = --> 输出变量的值
            输出文字 [*文字1] [*文字2] [*文字3] ... --> 输出一串文字""")
        
        elif is_print:
            for word_num in range(1,len(sentence)):
                if sentence[word_num] in key:
                    for key_num in range(len(key)):
                        if sentence[word_num] == key[key_num]:
                            print(answer[key_num])
                else:
                    raise_exception("变量错误","未定义的变量名 "+sentence[word_num])
                
        elif is_printword:
            for word_num_printword in range(1,len(sentence)):
                print(sentence[word_num_printword])
        
        else:
            try:
                if is_def:
                    if sentence[0] in key:
                        for key_num_def in range(len(key)):
                            if sentence[0] == key[key_num_def]:
                                answer[key_num_def] = sentence[2]
                    else:
                        key.append(sentence[0])
                        answer.append(sentence[2])
                    is_def = False
            except:
                pass
