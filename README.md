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

