Disable AAAA lookups in Unbound DNS
--------------------

### Set up machine

	vagrant up


### Testing

1st `vagrant ssh` session:

	vagrant@precise64:~$ sudo unbound -dv -c /etc/unbound/unbound.conf


2nd `vagrant ssh` session:

	vagrant@precise64:~$ dig google.com AAAA @8.8.8.8
	vagrant@precise64:~$ dig google.com AAAA @localhost

*Run above commands twice and check query time.*


### Production
 - Point resolv.conf to 127.0.0.1
 - unbound.conf: Proper logfile, lower verbosity
 - Uncomment `auto-trust-anchor-file` for DNSSEC support


### Version

	vagrant@precise64:~$ lsb_release -a
	No LSB modules are available.
	Distributor ID:	Ubuntu
	Description:	Ubuntu 12.04 LTS
	Release:	12.04
	Codename:	precise
	
	vagrant@precise64:~$ unbound -h
	Version 1.4.16
	linked libs: libevent 2.0.16-stable (it uses epoll), ldns 1.6.11, OpenSSL 1.0.1 14 Mar 2012
	linked modules: python validator iterator
	configured for x86_64-unknown-linux-gnu on Wed Feb  8 05:48:44 UTC 2012 with options: '--prefix=/usr' '--sysconfdir=/etc' '--disable-rpath' '--with-pidfile=/var/run/unbound.pid' '--with-libevent' '--with-pythonmodule' '--with-pyunbound'
