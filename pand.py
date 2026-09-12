import pandas as pd

store={
    "Product":["noodles","cake","doonote"],
    "quantity":[12, 13,12],
    "price":[100,200,250]
}
s=pd.DataFrame(store)

s["total_price"]=s["quantity"]+s["price"]
s["discount_price"]=s["price"]-10
avg_price=s["price"].mean()
sum_price=s["price"].sum()
mdeian_price=s["price"].median()
min_price=s["price"].min()
max_price=s["price"].max()
print(avg_price)