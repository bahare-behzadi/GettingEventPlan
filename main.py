from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from selenium.webdriver.edge.service import Service

#edge_service = Service("C:\developer\msedgedriver.exe")
chrom_service = Service("C:\developer\chromedriver.exe")
chrom_driver = webdriver.Chrome(service=chrom_service)
#edge_driver = webdriver.Edge(service=edge_service)

chrom_driver.get("https://www.python.org/")
#edge_driver.get("https://www.python.org/")

content_text = (chrom_driver.find_elements(By.CLASS_NAME,"event-widget li"))
event_list = [element.text for element in content_text]
print(event_list)
event_dic = {
    event_list.index(event): {
        "time": event.split("\n")[0],
        "name": event.split("\n")[1]
    }
             for event in event_list
}
print(event_dic)
