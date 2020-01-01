from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.magazine_url = "https://fedoramagazine.org/"
        self.twitter_url = "https://twitter.com/?logout=1577830181066"
        self.latest_article_file = "./latest_article.txt"

    def get_latest_article_link(self):
        self.driver.get(self.magazine_url)
        latest = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".post")))
        link = latest.find_element_by_css_selector(
            ".post-image").find_element_by_tag_name("a").get_attribute("href")
        return link

    def save_article_url_to_file(self, article_url):
        with open(self.latest_article_file, "w") as latest:
            latest.write(article_url)

    def login_twitter(self):
        self.driver.get(self.twitter_url)
        login_btn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/login']")))
        login_btn.click()
        username = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-username-field")))
        username.clear()
        username.send_keys(self.username)
        password = self.driver.find_element_by_css_selector(
            ".js-password-field")
        password.clear()
        password.send_keys(self.password)
        login_submit = self.driver.find_elements_by_css_selector(
            ".submit")[1]
        login_submit.click()

    def tweet(self, message):
        tweet_area = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".public-DraftStyleDefault-ltr")))
        tweet_area.send_keys(message)
        tweet_btn = self.driver.execute_script("let spans = document.querySelectorAll('span');" +
                                               "for (let span of spans) {" +
                                               "if (span.innerText === 'Tweet') return span;" +
                                               "};"
                                               )
        tweet_btn.click()

    def is_new_article(self, link):
        with open(self.latest_article_file) as last_recent:
            last_link = last_recent.read()
            if last_link != link:
                return True
            else:
                return False
