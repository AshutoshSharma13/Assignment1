#%%
f = open("file.txt")
r = f.read()
s = r.split(' ')

#%%
d = {}
for i in s:  
    if  d.get(i) is None:
         d[i] = 1 
    else:    
        d[i] = d[i]+1
#%%        
for i,j in d.items():
    print(i+" "+str(j))

f.close()

# %%
