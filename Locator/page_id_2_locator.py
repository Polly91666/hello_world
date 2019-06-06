from selenium.webdriver.common.by import By


class Page_id_2_Locator:
    # 用于 等待页面是否打开的定位
    page_open = (By.XPATH,'//div[@class="area_size"]//button[1]')  # /html/body/div[1]/div[1]/button[1]
