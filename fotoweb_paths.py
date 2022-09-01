from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

class Downloader:

    # def _init_(self, driver):
    #     self.driver = driver
    #     self.login = "login"
    #     self.senha = "pass"

    def start(self):
        self.login_fotoweb()
        self.until_em()
        self.em_menu()
        self.cad()
        # self.cad_menu()
        # self.download_them_all()

    def login_fotoweb(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\João Felipe\Desktop\chromedriver.exe")
        self.driver.get("http://iconografia.fotoweb.somoseducacao.com.br/fotoweb/cmdrequest/HomePage.fwx")
        sleep(2)
        self.driver.find_element_by_name(name="u").send_keys('rcavanha'+ Keys.TAB)
        sleep(1)
        self.driver.find_element_by_name(name="p").send_keys('47328' + Keys.ENTER)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/center[1]/div/div/input[2]').click()
        sleep(2)

    def until_em(self):
    # acervo
        self.driver.find_element_by_id("ArchiveMenu").click()
        sleep(2)
    # rolar pra baixo
        self.driver.find_element_by_xpath('//*[@id="ArchiveMenu"]/div/div[4]/span').click()
        sleep(2)
    # structure
        self.driver.find_element_by_xpath('//*[@id="Panel_2"]/a').click()
    # fibonacci
        self.driver.find_element_by_id("Archive_5036").click()
        sleep(2)
    # fibonnaci na estrutura
        self.driver.find_element_by_xpath('//*[@id="Panel_2"]/div/div/ul/li/div').click()
        sleep(1)
    # EM
        self.driver.find_element_by_xpath('//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/div').click()
    sleep(1)

    # Location to xpath on EM menu
    def em_menu(self):
        xpath_fgb_dic = {'FGB1_DIGITAL': "1", 'FGB1_IMPRESSO': "2", 'FGB2_DIGITAL': "3", 'FGB2_IMPRESSO': "4", 'IF1_DIGITAL': "5",
                      'IF1_IMPRESSO': "6"}

        em_select = input("Qual pasta gostaria de acessar em EM ? ").upper()
        if em_select in xpath_fgb_dic:
            em_select = f"{xpath_fgb_dic.values}"
            # Dinamic Path
            self.driver.find_element_by_xpath(f'//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li["{em_select}"]/div').click()
            sleep(1)
            # return self.driver.find_element_by_xpath(f'//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li["{em_select}"]/div')
            return em_select

        else:
            print("Menu EM não encontrado.")
            # em_select = input("Qual pasta gostaria de acessar em EM ?").upper()


# Location to xpath on Cad menu
    def cad(self):
        xpath_cad_dic = {'CAD1': "1", 'CAD2': "2", 'CAD3': "3"}
        xpath_materia_dic = {'BIOLOGIA': "1", 'ESPANHOL': "2", 'FILOSOFIA': "3"}

        cad_select = input("Qual caderno gostaria de acessar Cad1, Cad2 ou Cad3? ").upper()
        section_select = input("Qual materia gostaria de acessar ? ").upper()

        if cad_select in xpath_cad_dic and section_select in xpath_materia_dic:
            cad_select = f"{xpath_cad_dic.values}"
            section_select = f"{xpath_materia_dic.values}"
            #acessar caderno
            self.driver.find_element_by_xpath(f'//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li[1]/ul/li["{cad_select}"]/div')
            #acessar materia
            self.driver.find_element_by_xpath(f'//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li[1]/ul/li["{self.em_menu()}"]/ul/li["{section_select}"]/div')
            # self.driver.find_element_by_xpath(f'//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li[{em_select}]/ul/li[{cad_select}]/div').click()
            sleep(1)
            # Tratadas sector
            self.driver.find_element_by_xpath('//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[1]/ul/li[2]/a').click()
            sleep(1)
        else:
            print("Não encontrado.")
            # cad_select = input("Qual caderno gostaria de acessar ?").upper()

    # def cad_menu(self):
    #     em_answer = "initial"
    #     cad_answer = "initial"
    #Dinamic Path
        # self.driver.find_element_by_xpath(f'//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li[{em_answer}]/ul/li[{cad_answer}]/div').click()
        # sleep(1)
    #Tratadas sector
        # self.driver.find_element_by_xpath('//*[@id="Panel_2"]/div/div/ul/li/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[1]/ul/li[2]/a').click()
        # sleep(1)

    #Dowloading all pictures
    def download_them_all(self):
        amount_of_pics = input("Quantas imagens a seção possui ? ")
        # pic_counter = 0
        for pic in amount_of_pics:
            self.driver.find_element_by_xpath(f'//*[@id="imgCell{pic}"]/div/div[4]/span[2]').click()
            sleep(2)
            self.driver.find_element_by_xpath('//*[@id="downloadSuccessDialog"]/div/div[2]').click()
            sleep(1)
            # pic_counter = +1
