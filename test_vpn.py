import requests
import random
import os
import time

current_dir = os.getcwd()
linux_countries = ['al', 'ar', 'au', 'at', 'br', 'bg', 'ca', 'cl', 'cr', 'hr', 'cy', 'cz', 'dk', 'ee', 'fi',
                   'fr', 'ge', 'de', 'gr', 'hk', 'hu', 'is', 'in', 'id', 'ie', 'il', 'it', 'jp', 'lv', 'lu', 'my',
                   'mx', 'md', 'nl', 'nz', 'mk', 'no', 'pl', 'pt', 'ro', 'rs', 'sg', '', 'si', 'za', 'kr', 'es',
                   'se', 'ch', 'tw', 'th', 'tr', 'ua', 'So', 'uk', 'us']
windows_countries = ['United States', 'Canada', 'Argentina', 'Brazil', 'Mexico', 'Costa Rica', 'Chile',
                     'United Kingdom', 'Germany', 'France', 'Netherlands', 'Sweden', 'Switzerland',
                     'Denmark', 'Poland', 'Italy', 'Spain', 'Norway', 'Belgium', 'Ireland', 'Czech Republic',
                     'Austria', 'Portugal', 'Finland', 'Ukraine', 'Romania', 'Serbia', 'Hungary', 'Luxembourg',
                     'Slovakia', 'Bulgaria', 'Latvia', 'Greece', 'Iceland', 'Estonia', 'Albania', 'Croatia',
                     'Cyprus', 'Slovenia', 'Moldova', 'Bosnia and Herzegovina', 'Georgia', 'North Macedonia',
                     'Turkey', 'South Africa', 'India', 'Israel', 'Turkey', 'United Arab Emirates', 'Australia',
                     'Taiwan', 'Singapore', 'Japan', 'Hong Kong', 'New Zealand', 'Malaysia', 'Vietnam', 'Indonesia',
                     'South Korea', 'Thailand']

def nordvpn():
    os.chdir(r"C:\Program Files\NordVPN")
    server = "nordvpn -c -g \'"+random.choice(windows_countries)+"\'"
    print(server)
    os.system(server)
    time.sleep(2)
    os.system(current_dir)

ip = requests.get('https://api.ipify.org').text
print(f"\nBefore Using NordVpn\nIp:\t{ip}")
nordvpn()
ip = requests.get('https://api.ipify.org').text
print(f"\nBefore Using NordVpn\nIp:\t{ip}")