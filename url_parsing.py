## https://www.kaggle.com/datasets

url="https://www.kaggle.com/datasets"
protocol=url[0:url.find(":")]
print("protocol=",protocol)

dot1=url.find('.')
dot2=url.find('.',dot1+1)

domain=url[dot1+1:dot2]

print("domain=",domain)

page=url[url.find('/',dot2):]
print("page=",page)




