# shuffle
A "programming language" I made. I like multiple programming languages, but I found most of their syntax have things missing or rules that I'm not a big fan of. So I decided to create my own personalized language, mostly inspired by JS, Python and Java.

Shuffle code and syntax translates directly to Python, so you'll need to have python installed. (also this means you can use Python libraries in Shuffle - pretty cool)

# Running Shuffle scripts
Download all the files here, then open up the Shuffle terminal (labeled, shuffle.py). Then write,
```
open
your-file-path.txt
```
Then the file should run immediately.

# Writing Shuffle scripts
I won't go into a ton of detail how to write in Shuffle, but it should be pretty straight forward,
Python translation guide:
```
  keywords = {
      "log": "print",
      "(is)": "==",
      "~": "#",
      "{": ":",
      ">>": " ",
      "else if": "elif",
      "function": "def",
      "insert(plugin),": "import",
      "-[": "{",
      "]-": "}",
      "(refers)": "is",
      "&": "and",
      "(or)": "or",
      ";": "\n", # line break
      "(subtract)": "-=",
      "(add)": "+=",
      "}": "",
  }
```
Here is an example of Shuffle code in action:
```
from turtle insert(plugin), Turtle, Screen
i = 1
wn = Screen();
wn.bgcolor('yellow');
turtle = Turtle();
turtle.pendown();
rand = 0
while i (is) 1 {
 rand (add) 3
 turtle.setheading(rand);
 turtle.forward(5);
}
```

# Notes
Because I made this for myself, this language might not be for everyone :P
Also, I don't reccomend you write anything big using this, as it can be sensitive and janky.
