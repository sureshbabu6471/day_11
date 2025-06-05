import datetime
user_name=input("enter the User name :")
Qty=int(input("How many mobile you want : "))
cost=80000
amount=cost*Qty
cgst=1.5/100
sgst=1.5/100
amount_cgst=amount*cgst
amount_sgst=amount*sgst
total_amount=amount+amount_cgst+amount_sgst
Discount_amount=total_amount*15/100
if Qty==2:
    discout=amount*10/100
elif Qty<=5:
    discount=amount*15/100
elif Qty<=10:
    Discount=amount*17/100
elif Qty<=15:
    Discount=amount*23/100
elif Qty>15:
    Discount=amount*25/100

print("\n\n")
print("\t  SURI & MOBILE pvt ltd")
print("  CF10-19, sector1, MPL, AP-700064")
print("\t    ph : 9573607XXX")
print("\t GST IN NO:XXXXXXXXXXXXXXX")
print("\t      BILL")
print("------------------------------------------------------")
print("   Memo# 17/41840\t ",datetime.datetime.now())
print("   User : {}\t\t\tPax# 1".format(user_name))
print("\t\t  Order# 1")
print("------------------------------------------------------")
print("Product\t\t\tQty\t Rate\tAmount")
print("------------------------------------------------------")
print(" mobile\t\t\t{}\t {}\t{}".format(Qty,cost,amount))
print("-------------------------------------------------------")
print("Sub Total \t\t\t\t{}".format(amount))
print("C Gst @ 1.5%\t\t\t\t",amount_cgst)
print("S Gst @ 1.5%\t\t\t\t",amount_sgst)
print("Discount @15%\t\t\t\t",-Discount_amount)
print("------------------------------------------------------")
print("Total\t Qty : {}\t\tAmt\t{} \n".format(Qty,total_amount-Discount_amount))
print("Thank You , Please Visit again")