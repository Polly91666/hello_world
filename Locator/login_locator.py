from selenium.webdriver.common.by import By


class LoginLocator:

    # 登录页的用户名定位
    loc_login = (By.XPATH,'//*[@id="user_id"]')

    loc_id_2 = (By.XPATH, "//*[@id='gallery']/div[1]/p")

