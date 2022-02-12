import time
from domria import DomRia

def main():
    bot = DomRia()
    bot.load_page()
    bot.select_city(city="Чернівці")
    bot.select_state(state="Шевченківський")
    bot.select_price(10000, 20000)
    time.sleep(5)

if __name__ == "__main__":
    main()
