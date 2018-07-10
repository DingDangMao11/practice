# 记录常用命令, 方便查找
* QXDM:<br />
Xiaomi Xiao1210 3602
* 修改dpi:<br />
`wm density 400`
* 切换A/B槽: `fastboot set_active a`<br />
  验证: `adb shell getprop ro.boot.slot_suffix`
* 国际版MIUI打开root授权窗口:<br />
`adb shell am start -n com.miui.securitycenter/com.miui.permcenter.root.RootManagementActivity`
* 网络连接adb:<br />
1.`adb tcpip 5555`<br />
2.`adb connect 10.237.201.104:5555`
* 开启dump模式:<br />
`echo 1 > /sys/module/msm_poweroff/parameters/download_mode`<br />
验证:<br />
`cat /sys/module/msm_poweroff/parameters/download_mode`
* 查询source boot状态:<br />
`fastboot getvar secure`
* 连续抓取logcat:<br />
`adb logcat -v time -b all > logcat.txt`
* 验证recovery升级成功:<br />
`logcat |grep "Installing new recovery image"`
或者:<br />
`logcat |grep "Recovery image already installed"`
* 开机log<br />
`adb shell dmesg > dmesg.txt`
`adb bugreport > bugreport.txt`
* 华勤的717端口(diag)<br />
`*#*#13491#*#*`
闻泰wt_log<br />
`*#*#98284#*#*`
* subsystem:<br />
如果echo restart > /d/msm_subsys/slpi 不支持，请输入一下命令<br />
```
oxygen:/ # echo 'related' > /sys/bus/msm_subsys/devices/subsys2/restart_level
oxygen:/ # echo 'restart' > /sys/kernel/debug/msm_subsys/adsp
```
* monkey静音指令(E1之后):<br />
`tinymix "SmartPA Mute" 1`
* 设置core dump:<br />
`adb shell setprop persist.debug.trace 1`(只需设置一次)<br />
`adb shell setenforce 0`(重启失效)
* 查询是否刷debugpolicy:<br />
`adb shell getprop ro.boot.dp`
* 查询版本号:<br />
`adb shell getprop ro.build.version.incremental`
* 手动触发crash:<br />
`echo c > /proc/sysrq-trigger`
* 批量pull文件:<br />
`adb shell ls data/media/0/app*.txt | tr "\n\r" " " | xargs -n1 adb pull`
* 解密重启次数:<br />
可以使用以下解密：(python)<br />
```
>>> import base64
>>> from Crypto.Cipher import AES
>>> key = "112adsfqwe112adsfqweSDHqwhSDHqwh"
>>> cipher = AES.new(key)
>>> b64_str = "加密字符串"
>>> enc = base64.b64decode(b64_str)
>>> cipher.decrypt(enc)
```
手机异常重启的记录都会生成在在 `persist/stability/abnormal_poweroff_time.txt `
* 
