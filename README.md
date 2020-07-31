# RemoveStreches_Python
## A simple script to remove stretches in strings

---
this article was translated from (pt-br to en-us) using google translator

---
This script removes excerpts from within its text (such as, for example, this residue), and if there is any residue, just give the start parameter of the residue and the end parameter of the residue, for example, if you want to remove a list of credits beginning with <credits:> and ending with </end>, this code will work perfectly and remove all content between the start and end parameters

Possibly in the future I will make an inverse formula, so you can get the parameters from inside the text, instead of deleting them


That is, it is a simple, easy-to-use script that you can manually import into your project (because I do not know how to import (at the moment) by pip install) and use it to clean residues and excerpts from your code where you do not know the size or where the size can change, like (this) or (this here, but this one is bigger than the other) in the case used in this example, it would remove everything that is between '(' until ')' or if you have a return of an uncontrollable function, being able to return a simple Tip(text='some text') or returning Tip(width=50, heght=10, lang=en, text='some text') and you want to extract the text of this content, send it to a string str (), and make the call clearStrech, putting the text, the start being: 'Tip(' and the End being 'text=' and it will return only the text regardless of what comes after Start and before End

#### Example:
```
txt = str("Tip(width=50, heght=10, lang=en, text='some text') or  str(Tip(hidden=true, text='some text'")
txt = clearStrech(txt,"Tip(", "Tip(", "text=")
print(txt) is: "'some text'" with ''
print(txt.replace("'", "")) is: "some text" whithout the ''
```
---
#### phrases like: (<div class=>"js-stale-session-flash flash flash-warn flash-banner" hidden> == $0)
```
Input = str(<div class=>"js-stale-session-flash flash flash-warn flash-banner" hidden> == $0)
Input = clearStrech(Input, '<div', '=>"')
Input = clearStrech(Input, '" h', '$0')
Outputs(Input) = 'js-stale-session-flash flash flash-warn flash-banner'
```

#### or phrases like: (Source(config=False)>this is a exemple (or not?) of an string (or list<>), and list is: *pic one, pic two, pic three* the lists, yeah)
```
Input = 'Source(config=False)>this is a exemple (or not?) of an string (or list<>), and list is: *pic one, pic two, pic three* the lists, yeah'
Input = clearStrech(Input, 'Source', ')>') # remove all of thins are in the Source that )>
Input = clearStrech(Input, '(', ')')
Input = clearStrech(Input, '*', '*')
Outputs(Input) = 'this is a exemple of an string, and list is: the list, yeah'
```

---

## Example to use in your code:
Suppose you use an api to go to wikipedia and search for the value "michael jackson" and you get this return:
```
<wiki>/<div>/<option:en-us>/MainText:Michael Joseph Jackson (August 29, 1958 – June 25, 2009) was an American singer (usa), and dancer. Dubbed the "King of Pop
```
Notice, this return is not pleasant, because it has the birth date and some shortcuts in html that are irrelevant, in your case you can have other types of shortcuts, just follow this concept to remove them:

#### How to apply in python:
```
# first, place the 'RemoveStreches' file in your python project file !!! to import
from RemoveStreches import clearStrech

txt = '<wiki>/<div>/<option:en-us>/MainText:Michael Joseph Jackson (August 29, 1958 – June 25, 2009) was an American singer (usa), and dancer. Dubbed the "King of Pop". Its awesome!'
txt = clearStrech(txt, "<wiki>", "MainText:")
txt = clearStrech(txt, "(", ")")
txt = clearStrech(txt, '"', '"')
print(txt)
```
This will return to "txt" the value:
```
Michael Joseph Jackson was an American singer, and dancer. Dubbed the. Its awesome!
```
In this case, I removed all the content from the parentheses and also removed all the content inside the quotes and also removed the initial waste

I also noticed that you need to use it according to your choices, because removing quotes, or parentheses, can negatively affect the text, use it carefully!


