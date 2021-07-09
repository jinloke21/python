

def can_play(fn):
    print("定义装饰器就被调用了")
    def inner(name,game,**kwargs):
        #参数为张三和LOL
        print("参数为"+name+"和"+game)
        clock = kwargs.get("clock",21)
        if clock >= 21:
            print("太晚了,不能")
        else:
            fn(name,game)  #现在调用的fn函数就是paly_game函数
    return inner

@can_play  #立即调用can_Play函数，参数为paly_game
def paly_game(name,game):
    print(name + "正在玩" + game)

paly_game("张三","LOL",clock=18)  #现在如果调用paly_game函数就是使用can_Play的返回值函数


#高级装饰器
print(" _     _       _     ")
print("| |__ (_) __ _| |__")
print(" '_ \| |/ _` | '_ \ ")
print("| | | | | (_| | | | |")
print("_| |_|_|\__, |_| |_")
print("        |___/       ")

def can_play(clock):
    print("定义装饰器就被调用了")
    if def hand(fn):
        def inner(name,game,**kwargs):
            print("参数为"+name+"和"+game)
            if clock >= 21:
                print("太晚了,不能")
            else:
                fn(name,game)  #现在调用的fn函数就是paly_game函数
        return inner
    return hand


@can_play(20)
def paly_game(name,game):
    print(name+"正在玩"+game)
paly_game("李四","星际称霸")



















