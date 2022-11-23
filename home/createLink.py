def createLink(links):
    global link 
    link = links
    f = open('home\\templates\\pages\\links.html', 'w',encoding='utf-8')
    # the html code which will go in the file GFG.html

    temp = """{% extends "pages/base_links.html" %}\n"""
#đọc đường dẫn 
    for i in range(0,len(links)):
        temp+="""{% block link_href"""+str(i+1)+""" %}\n"""
        temp+="""/home/cmp"""
        temp+=str(i+1)
        temp+="/"
        temp+="""\n{% endblock %}\n"""
#đọc tên miền           
    for i in range(0,len(links)):
        temp+="""{% block ten_mien"""+str(i+1)+""" %}\n"""
        temp+= "Text "
        temp+=str(i+1)
        temp+="""\n{% endblock %}\n"""
#đọc đường link
    for i in range(0,len(links)):
        temp+="""{% block link"""+str(i+1)+""" %}\n"""
        temp+=links[i]
        temp+="""\n{% endblock %}\n"""

    f.write(temp)
    # close the file
    f.close()
    
    