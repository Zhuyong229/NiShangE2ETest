from playwright.sync_api import Page, expect, sync_playwright
import time 
import re
url = "https://ni-shang-web.vercel.app/"

    
def test_has_title(page: Page):
    page.goto(url)
    expect(page).to_have_title(re.compile("Create Next App"))
    
def test_home_link(page: Page):
    page.goto(url)
    page.get_by_role("link", name="Home").click()
    expect(page.get_by_role("heading", name="About NiShang Club")).to_be_visible()
    
    page.get_by_role("link", name="Events").click()
    time.sleep(5)
    expect(page).to_have_url(url+'events')

def handle_console_message(msg):
    if msg.type == "error":
        print('safe', f"Console {msg.type}: {msg.text}")
    else:
        pass

        
def test_run(page:Page):
    page.on("console", handle_console_message)
    page.goto(url+'booking')
    
    
    
        

    


    




    
