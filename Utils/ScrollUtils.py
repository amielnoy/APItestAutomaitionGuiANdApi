import time


class Scroling:
    @staticmethod
    def scroll_page(page, x, y) -> None:
        page.mouse.wheel(x, y)

    @staticmethod
    def scroll_page_down(page):
        for i in range(5):  # make the range as long as needed
            page.mouse.wheel(0, 15000)
            time.sleep(2)
