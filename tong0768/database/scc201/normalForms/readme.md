## 函数依赖 Functional Dependencies

反映了属性或属性组之间的相互依存和制约关系


##  范式

数据库的范式是关系数据库设计时的规范要求，这些规范确保了数据库的结构清晰、高效且一致。

### 第一范式 First Normal Form (1NF)

每个列都不可再分，即列中存储的都是原子值，不可再分的数据项

在一个学生信息表中，学生的姓名、年龄、学号等都应该是单独列，而不应该有一个列是“详细信息”，其中包含姓名、年龄等多个信息。

### 第二范式 Second Normal Form (2NF)

满足第一范式，并且每个非主属性都完全依赖于整个主键

考虑一个订单表，其中包括客户ID、产品ID、产品数量、产品价格。  
在这个表中，产品数量完全依赖于订单ID，但产品价格依赖于产品ID，不完全依赖于订单ID。  
因此，这个表不满足第二范式。为了满足第二范式，可能需要将产品价格移到另一个表中，如产品表。

### 第三范式 Third Normal Form (3NF)

满足第二范式，并且非主属性之间没有传递依赖

考虑一个学生表，其中包括学号（主键）、姓名、系别、系别地址。  
在这个表中，系别地址依赖于系别，而系别依赖于学号。这种传递依赖关系导致数据冗余和其他问题。  
为了满足第三范式，可以将系别和系别地址移到另一个表中，如系别表。

在某些情况下，为了查询性能和其他优化，可能会故意违反这些范式，但这通常需要深入的考虑和明确的理由。

### BCNF

A B C D

AB -> ABCD  A -> B X

BCNF