# htdetect.py

Used to detect if a web-server is using http, https or both. take domainlist as an input. (saparated by newline '\n')

### Uses :

* Download the script, and change the permission to executable file

```
$ chmod +x htdetect.py
```

* then run it as below 
```
$ cat domainList | ./htdetect.py
```
Output:
```
http://google.com
http://github.com
http://facebook.com
https://google.com
https://github.com
http://yandex.com
http://youtube.com
https://facebook.com
https://yandex.com
http://yahoo.com
https://youtube.com
https://yahoo.com
```
