# vyos-dns-ipv6-generator-ansible
Ansible-based Generator for AAAA and PTR entries (for BIND zonefile) from VyOS config 

This is quite a simple and unpolished script based on vyos-dns-ipv6-generator



First, You must add your VyOS routers to your Ansible hosts file under "vyos_routers". You can then run the playbook "ansible-playbook.yml" in order to copy all the router configs to the vyos_configs folder.
Then go to the folder, ensure you update your FQDN and prefix under "pytodns_cfg.py". Example:

```
#put your FQDN, here is mine
fqdn = "compumundohipermegared.one."

#now the uncompressed starting hextets of your prefix, example is mine.
prefix_sel = "2a0e:8f02:21d"
```

Then just run "dns_generator.py". Example output from it:

```
----FORWARD ZONE----
dum0.OSR1GLASS1    IN AAAA    2a0e:8f02:21d0:ffff::90
eth2.OSR1GLASS1    IN AAAA    2a0e:8f02:21d1:dead::90
eth3.OSR1GLASS1    IN AAAA    2a0e:8f02:21d0:f00d::2:52
eth4.OSR1GLASS1    IN AAAA    2a0e:8f02:21d0:f00d::2:62
----FORWARD ZONE----
----REVERSE ZONE----
0.9.0.0.0.0.0.0.0.0.0.0.0.0.0.0.f.f.f.f.0.d.1.2.2.0.f.8.e.0.a.2.ip6.arpa.    IN PTR dum0.OSR1GLASS1.compumundohipermegared.one.
0.9.0.0.0.0.0.0.0.0.0.0.0.0.0.0.d.a.e.d.1.d.1.2.2.0.f.8.e.0.a.2.ip6.arpa.    IN PTR eth2.OSR1GLASS1.compumundohipermegared.one.
2.5.0.0.2.0.0.0.0.0.0.0.0.0.0.0.d.0.0.f.0.d.1.2.2.0.f.8.e.0.a.2.ip6.arpa.    IN PTR eth3.OSR1GLASS1.compumundohipermegared.one.
2.6.0.0.2.0.0.0.0.0.0.0.0.0.0.0.d.0.0.f.0.d.1.2.2.0.f.8.e.0.a.2.ip6.arpa.    IN PTR eth4.OSR1GLASS1.compumundohipermegared.one.
----REVERSE ZONE----
```

Quite easy :) Now you have easy copy-paste lines for your BIND Zonefile.
