::adb shell dumpsys window windows | findstr "Current" //获取当前窗口
adb wait-for-device install -r mobileqq_android-7.2.5.apk
adb shell am start com.tencent.mobileqq/com.tencent.mobileqq.activity.SplashActivity