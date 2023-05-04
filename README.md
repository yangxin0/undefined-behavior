# Undefined Behavior

由于OpenAI屏蔽了中国大陆和中国香港地区所以该项目利用OpenAI提供的API搭建一个类似类ChatGPT的服务给被屏蔽地区的用户使用。原计划通过包装一层OpenAI的API提供类ChatGPT的产品进行商业化，但是在前期推广过程中发现对于ChatGPT有需求的客户已经通过其他手段获取到了ChatGPT的使用方式，对于这种第三方包装的产品并不感兴趣，另外对于ChatGPT感兴趣的客户更多想把ChatGPT集成到他们的工作中。后面这批客户需要的不仅是ChatGPT更深的需要我们协助他们去分析业务并且实现相关的工具，这个产品就从前期定位的2C慢慢演变成了2B，这并不是我们的初衷所以我们最终选择暂停掉这个商业项目。

虽然我们暂停了这个项目的商业化，但是依然会作为我个人的试验项目在后续集成更多厂家的模型为后面的项目服务，这里要感谢该项目的原作者提供了一个不错的startup，项目的原始地址如下：

- https://github.com/WongSaang/chatgpt-ui
- https://github.com/WongSaang/chatgpt-ui-server

### 概览

```
                                    port:80

                               ┌────────────────┐
                               │                │
                               │                │
                               │  nginx-server  │
                               │                │
                               │                │
                               └─────┬──────────┘
                                  │  │  │
                                  │  │  │
                                  │  │  └───────────┐   port: 3000
                                  │  │              │    path = /
                                  │  │              ▼
                                  │  │     ┌─────────────────┐
                                  │  │     │                 │
                 ┌────────────────┘  │     │                 │
                 │                   │     │    web-server   │
                 │                   │     │                 │
                 │    port: 8000     │     │                 │
path = /static/  │  path = /admin/   │     └─────────────────┘
                 │                   │               │
                 │                   │               │
                 │                   │               │    port: 8000
                 ▼                   │               ▼
        ┌─────────────────┐          │     ┌─────────────────┐
        │                 │          │     │                 │
        │                 │          │     │                 │
        │  chatgpt-server │          └────▶│  chatgpt-server │
        │  (static files) │                │                 │
        │                 │                │                 │
        └─────────────────┘                └─────────────────┘
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

