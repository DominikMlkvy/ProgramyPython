# coding: utf8


class Simple:

    def __init__(self, string):
        self.string=string
        self.array=self.parse(string)
        self.result=self.calculate(self.array)

    def parse(self, string):
        array=[""]
        index=0
        for i in string:
            if i == " ":
                array.append("")
                index += 1
            else:
                array[index]+=i
        # array[0]=float(array[0])
        # array[2]=float(array[0])
        return array

    def calculate(self, array):
        result=float(array[0])
        for i in range (1,len(array),2):
            result=self.operation(array[i],result,float(array[i+1]))
            if result=="fail":
                break
        return result

    def operation(self,operator,number1,number2):
        if operator == "+":
            return number1+number2
        elif operator == "-":
            return number1-number2
        elif operator == "*":
            return number1*number2
        elif operator == "/":
            return number1/number2
        elif operator == "^":
            return number1**number2
        else: return "fail"


