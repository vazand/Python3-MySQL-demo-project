import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", username="username", password="password", database="mobileshop"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mobileshop")
# mycursor.execute("SHOW DATABASES")
# print(mydb)

try:
    mycursor.execute("CREATE TABLE MobileProducts(id INT AUTO_INCREMENT PRIMARY KEY,mobilename VARCHAR(30), price INT(6))")
except :
    print("===> Table exists <===")

def showAllProducts():
    print("Showing List of Mobiles")
    mycursor.execute("SELECT * FROM MobileProducts")
    all_products = mycursor.fetchall()
    for details in all_products:
        print(details)

def addProduct(mobilename, price):
    sql = "INSERT INTO `MobileProducts` (mobilename,price) VALUES(%s,%s)"
    values = (mobilename, price)
    try:
        mycursor.execute(sql, values)
        mydb.commit()
        print("\n*** "+mobilename + " added ***\n")
    except:
        print("\n----> Price must be a Number <---\n")    

def updateProduct(id):
    try:
        if type(int(id)) == int:
            try:
                mobilename = input("Enter New Mobile Name : ")
                price = input("Enter NEW Mobile Price: ")
                sql = "UPDATE `MobileProducts` SET mobilename = %s,  price = %s WHERE id = %s ;"
                values = (mobilename, price, id)
                mycursor.execute(sql, values)
                mydb.commit()
                print("\n +++ Product %s updated +++\n"%mobilename)
            except:
                print("\n----> Failed to update! reason => Price must be a Number <---\n")    
    except:
        print("---> Failed to update! reason => ID must be a Number <---")

def deleteProduct(mobile_id_num):
    sql = "DELETE FROM `MobileProducts`  WHERE id = %s ;"
    try:
        mycursor.execute(sql, (mobile_id_num,))
        mydb.commit()
        print("\n --- Product %s Deleted --- \n "%mobile_id_num)
    except:
        print("----> NO Data Found id = %s <----"%mobile_id_num)

def showSingleProduct(mobile_id):
    sql = "SELECT * FROM MobileProducts WHERE id = %s;"
    try:
        mycursor.execute(sql, (mobile_id,))
        one_product = mycursor.fetchone()
        print(one_product)
        print("\n\n")
        no_inp = input("press any to continue...")
    except:
        print("----> NO Data Found id = %s <----"%mobile_id)


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
