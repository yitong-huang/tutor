import nodemailer from 'nodemailer';
import http from 'https';
import url from 'url';
import querystring from 'querystring';

const transporter = nodemailer.createTransport({
    host: 'smtp.qq.com',
    port: 465,
    auth: {
        user: '469099005@qq.com',
        pass: ''
    }
});

http.createServer(function (request, response) {

    var urlObj = url.parse(request.url)
    var query = urlObj.query
    var params = querystring.parse(query)

    try {
        transporter.sendMail({
            from: '"Test mail" <469099005@qq.com>',
            to: 'yitong0768@gmail.com',
            subject: 'Message from ' + params.name,
            text: params.comment
        })
        console.log('done')
    } catch (e) {
        console.dir(e, { depth: null, color: true })
    }

    //设置允许跨域的域名，*代表允许任意域名跨域
    response.setHeader("Access-Control-Allow-Origin", "*");
    response.writeHead(200, { 'Content-Type': 'text/plain' });
    response.end("Message is sent, Thanks");
}).listen(8800)

console.log('Server is runnine at https://127.0.0.1:8800')