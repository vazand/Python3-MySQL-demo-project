import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", username="username", password="password", database="mobileshop"
)

# mycursor.execute("CREATE DATABASE mobileshop")
# mycursor.execute("SHOW DATABASES")
# print(mydb)

def showTitle():
    mobile_id = "ID_Num"
    mobile_name = "Mobile_Name".center(25)
    mobile_price = "Price".title()
    print("\n" + mobile_id, mobile_name, mobile_price + "\n")


def showAllProducts():
    print("Showing List of Mobiles")
    mycursor.execute("SELECT * FROM MobileProducts")
    all_products = mycursor.fetchall()
    showTitle()
    for details in all_products:
        id = details[0]
        name = details[1].center(30)
        price = details[2]
        print(id, name, price)


def addProduct(mobilename, price):
    sql = "INSERT INTO `MobileProducts` (mobilename,price) VALUES(%s,%s)"
    values = (mobilename, price)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
        print("\n*** " + mobilename + " added ***\n")
    except:
        print("\n----> Price must be a Number <---\n")


def updateProduct(id):
    try:
        if type(int(id)) == int:
            try:
                mobilename = input("Enter New Mobile Name : ")
                price = input("Enter NEW Mobile Price: ")
                values = (mobilename, price, id)
                sql = "UPDATE `MobileProducts` SET mobilename = %s,  price = %s WHERE id = %s ;"
                mycursor.execute(sql, values)
                mydb.commit()
                print(mycursor.rowcount, "record updated")
            except:
                print("\n----> Failed to update! reason => Price must be a Number <---\n")    
    except:
        print("---> Failed to update! reason => ID must be a Number <---")


def deleteProduct(mobile_id_num):
    try:
        if type(int(mobile_id_num)) == int:
            sql = "DELETE FROM `MobileProducts`  WHERE id = %s ;" % mobile_id_num
            try:
                mycursor.execute(sql)
                mydb.commit()
                print(mycursor.rowcount, "record deleted")
            except:
                print("----> NO Data Found id = %s <----" % mobile_id_num)
    except :
        print("---> Failed to delete! reason => ID must be a Number <---")

def showSingleProduct(mobile_id):
    sql = "SELECT * FROM MobileProducts WHERE id = %s;"
    try:
        mycursor.execute(sql, (mobile_id,))
        one_product = mycursor.fetchone()
        showTitle()
        print(one_product[0], one_product[1].center(30), one_product[2])
        print("\n\n")
        no_inp = input("press any to continue...")
    except:
        print("----> NO Data Found id = %s <----" % mobile_id)


mycursor = mydb.cursor()
try:
    mycursor.execute(
        "CREATE TABLE MobileProducts(id INT AUTO_INCREMENT PRIMARY KEY,mobilename VARCHAR(30), price INT(6))"
    )
except:
    print("===> Table exists <===")


while True:
    showAllProducts()
    user_inp = input(
        """
    Enter 'a' to create a product
    Enter 'b' to update a product
    Enter 'd' to delete a product
    Enter 's' to Look selected product
    Enter 'q' to quit the program
    
    """
    )
    if user_inp == "q":
        print("exit \n")
        break
    elif user_inp == "a":
        print("\n a -> Adding a new Mobile \n")
        user_input_mobile_name = input("Mobile Name \n")
        user_input_mobile_price = input("Mobile Price\n")
        addProduct(user_input_mobile_name, user_input_mobile_price)
    elif user_inp == "b":
        print("\n b -> Editing Mobile data \n")
        user_input_mobile_name = input("Enter Mobile ID:")
        updateProduct(user_input_mobile_name)
    elif user_inp == "d":
        print("\n d -> deleting \n")
        user_input_id = input("Enter  Mobile ID: ")
        deleteProduct(user_input_id)
    elif user_inp == "s":
        print("\n Look selected product \n")
        user_input_id = input("Enter a Mobile ID :")
        showSingleProduct(user_input_id)
    else:
        print("Wrong Input, please check your input...!")
    mycursor.close()
    mycursor = mydb.cursor()

