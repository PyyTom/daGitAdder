import flet as fl,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from applescript import tell
def main(page:fl.Page):
    def xit(e):
        page.window_destroy()
    def select(e:fl.FilePickerResultEvent):
        path=(e.files[0].path)[41:-7]
        product=(path.split('/')[-2]).split('-')[0]
        technology=(path.split('/')[-2]).split('-')[1]
        options=Options()
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
        driver.get('https://github.com/login')
        time.sleep(2)
        driver.find_element(By.ID,'login_field').send_keys('tommaso_latorre@hotmail.com')
        driver.find_element(By.ID,'password').send_keys('Github23!')
        driver.find_element(By.NAME,'commit').click()
        driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/div[1]/a').click()
        driver.find_element(By.ID,':r4:').send_keys(product)
        driver.find_element(By.NAME,'Description').send_keys(technology)
        time.sleep(2)
        driver.find_element(By.XPATH,'/html/body/div[1]/div[6]/main/react-app/div/form/div[5]/button').click()
        driver.quit()
        tell.app('Terminal', 'do script "cd '+path+' ; git init ; git remote add origin https://github.com/PyyTom/'+(product+'.git')+' ; git add main.py ; git add readme.txt ; git push --set-upstream origin main"')
        page.dialog=d
        d.title=fl.Text(product + "'S REPOSITORY SUCCESSFULLY ADDED TO GITHUB.COM")
        d.open=True
        page.update()
    page.window_width=1000
    page.window_height=200
    page.window_resizable=False
    page.theme_mode=fl.ThemeMode.LIGHT
    d = fl.AlertDialog()
    picker=fl.FilePicker(on_result=select)
    page.overlay.append(picker)
    b_select=fl.ElevatedButton('SELECT PRODUCT',on_click=lambda _:picker.pick_files())
    page.add(fl.Row(controls=[fl.Text('daGitAdder')],alignment=fl.MainAxisAlignment.CENTER),
             fl.Row(controls=[b_select],alignment=fl.MainAxisAlignment.CENTER),
             fl.Row(controls=[fl.IconButton(icon=fl.icons.EXIT_TO_APP, icon_size=50, icon_color='red', on_click=xit)],alignment=fl.MainAxisAlignment.END))
fl.app(target=main)