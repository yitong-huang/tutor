## 索引

### 主键索引 Primary Index Week7.126

* 主键索引是指数据库表中的主索引
* 在数据库表中，Primary Index是唯一的，不允许有空值
* 主键索引建立在按主键排好序的文件上，例如学生的学号

### 聚集索引 Clustering Index Week7.130

* 聚集索引是一种数据库索引结构，它按照指定的列对表中的数据进行物理排序，以提高查询性能
* 聚集索引中，表的数据行按照键值的大小顺序存储，因此聚集索引中的键值决定了数据的物理存储顺序
* 聚集索引建立在按非主键归好类的文件上，例如学生的班级号
* 对于每个表，只能有一个聚集索引，因为表中的数据只能按照一种方式进行排序

### 辅助索引 Secondary Index Week7.p136

* 辅助索引也称为非聚集索引（Non-Clustered Index）或非聚簇索引
* 辅助索引并不直接存储表中数据的物理排序顺序，而是存储索引值和指向表中数据的指针
* 辅助索引建立在按主键排好序，但想要根据没被排序的键值查找记录的文件上
* 在查询时，数据库系统先使用辅助索引定位到表中符合条件的记录，然后再使用指针访问表中的实际数据
* 辅助索引可以有多个，因为它们并不改变表中数据的物理存储顺序

### 索引的实现

#### B树 Week8.p32

#### B+树 Week8.p45

#### Hash Week8.p108

