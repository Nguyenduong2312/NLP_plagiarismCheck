import yake
import re
import requests
from bs4 import BeautifulSoup
import math

def Tien_xu_ly(text):
    #lower case
    text = text.lower()
    #xóa các ký tự đặc biệt
    for char in text:
        if(((32<ord(char)<48) or( 57< ord(char)<65 )or(90< ord(char)<67) or (122 < ord(char)< 127))and(char!='.')):
            text = text.replace(char,'')
    # xóa khoảng trống dư thừa
    text = text.strip()
    x = re.search("  ",text)
    while(x != None):
        x = re.search("  ",text)
        text = text.replace("  ",' ')
    return text

# tách đoạn văn bản thành 1 câu
def split_line(text):
    sentences = text.split(".")
    return sentences
 
    
# Trích key_words bằng YAKE
def keyword(input):
    #custom stopword tiếng Việt 
    stopwords = open('home\stext\stopword_vietnamese.txt', encoding="utf-8").read().splitlines()
    
    # Khởi tạo YAKE với ngôn ngữ tiếng Việt, sinh ứng viên 1-gram và 2-gram, với custom stopwrod
    kw_extractor = yake.KeywordExtractor()
    custom_kw_extractor = yake.KeywordExtractor(lan='vi', n=2, stopwords=stopwords)
    keywords = custom_kw_extractor.extract_keywords(input)
    key = []
    for kw in keywords:
        key.append(kw[0])
    return key
# ghép các key_words thành đường link

def getLink(input):
    link = "https://www.google.com/search?q="
    key = keyword(input)
    for i in range(0,10):
        link+=key[i]
        if(i<9):
            link+='+'  
    print("Link sau khi trích từ key_words: ",link)
    return link

# lấy 5 link từ 5 kết quả tìm kiếm đầu tiên
def link_result(link_search):
    headers = {
        "User-Agent":
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'}
    
    response = requests.get(link_search, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    tuple_link=[]
    for links in soup.find_all('div', class_='yuRUbf'):
        if(len(tuple_link)<5):
            link = links.a['href']
            tuple_link.append(link) 
 
    return tuple_link

#----- cạo content từ link của 1 web
def Scraping(link):
    news = requests.get(link)
    soup = BeautifulSoup(news.content, "html.parser")
    tags = soup.findAll('div' and 'p')

    content = ""  
    for tag in tags:
        content += str(tag.string)
    Tien_xu_ly(content)  
    content = content.replace("none",'')    #xóa chữ dư thừa none

    return content

# tính mức độ giống nhau của 2 câu
def Similarity(sen1,sen2):

    bagOf1 = sen1.split(' ')
    bagOf2 = sen2.split(' ')

    uniqueWords = set(bagOf1).union(set(bagOf2))

    numOf1 =dict.fromkeys(uniqueWords,0)
    sumOf1 = 0
    for word in bagOf1:
        numOf1[word] +=1
    for word in numOf1:
        sumOf1 += math.pow(numOf1[word],2)

    numOf2 = dict.fromkeys(uniqueWords,0)
    sumOf2 = 0
    for word in bagOf2:
        numOf2[word] +=1
    for word in numOf2:
        sumOf2 += math.pow(numOf2[word],2)

    # tính L2 Norm
    L2Of1 =dict.fromkeys(uniqueWords,0.0)
    for word in bagOf1:
        L2Of1[word] = round(numOf1[word]/math.sqrt(sumOf1),3)
    L2Of2 =dict.fromkeys(uniqueWords,0)
    for word in bagOf2:
        L2Of2[word] = round(numOf2[word]/math.sqrt(sumOf2),3)

    t = 0.0
    for word in L2Of1:
        t += L2Of1[word]*L2Of2[word]
    return t

#so sánh 1 câu với 1 văn bản
def cmp_sen_text(sen,text):
    lines = split_line(text)
    for i in range(0,len(lines)):
        if(Similarity(sen,lines[i])>=0.7):  #độ giống nhau lớn hơn 0.7 thì trả về index của câu đó trong content
            return i
    return -1                               #ngược lại trả về -1

#so sánh 2 đoạn văn bản
def cmp_input_content(input,content):
    input_lines = split_line(input)
    same = {}
    for i in range(0, len(input_lines)):
        same[i]=cmp_sen_text(input_lines[i],content)
    print("Ket qua: ",same)
    return same

# hàm trả về các link đầu với đầu vào là input
def get_Link(input):
    links = link_result(getLink(input))  
    for link in links: 
        print(link)
    return links

# so sánh 2 văn bản input và content
def ThucThi(input,content):
    return  cmp_input_content(input,content)


