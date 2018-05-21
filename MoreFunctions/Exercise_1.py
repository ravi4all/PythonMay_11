products = [
    {'id':101,'name':'Apple','price':45000,'color':'white'},
    {'id':102,'name':'Redmi','price':13000,'color':'silver'},
    {'id':103,'name':'Vivo','price':22000,'color':'white'},
    {'id':104,'name':'Oppo','price':20000,'color':'grey'},
    {'id':105,'name':'Apple','price':55000,'color':'silver'},
    {'id':106,'name':'Vivo','price':25000,'color':'white'},
    {'id':107,'name':'Redmi','price':12000,'color':'black'},
    {'id':108,'name':'Redmi','price':8000,'color':'black'},
    {'id':109,'name':'Apple','price':67000,'color':'silver'},
    {'id':110,'name':'Samsung','price':58000,'color':'white'},
]

# for data in products:
#     if data['name'] == 'Apple':
#         print(data)

# def search(d):
#     return d['name'] == 'Apple'

# data = list(filter(search, products))

data = list(filter(lambda d : d['name'] == 'Apple', products))
print(data)