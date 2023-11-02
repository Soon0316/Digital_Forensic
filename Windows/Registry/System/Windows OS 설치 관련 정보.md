Windows OS 설치 관련 정보
=
+ ####  Windows OS 제품명
```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [ProductName]
```

+ ####  Windows OS 버전
```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [DisplayVersion]
```
+ ####  Windows OS Build Number
```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [CurrentBuild]
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [CurrentBuildNumber]
```
+ #### Windows OS 설치 시각
```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [InstallDate]  Unix Second(32bit)
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [InstallTime]  Windows Filetime(64bit)
```
[InstallDate] 는 Unix Second(32bit) 형식으로 기록되어 있으며 [InstallTime] 은 Windows Filetime(64bit) 형식으로 기록되어 있다. 

+ #### Windows OS 설치 시 등록하였던 Outlook 계정
```
HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion [RegisteredOwner]
```
