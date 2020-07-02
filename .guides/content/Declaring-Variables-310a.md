---

## Declaring a Variable
Declaring a variable has two parts - setting or declaring the **data type** and the **name** of the variable. These two properties of a variable do **not** change.

To declare a variable, type the data type and name of the variable you want to create, and a `;` (semi-colon). Copy the code below and `TRY IT`.

```c++
string my_var;
```

{Try it}(sh .guides/bg.sh g++ code/fundamentals/variabledecl.cpp -o code/fundamentals/variabledecl ./code/fundamentals/variabledecl 1)

You will notice we are not printing anything - that is because no value has been assigned yet. Thus, the message `Command was successfully executed.` appears when you click on the `TRY IT` button. The declaration step only sets aside empty memory.

|||challenge
## What happens if you:
* Create two variables with the same type and name?
* Create two variables with the same name but different capitalization (i.e. `my_var` and `My_var`)?
* Create two variables of different types with the same name?

|||

{Try it}(sh .guides/bg.sh g++ code/fundamentals/variabledecl.cpp -o code/fundamentals/variabledecl ./code/fundamentals/variabledecl 2)


## Variable Naming Rules
Here are the rules for naming a variable.

|Rule|Correct|Incorrect|
|----|-------|---------|
|Start with a letter, dollar sign or underscore|`variable`, `$variable`, `_variable`|`1variable`|
|Remainder of variable name is letters, numbers, or underscores|`var_i_able`, `var1able`|`var-i-able`, `var!able`|
|Cannot use a C++ keyword|`my_class`|`class`|
|Variables are case sensitive|`variable`, `Variable`, and `VARIABLE` are all different variables|

## What Are C++ Key Words?
C++ keys words are words that are reserved for specific functions or tasks within C++ programs. These words **cannot** be used to name variables and will result in errors if they are not handled correctly. Click below to see a list of C++ key words.

<details><summary>**List of C++ key words**</summary><table><tr><td>and</td><td>and_eq</td><td>asm</td><td>auto</td><td>bitand</td></tr><tr><td>bitor</td><td>bool</td><td>break</td><td>case</td><td>catch</td></tr><tr><td>char</td><td>class</td><td>compl</td><td>const</td><td>const_cast</td></tr><tr><td>continue</td><td>default</td><td>delete</td><td>do</td><td>double</td></tr><tr><td>dynamic_cast</td><td>else</td><td>enum</td><td>explicit</td><td>extern</td></tr><tr><td>false</td><td>float</td><td>for</td><td>friend</td><td>goto</td></tr><tr><td>if</td><td>inline</td><td>int</td><td>long</td><td>mutable</td></tr><tr><td>namespace</td><td>new</td><td>not</td><td>not_eq</td><td>operator</td></tr><tr><td>or</td><td>or_eq</td><td>private</td><td>protected</td><td>pubic</td></tr><tr><td>register</td><td>reinterpret_cast</td><td>return</td><td>short</td><td>signed</td></tr><tr><td>sizeof</td><td>static</td><td>static_cast</td><td>struct</td><td>switch</td></tr><tr><td>template</td><td>this</td><td>throw</td><td>true</td><td>try</td></tr><tr><td>typedef</td><td>typeid</td><td>typename</td><td>union</td><td>unsigned</td></tr><tr><td>using</td><td>virtual</td><td>void</td><td>volatile</td><td>wchar_t</td></tr><tr><td>while</td><td>xor</td><td>xor_eq</td></tr></table></details>

{Check It!|assessment}(multiple-choice-950845008)
