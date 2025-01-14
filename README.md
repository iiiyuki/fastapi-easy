### Book Management System
#### Description
- 项目使用 uv 作为包管理器 同时也兼容 pip3 with requirements.txt
- 项目使用 fastapi 作为后端框架
- 项目使用 pydantic 作为数据验证框架

#### Installation
- 使用 uv 安装
```shell
uv install && uv sync && uv run --with fastapi main.py   
```

- 使用 pip3 安装
```shell
pip3 install -r requirements.txt
python3 app.py
```

#### Usage
- 测试集在 tests 目录下
- 运行：
```shell
python3 tests/test.py
```
即可运行测试集

#### API
- 各 api 要求的参数在redoc 中有详细描述 数据类型&结构都有提示

# Good Luck
