# FASTcode
FASTcode is a free and open source programming language that is vastly superior to its competitors. Here are its features at a glance:

| | FASTcode | Python | Java |
| --- | --- | --- | --- |
| Open Source | ✓ | ✓ | ~ |
| Beginner Friendly | ✓ | ✓ | X |
| Static Typing | ✓ | X | ✓ |
| Dynamic Typing | ✓ | ✓ | X |
| Java Interop | ✓ | X | ✓ |
| Functional Programming Features | ✓ | ✓ | ~ |
| Backwards Compatibility with Python 2 | ✓ | X | X |
| Number of Keywords | 3 | 33 | 50 |
| **Characters Required to Print "Hello, World!"** | ***0*** | **13** | **92** |

Since FASTcode is the best in all 9 of these categories (especially the last one), it is the superior language.

How does FASTcode work? It's simple! FASTcode is defined by 3 simple rules:
- If the file is empty, it is outputted as a Python 3 file reading `print('Hello, World!')`
- If the file begins with a "2", the rest of the file is outputted as a Python 2 file
- If the file begins with a "3", the rest of the file is outputted as a Python 3 file
- If the file begins with a "J", the rest of the file is outputted as a Java file
- Otherwise, it is outputted as a Python 3 file reading `print('[rest of the file]')`

## Here are some examples:

### Python 2 backwards compatibility:

```
2
print 'I use Python 2!'
```

Becomes FAST.py:

```
#!/usr/bin/python2
print 'I use Python 2!'
```

### Python 3 coding:

```
3
print('I use Python 3!')
```

Becomes FAST.py:

```
#!/usr/bin/python3
print('I use Python 3!')
```

### Java Interop:

```
J
public class HelloWorld {
   public static void main(String[] args) {
      // This is a comment!!!
      System.out.println("I use Java");
   }
}
```

Becomes FAST.java:

```
public class HelloWorld {
   public static void main(String[] args) {
      // This is a comment!!!
      System.out.println("I use Java");
   }
}
```

### Print anything you want! (great for tutorials):

```
Hello and welcome to TutorialsPoint!
```

Becomes FAST.py:

```
#!/usr/bin/python3
print('Hello and welcome to TutorialsPoint!')
```

### Most important...

` `

Becomes FAST.py:

```
#!/usr/bin/python3
print('Hello World!')
```
