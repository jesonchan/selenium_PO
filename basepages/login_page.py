# coding=utf-8

from util.AutoDriver import AutomateDriver


class Wework():

    def __init__(self):
        self.auto_driver = AutomateDriver()
        self.driver = self.auto_driver.driver

    def login(self):

        url = 'https://work.weixin.qq.com/wework_admin/frame#index'
        self.auto_driver.get_url(url)
        self.driver.implicitly_wait(3)
        cookies = {
            "wwrtx.vst": "dNm9h1k0PyAHkbC4fUzArjUNg92aXNQ8DEMSNBWV6yc3ndCdeXJO4omH99D0xTU180O-1e1OfSkquVBaO9NYV9ZoveFiMR8MTQOD6To9GoSOkQXgO9QRwDFxjU_DLCgFgJhp5J4FphXNjjztuKUwD4Ohb_bM-oSUcqxiemuyewvHNRK9Eh6js5BjMP7aA9ynv6I3FsuKYr-_t6EtUcH8AiuXDHbeMzEt771CFiumfVBcFqV1TQA6WYGER16Q3heuhfeH-9NsVB96I4Hi3lO_qQ",
            "wwrtx.d2st": "a2390613",
            "wwrtx.sid": "mEHSrWzFcwUIBEwFY4fOX38zQI7DUqCAF-5TuV-NAkMovgI7sfSwBO7cqTnMSGRY",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324943079315",
            "wxpay.vid": "1688850588901896",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.auto_driver.get_url(url)

if __name__ == '__main__':
    we = Wework()
    we.login()

