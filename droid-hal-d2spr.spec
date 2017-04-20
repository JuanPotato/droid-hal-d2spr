%define device d2spr
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy S3 Sprint

%define straggler_files \
/initlogo.rle\
%{nil}

%define installable_zip 1
%include rpm/dhd/droid-hal-device.inc
