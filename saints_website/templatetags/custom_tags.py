

from django import template
register = template.Library()

@register.simple_tag()
def setvar(val=None):
  return val 

@register.simple_tag()
def printval(val=None):
  print(val)

@register.simple_tag()
def add_to(val, by):
  val = int(val)
  val+= int(by)
  return val 

@register.simple_tag()
def toggle(bool):
  if bool == True:
    bool = False
    print(bool, 1)
  elif bool == False:
    bool = True
    print(bool, 1)
  else:
    print(f"Bool cannot be turned into a bool: {bool}")
  return bool

@register.simple_tag()
def splice(text):
  
  html = []
  paragraph = []
  word = ""
  for charchter in text:
    if word != " /n":
      
      if charchter == " ":
        print(word)
        paragraph.append(word)
        word = " "
      else:
        word += charchter
    else:
      word = ""
      html_p = ""
      print("this worked")
      for p_word in paragraph:
        html_p += p_word
        print("this worked")
      print(html_p)
      html.append(html_p)
      paragraph = []
  print(html)
  return html
