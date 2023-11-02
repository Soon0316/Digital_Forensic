무선 네트워크 카드(NIC) 정보
=
+ #### 무선 네트워크 카드명 및 GUID
```
HKLM\SOFTWARE\Microsoft\Windows NT\NetworkCards\임의 숫자값 [Description]  #네트워크 카드명
HKLM\SOFTWARE\Microsoft\Windows Nt\NetworkCards\임의 숫자값 [ServiceName]  #네트워크 카드 GUID
```
+ #### 무선 네트워크 카드 MAC 주소
```
HKLM\SYSTEM\CurrentControlSet\Control\NetworkSetup2\Interfaces\{NIC GUID}\Kernel [CurrentAddress]
```
