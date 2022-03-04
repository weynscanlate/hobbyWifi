import subprocess


def wifi_password():
    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]

    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile {profile} key=clear').decode('CP866').split(
            '\n')

        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i][0]
        except IndexError:
            password = None

        with open(file='wifi_password.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Профиль: {profile}\nПароль: {password}\n{"_" * 40}\n')


def main():
    wifi_password()


if __name__ == '__main__':
    main()
