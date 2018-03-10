import time
for i in range (1, 28):
    import  urllib2
    url="https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_provinceData.php?country=UKR&provinceID="+str(i)+"&year1=1981&year2=2018&type=VHI_Parea"
    vhi_url = urllib2.urlopen(url)
    out = open('data2/vhi2_id_'+str(i)+time.strftime('_%Y%m%d_%H%M%S', time.localtime())+'.csv','wb')
    out.write(vhi_url.read())
    out.close()
    print "VHI for province "+str(i)+" is downloaded..."
print "Download successful!"
