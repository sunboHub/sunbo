import requests



def dan():
    url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    data = {'from': 'en',
            'to': 'zh',
            'query': 'dog',
            'transtype': 'translang',
            'simple_means_flag': '3',
            'sign': '871501.634748',
            'token': '403b8fd62a4da138741fbc6ac476f228'}

    headers = {'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length': '121',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie': 'BIDUPSID=0F1FDF9F4DD415972F301652F3256D3F; PSTM=1579488836; BAIDUID=0F1FDF9F4DD415976CB0CD9ECDADDA49:FG=1; delPer=0; BDRCVFR[QxxZVyx49rf]=I67x6TjHwwYf0; PSINO=1; H_PS_PSSID=1450_21105_30473_30481; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1579488860; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1579488860; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; __yjsv5_shitong=1.0_7_3b44b834f614bad3a380feb68cce2a559e5d_300_1579488862534_223.90.150.117_20bfc01c; yjs_js_security_passport=cd8ea62cfda78a0e2e92ac8e300697d00a7d1c56_1579488863_js; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
                'Host': 'fanyi.baidu.com',
                'Origin': 'https://fanyi.baidu.com',
                'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'}
    result = requests.post(url,data=data,headers=headers)
    result.encoding = result.apparent_encoding
    result = result.text
    return result




# dan()
a = dan()
print(a)