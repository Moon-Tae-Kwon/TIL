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

* vmstat (시스템 정보 모니터링)
    * [si(swap in)] :
    디스크 swap 공간에 있는 데이터를 메모리로 호출하는 양을 의미합니다. 사용되고 있는 swap 디스크가 해제되는 양(per sec)입니다.
    * [so(swap out)] :
    메모리에서 디스크로 보내는 데이터의 양을 의미합니다. 물리적 메모리가 부족할 경우 디스크로부터 사용되는 메모리 양(per sec)입니다. swap out이 지속적으로 발생한다면 메모리 부족을 의심해 볼 수 있습니다. swap out값이 증가하면 메모리가 부족하다는 의미이므로 메모리를 늘려야 합니다. Swap out값은 0에 가까워야 좋고 초당 10블럭 이하가 좋습니다. swap필드의 값이 높다고 해도 free 메모리에 여유가 있다면 메모리가 부족한 것은 아닙니다.

* iostat (디스크 입출력 상태 모니터링)
    * [tps] : 디바이스에 초당 전송 요청 건수
    * [kB_read/s] : 디바이스에서 초당 읽은 데이터 블록 단위
    * [kB_wrtn/s] : 디바이스에서 초당 쓴 데이터 블록 단위
    * [kB_read] : 디바이스에서 지정한 간격 동안 읽은 블록 수
    * [kB_wrtn] : 디바이스에서 지정한 간격 동안 쓴 전체 블록 수

* netstat (네트워크 모니터링)
    * [$ netstat -r] : 서버의 라우팅 테이블 출력
    * [$ netstat -na --ip] : tcp/udp의 세션 목록 표시
    * [$ netstat -na | grep ESTABLISHED | wc -l] : 활성화된 세션 수 확인
    * [$ netstat -nap | grep :80 | grep ESTABLISHED | wc -l] : 80포트 동시 접속자수
    * [$ netstat -nltp] : LISTEN 중인 포트 정보 표시