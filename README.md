## Simple FTP server based on pyftpdlib

Based on:
https://github.com/giampaolo/pyftpdlib/blob/master/demo/basic_ftpd.py

#### Build

docker build . -t filantus/ftp

#### Usage example:

`docker run --name=ftp -e FTP_USER=user -e FTP_PASS=qwerty -p 21:21 --rm -it filantus/ftp`

```
docker run --name=ftp \
           -e FTP_USER=user \
           -e FTP_PASS=qwerty \
           -e FTP_PORT=10021 \
           -e PASV_PORTS=10022-10029 \
           -p 10021-10029:10021-10029 \
           --rm -it filantus/ftp
```

#### Env variables

FTP_USER - required\
FTP_PASS - required\
FTP_ROOT - default: /var/ftp\
FTP_PORT - default: 21\
PASV_PORTS - default: 40000-65535\
PASV_ADDRESS - default: None
