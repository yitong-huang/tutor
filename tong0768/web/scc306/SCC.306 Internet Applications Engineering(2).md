# SCC.306: Internet Applications Engineering

##### 关键词

CoAP、MQTT、LwM2M

OSCORE、TLS、DTLS

6LoWPAN、Thread

whistleblower

monolithic、microservice

http

Wireless Sensor Network，Wireless Body Area Network，Unmanned Autonomous Vehicle Networks

CAM、BSM、DENM

Simple flow layouts、Table layouts、Absolute layouts、Fluid and fixed layouts、Responsive Web Design、Intrinsic Web Design

mobile first

Vision、Hearing、Motor control、Cognitive

describe、it、expect

cucumber、given、when、then、and

Testing Trophy、End-to-end、Integration、Unit和Static

WACG

Confidentiality、Integrity、Authenticity、Non-repudiation、CIA

Continuous Delivery、Continuous Deployment

[toc]

#### 网络架构和性能

HTTP是基于TCP的。用户需要先进行TCP连接，这需要客户端先发送TCP连接请求给服务器，服务器接受请求并把信息发送给客户端。客户端然后发送HTTP请求信息，服务器生成并发送回应信息。客户端会在初次收到一个html文件，分析这这个html文件，发现还需要其他资源，于是重复上述过程（可能是重复用同一个tcp连接，这主要看版本）。因此一次HTTP响应时间，等同于2RTT加文件传输时间

假如看瀑布图的话，就可以发现，第一次建立连接时，一部分时间被用于DNS查找，随后是TCP连接，然后是TTFB（Time to first byte，从发送请求到接受第一个byte的时间），最后是内容下载的时间。整体上会经历三个时间点，Start Render（从用户看到第一个像素点开始，同时也是DOMContentLoaded）、Document Complete（除了异步资源，全都加载完毕）和Fully loaded

在渲染前，必须收到HTML和完成DOM构建，这可能需要CSS和JS文件（如果是异步的就不需要阻塞）。

为了减少延迟，首先可以调整得到包的顺序，比如先得到css，再得到js。然后可以让页面变得更简单，减少文件的元素，合并小文件，例如讲多个图像合并为一个较大的图像（精灵图），以减少连接数量。使用压缩的图像/文件/JS库。也可以添加缓存机制。延迟加载用户不可见的部分（Lazy Loading）

上面都是客户端层面的性能瓶颈，还有服务器层面的瓶颈。服务器的目的是尽可能低延迟，高吞吐量。有三个性能指标，requests served per second、Latency、Throughput in bytes per second

横向扩展后，就可以把负载均匀分配到多个服务器上。一种形式是Load Balancer是通过硬件来实现流量分配。另一种形式是通过例如nginx的软件，通过反向代理reverse proxy对流量进行分配。IaaS灵活且适合用于扩展

一个优化的方式是缓存，把内容缓存到用户的浏览器，在离用户更近的地方设置服务器

常见的直方图结果是positively skewed normal distribution，这种情况用median衡量更好，因为里中心更近

#### HTTP

##### HTTP/0.9

HTTP目前有五个版本，即HTTP/0.9、HTTP/1.0、HTTP/1.1、HTTP/2.0、HTTP/3.0。最早的HTTP/0.9极其简单，这版本的请求只包括一行文本，只能使用get方法去请求某个资源。到了HTTP/1.0，才有了HTTP协议的雏形。

##### HTTP/1.0

HTTP/1.0的请求实现了请求头，请求头中添加了HTTP版本号。HTTP1.0的响应中包含了内容编码（Content-Encoding）和响应状态码（Response Codes）和元数据。响应状态码中的302码实现了重定向，而元数据中的Content-Type使得不只HTML，其他类型的文档也能被传输。请求方法也从只有get升级为了get、head和post

##### HTTP/1.1

HTTP/1.0的更新主要体现在对功能的扩展上，为后续发展铺平了道路。HTTP/1.1的更新则是一个性能上的重要更新。1.0版本中，每次请求都要新建一个TCP连接，然后马上关闭，这使得很大一部分的HTTP延迟都来源于建立TCP连接的延迟。到了1.1版本，这更新为了持久连接（persistent connection、Keep-Alive），同时一并实现了管道化（Pipelining）。管道化使得多个请求在一个TCP连接中，可以发送多个HTTP请求，不需要等前一个响应完全收到。这样就节约了TCP连接的时间，并且重叠了多个HTTP请求中，发送请求和等待响应的时间。

管道化虽然可以单连接多请求，但是多个请求不能并发，响应也不能乱序返回。不过可以通过并行连接（parallel connections）的方式，通过同时使用多个tcp连接，使得多个请求可以并行处理。但是如果允许的持久连接数太多，又容易造成ddos攻击

HTTP/1.1还扩展了一个功能，这与当时虚拟主机的发展相关。这版本的HTTP添加了Host header，这样当两个网站使用同一个服务器、同一个IP时，就可以根据HTTP请求中的Host header字段来分辨具体请求的是哪个网站。另外，1.1版本也追加了put、delete、trace和option四个功能

到了这一步，HTTP请求依旧是以REST为基准，完全无状态。不过，Cookies依旧实现了session management（登录、购物车），personalization和tracking（记录用户行为）。为了管理缓存，1.1版本增加了显式的缓存控制技术

##### HTTP/2.0

HTTP/2.0是一次重大地全面革新，上述的一些设计被完全推翻了。

首先，HTTP协议的数据包，在应用层上，被改变了。原来文本格式的请求头/响应头，改为了二进制的Headers frame；文本格式的响应内容，被改为了二进制的Data frame。应用层内部被添加了一个Binary framing layer，二进制的帧可以直接进入这一层，这使得电脑对帧的解析变快变容易。多个帧组成信息，流是一个HTTP请求和回应对所对应的一系列帧，是一种建立在TCP上的双向传输的字节流。每次请求都会新建一个流，一个TCP连接可以任意多个双向流，帧上的流标识符（Stream Identifier）记录了一个帧属于哪个流。这种一个TCP连接多个流的设计就叫多路复用（Multiplexing，Request-Response multiplexing）

在1.1版本中，pipeline要求服务器必须按顺序回应请求，这导致最前面的信息可能会阻塞后面的信息。2.0版本中，以帧为最小传输单元，这样多个请求和回应的帧就可以交错（interleave），这解决了头部阻塞问题（head-of-line blocking issue）

在1.1版本中，报文压缩，但是首部不压缩。而在2.0版本中，首部会使用HPACK压缩，避免每次都传输相同的信息。

帧有多种类型，包括Data、HEADERS、PRIORITY等。其中HEADERS帧用于新建一条流，而PRIORITY则会记录帧的优先级。

2.0版本还有一个技术名为服务器推送（Server push），这允许服务器在一个文件被请求前就推送。例如当被请求一个HTML文件时，不等浏览器解析哪个HTML文件，就提前推送浏览器可能需要的资源

2.0版本与1.1版本还有一个主要的区别，就是其变为了有状态的（Stateful）。2.0版本依旧是TCP/IP连接为基础，由客户端发起的。但是会定义连接层级的设置（connection-level settings）和头部表（header table，用于压缩首部），这就使得连接变得有状态了。这会在建立连接时带来一点额外的开销，但是其能带来更多的好处以及节约更多的资源

##### HTTP/3.0

虽然2.0在应用层解决了头部阻塞问题，但是传输层的问题依然存在。TCP依旧会试图可靠地按照顺序传递数据包，如果丢包就会重传丢了的包。而TCP本身是由系统内核实现的，这就很难修改，因为很难对世界上大部分的操作系统都进行升级。3.0版本通过在UDP协议上建立了QUIC协议解决了这一问题。QUIC协议是对TCP和TLS协议的整合。3.0版本是在一条QUIC连接上进行多个QUIC流

在2.0版本中，TCP 三次握手与TLS/1.3握手是分开的。而QUIC将连接握手（connection handshake）和TLS/1.3的握手整合在了一起，同时进行。

通过使用UDP协议，避免重传机制，这样就在有2.0的全部好处的基础上，避免了TCP协议的头部阻塞问题。使用UDP还避免了对系统内核进行修改，只需要在用户空间做修改就可以，并且加快了新版本开发的速度

#### 嵌入式计算和网络

##### 多种设备

一部分设备不会接入互联网，有些没有连接网络的能力，有些连接的网络也可能不是互联网连接主机的形式。网络结构会为了适配这些设备而特化

嵌入式系统的特点是cpu、内存、电池和网络资源低，它们需要联网以工作。例如wireless personal area network、body area network、UAV Communication、Intranet / Internet。很多时候人们关注的都是性能和效用（performance and utility），然而这却与有限的资源冲突。有时也必需IPv6所提供的大量地址

Wireless Sensor Network由大量分布式、具有通信能力的传感器节点构成，能够感知、收集并无线传输数据。应用场景包括Building Health、Environment Monitoring、Animal / Habitat Monitoring、Emergency Scenario Detection、Monitor Industrial Equipment

Wireless Body Area Network用于监测一个人的健康指标的，传感器在人体内部或外部，发送信息给本地或远程服务器

Unmanned Autonomous Vehicle Networks是一种操控无人机（Unmanned Aerial Vehicle、Drones）的系统，现主要用于农业或军事。无人机以蜂群形式（in swarm）通信，自主规划行动。无人机本身是数据骡子（Data mules），其用自身的飞行来传输数据，而非无限传输

##### IoT

IoT基于6LoWPAN（网络层）寻址，使用RPL在自组织网络（ad-hoc network）寻路，在网络拓扑上叠加（Overlay）有逻辑的（logical directed）无环图（acyclic graph），会对数据进行压缩

Thread（协议栈）是一种无线网状网络协议，基于6LoWPAN，有广泛的工业支持（industrial support），聚焦于简洁性和安全性（simplicity and security）

相较于TCP，IoT更喜欢使用UDP，因为不需要大缓冲区（TCP需要存储和重组乱序到达的数据包），也不需要维护连接状态

Constrained Application Protocol（CoAP）是一种类似HTTP请求模式的协议，其功能弱于HTTP但资源需求少，适用于IoT网络，家用小开关

MQTT（Message Queuing Telemetry Transport）是一种Pub-Sub协议，通过broker和订阅topic来工作，基于TCP。其更轻量级的存在是MQTT-SN，使用UDP协议，传感器，广播类型

Lightweight Machine to Machine (LwM2M)，车的ota更新

……以及很多其他例子

OSCORE、TLS、DTLS是安全协议，DTLS是UDP版的TSL，OSCORE是转为CoAP设计的安全协议

##### 车载网络

CAN Bus Internal network（Controller Area Network）历史上被认为是封闭的系统，没有加密或认证，现在已经普遍需要加密和认证了。这正在对向后兼容性，以及对时间约束的性能影响，做出挑战

现在的车辆会使用许多有线或无线的通信方式，例如USB、HDMI、蓝牙、WiFi、蜂窝网络、车对车网路等等等等

车辆之间的通信是Connected and Autonomous Vehicles（CAV）和Connected and Automated Mobility（CAM）的关键组成部分。这些需要车辆间通信来广播安全信息（CAM和BSM）、通知其他车辆事件发生、管理自动驾驶车队（autonomous platoons）等。还有DENM也是车辆通信

CAM和BSM是周期性向外发送信息，DENM是外部基础设施向车辆发送环境信息

Cooperative Awareness Message是由车辆发送的广播信息，用于帮助其他车辆做道路感知，以提升安全。主要区别在于CAM是周期性发送，每100-1000毫秒一次

除了车对车通信，还有对道路基础设施通信V2I，与云端通信V2C，与行人通信V2P，与家通信V2H

一些应用对延迟非常敏感，可以将任务提交至云端，也可以在系统边缘部署计算基础设施

#### 价值观

吹哨人（Whistleblowers）受到公众情感上支持，但往往受到打压和排挤（victimised and ostracised），即便所言被证实（vindicated）。在英国，披露（disclosure）受到Public Interest Disclosure Act 1998的保护，任何打压都可以申请赔偿（compensation），但是可能要花很多年。可能可以寻求professional bodies, trade unions and whistleblower charities的帮助

#### 在线服务架构

Monolithic Architecture是一种将所有功能模块集成在一个统一部署单元中的架构，扩展时，必须整体扩展整个应用。Microservice Architecture将系统拆分为多个独立的服务，每个微服务可以单独部署、扩展、更新

#### 内在网页设计

css是基于盒子模型工作的，盒子的基础参数包括amrgin、border、padding、content。在此基础上有多种不同的display，包括block flow，block felx，block grid，inline flow等

需要了解的布局机制、策略和哲学包括Simple flow layouts、Table layouts、Absolute layouts、Fluid and fixed layouts、Responsive Web Design、Intrinsic Web Design（按照时间排序）

##### Simple flow layouts

Simple flow layouts会使用默认的布局方式，从上到下、从左到右自然排列，

##### Table layouts

Table layouts会使用table元素布局，以网格的形式组织页面结构。这种结构不便管理和维护，可访问性也差

##### Absolute Layouts

Absolute Layouts会使用position: absolute，这个的问题在于对于多种屏幕参数需要维护多个网站

##### Fluid and fixed layouts

Fluid and fixed layouts会使用float: left，这在宽屏幕上看起来很屎，且内容要不然屎fixed，要不然是fluid

##### Responsive Web Design

Responsive Web Design会使用CSS media queries，也就是@media，来根据视口（viewport）大小来调整相同内容的布局

##### Intrinsic Web Design

Intrinsic Web Design是更现代的响应式方案，强调内容决定布局而非视口大小，在旧浏览器上可能需要替换方案（fallback）

在设计之初应该移动设备优先（mobile first），即先考虑小屏幕设备的需求和限制，然后逐渐增强（progressive enhancement），即逐渐为大屏幕添加更多功能。手机会默认将网页当作是为桌面浏览器设置的，需要设置meta viewport。	

通过设计理想的元素尺寸（dimensions），并容忍合理的偏差（variance），你实际上可以不需要使用 @media 媒体查询断点。你的组件可以自我处理布局，本质上不需要手动干预。

Intrinsic Web Design可以使用Container Queries，但不是必要的。Container Queries类似于media queries，可以允许你根据容器的尺寸来调整样式，而不仅仅是视口尺寸

可以使用vw或cqi（Container Query Inline Size）来调整尺寸，可以使用:has来选择对象

##### 对比Intrinsic Web Design和Responsive Web Design

Intrinsic Web Design的维护成不低，但对老旧浏览器兼容性差。而Responsive Web Design需要维护多个断点，维护成本高，但是支持更广泛

#### 可访问性

WCAG是对网站开发人员在可访问性方面的指导

这门课把可访问性问题分为了四个维度，即Vision、Hearing、Motor control和Cognitive。

从Cognitive角度考虑，需要考虑内容是会造成感官过载（sensory overload）或困扰（distress），内容是否容易理解，以及内容是否可以被放慢、改变或自定义

从Vision角度考虑，需要考虑是否有可听的或触觉的替代方案（audible or tacle alternaves），例如阅览器阅读文本或触觉震动（haptic vibration）。事物是否以容易被理解的方式呈现，可以以键盘或手势（gestures）导航（navigate）

从Hearing角度考虑，需要考虑是否有音频的文本或视觉替代方案（text or visual alternaves），是否能在听觉上清楚且容易被理解，是否有效利用了图标或图像（icons and images）

从Motor的角度考虑，需要考虑是否可以通过鼠标、触摸、键盘或语音导航和控制，是否容易控制和互动，焦点（focus）是否可见，内容的排序是否合理

#### 软件测试

##### 测试分类

测试的目的是减少漏洞、缩短反馈周期以减少修改成本、提供文档、利于重构、编写利于理解的代码、增加对代码的信心。测试的内容包括Specification、Functionality和Performance

不同类型的测试不同的特点。单元测试（Unit tests）有更快的执行速度和隔离性，但需要进行大量测试。End-to-end测试有更高的集成度（integration），运行更慢，需要的测试数量更少。

Testing Trophy是一种Kent C. Dodds推广的测试策略，有四个层级，即E2E、Integration、Unit和Static（按照颗粒度排序），主要注重integration testing。并使用工具在编写时就发现错误。单元测试（Unit tests）有更快的执行速度和隔离性，但需要进行大量测试。End-to-end测试有更高的集成度（integration），运行更慢，需要的测试数量更少，也能提供最大的信心。

在JS单元测试中，常见的测试框架的代码一般有describe、it和expect三部分组成。端对端测试一般使用Cypress这类框架，执行可能发生的不同操作流程，在完整的UI上进行

cucumber包括3部分，given、when、then、and

Test Driven Development测试驱动开发是一种开发策略，指的是先编写测试用例（最开始是失败的），然后再编写最少量的代码使其通过，然后再重构

##### CI/CD

CI/CD指Continuous Delivery/Continuous Deployment。在CI指，开发者频繁将代码集成到代码库中，然后代码会被自动编译和测试。CD指将将代码自动交付到所需的基础设施环境中的过程。源代码控制一般与CI/CD相连，例如设计成当被推送至main时就触发CD，而每次提交时都触发CI

#### 网络安全

##### 目标

软件开发在实践上缺乏必要的严格控制措施，无法最大限度地减少软件缺陷，尤其是对于复杂的软件，几乎不可能做到完全无 bug，这同样也是因为安全不是被优先考虑的。所以目标是让黑客的工作尽可能艰难，从而避免成为攻击的受害者

##### OWASP 前十名

OWASP指开放式 Web 应用安全项目，2021年的前10名包括Broken Access Control（没有正确限制用户权限），Cryptographic Failures（敏感数据泄露），Injection（注入攻击），Insecure Design（Design flaws，在架构或流程设计阶段存在安全缺陷）等，排名分先后

##### CIA

CIA安全三要素是一种策略，旨在最小化对系统的威胁，包括Confidentiality（仅对授权用户开放访问）、Integrity（资源只能被授权用户修改或删除）和Availability（任何时候都可供授权用户访问）

Confidentiality涉及Data confidentiality和Privacy，使用加密技术来保证这两点

Integrity涉及Data Integrity和System Integrity

Availability指通过提供保障，在发生故障时有冗余（Redundancy）或备份措施（backup measures），确保系统对用户在任何时候都是响应的，且不会终端或拒绝方法

##### 八条Security Design Principles

Economy of Mechanism指让设计尽可能简单和小巧。设计和实现中的错误可能导致不必要的访问路径，但这些错误在正常使用过程中通常不会被发现，因为正常使用通常不会尝试触发这些非法的访问路径。可以重用简单且高质量的组件或库。

Fail-safe Defaults指，一个保守的设计（conservative design）应该明确指出在什么条件下允许访问，默认情况下不授予权限

Complete Mediation指，每一次对每一个对象（系统内的所有object）的访问都必须进行权限检查，包括初始化、恢复、关机和维护

Open Design指，因为试图对任何广泛分发的系统（receives wide distribution）保持秘密是不现实的，系统的安全性不应依赖于潜在攻击者的无知，而应依赖于持有特定、更加容易保护的密钥或密码，同时应该将机制的保护与密钥或密码的保护解耦。

Separation of Privilege指，最好让多个用户共享特权，这样可以增加确保访问授权的保障。例如分离的密钥，这适用于任何需要满足两个或更多条件才能允许访问的情况

Least Privilege指，只提供完成任务所需的最少权限，每个程序和每个用户应仅使用完成任务所需的最少权限集，限制事故或错误可能导致的损害

Least Common Mechanism指，最小化多个系统组件共享的机制数量。密码、资源和进程都不应该共享

Psychological Acceptability指，安全防护措施需要尽可能地用户友好，增加可用性，以便用户能够日常且自动地正确应用保护机制

另一个类似的是Ten Immutable Laws of Security

##### Threat Modelling

威胁建模可以帮助识别系统中可能发生的潜在安全问题，发生在系统的早期阶段或整个生命周期中

这包含五个关键阶段，Asset Identification（确定需要保护的资产），Threat Analysis（分析并识别可能威胁到这些资产的潜在攻击者、恶意行为或其他危险源），Vulnerability Analysis（查找和评估系统中可能被利用的漏洞），Risk Assessment（评估每个威胁的风险）和Risk Communication。

##### STRIDE

STRIDE 是一种威胁建模方法，它代表了六种常见的攻击类型

Spoofing（伪装）：攻击者冒充合法用户或系统，获取未授权的访问。

Tampering（篡改）：攻击者修改系统中的数据或代码。

Repudiation（否认）：攻击者或用户否认他们的行为或操作，没有足够的日志记录或验证。

Information Disclosure（信息泄露）：未经授权的用户访问或泄露敏感信息。

Denial of Service (DoS)（拒绝服务）：攻击者通过使系统资源耗尽，导致合法用户无法访问服务。

Elevation of Privilege（权限提升）：攻击者通过系统漏洞，获得比预期更多的访问权限。

Confidentiality与Information Disclosure有关，Integrity与Tampering和Repudiation有关，Availability与Denial of Service有关

##### DREAD

DREAD 是一个评估威胁的评分系统，用于量化威胁的严重性，每个威胁根据以下五个标准进行评分

Damage Potential（损害潜力）：如果该威胁成功，可能造成的损害程度。

Reproducibility（可重现性）：该攻击能够被重复执行的难易程度。

Exploitability（可利用性）：该威胁被利用的难度，越容易被利用的威胁，分数越高。

Affected Users（受影响的用户数）：该威胁影响到的用户或系统的数量。

Discoverability（可发现性）：攻击者发现该漏洞的难易程度。

##### Insecure Design设计缺陷与相关风险

Insecure Design这条，注重于design flaws带来的风险。目的是使用安全的设计模式（design patterns）、原则（principles）和架构设计（architecture design）

##### Secure

Secure包括Confidentiality（无法读取）、Integrity（完整性）、Authenticity（不可使用Unicode编码、真实性）和Non-repudiation。使用加密来保证保密性，使用数字签名（digital signatures）来保证完整性和不可抵赖性，使用数字证书（digital certificates）来保证电子签名的真实性

在TCP握手完成后，会协商TLS（Transport Layer Security）协议版本，服务器发送证书，客户端对证书进行身份验证，然后生成对称加密密钥

自签名证书（self-signed）指分享公钥并用私钥对公钥签名，这样的问题是无法验证对方身份是否与声明相符。解决方法是让certificate authorities提供root certificates，然后Root CA可以自签名

如果无法获得根证书，也可以使用trust chains。根证书可以颁发机构（Root CA）可以给其他CA的公钥签名，让其代行办法证书的职责

TLS可以使用多种加密套件（Cipher Suites）加密套件是密钥交换算法（Key exchange）、数字签名算法（Digital signature algorithm）、加密算法（Encryption algorithm）和哈希算法（Hash function）的组合，这些组成部分可以建立一个安全的连接

##### 代码注入

代码注入是指恶意代码被注入，并被解释或执行。这可能导致可用性丧失、机密性丧失、完整性丧失或是提取有用信息。

一个解决措施是Prepared/Parametrised Statements，另一个解决措施是Escape Input。后者是将不可信的字符转化为原始字符串，不作为查询的一部分，例如添加\。后者较差，因为这仅使不可信的数据在提供给SQL查询时是安全的，在其他上下文中可能依旧是危险的

##### OS Command Injection和Shell Injection

指攻击者将恶意的操作系统命令注入到命令行中执行，这通常发生在应用程序直接将用户输入传递给shell去执行。解决方法包括仅允许无法注入命令的用户输入例如数值型输入，或是对代码进行转义

##### Cross Site Scripting

Persistent XSS指攻击者将恶意输入提交给网站，网站将这些内容展示给其他用户，例如推特和评论。Reflected XSS指用户点击了一个包含攻击代码的恶意链接，然后恶意代码被浏览器执行

Persistent XSS的解决办法是不信任所有用户提交的内容，并对所有不信任的内容进行消毒（Sanitise），并且避免在url中使用JS

DOM based XSS指将攻击代码注入到正在运行的应用程序中