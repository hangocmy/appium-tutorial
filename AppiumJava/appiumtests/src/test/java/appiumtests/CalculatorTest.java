package appiumtests;
import io.appium.java_client.AppiumDriver;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;

import java.net.URL;

public class CalculatorTest{

    static WebDriver<WebElement> driver;

    public static void main(String[] args) {

    }

    public static void openCalculator(){
        DesiredCapabilities cap = new DesiredCapabilities();

        //about phone
        cap.setCapability("deviceName", "sdk_gphone64_x86_64");
        cap.setCapability("udid", "emulator-5554");
        cap.setCapability("platformName", "Android");
        cap.setCapability("platformVersion", "12");

        //about app
        cap.setCapability("appPackage", "com.google.android.calculator");
        cap.setCapability("appActivity", "com.android.calculator2.Calculator");

        URL url = new URL("http://0.0.0.0:4723/");
        driver = new WebDriver(cap);


    }
}
