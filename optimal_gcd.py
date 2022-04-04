# 1. Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.
#     The program should take input from console or args and should handle unexpected inputs    
#     Constraints:
#         - For loop is not allowed
#         - input should be in words:
#             - e.g.: onetwo = 12, sixone = 61
#         - words will be within zero to nine
#         - Cannot use inbuilt methods like max, min, or any math function    
#     Example 1:
#         - Input 1: onezero
#         - Input 2: twozero
#         - Output: onezero
#     Example 2:
#         - Input 1: twosix
#         - Input 2: twofour
#         - Output: two

# # translator={'0':"zero" ,'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

def converter(text, translator):
    i=0
    itr = iter(translator)
    while i < 10:
        temp=next(itr)
        text = text.replace(temp,translator[temp])
        i += 1
    return text

def translator_func(text):
    translator = {"zero":'0',"one":'1',"two":'2',"three" : '3',"four" : '4',"five" : '5',"six" : '6',"seven" : '7',"eight" : '8',"nine" : '9',}

    if isinstance(text,str):
        return int(converter(text, translator))
    else:
        translator = dict((zip(translator.values(),translator.keys())))
        return converter(str(text), translator)


def GCD(a,b):
    if b==0: return a
    else:
        return GCD(b,a%b)

if __name__=='__main__':

    #a=input("Input1 : ")
    #b=input("Input2 : ")
    # a="onezero"
    # b="twozero"
    a="twosix"
    b="twofour"

    a,b = translator_func(a),translator_func(b)
    ans = translator_func(GCD(a,b))
    print(ans)