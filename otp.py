from requests import Session

get = Session().get
post = Session().post

url = "https://api16-normal-c-useast1a.tiktokv.com/passport/mobile/get_otp/?next=https%3A%2F%2Ftv.tiktok.com&account_sdk_source=app&passport-sdk-version=17&os_api=25&device_type=ASUS_Z01QD&ssmix=a&manifest_version_code=110908&dpi=240&carrier_region=DE&uoo=0&region=DE&app_name=tiktok_tv&version_name=11.9.8&timezone_offset=3600&ts=1680991802&ab_version=11.9.8&pass-route=1&cpu_support64=true&pass-region=1&storage_type=1&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=110908&_rticket=1680991802661&device_platform=android&iid=7219304446219192070&build_number=11.9.8&locale=de_DE&op_region=DE&version_code=110908&timezone_name=Europe%2FBerlin&cdid=f03bebda-f46d-48ac-a48c-94c3be811ac2&openudid=d8e48a4690fded4b&sys_region=DE&device_id=7191957835704632838&app_language=de&resolution=1280*720&device_brand=Asus&language=de&os_version=7.1.2&aid=4082&okhttp_version=4.0.71.6-tiktok"

headers = {
    "accept-encoding":"gzip",
    "connection":"Keep-Alive",
    "cookie":"store-idc=maliva; store-country-code=de; store-country-code-src=did; install_id=7219304446219192070; ttreq=1$61d3b081ce60c998b44f7b7190d5c3006ef38e90; odin_tt=b3d2f53798a67f4f047cfb9ffc40bcc738db759ef09452d06e0a9b19457ea8cad201edc274985908614eb37b8b6bb980a2d8153f700aefd6de7752b84a0e2e44a28c2cf70c02f91d4602a8551ad49ee9; passport_csrf_token=73325592c16331165e9aa4173fb5a3cd; passport_csrf_token_default=73325592c16331165e9aa4173fb5a3cd; msToken=-FKWjXsLY02ElQb95HnVFhQJnYt1FkV7uTTeZ8q56ALTOWmwPBf2hMqSIdPb4NzB-8gjZ1-NaKy1oGSFCyyrh5bMqGmQVC-m-3LJ1ID3w6yMqEWiK5lewNec",
    "host":"api16-normal-c-useast1a.tiktokv.com",
    "passport-sdk-version":"17",
    "sdk-version":"2",
    "user-agent":"com.tiktok.tv/110908 (Linux; U; Android 7.1.2; de_DE; ASUS_Z01QD; Build/N2G48H;tt-ok/3.10.0.2)",
    "x-gorgon":"040480aa400071b467ddbfce4d8e00fb639ee8273914aaa0ece7",
    "x-khronos":"1680968776",
    "x-ss-req-ticket":"1680968776054",
    "x-tt-passport-csrf-token":"73325592c16331165e9aa4173fb5a3cd",
    "x-tt-store-region":"de",
    "x-tt-store-region-did":"de",
    "x-tt-store-region-src":"did",
    "x-tt-store-region-uid":"",
}


r = get(url, headers=headers).json()
otp = r["data"]["otp"]
print(otp, "https://tv.tiktok.com/activate")
while True:
    url = f"https://api16-normal-c-useast1a.tiktokv.com/passport/mobile/check_otp/?otp={otp}&next=https%3A%2F%2Ftv.tiktok.com&client_secret=SC&account_sdk_source=app&passport-sdk-version=17&os_api=25&device_type=ASUS_Z01QD&ssmix=a&manifest_version_code=110908&dpi=240&carrier_region=DE&uoo=0&region=DE&app_name=tiktok_tv&version_name=11.9.8&timezone_offset=3600&ts=1680992294&ab_version=11.9.8&pass-route=1&cpu_support64=true&pass-region=1&storage_type=1&ac2=wifi&ac=wifi&app_type=normal&host_abi=armeabi-v7a&channel=googleplay&update_version_code=110908&_rticket=1680992294965&device_platform=android&iid=7219304446219192070&build_number=11.9.8&locale=de_DE&op_region=DE&version_code=110908&timezone_name=Europe%2FBerlin&cdid=f03bebda-f46d-48ac-a48c-94c3be811ac2&openudid=d8e48a4690fded4b&sys_region=DE&device_id=7191957835704632838&app_language=de&resolution=1280*720&device_brand=Asus&language=de&os_version=7.1.2&aid=4082&okhttp_version=4.0.71.6-tiktok"
    r = get(url, headers=headers)
    if "session_key" in r.text:
        cookies = str(r.cookies)
        sessionid = cookies.split('sessionid=')[1].split(' ')[0]
        print(sessionid)
        break
input()