# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'
import time

def sub_gen():
    break_ = 0
    while 1:
        break_ = yield break_
        if break_:
            break
    return 'stop'

sub_gen1 = sub_gen()
print(type(sub_gen1))
print(next(sub_gen1))
print(type(sub_gen1))
print(sub_gen1.send(None))
# try:
#     print(sub_gen1.send(1))
# except StopIteration as e:
#     print('*',e.value)
#
# time.sleep(3)
#
# print(sub_gen1.send(None)) #报错 StopIteration None
# try:
#     print(sub_gen1.send(1))
# except StopIteration as e:
#     print('*',e.value)


'''
总结：
    1、return或没有下一个yield时会向一层抛出一个StopIteration异常并将return的值或None放到StopIteration第1个参数，用StopIteration.value来获取
    2、委托生成器的yield from会自动将StopIteration异常的第一个参数(即子生成器return的值或None)提取出来
    3、子生成器的return的值必须由程序员显示的在委托生成器中用return返回，不然不会向调用方返回
    4、生成器()返回的是一个类
    5、next(生成器)与生成器.send(None)是同一回事
    6、当子生成器终止并抛出StopIteration异常时，其异常第1参数(return或None)会返回到委托生成器的空间中，然后如果委托生成器的while仍然有效就会自动从新进入子生成器里面，并返回一个值后才会因为调用方没有进一步next(生成器)或者生成器.send(?)
'''

# def a_gen():
#     yield 1
#     # yield 2
#     try:
#         yield 3
#     except BaseException as e:
#         print(e)
#
#     yield 4
#     yield 5
#
# a_gen1 = a_gen()
# print(a_gen1.send(None))
# print(a_gen1.send(None))
# print(a_gen1.close()) # 生成器.close()引发GeneratorExit异常，GeneratorExit异常继承的异常是BaseException，StopIteration和其他异常是继承于Exception异常