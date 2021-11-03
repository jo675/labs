## Dropbear SSH

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

Dropbear is a relatively small SSH server and client. It runs on a variety of unix platforms. Dropbear is open source software, distributed under a MIT-style license. Dropbear is particularly useful for "embedded"-type Linux (or other Unix) systems, such as wireless routers.

## Features

- A small memory footprint suitable for memory-constrained environments – Dropbear can compile to a 110kB statically linked binary with uClibc on x86 (only minimal options selected)
- Dropbear server implements X11 forwarding, and authentication-agent forwarding for OpenSSH clients
- Can run from inetd or standalone
- Compatible with OpenSSH ~/.ssh/authorized_keys public key authentication
- The server, client, keygen, and key converter can be compiled into a single binary (like busybox)
- Features can easily be disabled when compiling to save space
- Multi-hop mode uses SSH TCP forwarding to tunnel through multiple SSH hosts in a single command. dbclient user1@hop1,user2@hop2,destination

## Platforms

- Linux – standard distributions, uClibc, dietlibc, musl libc, uClinux from inetd
- Mac OS X (compile with PAM support)
- FreeBSD, NetBSD and OpenBSD
- Solaris – tested v8 x86 and v9 Sparc
- IRIX 6.5 (with /dev/urandom, or prngd should work)
- Tru64 5.1 (using prngd for entropy)
- AIX 4.3.3 (with gcc and Linux Affinity Toolkit), AIX 5.2 (with /dev/urandom).
- HPUX 11.00 (+prngd), TCP forwarding doesn't work
- Cygwin – tested 1.5.19 on Windows XP

## Tech

Dillinger uses a number of open source projects to work properly:

- [Dropbear SSH] - lightweight SSH server

## Installation

Install dropbear.

```sh
root@dev:~# apt install dropbear
Reading package lists... Done
Building dependency tree
Reading state information... Done
dropbear is already the newest version (2019.78-2build1).
0 upgraded, 0 newly installed, 0 to remove and 28 not upgraded.
```

## Configuration

Change the target port to 30042.

```sh
root@dev:~# nano /etc/default/dropbear
```

Confirm it's been changed.

```sh
root@dev:~# cat /etc/default/dropbear | grep  DROPBEAR_PORT
DROPBEAR_PORT=30042
```

Restart for change to take effect.

```sh
root@dev:~# systemctl restart dropbear
```

Open port 30042 for incoming connections using ufw.

```sh
root@dev:~# apt install ufw
Reading package lists... Done
Building dependency tree
Reading state information... Done
ufw is already the newest version (0.36-6).
ufw set to manually installed.
0 upgraded, 0 newly installed, 0 to remove and 28 not upgraded.
```

```sh
root@dev:~# ufw allow 30042/tcp
Rule added
Rule added (v6)
```

```sh
root@dev:~# ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
```


   [Dropbear SSH]: https://matt.ucc.asn.au/dropbear/dropbear.html
