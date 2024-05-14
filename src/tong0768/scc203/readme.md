## 什么是互联网

### 基本构成 W1L1.p5

#### Hosts

#### Communication links

#### Packet switches

### Internet

network of networks

### Protocols

* 信息的格式
* 接收信息后的动作

## Edge Core W1L2.p4

client & servers

routers & switches

physical media

### 数据传输 W1L2.p20

* 带宽
* 延迟

#### Packet Switching

不需要预约，每个connections都是竞争关系，先到先得。传输方会将要传输的信息分成小块，即Packet，交互机每次传输一个完成的Packet。

数据包会按顺序排队，如果队列满了，新到的数据包会被丢弃。

#### Circuit Switching

需预约传输线路才能进行持续通讯，在通讯过程中保持常数值的传输速率

#### 对比

分组允许更多用户同时使用网络，但可能产生拥塞、延迟和丢失

## 延迟 DELAY

### 四种延迟类型

#### 节点处理延迟 Processing Delay

它是指处理数据包的时间。  
主要取决于处理器的速度。

#### 排队延迟 Queuing Delay

数据包在网络设备队列中等待传输所需的时间。当数据包到达一个网络设备（如路由器）时，如果设备正在处理其他数据包，则新到达的数据包需要在队列中等待。  
主要取决于网络流量负载和设备缓冲区的大小。在网络拥塞或高流量情况下，排队延迟可能会显著增加。

#### 发送延迟 Transmission Delay

指将数据包从主机发送到传输介质所需的时间。  
主要取决于数据包的大小和发送设备的性能。

#### 传播延迟 Propagation Delay

指数据包在传输介质中从发送端传播到接收端所需的时间。  
主要取决于传输介质的长度和传播速度。

### RTT

是一个网络性能指标，用于衡量一个数据包从发送端发送到接收端，再由接收端返回发送端所需的总时间。

### traceroute

## 吞吐量 Throughput

单位时间内，通过某个通信信道或网络节点成功传输数据的平均速率。

### Goodput 有效吞吐量

相较于throughput，排除重复包、错误包、header等，只考虑“有用”的数据。

### iperf3

```shell
iperf3 -s
iperf3 -c 0.0.0.0 -b 10M -t 1 -d
```

## 丢包 Packet Loss

数据包在从发送端传输到接收端的过程中，由于各种原因未能成功到达预期目的地的现象。

### 原因：

* 网络拥堵
* 软硬件故障
* 传输路径问题
* 
### DOS攻击

## 网络分层 W2L2.p12

### Internet Protocol Stack 网络协议栈

#### Application

#### Transport

* TCP
* UDP

#### Network

* IP
* IPv6

#### Data Link

#### Physical

### ISO/OSI模型

#### Presentation

协商数据交换格式，以及进行数据加密、压缩等工作

#### Session

允许用户使用简单易记的名称建立连接

## 网络协议

### HTTP
### SMTP
### Skype

### TCP

* 连接性：TCP是面向连接的协议，建立连接前需要进行三次握手，确保双方准备好进行数据传输。
* 可靠性：TCP提供可靠的数据传输服务。它通过序号、确认和重传机制，确保数据包的顺序和完整性。
* 流控制：TCP具有流量控制和拥塞控制机制，能够动态调整发送速率，避免网络拥塞。
* 应用场景：适用于需要可靠数据传输的场景，如文件传输、电子邮件、网页浏览等。

### UDP

* 连接性：UDP是无连接的协议，发送数据前不需要建立连接。
* 可靠性：UDP不保证数据传输的可靠性，数据包可能会丢失或乱序。
* 应用场景：适用于对实时性要求较高、对可靠性要求相对较低的场景，如视频通话、音频流传输、实时游戏等。

### SSL

## 网络模型

### Client-server

### P2P

### CDN

## HTTP

### 请求 request W3L2.p18

### 响应 response W3L2.p22

### status code  W3L2.p23

* 200 OK
* 301
* 400
* 404
* 505

### Web Caching  W3L2.p32

### HTTP1.1

持久连接。默认开启Connection: keep-alive，可以在同一TCP连接中发送多个请求，减少了建立和关闭连接的消耗，提高了效率。

### HTTP2

多路复用。允许通过单一的TCP连接同时发送多重请求-响应消息，即多个请求或响应可以同时进行传输，且互不干扰。

## DNS

### hosts W4L2.p7

### 迭代查询 Recursive query W4L2.p24

### 递归查询 Recursive query W4L2.p25

### 安全

#### DDoS攻击

#### 攻击根服务器

#### 重定向攻击

* 中间人
* DNS污染攻击

#### 利用DNS进行DDoS攻击

## UDP

### segment W5L1.p6

## TCP

### Segment structure W5L2.p32

### TCP fast retransmit W5L2.p36

## Network Layer Week16-1

### Data Plane 数据平面 Week16-1.pp7

主要负责数据的转发，即决定数据包如何从路由器的输入端口转发到输出端口。

### Control Plane

负责决定数据包从源到目的地的路径，这通常是通过路由选择算法来实现的。

#### Traditional routing algorithms

分布式算法，每个路由器使用本地信息或与其他路由器交换的信息来独立计算路由。

#### Per-router control plane

每个路由器都有一个独立运行的控制平面，负责路由选择和网络路径的计算。

#### Software-Defined Networking (SDN) control plane

SDN 控制平面是逻辑集中的，允许从中央控制器对网络进行全局视图和集中管理。

#### 对比

Traditional routing algorithms 和 Per-router control plane 都是基于分布式决策的方法，其中每个路由器独立计算路由。  
它们的主要区别在于Per-router control plane强调每个路由器内部的控制逻辑，而Traditional routing algorithms更侧重于算法本身。

SDN control plane 提供了一个更加集中和灵活的网络控制方式，允许网络管理员通过中央控制器对网络进行全局优化和配置。  
这种方式特别适合需要快速、动态调整网络策略的大型和复杂网络环境。

### Network Neutrality 网络中立性 Week16-1.p20

不阻挡、不节流、无付费优先

### Packet Scheduling

#### First Come, First Served

#### priority

#### round robbin

#### weighted fair queueing

### Buffer Week16-1.p26

### TCP Congestion Window TCP拥塞窗口

TCP协议中一个重要的机制，用于控制数据的发送速率，以防止网络拥塞和数据丢失。

* 动态调整发送速率：TCP拥塞窗口的大小会根据网络的实时反馈进行动态调整。
* 增长与缩小：当数据传输顺利，即数据包被成功接收并返回确认消息时，TCP拥塞窗口会逐渐增大，允许发送端发送更多的数据。然而，当网络出现拥塞或数据包丢失时，拥塞窗口会迅速缩小，以降低发送速率，减轻网络负担。

## IP 

### Datagram format Week16-1.p46

### Address

#### DHCP Week16-2.p4

#### Hierarchical addressing: route aggregation 分层寻址：路由聚合

减小路由表的大小，提高路由效率，优化网络资源利用

### NAT: network address translation Week16-2.p15

网络地址转换，主要用于在本地网络中使用私有地址，并在连接互联网时将其转换为全局IP地址。

主要是为了解决IPv4地址短缺的问题，并能有效地避免来自网络外部的攻击，隐藏并保护网络内部的计算机。

### IPv6 Week16-2.p21