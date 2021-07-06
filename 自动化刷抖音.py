from appium import webdriver
import time
server="http://localhost:4723/wd/hub"
param = {
			  "deviceName": "127.0.0.1:5555",
			  "platformName": "Android",
			  "platformVersion": "5.1.1",
			  "appPackage": "com.ss.android.ugc.aweme",
			  "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity"
}
driver=webdriver.Remote(server,param)
time.sleep(10)
driver.quit()