import os
import requests
import random
import time



windows_countries = ['United States', 'Canada', 'Argentina', 'Brazil', 'Mexico', 'Costa Rica', 'Chile',
                     'United Kingdom', 'Germany', 'France', 'Netherlands', 'Sweden', 'Switzerland',
                     'Denmark', 'Poland', 'Italy', 'Spain', 'Norway', 'Belgium', 'Ireland', 'Czech Republic',
                     'Austria', 'Portugal', 'Finland', 'Ukraine', 'Romania', 'Serbia', 'Hungary', 'Luxembourg',
                     'Slovakia', 'Bulgaria', 'Latvia', 'Greece', 'Iceland', 'Estonia', 'Albania', 'Croatia',
                     'Cyprus', 'Slovenia', 'Moldova', 'Bosnia and Herzegovina', 'Georgia', 'North Macedonia',
                     'Turkey', 'South Africa', 'India', 'Israel', 'Turkey', 'United Arab Emirates', 'Australia',
                     'Taiwan', 'Singapore', 'Japan', 'Hong Kong', 'New Zealand', 'Malaysia', 'Vietnam', 'Indonesia',
                     'South Korea', 'Thailand']

def connect_to_vpn():
    current_dir = r'C:\Users\satom\Desktop\sui-airdrop'
    os.chdir(r"C:\Program Files\NordVPN")
    server = "nordvpn -c -g \'"+random.choice(windows_countries)+"\'"
    os.system(server)
    print(server)
    time.sleep(5)
    os.chdir(current_dir)

ip = requests.get('https://api.ipify.org').text
print(f"\nBefore Using NordVpn\nIp:\t{ip}")

connect_to_vpn()

ip = requests.get('https://api.ipify.org').text
print(f"\nAfter Using NordVpn\nIp:\t{ip}")
