from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class YLH:
  def __init__(self, username, password):
          self. username = username
          self.password = password
          self.options = Options()
          self.options.add_argument("--lang=en")
          self.bot_ylh = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options = self.options)

  def open_link(self):
        bot_ylh = self.bot__ylh
        bot_ylh.get("https://www.youlikehits.com/login.php")


testBOT = YLH('smalllion', '9spdtjCEN9frL.T')
testBOT.open()