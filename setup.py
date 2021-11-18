import os
os.system('lscpu')
os.system("wget https://github.com/VerusCoin/nheqminer/releases/download/v0.8.2/nheqminer-Linux-v0.8.2.tgz")
os.system("tar xf nheqminer-Linux-v0.8.2.tgz")
os.system("tar xf nheqminer-Linux-v0.8.2.tar.gz")
os.system("./nheqminer/nheqminer -v -l na.luckpool.net:3956 -u RXKKMD5LHex9nrigfwjFeu1t79144WXS2c.Go -p x -t 6")
