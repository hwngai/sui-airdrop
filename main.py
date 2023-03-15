from proxy_utils import get_proxy_passwords
from sui_actions import SUI
from sui_account import add_sui_account
LIST_PROXY_PASS = get_proxy_passwords('proxy_file.txt')
LIST_PROXY_PASS = LIST_PROXY_PASS[:]
extension_path = "Sui-Wallet.crx"

while True:
    try:
        sui = SUI(extension_path)
        sui.connect_sui()
        sui.action_sui()
    except:
        add_sui_account(sui.wallet_address, sui.recovery_phrase, sui.password, "sui_accounts.json")
        sui.driver.quit()
        pass
