from selenium import webdriver
import time
import random
driver = webdriver.Chrome("D:/chromedriver.exe")
n= int(input("Please enter the number of links you want to provide"))
videos= []
for j in range(n):
    v= str(input("Enter the links"))
    videos.append(v)
a= int(input("Enter the first duration"))
b= int(input("Enter the second duration"))
c= int(input("How many views you want"))    
for i in range(c):

    print("Running the videos for {} time".format(i))
    random_video = random.randint(0,n-1)
    driver.get(videos[random_video])
    sleep_time = random.randint(10, 20)
    time.sleep(sleep_time)

driver.quit() 


# In[ ]:




