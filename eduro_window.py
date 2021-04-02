from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
import datetime



now2 = 0
while True:
    now = datetime.datetime.now()
    now = now.strftime('%Y/%m/%d')
    while now == now2:
        now2 = datetime.datetime.now()
        now2 = now2.strftime('%Y/%m/%d')
    now2 = datetime.datetime.now()
    now2 = now2.strftime('%Y/%m/%d')
    print(' [자가진단] 날짜가 바뀌었습니다. 자가진단을 시작합니다.')
    print(' [자가진단] 오늘 날짜 : ' + str(now2))
    
    f = open("C:\stockauto\selenium\Your_Privacy.txt", 'r', encoding='UTF8')
    txtfile = f.readlines() #메모장 읽어오기
    for read in txtfile:
        Your_Privacy = read.split(" ") # 아이디들을 리스트에 저장
        Your_Area = Your_Privacy[0] # 서울특별시, 부산광역시, 대구광역시, 인천광역시, 광주광역시, 대전광역시, 울산광역시, 세종특별자치시, 경기도,강원도, 충청북도, 충청남도, 전라북도, 전라남도, 경상북도, 경상남도, 제주특별자치도
        Your_Class = Your_Privacy[1] # 유치원, 초등학교, 중학교, 고등학교, 특수학교등
        Your_School = Your_Privacy[2]
        Your_Name = Your_Privacy[3]
        Your_Date = Your_Privacy[4]
        Your_Pass = Your_Privacy[5]
        Your_Pass.rstrip('\n')
        
        # Your_area 설정
        areas = ["서울특별시", "부산광역시", "대구광역시", "인천광역시", "광주광역시", "대전광역시", "울산광역시", "세종특별자치시", "경기도", "강원도", "충청북도", "충청남도", "전라북도", "전라남도", "경상북도", "경상남도", "제주특별자치도"]
        if_area = ""
        x = 2
        for if_area in areas:
            if type(Your_Area) == "<class'int'>":
                continue 
            if Your_Area == if_area:
                Your_Area = str(x)
            x += 1
        
        # Your_Class 설정
        Classes = ["유치원", "초등학교", "중학교", "고등학교", "특수학교등"]
        if_Class = ""
        x = 2
        for if_Class in Classes:
            if type(Your_Class) == "<class'int'>":
                continue 
            if Your_Class == if_Class:
                Your_Class = str(x)
            x += 1
        

        driver = webdriver.Chrome('C:\stockauto\selenium\chromedriver.exe')
        driver.get("https://hcs.eduro.go.kr/#/loginHome")
        driver.find_element_by_id('btnConfirm2').click()
        driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[1]/td/button').click()
        driver.find_element_by_id('sidolabel').click()
        driver.find_element_by_xpath('//*[@id="sidolabel"]/option['+ Your_Area +']').click()  #시/도 설정 메뉴 * 반드시 코드 사용할 것 *
        driver.find_element_by_xpath('//*[@id="crseScCode"]/option['+ Your_Class +']').click() 
        elem = driver.find_element_by_xpath('//*[@id="orgname"]')
        elem.send_keys(Your_School)
        elem.send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul').click() #학교선택
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
        elem = driver.find_element_by_xpath('//*[@id="user_name_input"]')
        elem.send_keys(Your_Name)
        elem = driver.find_element_by_xpath('//*[@id="birthday_input"]')
        elem.send_keys(Your_Date)
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//input[@class='input_text_common']")
        elem.send_keys(Your_Pass)
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a/em').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[2]/dl[1]/dd/ul/li[1]/label').click()
        driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[2]/dl[2]/dd/ul/li[1]/label').click()
        driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div[2]/div[2]/dl[3]/dd/ul/li[1]/label').click()
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
        print(" [자가진단] 사용자 [이름]님의 자가진단이 마무리 되었습니다. 프로그램을 종료합니다.")
        time.sleep(1)
        driver.close()
    f.close() #메모장 닫기
