from database import Session
from Models import Restaurant, Customer, Review

session = Session()

restaurant1 = Restaurant(name='McDonalds', price=1)
restaurant2 = Restaurant(name='Burger King', price=2)
restaurant3 = Restaurant(name='Wendys', price=3)

customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

review1 = Review(star_rating=3, restaurant=restaurant1, customer=customer1)
review2 = Review(star_rating=4, restaurant=restaurant2, customer=customer1)
review3 = Review(star_rating=5, restaurant=restaurant3, customer=customer2)

session.add_all
