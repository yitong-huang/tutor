1. 时间与顺序(Time and ordering)
a. 向量时钟：事件排序、happens-before关系判断（`happensBefore()` 函数实现）。 
2023-24 Q1 a
b. Lamport逻辑时钟：因果关系的局限性。
2023-24 Q3 h
c. 事件顺序：FIFO、因果序（Causal）、全局序（Total）、同步序（Synchronous）的语义与应用场景。
2023-24 Q4 efgh
2020-21 Q4 c

2. 共识协议
a. Paxos：两阶段提交、崩溃容错（Crash Fault Tolerance, CFT）特性。 
2023-24 Q3 b
2020-21 Q3 a
b. Raft：领导者选举、日志复制、角色（Leader/Follower）。
2023-24 Q3 defg
c. PBFT：拜占庭容错（Byzantine Fault Tolerance, BFT）、容错节点数量（3f+1）。
2023-24 Q3 ij
d. 对比：PBFT vs. Paxos/Raft（容错类型、消息开销、延迟）。

3. 副本复制(Fault Tolerance)
a. 主动复制（Active）：所有副本独立执行请求，适用于区块链。 
b. 被动复制（Passive）：主副本处理请求后同步备份，适用于低延迟场景。
2023-24 q3 k
2022-23 q3 i
2020-21 q2 e
c. 读写一致性：Quorum机制（如 `r + w > n`）、最终一致性。
2021-22 q1 d

4. 容错与故障检测
a. 崩溃检测：心跳机制、超时设定、不可靠网络下的误判风险。
b. 拜占庭容错：最小节点数（3f+1）、Lamport算法。
2023-24 q2 b

5. 通信机制(RPC, Group Communication)
a. Java RMI：远程接口设计、对象序列化、安全性（防篡改票务机制）。
2023-24 q4 a
2022-23 q1 abc
b. 多播：不可靠多播、可靠多播（ACK机制）、原子多播（全有或全无）。
2023-24 q4 fgh
2020-21 q4 b
c. 间接通信：消息队列、发布-订阅模型（适用于移动环境）。
2023-24 q2 f

6. 分布式算法
a. 分布式哈希表（DHT）：节点扩展对流量分布的影响。
2023-24 q2 d
b. 幂等性设计：请求去重（如点赞系统的唯一ID）。
2021-22 q1a

7. 安全与认证(Security)
a. 防重放攻击：时间戳、Nonce值、数字签名。
2022-23 q1 abc q2 d
b 认证协议漏洞：反射攻击的防范（会话状态跟踪）。
c. 密钥管理：对称加密的共享密钥分发挑战。
2020-21 q3 b

8. 性能与扩展(Software containment)
a. 水平扩展：增加同类型节点（如分布式哈希表）。
b. 垂直扩展：升级单节点资源（如CPU、内存）。 
2023-24 q4 c
c. 批量处理：减少网络开销（如主副本批量同步备份）。
2022-23 q4 c
