
## Cook diskimages from cmd line

**From [ciarand's blog](https://blog.ciarand.me/posts/using-dd-and-pv-on-osx/index.html)**

`sudo dd if=/dev/rdisk | pv -tpreb -s $(du -k /dev/rdisk | awk '{print $1}')k | sudo dd of=rfcraftserver.img bs=1m`

`sudo dd if=raspbian.img | pv -tpreb -s $(du -k raspbian.img | awk '{print $1}')k | sudo dd of=/dev/rdisk bs=1m`

`sudo dd if=rfcraftserver.img | pv -tpreb -s $(du -k rfcraftserver.img | awk '{print $1}')k | sudo dd of=/dev/rdisk bs=1m`
