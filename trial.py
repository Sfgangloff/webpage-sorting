from strings_functions import *

x="Smallindex"
f= x + ".txt"

def formatting_head(s):
    start=first_opening(s,'head')[0]
    length_start=first_opening(s,'head')[1] 
    end=first_opening(s[start+length_start:],'head')[0]
    length_end=first_opening(s[start+length_start:],'head')[1]
    content=s[start+6:start+length_start+end+length_end-7]
    u=s[start+length_start+end+length_end:]
    t=clean(content)
    w=""
    while t!="":
        t=clean(t)
        v=t[len(tag(t)):]
        p=len(v)-len(clean(v))
        v=clean(v)
        if v[:2]=='</':
            l=len(tag(t))+p+len(tag(v))
            w += t[:l] +'\n'
            t=t[l:]
        else: 
            l=len(tag(t))
            w += t[:l]+'\n'
            t=t[l:]
    return w, clean(u) 

s='    <head> <title> Silvère Moon-Gangloff</title> \n     <link href="style.css" rel="stylesheet" media="all" type="text/css"> \n \n   \n <link rel="icon" type="image/jpg" href="images/image10.jpg" /> \n \n \n <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script> </head>'

with open(f,"r") as u:
    y=u.read()
    print("<!DOCTYPE html>\n\n<head>\n"+formatting_head(y)[0]+"</head>\n\n"+formatting_head(y)[1])



