class Honda :
     
	# constructor
	def __init__(self, modelName ,price, seatingCapacity, color):
		self.modelName = modelName
		self.price = price
		self.seatingCapacity = seatingCapacity
		self.color = color

manager = print ("Hello Sir, How can I help you? \n which car you are interested in?\n we are available with the following cars. ")
car1 = 'Honda'
car2 = 'Toyota'
car3 = 'BMW'
car4 = 'Suzuki'
name_of_the_car = print(car1, car2, car3,car4 )
client = input()

        


# list of car objects
Hondalist = [Honda('Honda All New City',1190000 ,5, 'Radient Red Metallic'),
			Honda('WR-V', 1068000, 4,'golden Metallic'),
			Honda('Jazz', 945000, 5,'brown Metallic'),
            Honda('Honda City' ,1116000, 7,'lunar Red Metallic'),
            Honda('Honda Amaze' ,813000, 7,'metolloid grey Red Metallic')]


if client == car1:
	print ("please let us know the bugget of your car ")
	customerbudget =  int(input())
	print(customerbudget)

	models_list =[]
	for  each_Hondacar in Hondalist:
		if customerbudget > each_Hondacar.price:
			print(each_Hondacar.modelName, each_Hondacar.price)
			models_list.append(each_Hondacar.modelName)
        
	print("Please select any of these models") 
	print(models_list)
	model_name = input()
 
 
	colors_d = {'WR-V':['golden', 'red'], 'Jazz': ['green', 'blue'], 'Honda Amaze': ['yellow', 'white']}
	for each_models in models_list:
		if model_name == each_models:
			print("This is the model", model_name)
			print("Please choose color")
			for key, value in colors_d.items():
				if key == model_name:
					print("Available colors", value)
					cust_color = input()
					print("Thank you. Available")
     

			
    
#         manager2=print("please enter the seating capacity prefered")
#         seatingcapacity =int(input())
#         print(seatingcapacity)
    
  																														
# for seater in carsList:
     
#     if seatingcapacity == seater.seatingCapacity:
#         print(seater.company, seater.seatingCapacity)
        
        
# client_choice = input()
# print (client_choice )
# if client_choice == car1 :
#  print( "Thank You sir,This is the most tranding car in 2023.\n Different models available in Honda are")
# list=['Honda Amaze', 'jazz']

        
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["maroon"])
# print("Honda is available in :")
# print(color_list_1)
# print(color_list_2)
# print("\nToyato and Chevrolet in:")
# print(color_list_1.difference(color_list_2))
# print("\nFord is present only in:")
# print(color_list_2.difference(color_list_1))


        
      
 

     
   
    



 
 






    
    
    
    
    



