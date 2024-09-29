#! /bin/sh

file=$1
tr '\n' ';\n' < "${file}" > "${file}".tmp && mv "${file}".tmp "${file}"