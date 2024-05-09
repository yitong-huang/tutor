## Relational Algebra

### 基础操作 week4.p35

#### 选择（Selection）σ

用于从关系中选择满足特定条件的元组。

#### 投影（Projection）π

用于从关系中选择特定的属性列，得到一个新的关系。

#### 乘积（Cross-product）X

将两个关系的元组进行组合，得到一个新的关系。

#### 差（Difference）—

用于从一个关系中删除另一个关系中的元组，得到一个新的关系。

#### 并（Union）∪

用于将两个关系的元组合并在一起，得到一个包含两个关系中所有元组的新关系。

#### 连接（Join）⨝

用于根据两个关系之间的共同属性，将它们的元组进行合并，得到一个新的关系。

#### 除法（Division）/

用于根据一个关系中的元组，找出另一个关系中满足条件的元组，得到一个新的关系。

### exam23.q3.b

I.  
π<sub>email</sub>(σ<sub>accountNo=19911938</sub>(Players))

II.  
π<sub>playerId</sub>(σ<sub>Wearable=1</sub>(Inventory) ⨝<sub>Inventory.item_type=Characters.item_type</sub> Characters ⨝ Players)

III.  
a. 找出所有wearable的items  
W = π<sub>Item_type</sub>(σ<sub>Wearable=1</sub>(Inventory))  

b. Join Characters和Players表  
CP = Characters ⨝ Players  

c. 将CP除W得到用了所有wearable items的players  
Result = CP / W

d. 投影email  
π<sub>email</sub>(Result)

---

## SQL

### 基础

#### CREATE Week5-Part1.p13

```roomsql
CREATE TABLE table_name (
    id INTEGER,
    attr1 VARCHAR(11),
    attr2 INTEGER,
    attr3 TEXT,
    createAt DATE,
    PRIMARY KEY(id),
    FOREIGN KEY(attr1) REFERENCES other_table(attr1),
    UNIQUE(attr2, attr3)
);
```

#### INSERT Week5-Part1.p66

```roomsql
INSERT INTO table_name (attr1, attr2) VALUES (value1, value2);
```

#### DELETE Week5-Part1.p67

```roomsql
DELETE FROM table_name WHERE condition;
```

#### SELECT Week5-Part1.p69

```roomsql
SELECT attr1, attr2 FROM table_name WHERE condition;
```

```roomsql
SELECT DISTINCT attr2 FROM table_name WHERE condition;
```

#### condition

AND, OR, NOT, >, >=, <, <=,  =, !=, LIKE, IN, NOT IN, EXISTS, UNIQUE, ANY, ALL

#### UNION Week5-Part1.p86

#### EXCEPT Week5-Part1.p86

### 聚合运算 Week5-Part2

#### COUNT

#### SUM

#### AVG

#### MAX

#### MIN

#### GROUP BY

#### HAVING

### exam23.q3.a


---  

---  

---

---

---

---
