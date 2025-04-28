# 教学教案：分布式系统中的容错机制（二）

## **第一课时：接口与类型兼容性**

1. **接口的严格性（Java 示例）**
    - 类型兼容性要求接口定义完全一致（示例：`Auction` vs `Potato` 接口）。
    - 客户端与服务器接口不一致的后果（如新增方法导致类型不兼容）。

2. **分布式系统中的类型冲突**
    - 同名但定义不同的类（示例：客户端与服务器的 `AuctionItem` 字段不一致）。
    - 包名不同导致的类型不兼容（示例：`org.me.services.AuctionItem` vs 默认包）。

3. **实现兼容性的关键**
    - 服务器必须严格遵循客户端公布的接口与类型定义。
    - 服务器内部实现可自由扩展（如分模块、负载均衡）。

## **第二课时：消息排序策略**

1. **消息排序的重要性**
    - 无序、FIFO、因果、全序的定义与对比（结合数学运算示例）。
    - 不同排序对系统一致性的影响（如状态机操作的不可交换性）。

2. **排序策略的适用场景**
    - **无序**：适用于操作可交换的场景（如统计计数）。
    - **FIFO**：保证单发送者消息顺序（TCP 实现）。
    - **因果**：处理跨进程的依赖关系（如社交媒体评论）。
    - **全序**：强一致性需求（如数据库事务，需领导者协调）。

3. **技术实现**
    - 时间戳与缓冲区的局限性（全局时间同步问题）。
    - 全序排序的领导者选举机制。

## **第三课时：共识算法与容错**

1. **共识问题**
    - 分布式系统中达成一致的挑战（如网络分区、领导者故障）。
    - 典型场景：领导者选举、事务提交顺序。

2. **主流算法**
    - **Paxos**：基于提案-批准的两阶段协议。
    - **Raft**：通过领导者选举和日志复制简化共识过程。

3. **故障处理**
    - 网络分区下的脑裂问题（示例：多个领导者导致数据不一致）。
    - 容错机制（如心跳检测、超时重选）。

以下是四份试题中与“Fault Tolerance II”课程相关的题目及解答：

---

### **2020-21 SCC.311 Exam**
#### **Question 2.c**
**题目**：  
*What are the two forms of replication for fault tolerance? Name and briefly describe the key properties of each form.*  
**解答**：
1. **Active Replication（主动复制）**
    - 所有副本同时处理客户端请求，保持相同状态。
    - 需要严格的消息全序（Total Ordering）以保证一致性。
    - 支持拜占庭容错（Byzantine Fault Tolerance）。
2. **Passive Replication（被动复制）**
    - 一个主副本（Primary）处理请求并同步状态到备份副本（Backups）。
    - 主副本故障时，备份副本接管。
    - 仅支持崩溃容错（Crash Fault Tolerance）。

#### **Question 3.k**
**题目**：  
*Which of the following statements about active and passive replication are true?*  
**解答**：  
正确选项：
- **a) Active replication does not require a primary replica**（主动复制中所有副本平等处理请求）。
- **b) Active replication is more suitable for a blockchain**（区块链需要拜占庭容错，主动复制更适用）。

### **2021-22 SCC.311 Exam**
#### **Question 3.d**
**题目**：  
*What kind of message ordering is sufficient in a client-server system with multiple clients whose updates to the server state are commutative and the state update operation is idempotent?*  
**解答**：
- **Unordered（无序）**
- 若操作可交换（Commutative）且幂等（Idempotent），无需严格顺序即可保证一致性。

#### **Question 4.a**
**题目**：  
*When sending a message with atomic multicast semantics, how many network messages in total would be sent among the group?*  
**解答**：  
假设组内有 \( N \) 个节点：
- **原子多播（Atomic Multicast）** 需确保所有节点要么全部收到消息，要么全部未收到。
- 使用两阶段提交（2PC），消息数为 \( 2(N-1) \)（协调者发送提案 + 接收确认）。
