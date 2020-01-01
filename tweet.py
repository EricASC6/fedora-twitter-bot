from TwitterBot import TwitterBot
from configs import configs


def main():
    try:
        global driver
        bot = TwitterBot(configs["username"], configs["password"])
        driver = bot.driver
        latest_link = bot.get_latest_article_link()
        if bot.is_new_article(latest_link):
            bot.save_article_url_to_file(latest_link)
            bot.login_twitter()
            bot.tweet(latest_link)
            print('\033[92m' + "Successful")
        else:
            print('\033[94m' + "No new articles")
    except:
        print('\033[91m' + "Something went wrong")


if __name__ == "__main__":
    main()
