# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

def sub_gen():
    while 1:
        break_ = yield 1
        if break_:
            break
    return 'stop'
def middle_gen():
    result = yield from sub_gen()
    print('*',result)

middle_gen1 = middle_gen()
print(middle_gen1.send(None))
print(middle_gen1.send(None))
print(middle_gen1.send(None))
print(middle_gen1.send(1))
# # a、子生成器终止的StopIteration异常的抛出是指向其调用语句
# # b、加了middle_gen委托生成器后，子生成器的return的值赋值给middle_gen，并继续执行middle_gen的语句


# def sub_gen():
#     while 1:
#         break_ = yield 1
#         if break_:
#             break
#     return 'stop'
# def middle_gen():
#     result = yield from sub_gen()
#     print('*',result)
#     return '----' #把'----'改成result时，就可以把子生成器的return值返回至调用方处
#
# middle_gen1 = middle_gen()
# print(middle_gen1.send(None))
# print(middle_gen1.send(None))
# print(middle_gen1.send(None))
# print(middle_gen1.send(1))
# # a、调用语句仍然报错StopIteration异常
# # b、委托生成器的return值随着StopIteration异常的抛出至调用方处

# def sub_gen():
#     while 1:
#         break_ = yield 1
#         if break_:
#             break
#     return 'stop'
# def middle_gen():
#     yield from sub_gen()
#     print('*')
#
# middle_gen1 = middle_gen()
# print(middle_gen1.send(None))
# print(middle_gen1.send(None))
# print(middle_gen1.send(None))
# print(middle_gen1.send(1))
# # try:
# #     print(middle_gen1.send(1))
# # except StopIteration as e:
# #     print(e.value)
# # a、调用语句仍然报错StopIteration异常
# # b、当middle_gen委托生成器没有赋值语接受子生成器的return的值时，其值就会被抛弃，调用方是不能接受到的

'''
总结：
  前提委托生成器没有while：
    1、有了中间的委托生成器，子生成器的StopIteration异常向上抛出
    2、有了中间的委托生成器，子生成器的return的值或None(没有return语句时)进入委托生成器的赋值语句，并继续执行委托生成器后续语句
    3、当委托生成器在赋值语句后面有return语句时或没有下一个yield时，委托生成器向上抛出异常，调用语句报错StopIteration异常
    4、委托生成器向调用方传递的StopIteration异常的第1参数可以用return指定子生成器的return的值，没有return则返回None
    5、当委托生成器没有赋值语句接收子生成器因中断返回的值(第2点)时，其返回的值就无法传到调用方处
    6、子生成器的return的值必须由程序员显示的在委托生成器中用return返回，不然不会向调用方返回
    
    不管是子生成器委托生成器，其return语句都会随着StopIteration向上返回
    StopIteration异常是不是只向上传递一层呢？自答案：应该是的。
'''

