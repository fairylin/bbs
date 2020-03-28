"""
数据库迁移
file -> mongo

1. python
duck type 鸭子类型语言

长的像，叫的像，那你就是**

2. 为什么duck type 不需要设计模式
设计模式
平常开发中很多问题，导致
    1.高耦合
    2.重构的时候痛苦，需要修改，数据库，配置，等内容

    1.针对这些问题特定的解决方案就是设计模式
        a.名字
        b 场景
        c uml
        d 代码

        优化结果，实现
        1.高内聚
        2.低耦合 依赖倒置

    2. 什么导致了高耦合 - 产生设计模式
        1.类型  - 强类型
        需要修改不同的数据到同一个类型
        monster hero hero_monster
        hreo  monster 本身不是一个类型，统一成一种类型
        base class xxx hero 和 monster都集成到一起


mongo
1. 快
2. 可多机使用（leveldb kv 只能单机使用）
3. 支持主从数据库  落地



Model -> Mongo
首先要保持新的mongoModel 接口和 老的 Model接口一致
所有被使用到的老的Model 接口在新的MongoModel中都有

1.new
2.find_by
3.find(id)
4.all
5.get
6.find_all()

orm sql

"""


class Duck(object):
    def bark(self):
        print("gagaga")

    def swim(self):
        pass


class Dog(object):
    def bark(self):
        print("hahah")

    def swim(self):
        pass


duck_list = []
for i in range(10):
    duck_list.append(Duck())
    duck_list.append(Dog())

for d in duck_list:
    d.bark()
