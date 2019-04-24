# -*- coding: utf-8 -*-
__author__ = 'Jazz_Qi'

def sub_gen():
    break_ = 0
    while 1:
        break_ = yield break_
        if break_:
            break
    return 'stop'

def middle_gen():
    while 1:
        result = yield from sub_gen()
        print('*',result)
    return result

middle_gen1 = middle_gen()
print(middle_gen1.send(None)) #0
print(middle_gen1.send(None)) #None
print(middle_gen1.send(None)) #None
print(middle_gen1.send(1))
print(middle_gen1.send(1))
print(middle_gen1.send(1))
print(middle_gen1.send(None))
# 0、第一个middle_gen1.send(None)，的None不会被赋值到 = yield的左边
# 1、middle_gen加了while后可以把子生成器返回的StopIteration异常及return返回的值或None“劫持”，不会抛出至调用方处，也不会终止委托方生成器(应该是yield from语句已经处理了)
# 2、子生成器抛出StopIteration异常时，进入委托生成器的只有子生成器的return值或None，其StopIteration异常不会进入委托生成器中
# 3、因为委托生成器里有while的while不终止或没有执行return，即使子生成器终止后仍然会被再一次进入执行
