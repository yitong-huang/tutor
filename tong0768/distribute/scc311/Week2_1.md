## Group Communication 组通信

### 通信模型

* Unicast 单播
  * 一对一
* Broadcast 广播
  * 一对多
* Multicast 组播
  * 一对多
  * 多对多

### 主要关注点

* 可靠性
* 原子性

网络层没有组播的支持，需要应用层自己实现

### 挑战

* 可靠性？
* 可扩展性？ 
* 消息顺序？
* 一致性？

### 可靠性保证

* Best effort
  * 尽力送达，不可靠
* Reliable multicast 可靠组播，抵御网络故障
  * 尽力确保消息在丢失后重传
  * 发送方崩溃时无法保证
* Atomic multicast 原子组播，抵御参与者故障 
  * 所有成员收到消息，或无成员收到 
  * 核心问题：容忍发送方崩溃

2020-21 Q4.a

i. 空间天气更新：
* 选择尽力而为多播（Best-Effort Multicast）
  * 理由：允许消息丢失（每2小时更新一次即可），网络可靠性70%足够，且发送成本高需减少重传。
  * 符合“Best Effort”语义，无强可靠性要求。

ii. 群聊服务：
* 选择可靠组播（Reliable Multicast）+ FIFO排序
  * 理由：需确保所有成员收到消息（可靠），并按发送顺序显示（FIFO）。
  * 可靠组播通过ACK/NACK机制保证交付，FIFO排序确保消息顺序。

iii. 购物服务：
* 选择原子组播（Atomic Multicast）
  * 理由：需确保所有副本服务器一致更新库存（要么全更新，要么全不更新）。
  * 原子组播确保消息要么全交付，要么不交付，防止状态不一致。

### ACK保证可靠性

2020-2021 Q3

1.a：设计一个可扩展的云服务（元组空间）

i. 该服务应设计为无状态（stateless）还是有状态（stateful）？

根据题目要求，服务需要支持数千甚至更多用户同时使用，且仅需提供标准的元组接口，无需记录事务数据（如访问日志、修改历史等）。在这种情况下，设计为**无状态（stateless）**更为合适。

ii. 用两个理由证明你的选择，并说明假设条件。

**理由**：

1. **可扩展性**：无状态服务更容易水平扩展，因为每个请求可以独立处理，无需维护会话或状态信息。

2. **容错性**：无状态服务在节点故障时恢复更快，因为不需要恢复丢失的状态数据。

**假设**：

- 元组空间的底层存储（如数据库）负责持久化状态，服务本身不维护状态。

- 网络层能够保证请求的正确路由和负载均衡。

1.b：基于UDP的接口 `executeOperation`

i. 该接口提供何种保证级别？

接口 `executeOperation` 基于UDP实现，UDP本身不提供可靠性保证。因此，该接口的保证级别是**尽力而为（Best Effort）**，即消息可能丢失、重复或乱序。

ii. 如何修改接口以提高保证级别？

原接口的保证级别：尽力而为（Best-Effort）

无确认机制，消息可能丢失（UDP特性）。

改进后的接口：

```java
public boolean executeOperation(int opId, byte[] args, int sequenceNumber);  
```

保证级别：reliable

添加序列号（Sequence Number）以检测重复消息。

接收方返回NACK，发送方在不是相应的NACK时重传失败内容。

对应PDF内容：可靠组播通过ACK和重传实现交付保证。

### 原子多播

2020-21 Q4.b

i. 在一个由三个副本服务器组成的系统中，假设没有服务器崩溃且没有消息丢失，客户端向其中一个服务器发送消息，该服务器使用原子多播协议将消息发送给其他服务器。根据协议设计（未进行任何优化），服务器组之间可能发送的最大消息数是多少？请解释你的答案。

初始发送：

客户端将消息发送到其中一个服务器（例如 Server A）。

Server A 作为发送方，通过原子多播协议将消息发送给其他两个服务器（Server B 和 Server C），共 2条消息。

二次传播：

Server B 收到消息后，根据原子多播协议要求，需确保所有副本接收消息，因此将消息发送给 Server A 和 Server C，共 2条消息。

Server C 收到消息后，同样将消息发送给 Server A 和 Server B，共 2条消息。

总消息数：

初始发送：2条（A→B, A→C）

二次传播：2条（B→A, B→C） + 2条（C→A, C→B） = 4条消息

总计：2 + 4 = 6条消息

ii.  描述一种对上述原子多播协议的简单优化方法。优化后，服务器组之间发送的最大消息数是多少？

引入协调者（Coordinator），优化后最大消息数为 3条

优化方法：

协调者模式：

客户端将消息发送给一个指定的协调者（例如 Server A）。

协调者负责将消息一次性组播给所有其他服务器（Server B 和 Server C）。

接收方（B 和 C）无需重新组播消息，因为协调者已确保全局交付。