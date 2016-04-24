import urllib2
import re
def getHtml(testUrl):
	
	request = urllib2.Request(testUrl)
	response = urllib2.urlopen(request)
	html=response.read()
	return html

def getProject(html):
	reg=r'row\s?=\d{2}'
	pro=re.compile(reg)
	project=re.findall(pro,html)
	return project


html=getHtml("http://www.chinawealth.com.cn/zzlc/jsp/lccp.jsp")
print getProject(html)
