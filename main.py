import PyPDF2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

pwd = os.environ.get("hackerrank_pwd")



class Problem:
    def __init__(self, name, input_text, output_text, inpfile_text, outpfile_text, problem_text) -> None:
        self.name = name
        self.input_text = input_text
        self.output_text = output_text
        self.input_file_text = inpfile_text
        self.output_file_text = outpfile_text
        self.problem_text = problem_text
    def create_challenge(self):
        driver = webdriver.Chrome()
        driver.get("http://www.hackerrank.com/login")
        elem = driver.find_element_by_id('input-1')
        elem.send_keys('pakth0')
        elem = driver.find_element_by_id('input-2')
        elem.send_keys(pwd)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        elem = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[3]')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/div[1]/nav/div/div[2]/ul[2]/li[3]/div/div[2]/ul/li[7]/a')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/header/ul/li[2]/a')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/section/div[1]/button')
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id('name')
        elem.send_keys(self.name)
        elem = driver.find_element_by_xpath('//*[@id="preview"]')
        elem.send_keys('n/a')

        elem = driver.find_element_by_xpath('//*[@id="input_format-container"]/div/div/div[2]/div[6]/div[1]/div')
        elem.click()
        elem = driver.switch_to_active_element()
        elem.send_keys(self.input_text + '\n**SAMPLE INPUT**\n' + self.input_file_text)
        time.sleep(3)

        elem = driver.find_element_by_xpath('//*[@id="problem_statement-container"]/div/div/div[2]/div[6]/div[1]/div')
        elem.click()
        elem = driver.switch_to_active_element()
        elem.send_keys(self.problem_text)
        time.sleep(3)

        elem = driver.find_element_by_css_selector('body')
        for i in range(0,100):
            elem.send_keys(Keys.DOWN)

        elem = driver.find_element_by_xpath('//*[@id="constraints-container"]/div/div/div[2]/div[6]/div[1]/div')
        elem.click()
        elem = driver.switch_to_active_element()
        elem.send_keys('n/a')

        elem = driver.find_element_by_xpath('//*[@id="output_format-container"]/div/div/div[2]/div[6]/div[1]/div')
        elem.click()
        elem = driver.switch_to_active_element()
        elem.send_keys(self.output_text + '\n**SAMPLE OUTPUT**\n' + self.output_file_text)



        elem = driver.find_element_by_class_name('tagsinput')
        elem.click()
        time.sleep(2)
        elem = driver.switch_to_active_element()
        elem.send_keys('none, ')

        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div/button')
        elem.click()


pdfFile = open('probset.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFile)

for i in range(1, pdfReader.numPages):  
    page = pdfReader.getPage(i)
    textArr = page.extractText().split('\n')
    arr = page.extractText().split('\n')
    for i in range(0, len(arr)):
        arr[i] = arr[i].replace(" ", "")
    input_text_start_index = 0
    output_text_start_index = 0
    input_file_start_index = 0
    output_file_start_index = 0
    inputText = ''
    outputText = ''
    input_file_text = ''
    output_file_text = ''
    problem_text = ''
    vanName = textArr[6]
    print(vanName[5:])
    name = vanName[5:]
    #print(name)
    for i in range(0, len(arr)):
        #if(arr[i]+arr[i+1] != 'Input File' and arr[i] == 'Input'):
        if(arr[i] == 'Input'):
            input_text_start_index = i
            print('found input start!')
            break
    for i in range(8, input_text_start_index):
        problem_text += textArr[i]
    for i in range(input_text_start_index, len(arr)):
        if(arr[i] == 'Out' or arr[i]=='Output'):
            print('found output start!')
            output_text_start_index = i
            #print(arr[output_text_start_index+1])
            break
    for i in range(output_text_start_index-5, len(arr)):
        #print((arr[i-2]+arr[i-1]+arr[i]))
        if((arr[i-2]+arr[i-1]+arr[i]) == 'ExampleInputFile' or arr[i] == 'File'):
            print('found input file start!')
            input_file_start_index = i
            break
    for i in range(input_file_start_index-5, len(arr)):
        if(arr[i] == 'toScreen' or arr[i] == 'OutputtoScree'):
            print('found output file start!')
            output_file_start_index = i
            #print(output_file_start_index)
            break
    for i in range(input_text_start_index, output_text_start_index):
        inputText += textArr[i]
    for i in range(output_text_start_index, input_file_start_index):
        outputText += textArr[i]
    for i in range(input_file_start_index+1, output_file_start_index):
        input_file_text += textArr[i] + '\n'
    for i in range(output_file_start_index+1, len(arr)):
        output_file_text += textArr[i] + '\n'
    curr_problem = Problem(name, inputText, outputText, input_file_text, output_file_text, problem_text)
    curr_problem.create_challenge()
    #print('INPUT TEXT \n' + inputText + '\n\nOUTPUT TEXT\n\n' + outputText + '\n\nINPUT FILE TEXT\n\n' + input_file_text + '\n\nOUTPUT FILE TEXT\n\n' + output_file_text)   
