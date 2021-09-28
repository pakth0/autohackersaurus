import PyPDF2
import requests

API_ENDPOINT = 'https://www.hackerrank.com/rest/administration/challenges'

class Problem:
    def __init__(self, name, input_text, output_text, inpfile_text, outpfile_text) -> None:
        self.name = name
        self.input_text = input_text
        self.output_text = output_text
        self.input_file_text = inpfile_text
        self.output_file_text = outpfile_text
    def create_challenge(self):
        data = {"skill":"null",
        "name": self.name,
        "preview":"none",
        "problem_statement_fields":{"problem_statement":"n/a",
                                    "input_format":self.input_text,
                                    "constraints":"n/a",
                                    "output_format":self.output_text + self.output_file_text
                                    },
        "tags":["a"]}
        headers = {"cookie":"_ga=GA1.2.580971557.1630095901", 
        "_gd_visitor":"7794f14d-75e1-46c8-8a50-e59e0ecf88d3", 
        "_gd_svisitor":"26241cb8a43100000d4a29611a02000099e98600",
        "_mkto_trk":"id:487-WAY-049&token:_mch-hackerrank.com-1631201167621-40662",
        "hackerrank_mixpanel_token":"c7ebc657-4aa1-45c4-8c8f-4471a5328c52",
        "_biz_uid":"29ff71c736604145e20484d390ee62fe",
        "hacker_editor_theme":"light",
        "enableIntellisenseUserPref":"true",
        "_uetvid":"aaa0c40077411ec966e9bd06f7c6870",
        "_gid":"A1.2.280117315.1632757323",
        "__utmz":"74197771.1632757418.11.2.utmcsr=quora.com|utmccn=(referral)|utmcmd=referral|utmcct=/",
        "show_cookie_banner":"false",
        "hackerrankx_mixpanel_token":"c7ebc657-4aa1-45c4-8c8f-4471a5328c52",
        "_biz_flagsA":'{"Version":1,"ViewThrough":"1","XDomain":"1","Mkto":"1"}',
        "remember_hacker_token":"eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFQRkxwZ2lJaVF5WVNReE1DUk5RMkZ6Ym5BNVdGaHBXRGhqU0V4SU9Ea3lSMkoxU1NJWE1UWXpNamMxT0RRd01TNDJOVEV6TWprNEJqb0dSVVk9IiwiZXhwIjoiMjAyMS0xMC0xMVQxNjowMDowMS42NTFaIiwicHVyIjpudWxsfX0=--f817f30db9533dd95b966bac7ee45122af066704",
        "metrics_user_identifier":"982ec5-6aa3e72fbafddcf92e9aa7cb779cd5057b5933f9",
        "react_var":"true__trm2",
        "react_var2":"true__trm2",
        "hrc_l_i":"T",
        "_hrank_session":"8e8eaa2166c4568b240223dddee310845198a38819ecfc8702745c8d5ee186e7fd459a31f43649c0bc416407be21bd3e6995483d0d18ceca0bbe3a2649027895",
        "session_id":"y1xb1yt6-1632788036422",
        "__utma":"74197771.580971557.1630095901.1632757418.1632788037.12",
        "__utmc":"74197771",
        "__utmt":"1",
        "_biz_sid":"900cfb",
        "__utmb":"74197771.8.9.1632788040651",
        "_biz_nA":"630",
        "_biz_pendingA":"[]"}

        r = requests.post(url=API_ENDPOINT, headers= headers, data = data)
        
        print(r)

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
    curr_problem = Problem(name, inputText, outputText, input_file_text, output_file_text)
    curr_problem.create_challenge()
    #print('INPUT TEXT \n' + inputText + '\n\nOUTPUT TEXT\n\n' + outputText + '\n\nINPUT FILE TEXT\n\n' + input_file_text + '\n\nOUTPUT FILE TEXT\n\n' + output_file_text)   
