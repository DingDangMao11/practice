# 实用技巧
## tiotest表格函数
```
=OFFSET($A$10,(ROW(A1)-1)*12,0)
=OFFSET($A$11,(ROW(A1)-1)*12,0)
=MID(J6,38,7)
=MID(K52,38,7)
=100%-R5/50
Write(MB/s)	Read(MB/s)
```
## 料号相关
emmc部分路径:
```
查看供应商: cat /sys/bus/mmc/devices/mmc0:0001/manfid
供应商
0x2  Sandisk   闪迪
0x11 Toshiba   东芝
0x13 Micron    镁光
0x15 Samsung   三星
0x90 Hynix     海力士
部分参数rev、name、cid、fwrev在/sys/class/block/mmcblk0/device/路径下，红米/sys/bus/mmc/devices/mmc0:0001
```
```
cat /proc/hwinfo
cat /sys/class/block/mmcblk0/device/name                                                                                                                                                         
HCG8a4
cat /sys/bus/mmc/devices/mmc0:0001/manfid
0x000090
cat /sys/class/block/mmcblk0/device/manfid
0x000090
cat   /sys/class/block/mmcblk0/device/oemid  
```
UFS部分路径:
```
查看供应商: cat  /proc/hwinfo
存储寿命：cat /sys/kernel/debug/ufshcd0/dump_health_desc
部分参数rev、name、cid、fwrev在/sys/class/block/sda/device/路径下
```
