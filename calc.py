class Calculator(object):
    def __init__(self):
        self.name = Calculator
        self.formula=input('Please input formula:').strip()#让用户输入公式
        self.formula_list=[]#定以一个空列表

    def Fun_Mul(self):
        i=0
        while i<len(self.formula_list):
            if self.formula_list[i] == '*' and (i+2)!=len(self.formula_list):
                Sum=int(self.formula_list[i-1])*int(self.formula_list[i+1])
                self.formula_list[(i-1):(i+2)]=[Sum]
                i=i-2
            elif self.formula_list[i] == '*' and (i+2)==len(self.formula_list):
                Sum=int(self.formula_list[i-1])*int(self.formula_list[i+1])
                self.formula_list[(i-1):]=[Sum]    
            else:
                i=i+1

    def Fun_Div(self):
        i=0
        while i<len(self.formula_list):
            if self.formula_list[i] == '/' and (i+2)!=len(self.formula_list):
                Sum=int(self.formula_list[i-1])//int(self.formula_list[i+1])
                self.formula_list[(i-1):(i+2)]=[Sum]
                i=i-2
            elif self.formula_list[i] == '/' and (i+2)==len(self.formula_list):
                Sum=int(self.formula_list[i-1])//int(self.formula_list[i+1])
                self.formula_list[(i-1):]=[Sum]    
            else:
                i=i+1

    def Fun_Sub(self):
        i=0
        while i<len(self.formula_list):
            if self.formula_list[i] == '-' and (i+2)!=len(self.formula_list):
                Sum=int(self.formula_list[i-1])-int(self.formula_list[i+1])
                self.formula_list[(i-1):(i+2)]=[Sum]
                i=i-2
            elif self.formula_list[i] == '-' and (i+2)==len(self.formula_list):
                Sum=int(self.formula_list[i-1])-int(self.formula_list[i+1])
                self.formula_list[(i-1):]=[Sum]    
                
            else:
                i=i+1
                
    def DealFormula(self):
        #将计算式由字符串转成列表,并对其包含的多位数进行处理
        self.formula_list=list(self.formula)
        sud=['+','-','*','/','(',')']
        num = 0
        Sum=''
        while num<len(self.formula_list):
            if self.formula_list[num].isdigit():
                Sum=Sum+self.formula_list[num]
                num=num+1
                if num==len(self.formula_list):
                    buc=len(Sum)
                    self.formula_list[(num-buc):num]=[Sum]  
                continue
            elif self.formula_list[num] in sud:
                buc=len(Sum)
                self.formula_list[(num-buc):num]=[Sum]
                Sum=''
                num=num+1-(buc-1)
                continue
            else:
                print('Input error')

    def main(self):
        self.DealFormula()
        self.Fun_Mul()
        self.Fun_Div()
        self.Fun_Sub()

        result = 0
        for number in self.formula_list:
            if number =='+':
                continue
            else:
                result=result+int(number)
        print(result)
            
calculator=Calculator()
calculator.main()