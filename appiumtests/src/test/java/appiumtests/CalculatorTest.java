package appiumtests;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.openqa.selenium.remote.DesiredCapabilities;

public class CalculatorTest{
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
        cap.setCapability("appPackage", "com.vttm.vietteldiscovery");
        cap.setCapability("appActivity", "");



    }
}
