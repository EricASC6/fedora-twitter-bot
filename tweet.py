from TwitterBot import TwitterBot
from configs import configs


def main():
    global driver
    bot = TwitterBot(configs["username"], configs["password"])
    driver = bot.driver
    latest_link = bot.get_latest_article_link()
    bot.save_article_url_to_file(latest_link)
    bot.login_twitter()
    bot.tweet(latest_link)


if __name__ == "__main__":
    main()
