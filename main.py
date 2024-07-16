import pandas as pd     #Import pandas and call it as 'pd'
import pyautogui, time  #Import pyautogui and time libraries

pyautogui.PAUSE = 0.5 #setting delay time between two pyautogui commands equals to 1/2 second

"""In this section, we say to the algorithm to press the 'win' button an then, write the browser's name
and finally press enter. This sequence will open the selected browser. In this case, we use 
Brave Browser.
After the steps mentioned before, the algorithm will wait for one second with command time.sleep(1) 
and then, the URL of our web page will be write on browser's search bar . Finally, the enter button 
will be pressed and our page loads on screen."""
pyautogui.press('win')      
pyautogui.write('brave')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(1) #The algorithm will wait one more second, to give time to browser to effectively load the page.

"""In this section, the algorithm will click on the e-mail field on our HTML page, with the correct 
coordinates (x=425, y=396) and then write the usermail. After these steps, the tab button will be pressed and
the cursor on the page goes to password field. At this point, the algorithm will write the password (which is 
the string password in this case) and then press enter to login."""
pyautogui.click(x=425, y=396)
pyautogui.write('leogeraldino95@gmail.com')
pyautogui.press('tab')
pyautogui.write('password')
pyautogui.press('enter')

time.sleep(1) #The algorithm will wait one more second, to give time to browser to effectively load the page.

"""In this last section, the algorithm will store the data from the produtos.csv file in a variable named table.
This is make by pandas library command pd.read_csv('produtos.csv'). After this, through a loop for, the pyautogui 
will be responsible for click on the Código do Produto's field and then, write the product id. So, the algorithm 
repeat this logics for all the columns of our table ('produtos.csv') through the loop, row to row untill the end 
of table."""
table = pd.read_csv('produtos.csv')
for linha in table.index:
    pyautogui.click(x=414, y=285)
    pyautogui.write(str(table.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(table.loc[linha, 'custo']))
    pyautogui.press('tab')
    
    obs = str(table.loc[linha, 'obs'])      #This part of the algorithm store the data in the column obs in a 
    if obs != 'nan':                        #variable named obs and then, it compares the variable content with 
        pyautogui.write(obs)                #'nan', which means Not a number. If the variable obs isn't equal to   
        pyautogui.press('tab')              #'nan', the algorithm will input the data stored in obs variable in
                                            #the related field on the HTML page.
    pyautogui.press('enter')
    pyautogui.press('PgUp')                 #When PgUp is pressed, the page returns to the header and in the next 
                                            #loop, the algorithm will click again on the Código do Produto's field 

