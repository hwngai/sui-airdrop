from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import pyperclip
from seleniumwire import webdriver
from sui_account import add_sui_account
from Generate_password import generate_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class SUI:
    def __init__(self, extension_path, PROXY_PASS):
        self.RECOVERY_PHRASE = ""
        self.PROXY_HOST = "nft.bullproxies.com"
        self.PROXY_PORT = "12323"
        self.PROXY_USERNAME = "PXY_2QSpZEOD"
        self.PROXY_PASS = PROXY_PASS
        self.wallet_address = ""
        self.windows = {}
        self.password = generate_password(15)


        self.seleniumwire_options = {
            'proxy': {
                'https': f'https://{self.PROXY_USERNAME}:{self.PROXY_PASS}@{self.PROXY_HOST}:{self.PROXY_PORT}'
            }
        }

        self.extension_path = extension_path
        self.options = Options()
        self.options.add_argument('--proxy-server=%s:%s' % (self.PROXY_HOST, self.PROXY_PORT))
        self.options.add_argument('--disable-gpu')
       # self.options.add_argument('--headless')
        self.options.add_argument("--window-size=1280,720")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_extension(self.extension_path)


        self.driver = webdriver.Chrome(seleniumwire_options=self.seleniumwire_options, options=self.options)
        self.wait = WebDriverWait(self.driver, 30, 1)

    def connect_sui(self):
        self.wait.until(lambda driver: len(driver.window_handles) >= 2)
        self.wait.until(EC.number_of_windows_to_be(2))
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])

        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div/div/div[2]'))).click()  # Get Started
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[1]/a'))).click() # Create a New Wallet

        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/form/div/fieldset/label[1]/div[2]/input'))).send_keys(self.password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/form/div/fieldset/label[2]/div[2]/input'))).send_keys(self.password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/form/div/fieldset/label[3]/span'))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/form/button'))).click()
        self.recovery_phrase = self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[3]/div/div[3]'))).text
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[3]/div/div[7]/label/span'))).click() # ô vuông



        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[3]/button'))).click() # click open Sui
        self.driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/button').click() # coppy địa chỉ ví
        self.driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/button').click() # coppy địa chỉ ví
        self.wallet_address = pyperclip.paste()
        handles = self.driver.window_handles
        self.windows['home'] = handles[-1]



    def action_sui(self):
        self.wait.until(lambda driver: len(driver.window_handles) >= 2)
        self.wait.until(EC.number_of_windows_to_be(2))
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[3]/button'))).click() # Request Devnet SUI Tokens

        self.driver.execute_script("window.open('{}', '_blank');".format(f"https://capy.art/collection"))
        handles = self.driver.window_handles
        current_handle = handles[-1]
        self.windows['capy'] = current_handle

        self.driver.execute_script("window.open('{}', '_blank');".format(f"https://ethoswallet.github.io/2048-demo/"))
        handles = self.driver.window_handles
        current_handle = handles[-1]
        self.windows['2048'] = current_handle

        self.driver.switch_to.window(self.windows['home'])

        time.sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/nav/div[2]/a[3]'))).click() # Apps
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div/section/div/div[1]/button'))).click() # Mint an NFT
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/nav/div[2]/a[1]'))).click() # Home
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/a'))).click() # Stake & Earn SUI
        random_number = random.randint(1, 4)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/div/div/div[2]/div[{random_number}]/div/div'))).click()
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/div/div[2]'))).click() # Select Amount
            # input Amount 0.01-0.04
        Amount = round(random.uniform(0.01, 0.035), 2)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/div/div[1]/form/div[2]/div[1]/div/input'))).send_keys(Amount) # Select a Validator
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/div/div[2]/button'))).click() # Stake Now
        time.sleep(6)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/button'))).click() # tick ok
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/button'))).click() # tick out

        self.driver.switch_to.window(self.windows['capy'])

        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="mainNavbar"]/div[2]/div/button'))).click() # Connect Your Wallet
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div[2]/div/div/div[1]/button'))).click()  # sui wallet

        self.wait.until(EC.number_of_windows_to_be(5))
        handles = self.driver.window_handles
        current_handle = handles[-1]
        self.driver.switch_to.window(current_handle)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]'))).click()  # connect
        time.sleep(1)

        self.driver.switch_to.window(self.windows['capy'])
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="app"]/div/main/div/div/div/div[2]/div/div[1]/p'))).click()
        self.wait.until(EC.number_of_windows_to_be(5))
        handles = self.driver.window_handles
        current_handle = handles[-1]
        self.driver.switch_to.window(current_handle)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]'))).click()  # connect
        time.sleep(1)

        self.driver.switch_to.window(self.windows['2048'])
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="ethos-start"]/button'))).click() # get started
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="ethos-close-on-click"]/div/div[2]/div[2]/div/button'))).click() # connect sui

        self.wait.until(EC.number_of_windows_to_be(5))
        handles = self.driver.window_handles
        current_handle = handles[-1]
        self.driver.switch_to.window(current_handle)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]'))).click()  # connect


        self.driver.switch_to.window(self.windows['2048'])
        actions = ActionChains(self.driver)
        keys = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]
        for i in range(15):
            key = random.choice(keys)
            time.sleep(1)
            actions.send_keys(key).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="claim-button"]'))).click()  # claim

        self.wait.until(EC.number_of_windows_to_be(5))
        handles = self.driver.window_handles
        current_handle = handles[-1]
        self.driver.switch_to.window(current_handle)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div/div[2]/main/div/div[2]/div/button[2]'))).click()  # connect

        self.driver.switch_to.window(self.windows['home'])
        add_sui_account(self.wallet_address, self.recovery_phrase, self.password, "sui_accounts.json")

        self.driver.quit()






