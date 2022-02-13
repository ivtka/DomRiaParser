import time
from domria import DomRia


def main():
    with DomRia() as bot:
        bot.load_page()
        city = input("What city you want to choose? ")
        bot.select_city(city)
        bot.select_state(input(f'What state of {city} you want to choose? '))
        bot.select_price(start_price=int(
            input("What is start price? ")), end_price=int(input("What is end price? ")))
        bot.refresh()
        bot.report()


if __name__ == "__main__":
    main()
