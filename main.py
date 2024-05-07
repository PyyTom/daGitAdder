import flet as fl,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from applescript import tell
def main(page:fl.Page):
    def xit(e):
        page.window_destroy()
    def select(e:fl.FilePickerResultEvent):
        path=(e.files[0].path)[41:-7]
        product=(path.split('/')[-2]).split('-')[0]
        technology=(path.split('/')[-2]).split('-')[1]
        '''
        driver = webdriver.Chrome()
        driver.get('https://github.com/login')
        time.sleep(2)
        driver.find_element(By.ID,'login_field').send_keys('tommaso_latorre@hotmail.com')
        driver.find_element(By.ID,'password').send_keys('Github23!')
        driver.find_element(By.NAME,'commit').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/a').click()
        driver.find_element(By.ID,':r4:').send_keys(product)
        driver.find_element(By.NAME,'Description').send_keys(technology)
        driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/main/react-app/div/form/div[3]/div[2]/div/div[1]/div/div[2]/label').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button').click()
        driver.quit()
        '''
        tell.app('Terminal', 'do script "cd '+path+' ; git init ; git remote add origin https://github.com/PyyTom/'+(product[:-3]+'git')+' ; git add main.py ; git commit -m '+"main.py just added"+' ; git push --set-upstream origin main"')
        page.dialog=d
        d.title=fl.Text(product + "'S REPOSITORY SUCCESSFULLY ADDED TO GITHUB.COM")
        d.open=True
        page.update()
    page.window_width=260
    page.window_height=150
    page.window_resizable=False
    d = fl.AlertDialog()
    picker=fl.FilePicker(on_result=select)
    page.overlay.append(picker)
    b_select=fl.ElevatedButton('SELECT PRODUCT',on_click=lambda _:picker.pick_files())
    page.add(fl.Text('            daWebsitePopulator'),
             fl.Row(controls=[b_select,fl.IconButton(icon=fl.icons.EXIT_TO_APP,icon_size=50,icon_color='red',on_click=xit)]))
fl.app(target=main)