#lets do exercise 4 in python

class Product:
    def __init__(self, ProductID, ProductName, Price): #Constructor
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.Price = Price
        
    def __str__(self): #this function for printing object
        return(f' {self.ProductID} -- {self.ProductName} -- {self.Price}')
    
    
    
class ShoppingCart:
    
    def __init__(self):#Constructor
        self.ProductList=[]
    
    def AddProduct(self,product):
        self.ProductList.append(product)
        
    def RemoveProduct(self,productID):
        for x in self.ProductList:
            if (x.ProductID ==productID):
                self.ProductList.remove(x)
        
    def ListProducts(self):
        for x in self.ProductList:
            print(x)
            
         
#create shopping cart object   
cart = ShoppingCart()
#Ading product tpo the cart
cart.AddProduct(Product(1,"Name1",2,3))
cart.AddProduct(Product(2,"Name2",3,3))
cart.AddProduct(Product(3,"Name3",4,3))
print('after adding')
#Print all products in cart
cart.ListProducts()
#Remove all products with ID 1
cart.RemoveProduct(1)
#Print all products in cart
print('after removing')
cart.ListProducts()