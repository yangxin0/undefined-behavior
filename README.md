# Undefined Behavior

该项目给客户提供一个统一的LLM的服务入口，客户可以通过该平台接入各种大模型从而不需要去挨个注册其他大模型平台如OpenAI、文心一言等。当前该系统支持GPT-3.5模型后续会逐步增加其他模型供客户选择，而且会逐步提供API供客服选择其他客户端如opencat等。

项目规划：

1. 提供基础GPT3.5模型服务，包含用户注册、流量统计***（进行中）***
2. 增加用户支付入口，支持用户直接使用strip充值，或者用户通过客服充值
3. 提供OpenAI兼容API供客户使用自备的客户端（通过模型选项支持其他平台如文心一言等）

### 概览

```
                           port:80

                      ┌────────────────┐
                      │                │
                      │                │
                      │  nginx-server  │
                      │                │
                      │                │
                      └────────────────┘
                               │
                               │
                               ├───────────┐   port: 3000
                               │           │    path = /
                               │           ▼
                               │  ┌─────────────────┐
                               │  │                 │
                ┌──────────────┘  │                 │
                │                 │    web-server   │
                │                 │                 │
                │                 │                 │
path = /static/ │                 └─────────────────┘
                │                           │
                │                           │
                │                           │    port: 8000
                ▼                           ▼
       ┌─────────────────┐        ┌─────────────────┐
       │                 │        │                 │
       │                 │        │                 │
       │  chatgpt-server │        │  chatgpt-server │
       │  (static files) │        │                 │
       │                 │        │                 │
       └─────────────────┘        └─────────────────┘
```

### nginx-server部署

nginx作为整个项目的入口所有的流量都经过nginx转发到后面的业务服务，由于web前端采用SSR所以中间包含了web-server的服务器而不是直接到chatgpt-server。nginx的作用如下：

1. 提供chatgpt-server的静态文件服务，由于django的gunicorn不支持静态文件所以需要nginx的支持。
2. 作为整个项目的入口（80端口），转发请求到后面的业务服务器

由于nginx要serve后面chatgpt-server的静态文件，所以在构建nginx镜像的时候要从chatgpt-server获取静态文件。nginx-server镜像在运行的时候需要提供BACKEND_URL环境变量，该环境变量是下一级服务的IP和端口。（如果是docker-compose部署则可能是一个DNS name）。如果要构建nginx-server的镜像参考下面：

```
./nginx/build.sh 版本信息（例如latest或者v1.0等）
```

### web-server环境部署

首先需要配置npm安装`node 18.x`和yarn构建工具，然后使用`yarn install`就可以安装开发Web的所有依赖和工具。

1. 开发环境可以使用`yarn dev`进行动态的打包和调试，默认端口是3000。
2. 生产环境使用`yarn build`就可以构建部署使用的文件，该文件默认会写入到`.output`目录
3. 构建镜像`./scripts/build.sh TAG(docker TAG)`

 ### chatgpt-server部署

基于django的RESTful模块实现所有的业务逻辑：openai查询、用户注册、计费系统等，该模块当前仅支持openai的GPT模型未来会整合更多的模型如百度文心一言。本项目原始作者设计的目标是text-to-text的模式所以较难的迁移到其他模式如：text-to-image等，主要原因是text-to-image通常需要耗费几分钟时间，按照目前的UX交互形式将会非常难用。所有后续主要新增更多的text-to-text模型为主，其他模态的模型不作考虑。以下是程序构建与运行的步骤，你可以根据程序的维护阶段选择性的执行：

1. 构建程序镜像 `./scripts/build.sh TAG(docker的TAG)`
2. 试用./scripts/console.sh进入容器在该容器中你可以：初始化数据库、数据库迁移与维护等
   - 删除数据库：根据settings.py的配置进入数据库环境删除数据（高危操作）
   - 初始化/迁移数据库： python manage.py migrate
   - 初始化配置和账户等信息：./scripts/seeds.py
3. 该容器包含一个可选的环境配置`SERVER_WORKERS`表示进程数量（默认为4），通常不需要更改

