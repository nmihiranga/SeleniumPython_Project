from booking.booking import Booking
from selenium import webdriver



with Booking() as bot:
    bot.land_first_page()
    #bot.change_currency()
    bot.select_place_to_go('colombo')
    bot.select_date('2024-05-10', '2024-05-12')
    bot.select_people()