#coding=utf-8
import codecs
import re

def txtFile2html(inFile,outFile=""):
    html0 = ""
    html0 += "<html>\n<body>\n"
    f = codecs.open(inFile,"r","utf-8")
    for line in f:
        html0 += "<p>\n"
        line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
        html0 += line
        html0 += "</p>\n"
    html0 += "</body>\n</html>"
    # print(html0)
    f.close()
    if outFile != "":
        out = codecs.open(outFile,"w","utf-8")
        out.write(html0)
        out.close()
    return html0

def str2html(str0,outFile=""):
    # html0 = ""
    # html0 += "<html>\n<body>\n"

    # lines = str0.split("\n")
    # print("\n".join(lines))
    # for line in lines:
    #     html0 += "<p>\n"
    #     line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
    #     html0 += line
    #     print(html0)
    #     html0 += "</p>\n"
    #     print(html0)
    # html0 += "</body>\n</html>"
    # print(html0)
    html0 = re.sub('\*(.+?)\*', r'<em>\1</em>', str0)
    html0 = str0.replace('\r\n', '\n</p>\n<p>\n')
    html0 = "<html>\n<body>\n<p>\n" + html0 + "\n</p>\n</body>\n</html>"
    if outFile != "":
        out = codecs.open(outFile,"w","utf-8")
        out.write(html0)
        out.close()
    return html0

if __name__ == "__main__":
    # print(txtFile2html("example.txt","example.html"))
    with codecs.open("example.txt","r","utf-8") as f0:
        str0 = codecs.open("example.txt","r","utf-8").read()
    print(str2html(str0))