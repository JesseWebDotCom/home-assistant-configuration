# REMOTE ACCESS

- [Duck DNS & Let's Encrypt](#duck-dns--lets-encrypt)
- [Router Configuration](#router-configuration)
  - [VPN](#vpn)
  - [Port Forwarding](#port-forwarding)
- [Nuba Casa](#nuba-casa)

To connect to your Home Assistant instance from outside your home network, you need:
- A fixed IP address or domain name (ex. my-ha.example.com)
- A valid SSL certificate (to encrypt communications)
- VPN or forwarded ports

## Duck DNS & Let's Encrypt

[Duck DNS](https://www.duckdns.org) gives you a free subdomain name (ex. your-choice.duckdns.org) while [Let's Encrypt](https://letsencrypt.org) gives you a free SSL certificate.  

1. Follow [these instructions](https://github.com/home-assistant/hassio-addons/blob/master/duckdns/README.md) to install and setup the Duck DNS and Let's Encrypt.
2. Ensure your Duck DNS add-on config looks like the below (replacing `YOUR_DUCK_DNS_TOKEN` and `YOUR_DUCK_DNS_SUBDMOAIN` appropriately):
```yaml
lets_encrypt:
  accept_terms: true
  certfile: fullchain.pem
  keyfile: privkey.pem
token: YOUR_DUCK_DNS_TOKEN
domains:
  - YOUR_DUCK_DNS_SUBDOMAIN.duckdns.org
seconds: 300
```
1. Ensure the HTTP section of your config/configuration.yaml looks like the below (replacing `YOUR_DUCK_DNS_SUBDMOAIN` appropriately):
```yaml
http:
  base_url: YOUR_DUCK_DNS_SUBDOMAIN.duckdns.org:8123
  ssl_certificate: /ssl/fullchain.pem
  ssl_key: /ssl/privkey.pem  
```  

## Router Configuration
Your home router likely has a firewall preventing people outside of your home to connect into your home.  While this is great for security, you'll need to make some changes to allow secure, remote access to your Home Assistant instance.  Since everyone's router is different, I'll outline the options and you'll need to consult your router's manual for how to implement them.

### VPN
A [VPN](https://en.wikipedia.org/wiki/Virtual_private_network) is the securest option, listed here, to remotely connect back to your home.  It also allows you to connect to all home resources, as opposed to just your Home Assistant server.  It does however require significantly more setup on your home router and on any device that will connect back to your home (ex. your phone, your spouse's phone, etc).

### Port Forwarding
[Port forwarding](https://en.wikipedia.org/wiki/Port_forwarding) is the easiest and most common way to remotely connect back to your Home Assistant server.  After its setup, you simply enter your domain name into the Home Assistant companion or web browser (you cal also enter your router's public IP if you know it).  

This ease of use comes with some security risk (as anyone who know your domain name or router's public IP can now access your Home Assistant server).

## Nuba Casa
You can avoid dealing with Dynamic DNS, SSL Certificates, and port forwarding by using a paid subscription to [Nuba Casa](https://www.nabucasa.com) (aka Home Assistant Cloud).  This subscription also helps support the core Home Assistant development team.

***

[Previous](backups.md) | [Next](../esphome-led-sensors/esphome.md) |
[Table of Contents](../README.md#table-of-contents)