## Using Images

### Image formats

#### GIF

Graphics Interchange Format，曾经被广泛应用，但是由于每个像素的只支持256种颜色，显示效果不佳，目前已经很少用于高清图片显示。  
支持简单动画，不支持声音和播放控制。

#### JPEG / JPG

Joint Photographic Experts Group，目前应用最广的图片格式。  
其实是一种有损的压缩算法，但一般肉眼无法察觉。

#### PNG

Portable Network Graphics，被设计来替代GIF。  
无损压缩，支持透明，压缩效率不如jpeg。

#### SVG

Scalable Vector Graphics，可以不失真的放大缩小。

### &lt;img&gt;

#### src

图片的url地址，可以是本地的，也可以是远程的。

#### alt

图片可能由于网络等问题无法加载，alternative text可以作为文字替代。

### &lt;div&gt;

### Images & Text

#### 对齐方式：

* baseline 与父元素基准线对齐
* top 与父元素上对齐
* middle 与父元素居中对齐
* bottom 与父元素下对齐
* text-top
* text-bottom
* sub
* sup
* length

#### 浮动 float

#### space around

### Images and Links

只需要用```<a>```标签将图片包含在里面即可增加超链接

### Image dimension

height & weight 表示图片的长宽，浏览器会根据给出的值进行伸缩。  
如果同时设置height和weight，则安好设置的值显示，如果只设定一个值，则按照原长款比重新计算显示。

```html
<img src="img/HtmlCssJs.png" alt="HTML CSS JS" style="height: 100px; width: 100px;">
```

### Image Backgrounds (div)

#### background-image

```html
<div style="background-image: url('img/HtmlCssJs.png');
 height: 600px;"></div>
```

#### background-repeat


```html
<div style="background-image: url('img/HtmlCssJs.png');
 height: 600px;
 background-repeat: no-repeat"></div>
```

#### background-color

```html
<div style="background-image: url('img/HtmlCssJs.png');
 height: 600px;
 background-repeat: no-repeat;
 background-color: #999"></div>
```

#### background-position

* upper right
    * 100% 0%
    * top right
    * right top
* center
    * 50% 50%
    * center center
    * 50%
* bottom center
    * 50% 100%
    * bottom center
    * center bottom

```html
<div style="background-image: url('img/HtmlCssJs.png');
 height: 600px;
 background-repeat: no-repeat;
 background-color: #999;
 background-position: center center;"></div>
```
