#Define a code called bank which accpets a variable n with a span value
#The code will return the largest series product of n
#For example if the n = 63915 and span is 3, the code will check all possible values in n consisting of 3 which is span
#The possible values in our example are: 639,391,915, then the code will calculate the product of each series and return the highest one
def bank(n,span):


    my_list =[]
    new_list=[]
    series_product =[]
    product =1

#Create a loop to insert series of adjacent digits until the end of the sequence of digits. 
#Note: Some elements in the list will be shorter than length of span
    for i in range(0,len(n),1):
        my_list.append(n[i:i+span:1])

#Create a loop to insert elements from above list to a new list where the length is only equal to span
    for i in my_list:
        if len(i) == span:
            new_list.append(i)
#Create a loop to add the product of digits for each series into the series_product list
    for k in new_list:
        for l in range(0,len(k),1):
            product = product * int(k[l])
        series_product.append(product)
        product =1
    
    return(f"The largest series product of {n} is {max(series_product)}")   

#Call the function with a series of digits and a span number which is 3 in this case
print(bank("63915",3))


