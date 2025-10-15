Rice_price = 45
Sugar_price = 40
Oil_price = 130

Rice_qty = 3
Sugar_qty = 2.5
Oil_qty = 1.8

Rice_total = Rice_price * Rice_qty
Sugar_total = Sugar_price * Sugar_qty
Oil_total = Oil_price * Oil_qty


final_total = Rice_total + Sugar_total + Oil_total
print ("final_total:", final_total)

final_total_int = int(final_total)
print ("final_total(integer form):",final_total_int)

final_total_str = str(final_total)
print ("the final bill is " + final_total_str + " rupees.")

import random
delivery_charge = random.randint(5,10)
final_total_with_delivery_charge = final_total + delivery_charge
print ("final total after adding delivery charge:", final_total_with_delivery_charge,"rupees.")