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

@app.get("/name/{name}")
def get_name_with_age(name: str, age: int):
    return {"name": name, "age": age}       #这里会报错了，因为在FastAPI里类型提示是强制执行的，会自动的转成声明的类型
print(get_name_with_age("John","17"))