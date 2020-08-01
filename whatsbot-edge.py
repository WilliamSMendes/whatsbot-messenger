""" Bot para WhatsApp utilizando Programação Orientada à Objetos no navegador Edge Chromium"""

# É necessário instalar as bibliotecas a seguir:
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import keyboard


class WhatsAppBot:

    def __init__(self):

        self.pessoas = ['Lucas', 'Mateus', 'João']
        self.mensagem = 'Olá mundo, sou um botzinho que está aprendendo a digitar sozinho'
        options = Options()
        options.page_load_strategy = 'eager'  # Carrega o essencial da pagina para melhorar a performance do algoritmo.
        self.driver = Edge(executable_path=r'./msedgedriver.exe')   # Path onde se encontra o webdriver

    def enviar_mensagem(self):

        self.driver.get('https://web.whatsapp.com/')

        time.sleep(5)

        for pessoa in self.pessoas:

            try:  # Tentará localizar a pessoa na lista de conversas ativas. 
                  # Utilizei a inspeção de elementos da página do whatsapp e copiei o XPATH para encontrar os elementos desejáveis:
                encontrar_pessoa = self.driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
                encontrar_pessoa.click()

                caixa_de_mensagem = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                caixa_de_mensagem.click()

                time.sleep(3)

                caixa_de_mensagem.send_keys(self.mensagem)

                enviar = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                enviar.click()

            except:  # Caso não ache, irá procurar na lista de contatos.
                time.sleep(4)

                nova_conversa = self.driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/label/div')
                nova_conversa.click()

                time.sleep(3)

                keyboard.write(f'{pessoa}')

                time.sleep(3)

                achar_pessoa = self.driver.find_element(By.XPATH, f"//span[@title='{pessoa}']")
                achar_pessoa.click()

                caixa_de_mensagem = self.driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                caixa_de_mensagem.click()

                time.sleep(3)

                caixa_de_mensagem.send_keys(self.mensagem)

                enviar = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                enviar.click()

        time.sleep(5)  # Tempo para cada loop para não travar seu pc (risos).


botzinho = WhatsAppBot()
botzinho.enviar_mensagem()
