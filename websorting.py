import os 
from strings_functions import *

# Input for the webpage cleaner.

x="index"
f= x + ".html"

# The following function formats a string coming from the extraction of head content in 
# a html page. It relies on the fact that there are no nested tags in the head part.
# A RETESTER

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
    w=w[:len(w)-2]
    u=clean(u)
    return w, u 



# The following function detects the svg environments and write a script to load the content 
# on the load of webpage. When a svg envionment is detected, detect the corresponding closing 
# tag, and extract all the text in between these two tags (it assumes that sub-images use 
# the tag 'g' instead of 'svg'). In the svg tag, if it has an id, 
# write in the js file a script that loads the content with this id, otherwise create a new id.

def collect_svg(s):
    collection=dict()
    c=0
    t=s
    w=""
    java=dict()
    while t!="":
        p=len(t)-len(clean(t))
        u=clean(t)
        d=decompose_tag(tag(u))[1]
        n=decompose_tag(tag(u))[0]
        new_tag=""
        content=""
        if n=="svg":
            v=u[len(tag(u)):]
            a,b = first(v,"svg")[0],first(v,"svg")[1]
            content=u[len(tag(u)):len(tag(u))+a]
            if 'id' in d:
                new_tag=tag(u)
                collection[d['id']]=content
                w=w+t[:p]+new_tag+"</svg>"
                t=v[a+b:]
                java[d['id']] = '\n\n' +  '(document).ready(function(){' +'$("#{}")'.format(d['id']) + '.load("' + x + '_svg_{}.txt");'.format(d['id'])+'});'
            else: 
                c=c+1
                collection['image_{}'.format(c)]=content
                
                new_tag="<"+n+" "
                for attribute in d:
                        new_tag=new_tag+attribute+'="'+d[attribute]+'" '
                new_tag += 'id="image_{}"'.format(c)
                new_tag += ">"

                w=w+t[:p]+new_tag+"</svg>"
                t=v[a+b:]
                java['image_{}'.format(c)] = '\n\n' +  '(document).ready(function(){'+'$("#image_{}")'.format(c) + '.load("' + x + '_svg_image_{}.txt"'.format(c)+');});'
        
        else:
            k=len(tag(u))
            w=w+t[:p+k]
            t=u[k:]    
    
    return java,collection,w



# The following function collects all the possible values of style attribute that 
# appear in a string. 

def collect_styles(s):
    collection=dict()
    c=0
    t=s
    w=""
    extracted_styles=''
    while t!="":
        p=len(t)-len(clean(t))
        u=clean(t)
        d=decompose_tag(tag(u))[1]
        n=decompose_tag(tag(u))[0]
        new_tag=""
        if 'style' in d:
            if d['style'] in collection:
                pass
            else:
                c=c+1
                collection[d['style']]=c
                extracted_styles += '\n\n' + '.class_{}'.format(c)+'{' + d['style'] + '}'
            if 'class' in d: 
                d['class']=d['class']+ ' ' + 'class_' + '{}'.format(c)
            else: 
                d['class']='class_'+'{}'.format(c)

            new_tag="<"+n+" "
            for attribute in d:
                if attribute != 'style':
                    new_tag=new_tag+attribute+'="'+d[attribute]+'" '
            new_tag= new_tag[:len(new_tag)-1]
            new_tag += ">"
        else:
            new_tag = tag(u)

        k=len(tag(u))
        w=w+t[:p]+new_tag
        t=u[k:]
    return w, extracted_styles
            

with open(f, "r",encoding='utf-8') as t: 
    line=t.read()
    extract_style=""

    # The following searches for the tags style, removing them from 
    # the webpage and collecting them into a css stylesheet with the same name.
    # It leaves also a link to the stylesheet.

    while first(line,"style")!="":
        extract_style=extract_style+cleanextract(firstextract(line,"style")[0]) 
        line=firstextract(line,"style")[1] 
    extract_style=extract_style.replace(" ","")
    extract_style=extract_style.replace("\n","")
    extract_style=extract_style.replace("}","}\n\n")
    extract_style=extract_style.replace('@keyframes', '@keyframes ')
    line=line.replace('</head>','<link rel="stylesheet" href="'+ x +'.css">\n\n</head>')
    with open(f, "w",encoding='utf-8') as u: 
        u.write(line)
    stylesheet=x+".css"
    with open(stylesheet,"a",encoding='utf-8') as v:
        v.write(extract_style)

    # The following does the same for scripts (assuming they are all in javascript)
    # with additional feature that puts the links to external .js documents to 
    # the head.

    extract_script=""
    extract_temporary=""
    while first(line,"script")!="":
        if 'src' in decompose_tag(tag(firstextract(line,"script")[0]))[1]: 
            extract_temporary=extract_temporary + "\n\n" + firstextract(line,"script")[0]
        else: 
            extract_script=extract_script+ "\n\n" + "//Part of script \n"+ cleanextract(firstextract(line,"script")[0])   
        line=firstextract(line,"script")[1]
    line=line.replace('</head>',extract_temporary+ "\n\n"+ '<script type="text/javascript" src="'+x+'.js"></script>\n\n</head>')    
    with open(f, "w",encoding='utf-8') as u: 
        u.write(line)
    scripts=x+".js"
    with open(scripts,"a",encoding='utf-8') as v:
        v.write(extract_script)

    # The following executes collect_styles, meaning that it migrates all the styles in 
    # tag to the css file that was already created.

    with open(f,"r",encoding='utf-8') as u:
        y=u.read()
        with open(f,"w",encoding='utf-8') as z: 
            z.write(collect_styles(y)[0])
        with open(x+'.css',"a",encoding='utf-8') as h:
            h.write(collect_styles(y)[1])

    # The following executes collect_svg, and store each of the svg images in 
    # text files.

    with open(f,"r",encoding='utf-8') as u:
        y=u.read()
        scripts=""
        for image_id in collect_svg(y)[1]:
            with open(x+'_svg_'+ image_id + '.txt',"w+",encoding='utf-8') as h:
                if h.read()=="":
                    h.write(collect_svg(y)[1][image_id])
                    scripts += collect_svg(y)[0][image_id]
        if scripts!="":
            scripts = "// Part of script: \n\n" + scripts 
        with open(x+'.js',"a",encoding='utf-8') as h:
            h.write(scripts)
        with open(f,"w",encoding='utf-8') as z: 
            z.write(collect_svg(y)[2])

    # The following cleans the head part of the document

    with open(f,"r",encoding='utf-8') as u:
        y=u.read()
        new_head_with="<!DOCTYPE html>\n\n<head>\n"+formatting_head(y)[0]+"</head>\n\n"+formatting_head(y)[1]
        with open(f,"w",encoding='utf-8') as v:
            v.write(new_head_with)




