# coding=utf-8
import logging
from util.AutoDriver import AutomateDriver

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class Wework:

    def __init__(self):
        self.auto_driver = AutomateDriver()
        self.driver = self.auto_driver.driver

    def open_url(self, url):
        self.auto_driver.get_url(url)
        self.driver.implicitly_wait(3)
        COOKIES = {
            "wwrtx.vst": "-pIKsm0KaZStGR7L-89VjjHxz66MW8p4ByabXtPQr9OqkeeLSI_OY-2_1KEoprNDmrmHtpgiH8xzPadBDoI0NdFNieSvcd5L50PbmUmU3YZ6li5tYhECf_RWcjbStvF23DHwrNSBniCDlYZbzOrmMYd3ZHD9y3_Yr8iY8jPt2e_Nll8BTj7Sxnw125k-mpwlSv4StuZcmucsxhu3fBmJMOms8VTu4fs4COKV0f5MpY4ANwimFF_S_iSGxWuvvNZI59Xl_i6e4VIZJYCufoyH-Q",
            "wwrtx.d2st": "a4407312",
            "wwrtx.sid": "mEHSrWzFcwUIBEwFY4fOX52hkatJK8is8otOujnDdQEZiqFKIpTUx8luTpTPuGuL",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324943079315",
            "wxpay.vid": "1688850588901896",
            "wwrtx.vid": "1688850588901896",
            "wwrtx.i18n_lan_key": "zh-CN%2Czh%3Bq%3D0.9%2Cen%3Bq%3D0.8",
            "wwrtx.i18n_lan": "zh-CN",
            "wwrtx.ref": "direct",
            "wwrtx.refid": "581665207310925",
            "wwrtx.logined": "true",
        }
        for k, v in COOKIES.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.auto_driver.get_url(url)

    def login(self):
        URL = 'https://work.weixin.qq.com/wework_admin/frame#index'
        self.open_url(URL)


if __name__ == '__main__':
    we = Wework()
    we.login()
