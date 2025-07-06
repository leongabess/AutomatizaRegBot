import time
import pyperclip
import getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

#por algum motivo o programa, no momento, faz um registro acima do pedido, se colocar 2, faz 3, deve-se efetuar mais testes quando tiver registro disponível.

usuario_citsmart = input("Digite o login do Citsmart: ")
senha_citsmart = getpass.getpass("Digite sua senha: ")
solicitante_ist = input("Digite o nome do solicitante em que o protocolo será feito: ")
print ("Por favor,  verifique se consta o https://, e tenha certeza que está com o link da planilha mais recente, na aba mais recente, com acesso ao público.")
planilha_mais_recente = input("Cole o link da planilha: ")
site_registro_chat = input("Digite o site de registro dos chats, com o https://: ")

while True:
    try:
        quantidade_bots = int(input('Quantos bots deseja fazer? '))
        break

    except ValueError:
        print('INSIRA UM NÚMERO')

def fazer_login():
   driver.find_element(By.ID, 'user_login').send_keys(usuario_citsmart)
   driver.find_element(By.ID, 'password' ).send_keys(senha_citsmart)
   driver.find_element(By.ID, 'password' ).send_keys(Keys.ENTER)

#função para quando estiver testando implementações, basta apenas comentar a função fazer_login() e tirar o comentário dessa, uma boa opção pra não ter que ficar digitando seus dados toda vez
#def fazer_login_sem_senha():
    #driver.find_element(By.ID, 'user_login').send_keys("usuário")
    #driver.find_element(By.ID, 'password' ).send_keys("senha do usuário")
    #driver.find_element(By.ID, 'password' ).send_keys(Keys.ENTER)

def esperar_elemento(by, seletor, timeout=15):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, seletor))
    )

def registrar_protocolo_bot():
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    mover_dentro_planilha = ActionChains(driver)
    mover_dentro_planilha.send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(2)
    mover_dentro_planilha.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])
    opcao_registro_bot = esperar_elemento(By.CSS_SELECTOR, 'input[name="tipo_canal"][value="BOT"]')
    opcao_registro_bot.click()
    protocolo_copiado = pyperclip.paste()
    driver.find_element(By.NAME, "protocolo").send_keys(protocolo_copiado)
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)

def pagina_manifestacao_nova_ist():
    hoover_nova_ist = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//i[text()='more_vert']"))
    )
    actions = ActionChains(driver)
    actions.move_to_element(hoover_nova_ist).perform()
    time.sleep(0.5)
    esperar_elemento(By.XPATH, "//i[text()='add']")
    driver.find_element(By.XPATH, "//i[text()='add']").click()
    WebDriverWait(driver, 15).until(
        EC.url_contains("https://portaldeservicos.anac.gov.br/citsmart/pages/serviceRequestIncident/serviceRequestIncident.load#/request")
    )
    
def gravacao_de_ist ():
    driver.find_element(By.ID, 'request-solicitante').send_keys("leonardo gabriel")#send_keys(solicitante_ist)
    time.sleep(2)
    solicitante = esperar_elemento(By.ID, 'request-solicitante')
    solicitante.send_keys(Keys.DOWN)
    solicitante.send_keys(Keys.ENTER)
    esperar_elemento(By.ID, 'select-request-origem-atendimento').send_keys('c')
    esperar_elemento(By.ID, 'citsmart-service-request-portfolio-search-input').send_keys("informacao sem tramite")
    time.sleep(2)
    driver.find_element(By.ID, 'citsmart-service-request-portfolio-search-input').send_keys(Keys.DOWN)
    time.sleep(1)
    driver.find_element(By.ID, 'citsmart-service-request-portfolio-search-input').send_keys(Keys.ENTER)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    copiar_objetos_dentro_planilha = ActionChains(driver)
    copiar_objetos_dentro_planilha.send_keys(*[Keys.ARROW_RIGHT]*2).perform()
    copiar_objetos_dentro_planilha.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)
    numero = pyperclip.paste()
    driver.find_element(By.ID, "question8702").send_keys(numero)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(2)
    pyperclip.copy("")
    copiar_objetos_dentro_planilha.send_keys(Keys.LEFT).perform()
    time.sleep(4)
    copiar_objetos_dentro_planilha.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    roteiro_usado = pyperclip.paste()
    time.sleep(4)
    copiar_objetos_dentro_planilha.send_keys(Keys.LEFT).perform()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])   
    driver.find_element(By.CSS_SELECTOR, ".service-request-menu-toggle").click()    
    time.sleep(2)    
    seta_esquerda_pesquisa = driver.find_element(By.ID, "nav-item-service-request-knowledges")
    driver.execute_script("arguments[0].click()", seta_esquerda_pesquisa)
    esperar_elemento(By.XPATH, "//button[contains(text(), 'Pesquisa de Conhecimentos')]").click()
    esperar_elemento(By.NAME, "modal-request-conhecimento-pesquisar").send_keys(roteiro_usado)
    time.sleep(3)
    driver.find_element(By.NAME, "modal-request-conhecimento-pesquisar").send_keys(Keys.ENTER)
    time.sleep(5)
    driver.find_element(By.ID, "lookup-item-0").click()
    time.sleep(9)
    esperar_elemento(By.CSS_SELECTOR, "button.close[aria-hidden='true']")
    driver.find_element(By.CSS_SELECTOR, "button.close[aria-hidden='true']").click()
    time.sleep(9)

    #Posteriormente devo testar outra maneira de "copiar e colar" coisas como protocolo, pois ao fazer ctrl c + ctrl v, acaba ficando na área de transferencia, implementar uma maneira de armazenar o valor dos protocolos e roteiros em uma variável

    if roteiro_usado == "CTA-002":
        editor = driver.find_element(By.CSS_SELECTOR, "trix-editor")
        chat_abandonado_descricao = "Chat abandonado"
        driver.execute_script("arguments[0].editor.loadHTML(arguments[1])", editor, chat_abandonado_descricao)
        select_element = driver.find_element(By.ID, "question8701")
        select = Select(select_element)
        time.sleep(5)
        select.select_by_value("10201")

    else:
        editor = driver.find_element(By.CSS_SELECTOR, "trix-editor")
        duvida_solucionada = pyperclip.paste()
        driver.execute_script("arguments[0].editor.loadHTML(arguments[1])", editor, duvida_solucionada)
        select_element = driver.find_element(By.ID, "question8701")
        select = Select(select_element)
        time.sleep(5)
        select.select_by_value("10203")

    time.sleep(2)
    esperar_elemento(By.ID, "request-save-submit")
    driver.find_element(By.ID, "request-save-submit").click()
    time.sleep(9)
    protocolo = esperar_elemento(By.ID, 'serviceRequestIncidentNumberCreated')
    numero_protocolo_ist = protocolo.text.strip()
    time.sleep(3)
    pyperclip.copy(numero_protocolo_ist)
    time.sleep(2)
    sair_numero_protocolo = ActionChains(driver)
    sair_numero_protocolo.send_keys(Keys.ESCAPE).perform()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[2])
    driver.find_element(By.CSS_SELECTOR, 'input[name="tipo_sistema"][value="IST"]').click()
    IST_copiada = pyperclip.paste()
    time.sleep(1)
    driver.find_element(By.NAME, "protocolo_demanda").send_keys(IST_copiada)
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Enviar"]').click()
    time.sleep(5)

def tentar_enviar_de_novo():
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Enviar"]').click()
    time.sleep(5)

#Quando tiver registros disponíveis para fazer, verificar qual a mensagem correta, se é de fato "Agradecemos sua mensagem."

def verifica_mensagem():
    mensagem_certa = "Agradecemos sua mensagem."
    mensagem_recebida = driver.find_element(By.CLASS_NAME, "wpcf7-response-output").text
    if mensagem_recebida != mensagem_certa:
        return False
    else:
        return True

def enviado_ou_nao():
    tentativas = 0
    tentativas_maximo = 10
    while verifica_mensagem() == False:
        tentativas+=1
        tentar_enviar_de_novo()
        if tentativas >= tentativas_maximo:
            return False
    return True



driver = webdriver.Edge()
driver.get('https://portaldeservicos.anac.gov.br/citsmart/webmvc/login')
driver.execute_script("window.open(arguments[0], '_blank');", site_registro_chat)
driver.execute_script("window.open(arguments[0], '_blank');", planilha_mais_recente)
time.sleep(3)
driver.switch_to.window(driver.window_handles[0]) #0=citsmart, 1=site de registro do chat, 2=planilha recente
dropdown = esperar_elemento(By.CLASS_NAME, "input-group-addon")
dropdown.click()
citsmart_local = esperar_elemento(By.XPATH, "//span[contains(text(), 'citsmart.local')]")
citsmart_local.click()
time.sleep(2)
fazer_login()
#fazer_login_sem_senha()

WebDriverWait(driver, 10).until(
    EC.url_contains("https://portaldeservicos.anac.gov.br/citsmart/pages/smartPortal/smartPortal.load")
)

driver.find_element(By.XPATH, "//i[text()='home']").click()

WebDriverWait(driver, 10).until(
    EC.url_contains("https://portaldeservicos.anac.gov.br/citsmart/pages/smartDecisions/smartDecisions.load#/acesso-rapido")
)

esperar_elemento(By.LINK_TEXT, "Ticket").click()

WebDriverWait(driver, 10).until(
    EC.url_contains("https://portaldeservicos.anac.gov.br/citsmart/pages/serviceRequestIncident/serviceRequestIncident.load#/")
)

time.sleep(1)

for _ in range(quantidade_bots):
    registrar_protocolo_bot()
    pagina_manifestacao_nova_ist()    
    time.sleep(2)
    gravacao_de_ist()
    if enviado_ou_nao() == False:
        print("Tentativas demais para enviar protocolo e IST, tente de novo mais tarde")
        print(input("Insira algum texto para sair"))
        break
    time.sleep(10)

print ("Bot finalizado com sucesso, insira algum texto para sair :)")
input()







    

















