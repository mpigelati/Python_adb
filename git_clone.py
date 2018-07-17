import json
lst=[]
d={}
with open ("log_msg.txt", "r") as fr:
    data=fr.readlines()
    #print(data)
with open("git_log.json","w") as fp:
    for line in data:
        if "commit" in line and len(d)>0:
            lst.append(d)
            d={}
        if "commit" in line:
            s=line
            d["commit"]= line.rstrip("\n")
        elif "Author:" in line:
            l1=line.split("Author:")
            d["Author"]= l1[1].rstrip("\n")
        elif "Date:" in line:
            l1=line.split("Date:")
            d["Date"]=l1[1].rstrip("\n")
        elif not line == "\n":
            d['message']=line.rstrip("\n")
    json.dump(lst,fp,indent=4,separators=(',',':'))
    fr.close()
    fp.close()

