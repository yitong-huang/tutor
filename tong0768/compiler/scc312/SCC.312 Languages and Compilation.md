# 312 Languages and Compilation

[toc]

## language

##### 语言的基本元素

语言的最基本元素是Alphabet，Alphabet包含了所有的原子的符号。String是用Alphabet中的元素组合成的（也包括Empty String，这一半用epsilon来代表）。而language就是从Alphabet中可以构成的所有有限长度的String的集合。当一个String是language中的元素时，就是sentence

对string的操作包括取长度，符号时||。拼接，没有符号，只是把两个string的代号写在一起。Power，一个字符串的n次方就是重复写几遍。下标则是索引，但是是从1开始的。

##### 定义形式语法

有三种定义形式语法的方式，Set Definitions、Decision Programs和Grammars。如果一个语言的字符串遵循某种某事，就可以用集合来定义这个语言，例如{$a^ib^i:i>1$}。另一种定义方式是Decision Programs，输入一段string，程序可以告诉你这是否属于某个语言，而language就是所有会让程序输入属于这个language的string的集合。最后一种是Grammars，这是一组规则，定义了哪种string是语法正确的（grammatical），这有助于处理人类语言或是计算机语言。

##### 语法分析树和派生树

三种定义形式语法之一的grammar，其中一种定义方式是由很多条rule来定义，这可以由树来表示

有两种树，语法分析树parse tree和派生树derivation tree。派生树从start symbol开始通过rules得到一个valid sentence，而语法分析树从sentence开始得到start symbol来判断sentence是否valid

##### BNF

英语语法本身模糊且复杂，假如要创建一种正式版的语法，需要能做到定义什么是符合语法的，什么不是，以及字符串可能的结构，这可以使用Phrase Structure Grammars。这由terminals（vocabulary、alphabet）、non-terminals（保留词，要全大写）、start symbol、rules（productions）。句子的中间形式称为sentential form

一种正式的grammar的写法是Backus-Naur Form（BNF）。production写为::=，terminal直接写，non terminal写于尖括号中，同一个终结符的多个可能用|分割

##### Regular Grammars

Regular Grammars属于一种phrase structure grammars，属于三种定义形式语法的方法中的grammar。在Regular Grammars中，production的形式总是NON-TERMINAL -> terminal NON-TERMINAL或NON-TERMINAL ->terminal

L(G)的意思是有由文法G生成的语言（Language of the grammar），指由这个文法生成的，包含所有由终结符组成的字符串的集合。

##### FSR

Regular Grammars的结构非常简单，相较于语法分析树和派生树，Regular Grammars可以用另一种语法分析和派生的方式，即FSR（Finite State Recogniser），也叫Finite State Machine FSM或 Finite State Automaton FSA。这需要一组state，一个无源箭头指向一个start state，指向finish state，其余指向其他state。finite state是正方形，其余是圆形

FSR也可以用state transition tables来表达，其每行代表一个状态，每列代表一个输出的终结符，表格中是输出的状态

有时会遇到非确定性的情况（Non-determinism），指下个节点可以往多个方向走，往哪走都行，这种就叫NFSR，这是不好的。最好是找到有确定性的FSR

##### Subset construction algorithm

子集构造算法是一种将NFSR转换为FSR的方法，本质上就是保证每个节点的下一步都是确定的，也就是说可能有多个分支，但是每个分支的输出的终结符都是不同的。如果有相同的输出，就归类到一个节点。如果需要表示finite state，可以用H（halt）.注意转换后的状态要用画括号包裹，

转换后的自动机和原本的自动机，在判断是否符合语法时一致，因此是equivalent。但是赋予字符串的结构不一致，因此被称为weakly equivalent。每个FSR都可以转换为regular grammar，这两者是equivalent的

##### Regular Expressions

正则表达式是一种表达Regular Expressions的方式，常用于模式匹配和替换，十分简洁。其由两部分组成，Individual characters和具体数量限定符（Specific quantifiers），我们只会关注三种限定符，即*、+和？

限定符号规定了其前面的字符可以重复几次。*代表0或多个，+代表1或多个，？代表0或1个

一些编译器可以理解正则表达式，因此可以用于变量名，数字，字符串，符号，保留字。但是一定经典的问题是，无法在括号长度不受限制的情况下，检查括号是否匹配

编译器由Lexical analyser和Syntax analyser组成，前者一般用regular expression 或 grammar来定义，后者用context-free grammar来定义

正则表达式最终也可以转换为一个等价的集合定义，也可以转换为等价的regular grammar（以productions），也可以转换成等价的NFSR

##### context free grammars

Repeat State定理是，FSR能接受的一定能被表达为vwx，v和x都是字符串，w是重复的字符串。这就指出了${a^ib^i:i>1}$不被FSR接受，也就不正则。又或者用production来表达，S->ab，S->aSb

因此就要介绍Context Free Grammars（CFLs）了，这是Regular grammars的超集，其语法是X->RHS，其中RHS是任意终结符和非终结符的任意组合。注意等式左边一定只有一个非终结符

##### pushdown recogniser

类似FSR，context free machine有Pushdown Recogniser（PDR），有时也叫PDA。其本质是一种有堆作为储存器的FSR。其可以无限储存terminal和non terminal，但是只能使用pop（只能出一个元素）和push。注意有些地方是不允许pop一个空的string（epsilon）。输入时第一个字母在最上面

PDR的写法是a/b/cd，其中a是要读取的，b是pop，cd是push，需要最后得到一个H。一般最后一个操作会是 epsilon/empty stack/empty stack，来使PDR变得确定，但不是所有CFL都可以变确定。第一次也可以输出empty stack再输入empty stack，但只要pop了就要重新push

##### Ambiguity

Ambiguity指一种语法可以用多种方式解析一个字符串，或说解析为不同结构，生成两种不同的解析树。这会在编译中产生危害，产生不同的语义，使得程序执行出错或不可预期的行为。歧义本身不会带来危害，只有当有semantic implications时才会有危害。并且不是所有SFL都能做到没有起义，某些会有inherently ambiguous

##### Context Sensitive language

任何一个无限的context free grammar，对于足够长的string，都可以被划分为uvwxy，其中v和x是重复的且不为空。反过来说，如果出现一个字符串不满足这个，就不是CFL

context sensitive language是一种更发杂的语言，可以在推导中使用上下文信息。其规则是LHS->RHS，其中LHS是a非终结符b，RHS是a终结符b

CSL足以应对大多是正常的自然语言和编程语言，但也有一切奇怪的无法被CSL概括

##### Unrestricted language

UL能描述所有能被图灵机理解的语言，其规则是LHS->RHS，LSH至少包含一个非终结符，RHS是任意组合，对于LHS和RHS没有任何限制，所以叫无限制文法。一个相较于上下文有关语言的特点是，其可以左侧的符号数可以大于右侧的符号数。一个例子是${a^ib^jc^{i*j}:i,j>1}$

##### Linear Bounded Turing Machine

FSR和PDR显然都不足以用于处理UL，这就需要图灵机了。图灵机由一个带子（tape）和一个读写头（read-write head）组成。图灵机的行为也可以被以类似FSR的方式描述，弧线上的内容要换为a/b L或a/b R，意思是读a，写b，向左或向右移动，其中a和b可以是0或1或B或终结符或非终结符。一般从最左的非B开始

Linear Bounded Turing Machines指的是，只用了等同于输入长度加上一段长度的tape。LBTM就足够作为CSL的语言识别器了。对于无限制规则，则可能需要TM。TM可以实现一切文法规则，所以可以替换FSR、PDR

##### abstract machine

短语结构文法可以看作语言学工具，也可以看作是计算工具。编译器本质上是一种机器，用于判断一个程序是否合法

有两种抽象机器，一种是Finite State Machine，一种是Turing Machine。finite state transducer是一种可以输出的FSM。FSM遍历一条弧时，可以输出一个符号，写作a/b，意思时读取a输出b，因此可以执行除接受语言之外的功能

FST可以实现简单的记忆功能，例如实现任意大小字母表和任意位数移位shift操作，但只能作用于固定大小。可以实现加法和减法，但是不能实现乘法。同时，这也不是一个对实际计算有实际用处的模型。

通用图灵机可以模拟任意图灵机的行为，只要有那个图灵机的编码和输入数据。一个有程序的计算机本质上就是一个通用图灵机

任何一个电脑，可以模拟图灵机，就说明是图灵完备的了

##### 停机问题

停机指的是一个程序是否能在有限的时间内停止执行，由于存在悖论，所以一定不存在一个程序能判断所有程序是否会停机

##### The Chomsky Hierarchy

总结来说，Phrase Structure Grammars分为Unrestricted，Context Sensitive，Context Free，Regular。分别对应Turing Machine，Linear Bounded Turing Machine，Push Down Recogniser，Finite State Recogniser

## compile

##### compiler的概念和功能

compiler的输入是source language下的source program，输出是target language下的target program，并且会输出error messages。Assemblers较为早期也更简单，但功能类似。另一种结构是以Java为首的Interpreter，首先源码被compiler编译为二进制码，然后在不同平台上用不同interpreter解释

##### compiler的模块化结构

compiler应该是模块化的，一般包括两部分，即analysis element（front-end）和synthesis element（back-end）。其中analysis部分的作用是分析语法是否合法、用某种树+symbol的方式表示程序。而syhthesis部分的作用是将analysis的结果转换为机器码

更细分下来，analysis section下包括lexical analysis、syntax analysis和一些semantic analysis。其中lexical analyser的作用是将源代码转换成token。syntax analyser则需要根据语法生成一个以token组成的syntax tree，以及是否符合语法。semantic analysis则是从语义上分析一段代码有没有逻辑问题，例如变量是否声明前就被使用，类型是否匹配，函数参数是否正确等。

synthesis section会使用syntax tree生成对应的机器码，细分下来包括code generation phase和optimization phase

接下来会关注于lexical analysis、syntax analysis和code generation phase

##### lexical analysis

lexical anaysis的作用是purifies和simplifies。具体来说，就是删除不必要的内容，包括空格、注释等，然后把代码拆分为token。token包括语言当中的symbol、identifier和Literal constants。

symbol就是各种关键词，像是for、while这种，或是各种保留符号，像是等号。Identifiers就是各种变量名，常量名，方法或是类等等。字面常量就包括数字、字符或是字符串等。

tokeniser指的是使用分隔符分词，仅分词对于编程语言的源代码来说并不够强大，因此需要lexical analysis。Lexical的意思是关于words或vocabulary的。其可以理解像带引号的字符串、不同格式的数字、括号嵌套等复杂的情况，适合解析具有语法结构（syntax-bearing）的文本或数据

需要lexical analysis的原因是，这样做会更简单和清晰，同时因为语法可以被定义为regular grammar，且因为这部分被单独划分单独处理，所以lexical analysis可以以一种高效的方式进行。一些语言会允许多种输入格式，那么就只需要替换lexical analyser，而不需要替换lexical analyser

在java下，写lexical analyser的一个较好的范式是，先实例化一个lexical analyser，传入整个原始文本，然后不断get next token。

lexical analyser需要做到一些事，例如检测double quote，escape character。要把numeric value转换为numeric token，要考虑前缀后缀对进制的影像，以及在16进制下对a-f的处理，还有科学计数法还有小数。对于identifiers，传统格式要求首先是字母，然后可以是数字，有些语言会允许下划线。

lexical analyser的程序，具体来说，可以有一个会从input中一个一个提取字符，存到一个临时的token buffer中，当遇到token delimiter时，检查一下是否是一个合法的token。

##### syntactic analysis

syntatic analysis的目的就是构造一个parse tree。树的根是distinguished symbol，树的叶是词法分析阶段得到的token，而每一个分支点都被一个文法规则Sanctioned。有时syntactic analysis会同时进行semantic analysis，如果发现错误需要展示错误信息

有两种parsing strategy，top-down和bottom-up。bottom-up就是根据文法规则，从原本的token，一步步转换为distinguished symbol。top-down就是从distinguished symbol开始，一步步得到token。

如果仅凭简单暴力的算法，对于上下文无关文法，对其的解析的复杂度可能是以指数的方式增长。存在一些更高效的方式，例如Earley’s algorithm和Cocke-Younger-Kasami algorithm

对于解析策略，需要从五个方面衡量，即Power（指能处理的文法的复杂度，例如LL1的能力就不如LR1），Back-tracking（遇到失败时，回头尝试其他路径，这样虽然能增加能力，但是效率低），Lookahead（在做出决策前，预读接下来的符号），Efficiency和small（实现简单，代码量小，资源占用小）

parsing strategies有两种主要的方式，即LL(k)，LR(k)。第一个L的意思是，对于input stream从左到右读。第二个L或R指可以提前向左或向右读k个。LLK会生成最左推导，这是一种top-down的解析方法。LRK会生成最右推导，这是一种自底向上的方法。这两种方法相较于Earley’s algorithm和CYK来说是更局限

##### First set和Follow set

给定一个规则，从该规则中可以推导出的字符串中，可能出现的第一个终结符的集合，就是First set

哪些终结符可能出紧跟在该规则推导出的字符串之后，就是Follow set。

某些终结符是null production，这会使得第一个符号变为空，这是First set就需要包含其后面的终结符的第一个token了。但是第一个终结符的token可以是空，第一个终结符的follower还是第二个终结符的第一个token

为了获取一个非终结符的first，假如这个production的第一位是一个terminal，那么就直接是first。如果第一个是non-terminal，就取这个non-terminal的first。如果是null，就获取下一个。

在处理一个production的follow时，取下一个非终结符的first或是下一个终结符，如果是在结尾，就与上级的non terminal的follow合并。如果要取distinguished symbol的follow，那么首先要加入EOF

##### Recursive Descent Parser

第一个L的意思是这是一个left to right token processing，第二个L是leftmost derivation

Recursive Descent Parser是一种实现自顶向下的parser实现方法，也叫predictive recursive descent

Recursive Descent Parser的实现方法是，当parser想识别某个非终结符时，就调用对应的函数。这个函数会consume这个非终结符，并让parser准备好处理下一个非终结符中的终结符，同时会建立对应的parse tree。对于每种非终结符，都有一个对应的函数。同时要求有一个函数（nextSymbol）来读下一个token。调用某个非终结符的函数后，这个函数会期望下一个token在first set中。当结束时，期望看到下一个token在follow set中，并且是另外一个非终结符的firts set中

也就是说，LL(1)需要知道所有非终结符的第一个终结符可能是什么，才能工作，这也就诞生了一系列的规则。一个非终结符的内部可以是终结符，或非终结符，或终结符加非终结符，或三种都可以。同时这必须是完全deterministic。

deterministic在这里指，两种文法不能从一个terminal开始。当出现这种冲突时，例如if后面有没有else是两种文法，就可以用Left-Factoring去解决。这会把不确定的部分单独定位一个文法，然后这种文法有两种不同的开头。但是这改变了结构，可能导致后续的机器码变得难以生成。

左递归（Left-Recursion）的意思是一个非终结符在自己的推导规则中出现在最左边的位置。这一定会造成non deterministic，并导致无限递归。这需要重写这一部分并避免左递归来解决，又或是以循环而非递归的方法解决（这要求有一个是否能循环的判断条件）

另一种情况是，一个非终结符可以是noll，这时就要检测自己的下一个token在不在follow set里了。这就导致了一个新的约束条件，即如果结尾是null，则follow set必须与其他所有First set不相交

##### LL(1)

如果一门编程语言是LL1的，那么就一定能写出一个对应的recursive descent parser，可以被没有扩展的BNF表示

这要求在一个switch中，多个选项的First set都必须不相交。任何一个可以是null的非终结符，都要满足其first set与follow set不相交

另一个问题是dangling else问题，即在嵌套if中，不确定else属于哪个if。一部分写法，可能会导致所有else都属于最内层的if。这样的话这个规则没有在文法规则中写明，而是写于了解析器中，这可能会带来问题

##### Bottom-Up Parsing

Bottom-Up Parsing是一种通过应用production rule来缩短sentence。其会有一个Parse Stack，存储最近读到的内容，然后使用一个grammar reduction，来不断缩减。正式地讲，有两种操作，即shift和reduce。shift指读取一个token并加入到parse stack中。reduce指使用某个production，将n个元素替换为某个非终结符

有些时候，可能会有多种不同的reduce可以执行，或是既可以执行reduce也可以执行shift，这就产生了ambiguous

##### LR(0)

LR0通过使用action table和goto table解决了上面的问题。除此之外，LR0还需要一个stack和一个input buffer

action table由解析器的状态和终结符（包括end of input这个非终结符）来索引，其内容包括shift（sn，n是下一个state），reduce（rm，m是文法规则）和acc（accept）。也可以有no action

Goto table由一个parser和一个非终结符索引，内容是下一状态

stack一开始会被初始化为state 0，current state指的是stack最上面的state。有了current state和current terminal（还没读的），就可以从action table中得到一个action。根据action，可能会执行sn或rm或别的。sn会移除input stream中的current terminal（也就是读取一个），并写入一个state。rm会对于规则m中RHS的每一个symbol，都从栈中移除一个状态，然后把使用到的规则发送到output stream，然后根据m的LFS symbol和新状态，去goto表找到对应的状态，并推入栈。

总的来说就是，action table告诉你根据你的state和terminal，应该做什么。goto table告诉你，reduce之后，state是什么（类似一个shift，shift本身是否执行取决于state和current terminal，然后会告诉你新state是什么，goto需要state和reduce给的non terminal，然后在goto表中查新的state是什么）

这本质上是一个有限状态自动机Finite State Automaton

通过stack中条目的记录，可以构建对应的树。新push的会成为刚被pop的条目的父节点

##### 生成Action and Goto tables

首先要根据grammar rule和一个代表parser位置的点来生成不同的情况。例如E->E+B会得到4种情况。一个特例是A->epsilon只会得到一种情况。这种不同的情况叫item set或configuration set

然后，将一组item聚合在一起，显示出解析器处于某种状态时，所有可能的情况。dot前的所有non terminal都要转换成terminal。另外需要一个S->sth dot，这样parser就能知道遇到这个item时，说明已经匹配完毕，可以accept。然后要找item之间的转移，这总是从S->dot sth开始的。有时为了把non terminal转换为terminal，需要一些辅助item，这会在其前面写一个加号。没有加号的原始项目称为kernal item或core item。

为了得到同一item set下的不同情况，需要先把item parse tree画出来，根据相同情况的item（下一个是同一个symbol，即之前的情况），把他们都在某一个symbol之后的item都聚合在一起（即之后的情况）。给不同的set不同的数字，然后观察某个item set有什么潜在的input，以及应该做什么

##### Symbol table

符号表是用于储存所有标识符的数据结构。这个数据结构需要能插入新的标识符，也需要被用来查找某个标识符有没有被正确使用，因此需要一个插入和查找都高效。符号表既可以直接保存变量名（这需要预先觉得最大长度），也可以储存一个指向标识符的指针。符号表还要保存变量类型，对于数组要保存下标数量（几维数组）、类型和取值范围，对于函数需要保存参数的数量和类型以及返回值的类型，对于record（构造类型）需要保存字段（field）及其类型。还需要保存特点变量的作用域、生命周期，对象的储存地址。这些可能是基于二叉树或哈希表

symbol table还需要处理作用域（scope）。有三种管理方案，Monolithic、Flat（多个作用域并排）、Nested（作用域嵌套保存）。这里嵌套内部的可以重新定义一个标识符，如果没有重新表示上层标识符，也可以访问上层标识符（most-closely nested rule）

##### Semantic Checking

说到Semantic Checking，首先是考虑类型检查。类型检查的spectrum，可以分为None，Weak，Strong

无类型检查主要发生在汇编语言中，这是因为在汇编语言中，对内存使用的灵活性要求很高。这少在高级语言中出现，因为这意味着bug在运行时才会被发现，

弱类型检查，其含义包括变量可以不按照其被定义的类型处理，函数可以在输入参数不匹配的情况下调用

强类型检查，意味着必须做显示地类型转换。这会导致编程上的不灵活。

这种检查是一种static type checking，意味着这是在编译过程中的检查。其要判断的是类型等价性Type Equivalence。有两种等价性，name equivalence和structure equivalence。后者遍历类型树并递归地检查是否匹配以及是否允许类型转换。强制类型转换是Coercions。名称等价性需要两个变量的类型名相同。

semantic checking中，除了type checking，还有例如declaration checks，要求在使用前必须声明，以及在作用域外不可见。除此之外还有Flow of control checks，例如某些关键词只能出现在循环内部，这可以用语法约束实现，但是可以基于语义检查

##### TAC

三地址码是一种编译器中间状态，每个三地址码涉及三个地址，例如一个operator和两个operand。对于复合指令，则先拆分再用三地址码表示，这样就能表示多于或少于两个operand（例如NOP没有operand）。这一切都是关于地址的，因此某个operand也可以是另一个三地址码结果的临时地址

Literal Table类似符号表，储存的事输入流中的任何字面量，例如数字、字符、字符串。其存在的目的是为了直接索引地址而非字面量

用TAC表示后，就可以进入Optimisation Phase。TAC会被parse tree更容易优化

##### Intermediate Language Compilers

有两种Split-Stage Compilation，一种是先编译成intermediate language，然后再编译一次，另一种是编译成interpreter可以理解的形式

两次编译的Split-Stage Compilation，特点是会有两次code generation phase和优化。假如有一个统一的中间代码，那么多种语言之间就可以在IL层面互通，同一份代码也能在多平台上运行。但是这可能会导致前端过度优化，后端代码低效冗长，架构适配性差，语义信息丢失（难以debug）等

##### Just-In-Time Compilation

JIT于分阶段编译不同，其中间语言会混合高级和低级操作，在程序的执行阶段再完成最后的编译。这样就可以根据最后运行的平台的需求，使用运行时环境补丁Runtime-environment patches。甚至还可以在编译后继续修改代码。Java就是这样做的

##### 基于LR0的解释器

LR0是一个从底向上的编译过程，不用构造整个parse tree，这样适合解释器。区别在于，解释器的stack machine会保留一些original metadata

LR0因为没有lookahead，所以语法必须完全没有歧义。LR1就能更好地解决这个问题，例如处理Precidence Modifiers。

还有一个问题是，如果要调用一个函数，但是这个函数目前还没处理到，又或是recursion，怎么办？一个方法是构建partially compiled tree，另一个方法是enforce a declare-first language，强制要求声明在调用之前
