# linux

## key

* lsblk
    * 블록 스토리지 현황 (ex: lsblk)

* LVM
    * PV 만들기
        * pvcreate 디스크 초기화나 LVM에 사용될 파티션을 만드는데 쓰입니다. 또한 완전한 물리디스크나 물리디스크 위의 파티션 초기화에도 쓸 수  있습니다. (ex: pvcreate /dev/xvdf)
    * VG, LV 만들기
        * vgcreate [vg이름] [블록스토리지 경로]
        * vgdisplay (정상적으로 만들어 졌는지 확인)
        * lvcreate -n [LV이름] -L [LV용량] [VG이름]
        * lvdisplay
    * 매핑 확인
        * ls /dev/mapper (VG에 LV 2개가 매핑된것 확인)
    * mkfs.[파일시스템] [LV의 경로]
    * mount [option] [device] [directory]
    * 재부팅 유지 /etc/fstab
        * [device_name] [mount_point] [file_system_type] [fs_mntops] [fs_freq] [fs_passno]
    * blkid [LV경로] (UUID 확인)

* sudo
    * sudo -s 옵션은 권한 유지