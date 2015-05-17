# CV_Inventory
Personas:
Marina Valmy is the owner of a beauty school and also has her own product line. She currently has a software application that manages all the daily tasks in the school but does not have any functionality to manage product sales and inventory. Marina is looking to implement a new POS system that will help her keep track of product sales and inventory. This system will also help in the actual sales as it works integrated with the cash register.

Problem Scenarios:
Marina wants to streamline the product sales and the inventory in order to have a more organized system and to know when a product is needed.

Current Alternatives:
If Marina wants to know how many products she has in stock she tells the receptionist to count manually the number of products available. When a customer wants to buy products this sale is done manually there is a need for a calculator and a written receipt. 

Value Proposition:
By implementing a new Point of Sale (POS) system the receptionist will spend less time in the process of selling the product and will be able to improve customer service. It will allow more time to spend in creating a better relationship with the customer and the place will look more organized.
Creating a digitized index, cataloging the location, album, song and artist, Byron could better locate and enjoy a specific music selection making better use of his limited timeframes.

User Stories:
Marina wants to be able to have an up to date inventory, daily sales and revenues. She also wants to be able to have an automated sales system to streamline her sales.

Acceptance Story:
Scenario 1: Adding products
Given that I have a new product
And I would like to add it to the program
When I select the “Add New Product” option
Then I will be asked to enter Product Code, Product Name, Quantity and Price
And the product will be added to the inventory

Scenario 2: Selling Products
Given that I would like automate the product sales
When I select the “Sell Product” option
Then I will be asked to enter product code, and quantity to be sold
And the Quantity will be updated in the inventory
And a message will show total amount to be paid. It will ask for cash paid and will give change amount.  

Scenario 3: View Inventory
Given that I want to keep track of my inventory
When I select “View inventory”
Then I will view total number of product available

Scenario 4: View Daily Sales
Given that I want know my daily sales
When I select “View inventory”
Then I will view total number of items sold

Scenario 5: Updating existing products
Given that more products came in
And I would like to update the quantity of existing products
When I select the “Update Existing Product” option
Then I will be asked to enter Product Code and Quantity 
And the product will be updated in the inventory

Scenario 6: Delete existing products
Given that some products might be discontinued 
And I would like to remove them from the inventory
When I select the “Delete Existing Product” option
Then I will be asked to enter Product Code 
And the product will be deleted from the inventory


