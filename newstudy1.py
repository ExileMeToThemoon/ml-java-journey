from fastapi_cli.cli import app

# 把函数参数从：
#           first_name, last_name
# 改成：
#           first_name: str, last_name: str
# 这就是类型提示，在函数参数后加冒号（:），通常不会改变代码本来的行为，本来不可以自动补全
# 但是因为编辑器知道变量的类型了，因此不仅能得到补全，还能获得错误检查
def get_full_name(first_name:str,last_name:str):
    full_name = first_name.title()+ ' ' + last_name.title()
    return full_name

print(get_full_name("John","Doe"))

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age
print(get_name_with_age("John","17"))       #此处不会报错，是因为python强制类型转换了

# @app.get("/name/{name}")
# def get_name_with_age(name: str, age: int):
#     return {"name": name, "age": age}       #这里会报错了，因为在FastAPI里类型提示是强制执行的，会自动的转成声明的类型
# print(get_name_with_age("John","17"))


# 可以使用类星提示在列表元组字典等，以列表为例，冒号后先是列表，列表后的方括号写数据的类型str
def process_items(items: list[str]):        #列表
    for item in items:
        print(item)

def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):  #元组
    return items_t, items_s

def process_items(prices: dict[str, float]):        #字典
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
# 联合类型：可以声明一个变量是若干种类型的任意一种，比如既可以是int也可以是str。定义时使用竖线(|)隔开
def process_item(item: int | str):
    print(item)
# 可以声明一个值的类型是none;若传入名字打招呼，若为空输出hello world
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi()
say_hi("John")


# 类作为类型：
# 你也可以把类声明为变量的类型。
# 假设你有一个名为 Person 的类，带有 name：
class Person:
    def __init__(self, name: str):
        self.name = name
def get_person_name(one_person: Person):
    return one_person.name
