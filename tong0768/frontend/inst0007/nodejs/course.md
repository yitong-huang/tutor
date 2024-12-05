## 第一个node程序

nodejs基于js，是运行在服务端的JavaScript

### node环境安装

### hello world

```javascript
console.log("hello world")
```

```shell
node ./src/helloworld.js
```

## 第一个http服务器

### 引入模块

* require
* import

## npm

### npm install

### package.json

## nodemailer

### createTransport

### sendMail

## 前端后端

### 前端

### 后端

### 交互

```javascript
    // Ajax
    const request = new XMLHttpRequest();
    const url = "http://localhost:8800"
    request.open("GET", url);
    request.send();
    request.onloadend = (e) => {
        alert(request.responseText)
    }
```

#### 跨域问题

```javascript
    //设置允许跨域的域名，*代表允许任意域名跨域
    response.setHeader("Access-Control-Allow-Origin","*");
```

## 完善服务端

### 传递参数

```javascript
    const url = "http://localhost:8800?name=" + encodeURIComponent(name) + "&comment=" + encodeURIComponent(comment)
```

### 获取参数

```javascript
    console.log("url", request.url)
    var urlObj = url.parse(request.url)
    console.log("urlObj", urlObj)
    var query = urlObj.query
    var params = querystring.parse(query)
    console.log("params", params)
```

## 服务器部署

### 购买服务器

### 安装node

https://nodejs.org/en/download/package-manager

```shell
apt-get update
apt-get install unzip
```

### 上传文件

filezilla

### 启动服务

```shell
node sendmail.js
```

### pm2

```shell
npm install pm2 -g
pm2 start sendmail.js

pm2 stop sendmail

pm2 status

pm2 logs
```

### 修改客户端指向服务器

### 完善

### DNS
