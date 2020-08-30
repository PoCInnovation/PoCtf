#!/usr/bin/bash

key="Imp0st3r_4_T34m_M4gm4"
relic='I_l0v3_Br0di3'

xenc () {
    perl -e '$p=$ARGV[0]; $k=$ARGV[1]; use MIME::Base64; print encode_base64($p ^ $k)' $1 $2
}

xdec () {
    perl -e '$k=$ARGV[0]; use MIME::Base64; $p=decode_base64($ARGV[1]); print $p ^ $k' $1 $2
}

xdec $key `xenc $key $relic`
echo -e "\n"`xenc $key $relic`
