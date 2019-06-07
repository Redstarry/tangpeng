# 1. 导入Flask扩展
from flask import Flask

# 2.创建Flasik应用程序实例
# 需要传入__name__,作用为了确定资源所在的路径
app = Flask(__name__)

# 3. 定义路由及视图函数
# Flaskz中定义路由是通过装饰器实现的
@app.route('/')
def index():
    return 'hello flask'

# 4.启动程序

if __name__ == '__main__':
    # 执行了app.run 就会将flask程序运行在一个简易的服务器上
    app.run()