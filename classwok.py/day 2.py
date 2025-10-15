Header = "ABC Bookstore"
Customer_receipt = "Customer Receipt"

Book1_title = "Python basics"
Book1_price = 450

Book2_title = "Data science Intro"
Book2_price = 600

Line1 = "Book Title: {}\t Price: Rs {}".format(Book1_title,Book1_price)
Line2 = "Book Title: {}\t Price: Rs {}".format(Book2_title,Book2_price)
 

Total_price = Book1_price + Book2_price
Total_Line  = "Total Price:\t Rs {}".format(Total_price)

Thank_you = "\n\tThank you for shopping with us!"
receipt = Header + "\n" + Customer_receipt + "\n\n" + Line1 + "\n" + Line2 + "\n" + Total_Line + Thank_you

print(receipt.upper())
