"""
This is a list of function for manipulating html documents as a text framed by tags.
"""

# The following function outputs the first tag that appears in a string, assuming it 
# starts with this tag.

def tag(s):
    c=0
    j=0
    try:
        while c==0:
            if s[j]==">":
                c=1
            else:
                j=j+1
        w=s[:j+1]
    except:
        w=""
    return w

# The following function extracts the name of the first tag.

def tagid(s):
    l=len(s)
    j=0
    c=0
    try:
        while c==0:
            if s[j].isalpha():
                c=1
            else: 
                j=j+1
        c=0        
        k=j+1
        while c==0:
            if s[k].isalpha():
                k=k+1
            else:
                c=1
        w=s[j:k]
    except:
        w=""
    return w

# The following function clears everything before the first tag in a string.

def clean(s):
    k=0
    try:
        while s[k]!="<":
            k=k+1
    except:
        k=len(s)
    s=s[k:]
    return s

# Once extracted a pair of tags and the text in between, the following function removes the 
# tags, and the spaces left at the beginning after this removal.

def cleanextract(s):
    try: 
        k=0
        while s[k]!=">":
            k=k+1
        s=s[k+1:]

        k=0
        while s[k]==" ":
            k=k+1
        s=s[k:]

        k=0
        while s[k]!="<":
            k=k+1
        s=s[:k]

        return s

    except:
        return ""

# The following function eliminates all the spaces in a string.

def eliminatespaces(l):
    while '' in l: 
        c=0
        k=0
        while c==0:
            if l[k]=='':
                del l[k]
                c=1
            else:
                k=k+1

# The following function search for the first tag whose name is q in the string s
# and return its position and length of the block it encloses (assuming no other nested tags).

def first(s,q):
    t=clean(s)
    c=0
    try:
        while c==0:
            l=len(tag(t))
            u=clean(t[l:])
            if tagid(t)!=q:
                t=u
            else:
                d=len(tag(t))+len(t[l:])-len(u)+len(tag(u))
                p=len(s)-len(t)
                return p,d
                c=1
            if tagid(t)=="":
                return ""
    except: 
        return ""


# The following function is similar to the last one, except that it takes the length of the 
# opening tag

def first_opening(s,q):
    t=clean(s)
    c=0
    try:
        while c==0:
            l=len(tag(t))
            u=clean(t[l:])
            if tagid(t)!=q:
                t=u
            else:
                d=len(tag(t))
                p=len(s)-len(t)
                return p,d
                c=1
            if tagid(t)=="":
                return ""
    except: 
        return ""

# The following function returns the first tag of name q and the string s after removing the 
# tag from it. 

def firstextract(s,q):
    try:
        p=first(s,q)[0]
        d=first(s,q)[1]
        w=s[p:p+d]
        s=s[:p]+s[p+d:]
        return w,s
    except:
        return ""

# The following function gets the name of the tag and a dictionnary of the attributes of a tag under the form < tag ... > with 
# their values

def decompose_tag(s):
    l=s.replace('<','')
    l=l.replace('>','')
    c=-2
    w=""
    u=""
    v=""
    d=dict()
    while l!='':
        if c==-2: 
            if l[0].isalpha(): 
                c=-1
                w=w+l[0]
            l=l[1:]
            continue
        if c==-1: 
            if l[0].isalpha():
                w=w+l[0]
            else:
                c=0
            l=l[1:]
            continue
        if c==0:
            if l[0].isalpha():
                u=u+l[0]
            if l[0]=='"':
                c=1
            l=l[1:]
            continue
        if c==1:
            if l[0]=='"':
                c=0
                if u!="":
                    d[u]=v
                u=""
                v=""
            else: 
                v=v+l[0]
            l=l[1:]
            continue
    return w,d
        
     