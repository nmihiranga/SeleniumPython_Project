from booking.booking import Booking

# calling functions
with Booking() as bot:
    bot.land_first_page()
    bot.select_place_to_go('colombo')
    bot.select_date('2024-05-10', '2024-05-12')
    bot.select_people(4, 2)
    bot.click_search()
    bot.apply_filterations()