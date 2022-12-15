import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
import undetected_chromedriver as uc
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import random

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Pakakumi Bot')
        self.geometry('500x300')
        self.configure(bg='orange')
        # create all of the main containers
        self.top_frame = tk.Frame(self, bg='orange', width=450, height=30, pady=3)
        self.top_frame.grid(row=0, sticky="ew")
        

         # layout all of the main containers
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create the widgets for the top frame
        self.model_label = tk.Label(self.top_frame, text='Fill all the fields below')
        self.model_label.grid(row=0, columnspan=3)
        self.width_label = tk.Label(self.top_frame, text='Phone:')
        self.width_label.grid(row=1, column=0)
        self.phone = tk.Entry(self.top_frame, background="orange")
        self.phone.grid(row=1, column=2)
        self.width_label1 = tk.Label(self.top_frame, text='Password:')
        self.width_label1.grid(row=1, column=3)
        self.password = tk.Entry(self.top_frame, background="orange")
        self.password.grid(row=1, column=4)

       
        self.width_label = tk.Label(self.top_frame, text='Amount:')
        self.width_label.grid(row=3, column=0)
        self.amount = tk.Entry(self.top_frame, background="orange")
        self.amount.grid(row=3, column=2)
        self.width_label1 = tk.Label(self.top_frame, text='Max Auto Cashout:')
        self.width_label1.grid(row=3, column=3)
        self.auto = tk.Entry(self.top_frame, background="orange")
        self.auto.insert(0, 1.12)
        self.auto.grid(row=3, column=4)

        self.start_button = tk.Button(self.top_frame, background="pink", text="START", width=15)
        self.start_button['command'] = self.start_task
        self.start_button.grid(row=7, column=2, pady=7)

    def start_task(self):
        url = 'https://play.pakakumi.com/'
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument("--disable-javascript")
        driver = uc.Chrome(chrome_options=chrome_options, service_args=['--quiet'])
        driver.maximize_window()
        driver.get(url)
        time.sleep(20)

        try:
            remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/div/div[1]/div[2]/div/button')
            remove_modal.click()
            
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

        try:
            remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-1"]/div/div/div[1]/div[2]/div/button')
            remove_modal.click()
            
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

        try:
            remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-2"]/div/div/div[1]/div[2]/div/button')
            remove_modal.click()
            
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass


        #login xpath 
        # WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/div/div[4]/div/a[1]')))
        login_popup = driver.find_element(By.CSS_SELECTOR, '#root > div.css-18t74jv > div:nth-child(1) > div > div.css-1cmveru > div > a:nth-child(1)')
        login_popup.click()

        time.sleep(10)

        phone_field = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div/div[1]/div/input')
        phone_field.send_keys(self.phone.get())
        find_pass_field = (By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div/div[2]/div/input')
        WebDriverWait(driver, 50).until(
            EC.presence_of_element_located(find_pass_field))
        pass_field = driver.find_element(*find_pass_field)
        WebDriverWait(driver, 50).until(
            EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password.get())
        driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div/div/div/div[3]/button').click()
        time.sleep(10)

        try:
            remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/div/div[1]/div[2]/div/button')
            remove_modal.click()
            
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

        try:
            remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-1"]/div/div/div[1]/div[2]/div/button')
            remove_modal.click()
            
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

        try:
            remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-2"]/div/div/div[1]/div[2]/div/button')
            remove_modal.click()
            
        except NoSuchElementException:
            pass
        except StaleElementReferenceException:
            pass

        

        while True:
            try:
                remove_modal = driver.find_element(By.XPATH, '//*[@id="react-joyride-step-0"]/div/div/div[1]/div[2]/div/button')
                remove_modal.click()

            except NoSuchElementException:
                pass
            except StaleElementReferenceException:
                pass

            try:
                # driver.find_element(By.XPATH, '//*[@id="tour_multiplier"]/div/div[2]').text
                next_round = driver.find_element(By.XPATH, '//*[@id="tour_multiplier"]/div/div[2]').text
                if next_round == '4.0':
                    amount_field = driver.find_element(By.XPATH, '//*[@id="tour_bet_amount"]')
                    amount_field.send_keys(Keys.CONTROL + "a")
                    amount_field.send_keys(Keys.DELETE)
                    # time.sleep(3)
                    amount_field.send_keys(self.amount.get())
                    auto_cashout_field = driver.find_element(By.XPATH, '//*[@id="tour_bet_auto_cashout"]')
                    auto_cashout_field.send_keys(Keys.CONTROL + "a")
                    auto_cashout_field.send_keys(Keys.DELETE)
                    # time.sleep(3)
                    if self.auto.get():
                        auto_cashout_field.send_keys(random.randint(101, 112)/100)
                    else:
                        auto_cashout_field.send_keys(5.12)

                    bet_button = driver.find_element(By.XPATH, '//*[@id="tour_bet_button"]')
                    try:
                        if bet_button.is_enabled():
                            bet_button.click()
                        else:
                            pass
                    except StaleElementReferenceException:
                        pass
            except NoSuchElementException:
                pass
            except StaleElementReferenceException:
                pass

if __name__ == "__main__":
  app = App()
  app.mainloop()