from .XuLy import*
def createCmp(input,content,ketqua):
    color=['ffaaaa','ffd4aa','aaaaff','ffaaff','aaffd4','5FE3F5','ffff00','5f00bf','00bf00','ff0000','00ffff','7f007f','00ff7f','7B68EE','483D8B','DC143C','FFA500','00FF00','66CDAA','B0C4DE','808000','BC8F8F','0000FF','1E90FF']
    input_lines = split_line(input)
    content_lines = split_line(content)
    key_list = list(ketqua.keys())
    val_list = list(ketqua.values())

    f = open('home\\templates\\pages\\cmp.html', 'w',encoding='utf-8')
    # the html code which will go in the file GFG.html

    temp = """{% extends "pages/base_cmp.html" %}\n"""
    temp+="""{% block text %}"""

    for i in range(0,len(input_lines)):
        if(i in ketqua and ketqua[i]!=-1):
            temp+="""\n<mark style=" background-color: #"""
            temp+=color[i%len(color)]
            temp+="""">"""
            temp+=input_lines[i]
            temp+="</mark>."
        else:
            temp+=input_lines[i]
            temp+="."
    temp+="""\n{% endblock %}\n"""


    temp+="""{% block content %}"""
    for i in range(0,len(content_lines)):
        if(i in val_list and val_list.index(i) < len(key_list)-1):
            temp+="""\n<mark style=" background-color: #"""
            temp+=color[val_list.index(i)%len(color)]
            temp+="""">"""
            temp+=content_lines[i]
            temp+="</mark>."
        else:
            
            temp+=content_lines[i]
            temp+='.'
    temp+="""\n{% endblock %}\n"""
    f.write(temp)
    # close the file
    f.close()


