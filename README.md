# 如火七月, 不容停歇
* 这里是`2018年7月份`作业
# 心得体会
* 2018-07-06
	1. `adb shell dumpsys window windows | findstr "Current" ` 获取当前窗口
* 2018-07-17
	2. 如果没安装apk, 或者由于特殊原因无法定位到当前窗口, 则可借助`aapt`获取`包名`和`入口activity`:
		`aapt dump xmltree xxx.apk  AndroidManifest.xml`
		以QQ为例:
		```
			$ aapt dump xmltree mobileqq_android-7.2.5.apk   AndroidManifest.xml
			N: android=http://schemas.android.com/apk/res/android
			  E: manifest (line=2)
				A: android:versionCode(0x0101021b)=(type 0x10)0x2e8
				A: android:versionName(0x0101021c)="7.2.5" (Raw: "7.2.5")
				A: android:installLocation(0x010102b7)=(type 0x10)0x0
				A: package="com.tencent.mobileqq" (Raw: "com.tencent.mobileqq")  //包名
				E: uses-sdk (line=10)
				  A: android:minSdkVersion(0x0101020c)=(type 0x10)0xf
				  A: android:targetSdkVersion(0x01010270)=(type 0x10)0x9
				E: supports-screens (line=12)
				  A: android:anyDensity(0x0101026c)=(type 0x12)0xffffffff
				  A: android:smallScreens(0x01010284)=(type 0x12)0xffffffff
				  A: android:normalScreens(0x01010285)=(type 0x12)0xffffffff
				  A: android:largeScreens(0x01010286)=(type 0x12)0xffffffff
				E: uses-permission (line=15)
				  A: android:name(0x01010003)="com.android.launcher.permission.INSTALL_SHORTCUT" (Raw: "com.android.launcher.permission.INSTALL_SHORTCUT")
				E: uses-permission (line=16)
				  A: android:name(0x01010003)="android.permission.WRITE_EXTERNAL_STORAGE" (Raw: "android.permission.WRITE_EXTERNAL_STORAGE")
				E: uses-permission (line=17)
				  A: android:name(0x01010003)="android.permission.INTERNET" (Raw: "android.permission.INTERNET")
				E: uses-permission (line=18)
				  A: android:name(0x01010003)="android.permission.VIBRATE" (Raw: "android.permission.VIBRATE")
				...
				//中间是各种权限
				...
				E: activity (line=531)
					A: android:theme(0x01010000)=@0x7f0e0330
					A: android:label(0x01010001)=@0x7f0b16b2
					A: android:name(0x01010003)=".activity.SplashActivity" (Raw: ".activity.SplashActivity") //找到app入口
					A: android:launchMode(0x0101001d)=(type 0x10)0x1
					A: android:screenOrientation(0x0101001e)=(type 0x10)0x1
					A: android:configChanges(0x0101001f)=(type 0x11)0x4a4
					A: android:alwaysRetainTaskState(0x01010203)=(type 0x12)0xffffffff
					A: android:windowSoftInputMode(0x0101022b)=(type 0x11)0x20
					A: android:hardwareAccelerated(0x010102d3)=(type 0x12)0xffffffff
					E: intent-filter (line=541)
					  E: action (line=542)
						A: android:name(0x01010003)="android.intent.action.MAIN" (Raw: "android.intent.action.MAIN")
					  E: category (line=543)
						A: android:name(0x01010003)="android.intent.category.LAUNCHER" (Raw: "android.intent.category.LAUNCHER")
					E: intent-filter (line=545)
					  E: action (line=546)
						A: android:name(0x01010003)="com.tencent.mobileqq.action.MAINACTIVITY" (Raw: "com.tencent.mobileqq.action.MAINACTIVITY")
					  E: category (line=547)
						A: android:name(0x01010003)="android.intent.category.DEFAULT" (Raw: "android.intent.category.DEFAULT")
				  E: activity (line=554)
					A: android:label(0x01010001)="" (Raw: "")
					A: android:name(0x01010003)=".activity.contact.troop.TroopActivity" (Raw: ".activity.contact.troop.TroopActivity")
					A: android:exported(0x01010010)=(type 0x12)0x0
					A: android:screenOrientation(0x0101001e)=(type 0x10)0x1
					A: android:configChanges(0x0101001f)=(type 0x11)0x4a4
					A: android:hardwareAccelerated(0x010102d3)=(type 0x12)0xffffffff
		```
