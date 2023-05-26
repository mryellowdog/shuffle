import sys
import time
import webbrowser

print("Welcome to Shuffle created by mryellowdog")
print("TO RUN FILES: Type open, + enter")
print("Then type name of file")

def translate_syntax(source):
  # Translate code into python

  # Translation
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

  # Replace all Shuffle keywords with their corresponding Python keywords.
  translated_source = source
  for key, value in keywords.items():
    translated_source = translated_source.replace(key, value)

  return translated_source

def main():
  src = input()
  if src == "open":
      # Translate all the shuffle code into python and run it
      code = input()
      langfile = open(code, "r")
      #print(langfile.read())
      #stuff = langfile.read()
      it = langfile.read()
      translated_source = translate_syntax(it)
      print(translated_source)
      file = open("placeholder.py", "w")
      file.write(translated_source)
      file.close()
      webbrowser.open("placeholder.py")
if __name__ == "__main__":
  main()


