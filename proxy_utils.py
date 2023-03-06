def get_proxy_passwords(file_path):
    proxy_passwords = []

    with open(file_path, 'r') as f:
        for line in f:
            proxy_password = line.strip().split(':')[-1]
            proxy_passwords.append(proxy_password)

    return proxy_passwords
