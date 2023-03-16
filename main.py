from sui_actions import SUI
import time
extension_path = "Sui-Wallet.crx"

while True:
    try:
        sui = SUI(extension_path)
        sui.connect_sui()
        try:
            sui.action_home()
        except:
            pass
        try:
            sui.action_capy()
        except:
            pass
        try:
            sui.action_2048()
        except:
            pass
        # try:
        #     sui.action_keepsake()
        # except:
        #     pass

        # try:
        #     sui.action_dns()
        # except:
        #     pass

        sui.driver.switch_to.window(sui.windows['home'])
        time.sleep(1)
        sui.driver.quit()
    except:
        sui.driver.quit()
        pass
