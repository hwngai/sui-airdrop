from proxy_utils import get_proxy_passwords
from sui_actions import SUI
LIST_PROXY_PASS = get_proxy_passwords('proxy_file.txt')
extension_path = "Sui-Wallet.crx"

def run_sui(proxy_pass):
    sui = SUI(extension_path, proxy_pass)
    try:
        sui.connect_sui()
        sui.action_sui()
    except:
        sui.driver.quit()

for proxy_pass in LIST_PROXY_PASS[2:10]:
    run_sui(proxy_pass)



#
# index = 0
# while True:
#     proxy_pass = LIST_PROXY_PASS[index]
#     sui = SUI(extension_path, proxy_pass)
#     sui.connect_sui()
#     sui.action_sui()
#     index = (index + 1) % len(LIST_PROXY_PASS)
