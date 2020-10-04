""" Bot para WhatsApp utilizando Programação Orientada à Objetos no navegador Firefox
"""

# É necessário instalar as bibliotecas a seguir:
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
import time
import keyboard


class WhatsAppBot:

    def __init__(self):

        self.pessoas = ['Duardokkkkk']
        self.mensagem = 'Olá mundo, sou um botzinho que está aprendendo a digitar sozinho'
        op = options
        op.page_load_strategy = 'eager'  # Carrega o essencial da pagina para melhorar a performance do algoritmo.
        self.driver = Chrome(executable_path=r'./chromedriver.exe')

    def enviar_mensagem(self):

        self.driver.get('https://web.whatsapp.com/')

        time.sleep(5)

        for pessoa in self.pessoas:

            try:  # Tentará localizar a pessoa na lista de conversas ativas
                encontrar_pessoa = self.driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
                encontrar_pessoa.click()

                caixa_de_mensagem = self.driver.find_element(By.XPATH,
                                                             '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                caixa_de_mensagem.click()

                time.sleep(3)

                caixa_de_mensagem.send_keys(self.mensagem)

                enviar = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div['
                                                            '3]/button')
                enviar.click()

            except:  # Caso não ache, vai procurar na lista de contatos
                time.sleep(4)

                nova_conversa = self.driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div')
                nova_conversa.click()

                time.sleep(3)

                keyboard.write(f'{pessoa}')

                time.sleep(3)

                achar_pessoa = self.driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
                achar_pessoa.click()

                caixa_de_mensagem = self.driver.find_element(By.XPATH,
                                                             '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                caixa_de_mensagem.click()

                time.sleep(3)

                caixa_de_mensagem.send_keys(self.mensagem)

                enviar = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                enviar.click()

        time.sleep(5)  # Tempo para cada loop para não travar seu pc (risos)


botzinho = WhatsAppBot()
botzinho.enviar_mensagem()
