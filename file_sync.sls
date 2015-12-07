/etc/security/limits.conf:
  file:
    - managed
    - source: salt://pkg/online/watch/limits.conf
    - mode: 0755

/etc/sysctl.conf:
  file:
    - managed
    - source: salt://pkg/online/watch/sysctl.conf
    - mode: 0644

/etc/ld.so.conf:
  file:
    - managed
    - source: salt://pkg/online/watch/ld.so.conf
    - mode: 0644

ldconfig:
  cmd:
    - wait
    - watch:
      - file: /etc/ld.so.conf

/usr/local/openresty/:
  file:
    - recurse
    - source: salt://pkg/online/openresty/
    - dir_mode: 0755
    - file_mode: 0755


/etc/logrotate.d/nginx:
  file:
    - managed
    - source: salt://pkg/online/watch/nginx.logrotate


/etc/init.d/680rtmpd:
  file:
    - managed
    - source: salt://pkg/online/watch/680rtmpd
    - mode: 0755

/etc/init.d/680html5d:
  file:
    - managed
    - source: salt://pkg/online/watch/680html5d
    - mode: 0755

/etc/rc.d/chk680server_localcore.sh:
  file:
    - managed
    - source: salt://pkg/online/watch/chk680server_localcore.sh
    - mode: 0755

/etc/rc.d/chk680server_edge.sh:
  file:
    - managed
    - source: salt://pkg/online/watch/chk680server_edge.sh
    - mode: 0755
{% if 'LIVE-TT' in grains['id'] %}           //111
/usr/local/680/:
  file:
    - recurse
    - source: salt://pkg/online/680_TT/
    - dir_mode: 0755
    - file_mode: 0755
/etc/init.d/680localcored4000:
  file:
    - managed
    - source: salt://pkg/online/watch/680localcored4000
    - mode: 0755
/etc/init.d/680localcored5000:
  file:
    - managed
    - source: salt://pkg/online/watch/680localcored5000
    - mode: 0755
/etc/init.d/680localcored6000:
  file:
    - managed
    - source: salt://pkg/online/watch/680localcored6000
    - mode: 0755

{% else %}                                  //111
/usr/local/680/:
  file:
    - recurse
    - source: salt://pkg/online/680/
    - dir_mode: 755
    - file_mode: 755
/etc/init.d/680localcored:
  file:
    - managed
{% if '172.16.0.254' in grains['ipv4'] %}
    - source: salt://pkg/online/watch/680localcored
{% else %}
    - source: salt://pkg/online/watch/680localcored
{% endif %}
    - mode: 0755

{% endif%}                              //111

{% if grains['isp'] == '6rooms'%}       //222

{% if '172.16.0.254' in grains['ipv4'] %}
/etc/rc.d/ngx_socket.sh:
  file:
    - managed
    - source: salt://pkg/online/watch/ngx_socket.sh.local
    - mode: 0755
/var/spool/cron/root:
  file:
    - managed
    - source: salt://pkg/online/watch/crontab.root.localcore
    - mode: 0644
{% else %}
/etc/rc.d/ngx_socket.sh:
  file:
    - managed
    - source: salt://pkg/online/watch/ngx_socket.sh
    - mode: 0755
/var/spool/cron/root:
  file:
    - managed
    - source: salt://pkg/online/watch/crontab.root.watch
    - mode: 0644
{% endif %}


{% if 'LIVE-CUC' in grains['id'] %}
/etc/hosts:
  file:
    - managed
{% if '172.16.0.254' in grains['ipv4'] %}
    - source: salt://hosts/hosts_ltzz
{% else %}
    - source: salt://hosts/hosts_ltgk
{% endif %}
    - mode: 0644
{% elif 'LIVE-CTC' in grains['id'] %}
/etc/hosts:
  file:
    - managed
{% if '172.16.0.254' in grains['ipv4'] %}
    - source: salt://hosts/hosts_dxzz
{% else %}
    - source: salt://hosts/hosts_dxgk
{% endif %}
    - mode: 0644
{% else %}
/etc/hosts:
  file:
    - managed
{% if '172.16.0.254' in grains['ipv4'] %}
    - source: salt://hosts/hosts_ltzz
{% else %}
    - source: salt://hosts/hosts_ltgk
{% endif %}
    - mode: 0644
{% endif %}

{% else %}

{% if grains['islocalcore'] == True %}
/etc/rc.d/ngx_socket.sh:
  file:
    - managed
    - source: salt://pkg/online/watch/ngx_socket.sh.local
    - mode: 0755
/var/spool/cron/root:
  file:
    - managed
    - source: salt://pkg/online/watch/crontab.root.localcore
    - mode: 0644
{% else %}
/etc/rc.d/ngx_socket.sh:
  file:
    - managed
    - source: salt://pkg/online/watch/ngx_socket.sh
    - mode: 0755
/var/spool/cron/root:
  file:
    - managed
    - source: salt://pkg/online/watch/crontab.root.watch
    - mode: 0644
{% endif %}

{% endif %}

/usr/local/680/crtmpserver_dev_intel/builders/cmake/crtmpserver/crtmpserver_localcore.lua:
  file:
    - managed
{% if 'LIVE-CUC' in grains['id'] %}
    - source: salt://pkg/online/680/crtmpserver_dev_intel/builders/cmake/crtmpserver/crtmpserver_localcore.lua.cuc
{% elif 'LIVE-CTC' in grains['id'] %}
    - source: salt://pkg/online/680/crtmpserver_dev_intel/builders/cmake/crtmpserver/crtmpserver_localcore.lua.ctc
{% else %}
    - source: salt://pkg/online/680/crtmpserver_dev_intel/builders/cmake/crtmpserver/crtmpserver_localcore.lua.cuc
{% endif %}


log:
  cmd.run:
    - name: "echo [`date '+%Y.%m.%d %H:%M:%S'`] Sync Live-watch conf files successfully by salt >> /usr/local/work/SixRooms"
    - onlyif: test -f /usr/local/work/SixRooms
