from datetime import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
perfil = webdriver.FirefoxProfile("Caminho do seu profile do firefox (%appdata%)")
options.headless = True
browser = webdriver.Firefox(firefox_profile=perfil, options=options)
browser.get('https://web.whatsapp.com')

data = datetime.today().day
data = data+1
notificados = []


def abrir():
    browser.get('https://web.whatsapp.com')
    sleep(10)


def registro(arq, nome, numero, vencimento):
    try:
        a = open(arq, 'rt')
    except:
        a = open(arq, 'wt+')
        a.close()
    else:
        a = open(arq, 'at')
        a.write(f'{nome};{numero};{vencimento}\n')
        a.close()


def notificar(arq, rev):
    try:
        a = open(arq, 'rt')
    except:
        a = open(arq, 'wt+')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            if int(dado[2]) == data:
                print(f'{dado[0]} vence AMANHÃ!')
                rev(dado[0], dado[1])


def revenda1(nome, numero):
    msg = f"""%2AOi%2C%20{nome}%21%2A%0D%0ANÃO%20FIQUE%20NO%20TÉDIO%21%0D%0A%0D%0A-%20Aquele%20filme%20em%20familía%20👨%E2%80%8D👩%E2%80%8D👧%0D%0A-%20Sua%20novela%20preferida%20📺%0D%0A-%20O%20jogo%20do%20seu%20time%20⚽%0D%0A%0D%0ATudo%20isso%20você%20acompanha%20com%20a%20gente%21%0D%0A%0D%0ASeu%20plano%20irá%20vencer%20%2AAMANHÃ%2A%2C%20realize%20o%20pagamento%20e%20continue%20aproveitando%20suas%20vantagens%21%0D%0A%0D%0A%2A%2AMENSAGEM%20AUTOMÁTICA%2C%20EM%20CASO%20DE%20DÚVIDAS%20CONTATE%20SEU%20REVENDEDOR%2A"""
    try:
        browser.get(f'https://web.whatsapp.com/send?phone=55{numero}&text={msg}%21&app_absent=0')
        sleep(10)
        browser.find_element_by_xpath(
            '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        sleep(10)
    except:
        print(f'Houve um erro ao notificar {nome}')
        notificados.append(f'ERRO: {nome}')
    else:
        print(f'{nome} foi notificado.')
        notificados.append(nome)


def revenda2(nome, numero):
    msg = f"""%2AOi%2C%20{nome}%21%2A%0D%0ANÃO%20FIQUE%20NO%20TÉDIO%21%0D%0A%0D%0A-%20Aquele%20filme%20em%20familía%20👨%E2%80%8D👩%E2%80%8D👧%0D%0A-%20Sua%20novela%20preferida%20📺%0D%0A-%20O%20jogo%20do%20seu%20time%20⚽%0D%0A%0D%0ATudo%20isso%20você%20acompanha%20com%20a%20gente%21%0D%0A%0D%0ASeu%20plano%20irá%20vencer%20%2AAMANHÃ%2A%2C%20realize%20o%20pagamento%20e%20continue%20aproveitando%20suas%20vantagens%21%0D%0A%0D%0A%2A%2AMENSAGEM%20AUTOMÁTICA%2C%20EM%20CASO%20DE%20DÚVIDAS%20CONTATE%20SEU%20REVENDEDOR%2A"""
    try:
        browser.get(f'https://web.whatsapp.com/send?phone=55{numero}&text={msg}%21&app_absent=0')
        sleep(10)
        browser.find_element_by_xpath(
            '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        sleep(10)
    except:
        print(f'Houve um erro ao notificar {nome}')
        notificados.append(f'ERRO: {nome}')
    else:
        print(f'{nome} foi notificado.')
        notificados.append(nome)


def revenda3(nome, numero):
    msg = f"""%2AOi%2C%20{nome}%21%2A%0D%0ANÃO%20FIQUE%20NO%20TÉDIO%21%0D%0A%0D%0A-%20Aquele%20filme%20em%20familía%20👨%E2%80%8D👩%E2%80%8D👧%0D%0A-%20Sua%20novela%20preferida%20📺%0D%0A-%20O%20jogo%20do%20seu%20time%20⚽%0D%0A%0D%0ATudo%20isso%20você%20acompanha%20com%20a%20gente%21%0D%0A%0D%0ASeu%20plano%20irá%20vencer%20%2AAMANHÃ%2A%2C%20realize%20o%20pagamento%20e%20continue%20aproveitando%20suas%20vantagens%21%0D%0A%0D%0A%2A%2AMENSAGEM%20AUTOMÁTICA%2C%20EM%20CASO%20DE%20DÚVIDAS%20CONTATE%20SEU%20REVENDEDOR%2A"""
    try:
        browser.get(f'https://web.whatsapp.com/send?phone=55{numero}&text={msg}%21&app_absent=0')
        sleep(10)
        browser.find_element_by_xpath(
            '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
        sleep(10)
    except:
        print(f'Houve um erro ao notificar {nome}')
        notificados.append(f'ERRO: {nome}')
    else:
        print(f'{nome} foi notificado.')
        notificados.append(nome)


def avisar(revendedor):
    number = []
    if revendedor == 'revenda1':
        number.append('84999999999') #Insira o número das suas revendas para eles serem notificados sobre os usuarios avisados.
    elif revendedor == 'revenda2':
        number.append('84999999999')
    elif revendedor == 'revenda3':
        number.append('84999999999')
    notificadosmsg = f'{notificados} foram notificados!'
    if len(notificados) == 0:
        notificadosmsg = f'[ *Nenhum usuario vencendo amanhã, ninguem foi notificado.* ]'.upper()
    browser.get(f'https://web.whatsapp.com/send?phone=55{number[0]}&text={notificadosmsg}')
    sleep(10)
    browser.find_element_by_xpath(
        '/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
    sleep(10)
    print(f'[ {revendedor} RECEBEU AS INFORMAÇÕES! ]')
    notificados.clear()
    number.clear()
