import nodemailer from 'nodemailer';

const transporter = nodemailer.createTransport({
    host: 'smtp.qq.com',
    port: 465,
    auth: {
        user: '469099005@qq.com',
        pass: ''
    }
});

try {
    const send = await transporter.sendMail({
        from: '"Test mail" <469099005@qq.com>',
        to: 'yitong0768@gmail.com',
        subject: 'Hello!',
        text: 'hello world',
        html: '<p>hello world</p>'
    })
    console.dir(send, {depth: null, color: true})
} catch (e) {
    console.dir(e, {depth: null, color: true})
}