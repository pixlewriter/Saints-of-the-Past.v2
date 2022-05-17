

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
  elif bool == False:
    bool = True
  else:
    print(f"Bool cannot be turned into a bool: {bool}")
  return bool

@register.simple_tag()
def splice(text):
  text += "This text does not matter"
  html = []
  paragraph = []
  word = ""
  for charchter in text:
    if word != " /n":
      
      if charchter == " ":
        paragraph.append(word)
        word = " "
      else:
        word += charchter
    else:
      word = ""
      html_p = ""
      for p_word in paragraph:
        html_p += p_word
      html.append(html_p)
      paragraph = []
  print(html)
  return html

@register.simple_tag()
def makeSummary(entry):
  return entry[:150] + "..."

@register.simple_tag()
def makeStr(val):
  return str(val)