### Question 1

#### 1a.

A1 = <1, 0, 0>      B1 = <0, 1, 0>      C1 = <0, 0, 1>
A2 = <2, 0, 0>
m1 = <2, 0, 0>      B2 = <2, 2, 0>
A3 = <3, 0, 0>      B3 = <2, 3, 0>
                    m2 = <2, 3, 0>      C2 = <2, 3, 2>
                                        C3 = <2, 3, 3>
                                        m3 = <2, 3, 3>
A4 = <4, 3, 3>

#### 1b.

C2 = <2, 3, 2>
A1, A2, B1, B2, B3, C1

#### 1c.

B2 = <2, 2, 0>
B3, C2, C3, C4

#### 1d.

```java
public static boolean happensBefore(int[] T1, int[] T2) {
    boolean lessThan = false;
    for (int i = 0; i < T1.length; i++) {
        if (T1[i] > T2[i]) {
            return false;
        }
        if (T1[i] < T2[i]) {
            lessThan = true;
        }
    }
    return lessThan;
}
```

#### 1e.

A3 = <3, 0, 0>
C2 = <2, 3, 2>
无因果关系，无法比较顺序

C1 = <0, 0, 1>
A2 = <2, 0, 0>
无直接关系，无法比较顺序

B2 = <2, 2, 0>
A4 = <4, 3, 3>
B2 < A4，B2在A4之前

### Question 2

#### 2a.

1和3错误，无法确定连接问题or节点问题
2正确，系统应设计为容忍错误故障检测
4正确，故障检测器通过发送消息并等待固定时间来判断节点是否故障

#### 2b.

i. 拜占庭错误，3f+1
ii. 论述f+1

#### 2c.

i. 这是一种 主从复制（Primary-Backup Replication）。
  请求是从主节点 A 发起，通过 中间节点 B 扇出传播给多个副本节点。
ii. 客户端（Client）
  它是最初向系统发送请求的节点，并不直接参与复制协议执行。
iii. 主节点（Primary）
  它从 A 接收请求，并将其广播或分发给副本节点（C、D、E），因此它负责组织复制过程。
iv. 不完全正确
  ✔️ 优点 / 正确的方面：
  请求被协调者（B）转发到所有副本节点（C、D、E） → 满足主动复制的“所有副本同时处理相同请求”的要求。
  采用中心分发可以统一顺序，避免副本间状态不一致。

  ❌ 潜在问题 / 不完整的地方：
  没有说明副本节点如何对请求做出响应：例如是否反馈给 B，再由 B 返回给客户端？
  没有提及故障处理机制：比如如果 B 崩溃了，系统是否还能继续工作？ 
  未涉及副本一致性保证：比如是否使用一致性协议（如 Paxos / Raft）保持状态同步？

#### 2d.

i. 从单个节点的角度来看，网络流量会减少。
  在 DHT 网络中，每个文件（或文件的键）通过哈希算法分布在多个节点上，每个节点负责一部分文件的索引和响应请求。当主机数量增加时：
  每个主机仍然每秒只发出一个请求，所以总请求量随主机数线性增加。
  但由于 DHT 是分布式的，所有请求会被平均分配到整个网络中。
  节点越多，每个节点负责的哈希空间越小，也就意味着它被选中处理请求的概率变小。
  所以，单个节点平均要处理的请求数量变少，网络流量对它而言就会下降。

ii. 从单个服务器的角度来看，网络流量会增加。
  虽然服务器数量是固定的，但客户端数量在增加。 
  每个客户端会从一个随机选中的服务器请求文件。 
  因为客户端是随机选择服务器的，所以服务器之间平均分担请求。 
  客户端越多，服务器要处理的请求总数越多，每台服务器被选中的概率不会变，但总体被访问的次数会增加。 
  所以，即使每个客户端只请求一次，随着客户端的增长，单台服务器平均处理的请求数也会增加。


#### **3.a 共识协议的可能用例**
**正确答案**：a)、d)、e)
- **a) 无故障时的状态机复制**：共识协议用于确保副本状态一致，即使无故障也需要协调。
- **d) 故障存在时保证消息全序传递**：共识协议可确保消息在分布式系统中按全序传递。
- **e) 故障存在时保证副本状态一致**：共识的核心目标是维护一致性。  
  **错误选项**：
- **b) 最大化网络吞吐量**：共识协议关注一致性而非吞吐量优化。
- **c) FIFO组通信**：FIFO可通过简单机制实现，无需复杂共识。

---

#### **3.b Paxos协议的特性**
**正确答案**：b)、e)
- **b) 两阶段提交协议**：Paxos包含类似两阶段的“准备-提交”流程。
- **e) 处理崩溃故障**：Paxos设计用于崩溃故障（Crash Fault Tolerance, CFT）。  
  **错误选项**：
- **a) 点对点**：Paxos需要明确的角色（提议者、接受者）。
- **c) 拜占庭容错**：Paxos无法处理恶意节点。
- **d) 最终一致性**：Paxos提供强一致性，非最终一致性。

---

#### **3.c Raft领导者的角色**
**正确答案**：b)、e)
- **b) 提议日志条目**：领导者负责接收客户端请求并提议日志。
- **e) 处理客户端请求并转发给跟随者**：领导者直接与客户端交互。  
  **错误选项**：
- **a) 发起选举**：选举由跟随者超时后触发，非领导者职责。
- **c) 分发投票**：投票由跟随者发送给候选人。
- **d) 监控节点**：Raft无显式健康监控机制。

---

#### **3.d 共识的关键要求**
**正确答案**：a)
- **a) 仲裁达成协议**：共识需多数节点（quorum）同意。  
  **错误选项**：
- **b) 无网络分区**：实际系统需容忍网络分区（CAP定理）。
- **c) 异步通信**：共识协议通常假设部分同步模型。
- **d) 全体一致**：只需多数同意，非全体一致。
- **e) 无节点崩溃**：共识协议需容忍节点崩溃。

---

#### **3.e 不适用于状态机复制的协议**
**正确答案**：d)、e)
- **d) 两阶段提交（2PC）**：用于原子提交，不维护状态机顺序。
- **e) 工作量证明（PoW）**：用于区块链共识，非状态机复制。  
  **正确协议**：a) Paxos、b) Raft、c) PBFT 均适用于状态机复制。

---

#### **3.f Paxos/Raft在区块链中的缺点**
**正确答案**：a)、c)、d)
- **a) 不抗女巫攻击**：传统共识假设固定身份，无法阻止恶意节点伪装。
- **c) 去中心化有限**：Paxos/Raft依赖少数领导者，中心化程度高。
- **d) 不处理拜占庭故障**：无法应对节点恶意行为。  
  **错误选项**：
- **b) 低容错**：实际容错性较高（可容忍少数节点故障）。
- **e) 不处理崩溃故障**：Paxos/Raft专门处理崩溃故障。

---

#### **3.g 分布式日志的作用**
**正确答案**：b)、e)
- **b) 记录已提交事务**：日志保存已达成共识的操作。
- **e) 记录待复制的客户端请求**：日志用于复制未提交的请求。  
  **错误选项**：
- **a) 存储副本状态**：状态由状态机管理，非日志。
- **c) 缓存数据**：非日志核心功能。
- **d) 维护路由信息**：路由由网络层处理。

---

#### **3.h Lamport时钟的特性**
**正确答案**：c)、d)
- **c) 捕获因果关系**：若事件A→B，则A的时钟 < B的时钟。
- **d) 分配唯一时间戳**：每个事件有唯一逻辑时间戳。  
  **错误选项**：
- **a) 全局有序**：仅部分有序，需向量时钟实现全序。
- **b) 依赖全局时钟**：Lamport时钟无需物理时钟同步。
- **e) 向量时间戳**：向量时钟的特性，非Lamport。

---

#### **3.i PBFT未解决的挑战**
**正确答案**：c)、d)
- **c) 网络分区**：PBFT假设同步网络，无法处理长期分区。
- **d) 最终一致性**：PBFT提供强一致性，而非最终一致性。  
  **错误选项**：
- **a) 崩溃容错**：PBFT可处理崩溃故障。
- **b) 拜占庭容错**：PBFT的核心目标。
- **e) 状态机复制**：PBFT支持状态机复制。

---

#### **3.j PBFT vs Paxos/Raft**
**正确答案**：c)、e)
- **c) 处理崩溃故障**：PBFT可容忍崩溃故障（作为拜占庭故障的子集）。
- **e) 容忍更难检测的故障**：拜占庭故障比崩溃更难检测。  
  **错误选项**：
- **a) 更高比例故障**：PBFT需3f+1节点容忍f故障，与Paxos相同。
- **b) 更少消息交换**：PBFT消息复杂度为O(n²)，高于Paxos。
- **d) 更低延迟**：PBFT需多轮通信，延迟更高。

---

#### **3.k 主动与被动复制**
**正确答案**：b)
- **b) 区块链适合主动复制**：区块链中所有节点主动验证交易。  
  **错误选项**：
- **a) 无需主副本**：主动复制可能仍需协调者。
- **c) 被动更复杂**：被动复制（主备模式）更简单。
- **d) 副本独立执行**：被动复制中备副本不执行请求。
- **e) 不容忍崩溃故障**：主动复制可容错。

---

#### **3.l 最终一致性定义**
**正确答案**：c)
- **c) 副本可能暂时不一致，最终收敛**：最终一致性的核心定义。

---

#### **3.m 最终一致性与冲突**
**正确答案**：c)
- **c) 承认冲突并提供解决机制**：最终一致性需显式冲突解决。

---

#### **3.n CRDT的作用**
**正确答案**：c)
- **c) 无需协调解决冲突**：CRDT通过数学结构确保操作可交换/结合。

---

#### **3.o CAP定理**
**正确答案**：b)
- **b) CAP定理指出只能满足两个属性**：经典描述。

---

### 第四题答案与解析

#### **4.a Java RMI的正确描述**
**正确答案**：a)、e)
- **a) 远程对象需实现远程接口**：RMI强制要求`Remote`接口。
- **e) 支持对象作为参数/返回值**：RMI通过序列化传递对象。  
  **错误选项**：
- **b) 仅限同JVM**：RMI支持跨网络调用。
- **c) 仅适合C/S架构**：RMI可用于P2P。
- **d) 无法跨主机调用**：RMI设计支持跨主机。

---

#### **4.b RMI方法执行位置**
**正确答案**：b)
- **b) 服务器端执行**：RMI方法在远程对象所在服务器执行。

---

#### **4.c 水平与垂直扩展**
**正确答案**：b)、c)
- **b) 水平添加同类资源**：例如增加服务器数量。
- **c) 分布负载**：水平扩展的核心目标。  
  **错误选项**：
- **a) 垂直增加资源大小**：描述相反。
- **d) 特定场景适用性**：水平扩展广泛适用，非仅限于数据库。
- **e) 成本效益**：需具体场景分析，非绝对。

---

#### **4.d 时空解耦的错误描述**
**正确答案**：b)、c)
- **b) 分布式共享内存扩展性高**：实际扩展性差（需全局同步）。
- **c) 消息队列时空耦合**：消息队列是时空解耦的典型例子。  
  **正确描述**：a)、d)、e)正确。

---

#### **4.e 顺序保证**
**正确答案**：b)
- **b) FIFO顺序**：保证同一发送者的消息按发送顺序传递。

---

#### **4.f 图2是否全序**
**答案**：否  
**解析**：各副本按本地到达顺序传递消息，不同副本的传递顺序可能不一致，因此未达成全局全序。

---

#### **4.g 时间戳能否保证全序**
**答案**：否  
**解析**：网络延迟可能导致时间戳顺序与实际接收顺序不一致（例如A发送早于B，但B的消息先到达副本），因此无法保证全序。

---

#### **4.h 全局顺序**
**正确答案**：d)
- **d) 全序**：要求所有节点以相同顺序传递消息。

---

#### **4.i 因果顺序**
**正确答案**：a)、e)
- **a) B需先收A的消息**：因果顺序要求A→C的消息被B正确处理。
- **e) A→C存在happens-before关系**：C发送消息依赖A的消息。

---

#### **4.j 实现FIFO**
**答案**：
- **客户端**：为每条消息附加递增序列号。
- **副本**：按客户端维护序列号，确保顺序处理。

---

#### **4.k 广播机制**
**i. 是否全序**：是  
**解析**：领导者按FIFO广播，所有节点接收相同顺序消息。  
**ii. 缺点**：单点故障（领导者崩溃导致系统不可用），性能瓶颈（所有流量经领导者）。  
**iii. 改进**：引入多领导者或使用Raft等共识算法选举领导者，提高容错性。