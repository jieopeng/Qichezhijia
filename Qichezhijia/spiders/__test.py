import requests

headers = {
    "Host": "k.autohome.com.cn",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "fvlid=1556498692909INDnQoK3C0; sessionid=53754248-0D23-42DD-A705-0D21534DAC5E%7C%7C2019-04-29+08%3A44%3A46.172%7C%7Cwww.baidu.com; autoid=ce24565735b101a70e6b5fc345c0bb8a; area=440104; ahpau=1; sessionuid=53754248-0D23-42DD-A705-0D21534DAC5E%7C%7C2019-04-29+08%3A44%3A46.172%7C%7Cwww.baidu.com; ASP.NET_SessionId=piopkyfyny33wttsgduf2mc1; guidance=true; sessionip=121.33.144.124; sessionvid=3198BE2C-A413-4507-84DD-622F0C52C373; __ah_uuid_ng=u_5012658; _fmdata=4Hm5EKSxMXE5X1BsTRHfhRQG6zq1YIvVi4t24PzThZaEYQVB%2FSQRkzeVUY4X5B7zOwJmoXcca9kBT1HRs6AI4XruSIbE0AjA%2FcV%2FXfIrqXg%3D; ref=www.baidu.com%7C0%7C0%7C0%7C2019-04-29+21%3A28%3A57.784%7C2019-04-29+08%3A44%3A46.172; ahpvno=38; ahrlid=1556544534497yTTcqjYVw6-1556545077582; autoac=77CA758C663D450D803F151CC1EA8078",

}
url = "https://k.autohome.com.cn/4887/"
res = requests.get(url, headers=headers)
with open("__test.html", "w", encoding="utf-8")as f:
    f.write(res.text)
