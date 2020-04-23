# XML tp Xpath elements parser

## Description

### General

This module is able to parse and XML source file and print all the element/Xpath pairs to comand line. 



### Example of output

```shell
$ python xml_to_xpath.py source.xml

Element: 'hierarchy'
Xpath: //hierarchy[@rotation=0]

Element: 'android.widget.FrameLayout'
Xpath: //hierarchy/android.widget.FrameLayout[@bounds=[0,0][1080,1794]][@checkable=false][@checked=false][@class=android.widget.FrameLayout][@clickable=false][@content-desc=][@enabled=true][@focusable=false][@focused=false][@index=0][@instance=0][@long-clickable=fa
lse][@package=com.houzz.app][@password=false][@resource-id=][@scrollable=false][@selected=false][@text=]
...........

Element: 'android.view.View'
Xpath: //hierarchy/android.widget.FrameLayout/android.view.View[@bounds=[0,1794][1080,1920]][@checkable=false][@checked=false][@class=android.view.View][@clickable=false][@content-desc=][@enabled=true][@focusable=false][@focused=false][@index=1][@instance=3][@long-
clickable=false][@package=com.houzz.app][@password=false][@resource-id=android:id/navigationBarBackground][@scrollable=false][@selected=false][@text=]
```


