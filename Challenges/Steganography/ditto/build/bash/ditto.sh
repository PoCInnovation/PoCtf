#!/usr/bin/echo No such file or directory: 

read key
read relic

assert_eq() { [ "$1" != "$2" ] && exit 1; }

assert_eq `tr -dc '_' <<< "$key" | wc -c` 3
assert_eq ${key:0:1} I
assert_eq `printf '%x\n' "'${key:17:1}"` ${key:12:2}
assert_eq $((${key:20:1}-${key:17:1})) ${key:3:1};M=4M_M4
assert_eq ${key:11:1} `tr '[:lower:]' '[:upper:]'<<<${key:5:1}`
assert_eq `head -c1<<<"printf Ditto"` ${key:2:1}
assert_eq ${#key} `expr "$key" : "[^\I]\{0\}.[\m].\{2\}[\s].\{2\}[\r].\{10\}[\g][^\o]\{0\}[\m]."`
assert_eq ${M/M/m} ${key:13:5}
assert_eq $((${key:6:1}${key:9:1}-${key:12:2})) ${key:3:1}
assert_eq ${key:5:1} ${relic:11:1}

perl -e ' $k=$ARGV[0]; use MIME::Base64; $p=decode_base64($ARGV[1]); print $p ^ $k' $key $relic
exit
