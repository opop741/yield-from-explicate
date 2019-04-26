# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

def sub_gen():
    while 1:
        break_ = yield 1
        if break_:
            break

sub_gen1 = sub_gen()
print(sub_gen1.send(None))
print(sub_gen1.send(None))
print(sub_gen1.send(None))
# print(sub_gen1.send(1)) #引发sub_gen1中断的语句
# # a、子生成器终止的StopIteration异常的抛出是指向其调用语句
# try:
#     print(sub_gen1.send(1))
# except StopIteration as e:
#     print(e.value)
# # b、调用方可以捕获StopIteration异常并使用.value获得的值是None

# def sub_gen():
#     while 1:
#         break_ = yield 1
#         if break_:
#             break
#     return 'stop'
#
# sub_gen1 = sub_gen()
# print(sub_gen1.send(None))
# print(sub_gen1.send(None))
# print(sub_gen1.send(None))
# # print(sub_gen1.send(1)) #引发sub_gen1中断的语句
# # a、sub_gen1终止时的StopIteration异常的抛出是指向其调用语句
# # b、StopIteration会携带sub_gen1的return返回
# try:
#     print(sub_gen1.send(1))
# except StopIteration as e:
#     print(e.value)
# # c、调用方可以捕获StopIteration异常并使用.value获得sub_gen1的return的值

'''
总结：
    1、一层的生成器在调用方使其中断时，其StopIteration异常是指向调用语句的
    2、一层的生成器里面有return时其值跟随StopIteration一起(第1个参数)抛出到调用语句处，用StopIteration.value来提取，没有return时返回的值其实就是None
'''