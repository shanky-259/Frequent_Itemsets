import sys
import itertools
files=sys.argv

def hashing(x):
    return x%int(files[3])

def apriori():
    basket_items=[]
    set_items=set()
    lines=[l.rstrip() for l in open(files[1],'r')]
    for line in lines:
        basket_items.append(line.split(','))
    for basket in basket_items:
        for item in basket:
            set_items.add(item)
    unique_items=sorted(set_items)
    indexed={}
    for i,item in enumerate(unique_items):
        indexed[item]=i+1
    dict_item={}
    for item in unique_items:
        dict_item[item]=0
     
    for basket in basket_items:
        for item in basket:
            dict_item[item]+=1
           
    freq_item=[[]]       
    for item in dict_item:
        if dict_item[item]>=int(files[2]):
            freq_item[0].append(item)
    
    print("Frequent itemsets of size 1")        
    for eachitem in freq_item[0]:
        print(eachitem)
    cand_items=[]
    k=0
    
    '''........................the main part starts here .......................'''
    
    while('true'):
        freq_item.append([])
        cand_items.append([])
        table=[0 for x in range(int(files[3]))]  
        
        for basket in basket_items:
            for item in list(itertools.combinations(basket,k+2)):
                item=sorted(item)
                value=''
                for i in range(len(item)):
                    value+=str(indexed[item[i]])
                value=int(value)
                table[hashing(value)]+=1
        
               
        bitmap=[0]*int(files[3])
        for i,bucket_size in enumerate(table):
            if bucket_size>=int(files[2]):
                bitmap[i]=1
        
        
        for item in list(itertools.combinations(freq_item[0],k+2)):
            if (k+2)==2:
                item=sorted(item)
                value=''
                for i in range(len(item)):
                    value+=str(indexed[item[i]])
                value=int(value)
                bucket=hashing(value)
                if bitmap[bucket]==1:
                    cand_items[k].append(item)
                else:
                    continue
                
            else:
                count=0
                item=sorted(item)
                value=''
                for i in range(len(item)):
                    value+=str(indexed[item[i]])
                value=int(value)
                bucket=hashing(value)
                for items in list(itertools.combinations(item,k+1)):
                    items=sorted(items)
                    if items in freq_item[k]:
                        count+=1
                if count==(k+2) and bitmap[bucket]==1:           
                    item=sorted(item)
                    cand_items[k].append(item)
                
        
        
        count=[0]*len(cand_items[k])
        for basket in basket_items:
            for index,each_item in enumerate(cand_items[k]):
                if [i for i in each_item for b_item in basket if i==b_item]==list(each_item):
                    count[index]+=1
        for i in range(len(count)):
            if count[i]>=int(files[2]):
                freq_item[k+1].append(cand_items[k][i])
        
        if not freq_item[k+1]:
            break
        else:
            print("\nFrequent itemsets of size %d"%(k+2))
            for eachitem in freq_item[k+1]:
                out=''
                eachitem=list(eachitem)
                for item in eachitem:
                    out+=''.join(item)+','
                out=out.rstrip(',')
                print(out)
        k+=1
        
        
apriori()