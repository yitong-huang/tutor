## Formatting Text with HTML and CSS

### Character-Level Elements

#### Semantic HTML Tags 语义化标签

* ```<em> emphasized```  
  强调，通常显示为*斜体*
* ```<strong> strongly emphasized```  
  相比em更加强调，通常显示为**加粗**
* ```<code>```  
  代码块
* ```<samp>```  
  标识计算机程序输出，通常使用浏览器缺省的 monotype 字体
* ```<kbd>```  
  表示用户输入，它将产生一个行内元素，通常使用浏览器的默认 monospace 字体显示
* ```<var>```  
  表示数学表达式或编程上下文中的变量名称，通常显示为*斜体*
* ```<dfn>```  
  表示术语的一个定义，通常显示为*斜体*
* ```<cite>```  
  表示一个内容的引用，通常显示为*斜体*
* ```<abbr>```  
  表示一个缩略词

#### Physical Style tags 实体标签

直接告诉浏览器用什么格式来显示文字。现在比较建议使用语义化标签。

* ```<b>```  
  **粗体**
* ```<i>```  
  *斜体*
* ```<u>```  
  <u>下划线</u>
* ```<small>```  
  <small>小号字体</small> 正常字体
* ```<sub>``` Subscript  
  文本<sub>下标</sub>
* ```<sup>```  Superscript  
  文本<sup>上标</sup>

### Character Formatting Using CSS

#### ```<span>```

用于在同一段落内展示不同的样式。

```html
<p>Here is some <span style="text-decoration: underline;">underlined text
</span>.</p>
<p>Here is some <span style="text-decoration: overline;">overlined text</span>.
</p>
<p>Here is some <span style="text-decoration: line-through;">line-through text
</span>.</p>
<p>Here is some <span style="text-decoration: blink;">blinking text</span>.</p>
```

#### font properties

* font-style
    * normal (default)
    * italic
    * oblique
* font-weight
    * bold
    * bolder (通常浏览器无效)
    * lighter
    * 100 - 900
* font-family
    * serif
    * sans-serif
    * cursive
    * fantasy
    * monospace
    * ...
* font-variant
    * normal (default)
* font-size
    * 12px
    * 200%

#### ```<pre>```

#### ```<hr>```

#### ```<address>```

#### ```<blockquote>```

### Special Characters

| val           | code    |
|---------------|---------|
| ```&quot;```  | &quot;  |
| ```&copy;```  | &copy;  |
| ```&lt;```    | &lt;    |
| ```&gt;```    | &gt;    |
| ```&amp;```   | &amp;   |
| ```&nbsp```   | space   |

## Using CSS to Style a Site

### 引入style sheets
* ```<style>``` page-level
```html
<style">
h1 { font-size: x-large; font-weight: bold; }
h2 { font-size: large; font-weight: bold; }
</style>
```
* ```<link>``` site-wide  
```html
<link rel="stylesheet" href="css/MyStyle.css" type="text/css" >
```

### CSS语法

```
selector { property1: value1; property2: value2; .. }
```

### Selectors

```
p, ol, ul { color: blue; }
```

#### Contextual Selectors

```
p cite { color: red; }
```

#### classes

```html
<p class="imprtnt">Some text.</p>
then you write the rule like this
.imprtnt { color: red; font-weight: bold; }
```

#### ids

```html
<p id="number1">Some text.</p>
then you write the rule like this
#number1 { color: red; font-weight: bold; }
```

### Cascading 级联

父级的属性会传递给

### 长度单位

### 颜色

---

### Links

### The Box Model

### &lt;body&gt; tag

