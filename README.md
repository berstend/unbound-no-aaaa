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
