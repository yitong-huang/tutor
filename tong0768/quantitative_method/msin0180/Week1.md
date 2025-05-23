### 第10页
**学习目标：微积分基础**
- 函数、极限、连续函数的严格定义
- 向量

---

### 第11页
**函数、定义域、余定义域与值域**  
函数 \( f \) 是从集合 \( D \) 到集合 \( Y \) 的规则，为每个 \( x \in D \) 唯一指定 \( f(x) \in Y \)。
- \( D \) 为定义域，\( Y \) 为包含值域的余定义域。
- 余定义域是包含函数所有可能输出的集合。

---

### 第12页
**满射性**  
若余定义域等于值域，则函数为**满射**。  
**定义**：对余定义域中的每个 \( y \)，存在 \( x \in D \) 使得 \( f(x) = y \)。

---

### 第13页
**区间表示法**
- \( (0, \infty) \)：所有正数
- \( (-\infty, 0) \)：所有负数
- \( [0, \infty) \)：非负数
- 方括号表示包含端点，圆括号表示不包含。

---

### 第14页
**数集符号**
- \( \mathbb{N} \)：自然数（0, 1, 2, ...）
- \( \mathbb{Z} \)：整数（..., -2, -1, 0, 1, 2, ...）
- \( \mathbb{R} \)：实数
- \( \mathbb{C} \)：复数

---

### 第15页
**自然定义域**  
自然定义域是公式能产生实数值的最大实数 \( x \) 集合。  
**示例**：
- \( y = x^2 \)：定义域 \( (-\infty, \infty) \)，值域 \( [0, \infty) \)
- \( y = \sqrt{x} \)：定义域 \( [0, \infty) \)，值域 \( [0, \infty) \)

---

### 第16页
**函数的严格定义**  
示例：  
\( f: [-2, \infty) \to \mathbb{R} \)  
\( x \mapsto \sqrt{x + 2} \)

---

### 第17-23页
**Mathematica示例**  
（代码与图表保留原文，附中文注释）
- 定义分段函数：`Piecewise[{ {-x, x<0}, {x^2, 0≤x≤1}, {1, x>1} }]`
- 绘制图形：`Plot[f[x], {x, -3, 3}]`

---

### 第24页
**偶函数与奇函数**
- **偶函数**：\( f(-x) = f(x) \)
- **奇函数**：\( f(-x) = -f(x) \)

---

### 第25页
**复合函数**  
复合函数 \( f \circ g \) 的定义域为满足 \( g(x) \) 属于 \( f \) 定义域的 \( x \) 值。  
示例：  
\( (f \circ g)(x) = f(g(x)) \)

---

### 第26-27页
**单射函数与反函数**
- **单射函数**：若 \( f(x_1) = f(x_2) \) 则 \( x_1 = x_2 \)
- **反函数**：\( f^{-1}(b) = a \) 当且仅当 \( f(a) = b \)

---

### 第28-29页
**Mathematica求反函数**  
代码示例：
```mathematica  
f[x_] := 5x + 4  
InverseFunction[f][x]  
(* 输出：\(\frac{1}{5}(x - 4)\) *)  
```

---

### 第30页
**极限与连续性**  
极限提供了描述函数行为的精确方法，是连续性定义的基础。

考虑函数 \( f(x) = \frac{x^2 - 1}{x - 1} \) 在 \( x \to 1 \) 附近的行为：  
\[
f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad (x \neq 1)
\]  
当 \( x \neq 1 \) 时，函数简化为 \( x + 1 \)，但 \( x = 1 \) 处无定义。

---

### 第31页
**极限的非正式定义**  
如果当 \( x \) 足够接近 \( x_0 \) 时，\( f(x) \) 可以任意接近 \( L \)，则称 \( f(x) \) 的极限为 \( L \)，记为：  
\[
\lim_{x \to x_0} f(x) = L
\]  
**示例**：  
\[
\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = 2
\]

---

### 第32页
**极限法则**  
已知 \( \lim_{x \to c} f(x) = L \) 和 \( \lim_{x \to c} g(x) = M \)，则：
- **和法则**：\( \lim_{x \to c} [f(x) + g(x)] = L + M \)
- **常数倍法则**：\( \lim_{x \to c} [k \cdot f(x)] = k \cdot L \)
- **乘积法则**：\( \lim_{x \to c} [f(x) \cdot g(x)] = L \cdot M \)
- **商法则**：\( \lim_{x \to c} \frac{f(x)}{g(x)} = \frac{L}{M} \quad (M \neq 0) \)
- **幂法则**：\( \lim_{x \to c} [f(x)^n] = L^n \quad (n \in \mathbb{N}) \)

---

### 第33页
**极限计算示例**  
求 \( \lim_{x \to c} (x^3 + 4x^2 - 3) \)：  
\[
= \lim_{x \to c} x^3 + \lim_{x \to c} 4x^2 - \lim_{x \to c} 3 = c^3 + 4c^2 - 3
\]

---

### 第34页
**夹逼定理（Sandwich Theorem）**  
若在包含 \( c \) 的区间内（除 \( c \) 外），有 \( g(x) \leq f(x) \leq h(x) \)，且  
\[
\lim_{x \to c} g(x) = \lim_{x \to c} h(x) = L,
\]  
则 \( \lim_{x \to c} f(x) = L \)。

---

### 第35页
**夹逼定理示例**  
计算 \( \lim_{x \to 0} x^2 \sin\left(\frac{1}{x}\right) \)：  
由 \( -x^2 \leq x^2 \sin\left(\frac{1}{x}\right) \leq x^2 \)，且 \( \lim_{x \to 0} -x^2 = \lim_{x \to 0} x^2 = 0 \)，得极限为 **0**。

---

### 第36页
**分段函数的极限**  
研究函数 \( f(x) = \begin{cases} \frac{1}{x} & x \neq 0 \\ 0 & x = 0 \end{cases} \) 在 \( x \to 0 \) 时的行为。  
当 \( x \to 0^+ \)，\( f(x) \to +\infty \)；当 \( x \to 0^- \)，\( f(x) \to -\infty \)，故极限不存在。

---

### 第37页
**单侧极限**  
函数 \( f(x) = \frac{x}{|x|} \) 的单侧极限：
- 右极限：\( \lim_{x \to 0^+} f(x) = 1 \)
- 左极限：\( \lim_{x \to 0^-} f(x) = -1 \)

---

### 第38页
**极限存在的条件**  
函数 \( f(x) \) 在 \( x \to c \) 时有极限 \( L \) 当且仅当：  
\[
\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x) = L
\]

---

### 第39页
**连续性定义**  
函数 \( f(x) \) 在点 \( c \) 处连续需满足：
1. \( f(c) \) 存在；
2. \( \lim_{x \to c} f(x) \) 存在；
3. \( \lim_{x \to c} f(x) = f(c) \)。

---

### 第40页
**不连续性的类型**
- **跳跃不连续**：左右极限存在但不相等。
- **无穷不连续**：极限为无穷大（如 \( f(x) = \frac{1}{x} \)）。
- **振荡不连续**：极限振荡不定（如 \( f(x) = \sin\left(\frac{1}{x}\right) \)）。

---

### 第41页
**连续函数的性质**  
若函数在区间内每一点连续，则称其在该区间上连续。

---

### 第42页
**中值定理**  
若 \( f \) 在闭区间 \([a, b]\) 上连续，且 \( y_0 \) 介于 \( f(a) \) 和 \( f(b) \) 之间，则存在 \( c \in [a, b] \) 使得 \( f(c) = y_0 \)。

---

### 第43页
**中值定理示例**  
证明方程 \( x^2 - x - 1 = 0 \) 在 \((1, 2)\) 内有根：  
令 \( f(x) = x^2 - x - 1 \)，则 \( f(1) = -1 < 0 \)，\( f(2) = 5 > 0 \)，由中值定理，存在 \( c \in (1, 2) \) 使得 \( f(c) = 0 \)。

---

### 第44页
**渐近线**
- **水平渐近线**：若 \( \lim_{x \to \pm\infty} f(x) = b \)，则 \( y = b \) 是水平渐近线。
- **垂直渐近线**：若 \( \lim_{x \to a} f(x) = \pm\infty \)，则 \( x = a \) 是垂直渐近线。

---

### 第45页
**向量基础**
- 向量具有大小和方向，可用箭头符号（如 \( \vec{AB} \)）或粗体（如 \( \mathbf{u} \)）表示。
- 可表示为行向量 \((x \quad y)\) 或列向量 \(\begin{pmatrix} x \\ y \end{pmatrix}\)。

---

### 第46页
**位置向量**  
位置向量以原点 \( O = (0, 0) \) 为起点，表示点 \( B = (x, y) \)。

---

### 第47页
**向量的模长与单位向量**
- **模长**：向量 \( \vec{AB} = \begin{pmatrix} x \\ y \end{pmatrix} \) 的模长为  
  \[
  |\vec{AB}| = \sqrt{x^2 + y^2}
  \]
- **单位向量**：模长为1的向量（如基向量 \( \mathbf{i}, \mathbf{j} \)）。

---

### 第48页
**点积（Dot Product）**  
向量 \( \mathbf{u} = \begin{pmatrix} u_1 \\ u_2 \end{pmatrix} \) 与 \( \mathbf{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} \) 的点积为：  
\[
\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 = |\mathbf{u}| |\mathbf{v}| \cos\theta
\]

---

### 第49页
**点积示例**  
求向量 \( \mathbf{u} = \begin{pmatrix} 1 \\ 2 \end{pmatrix} \) 与 \( \mathbf{v} = \begin{pmatrix} 3 \\ 4 \end{pmatrix} \) 的夹角 \( \theta \)：  
\[
\cos\theta = \frac{\mathbf{u} \cdot \mathbf{v}}{|\mathbf{u}| |\mathbf{v}|} = \frac{1 \cdot 3 + 2 \cdot 4}{\sqrt{1^2 + 2^2} \cdot \sqrt{3^2 + 4^2}} = \frac{11}{\sqrt{5} \cdot 5} \implies \theta = \cos^{-1}\left(\frac{11}{5\sqrt{5}}\right)
\]

--- 

**注**：数学公式与符号保留原格式以确保准确性。