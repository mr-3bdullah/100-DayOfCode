# wellcom
# this is finall project.

print("wellcom to the Tip calculator 👋")


bill_price = int(input("what is the Total bill: "))

Tib = int(input("how much tip would ypu like to give? |-> 10, 12, 15 <-| : "))

tip_per = Tib / 100

pep_split = int(input("how many pepole split the bill? : "))

tt = bill_price * tip_per

res = (bill_price + tt) / pep_split

print(f"{res:.2f}")
