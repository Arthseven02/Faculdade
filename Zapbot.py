from selenium import webdriver
import time


class WhatsappBot:
    def __init__(self):
        # mensagem que você quer enviar
        self.mensagem = "Video teste projeto  https://www.youtube.com/watch?v=xiTev1s2UX0 "
        # Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos = ["TOCA DO HAMBURGUER","Projeto"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(
            executable_path=r'./chromedriver.exe', chrome_options=options)

    def EnviarMensagens(self):
        self.driver.get('https://web.whatsapp.com')
        time.sleep(15)
        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_class_name('_3uMse')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)


bot = WhatsappBot()
bot.EnviarMensagens()


#<span dir="auto" title="TOCA DO HAMBURGUER" class="_3ko75 _5h6Y_ _3Whw5">TOCA DO HAMBURGUER</span>
#<div tabindex="-1" class="_3uMse"><div tabindex="-1" class="_2FVVk _2UL8j">
#<span data-testid="send" data-icon="send" class="">