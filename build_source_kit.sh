#!/bin/bash

cleanup_and_exit()
{
    echo $tmpdir | grep "/tmp/"
    if [ $? -ne 0 ]; then 
	echo "Error: tmpdir ($tmpdir) is invalid."
	exit 1
    fi
    rm -rf $tmpdir
    exit $1
}

if [ -d ./release ]; then
    echo "Error: Please run make clean before running this script."
    exit 1
fi

printf "Making temporary directory..."
tmpdir=`mktemp -d`
if [ $? -ne 0 ]; then
    echo "Error: Unable to create temp directory in /tmp"
    exit 1
fi
echo " $tmpdir/dsc."
mkdir -p $tmpdir/dsc
echo "Copying current directory to $tmpdir/dsc."
cp -R ./* $tmpdir/dsc
cd $tmpdir/dsc

echo `pwd` | grep "/tmp/"
if [ $? -ne 0 ]; then
    echo "Error: Unable to change directory to $tmpdir/dsc"
    cleanup_and_exit 1
fi

echo "Removing unwanted files."
# Remove omi symlink
if [ -h ./omi-1.0.8 ]; then
    rm omi-1.0.8
fi

# Remove unwanted base directories
rm -rf ./bootstrap ./build ./build_source_kit.sh ./doc ./ext ./installbuilder ./Test

# Remove blue win7 win8
rm -rf ./LCM/codec/mof/blue ./LCM/codec/mof/win7 ./LCM/codec/mof/win8

# Remove tests
rm -rf ./LCM/dsc/tests

# Remove cs files
rm -rf ./LCM/dsc/engine/ca/psinfrastructure/PsPluginManager.cs

# Remove module providers
rm -rf ./Providers/nxDNS* ./Providers/nxIPAddress ./Providers/nxFirewall ./Providers/nxComputer

# Remove scripts associated with above providers
rm -rf ./Providers/Scripts/2.4x-2.5x/Scripts/nxDNSServerAddress.py ./Providers/Scripts/2.6x-2.7x/Scripts/nxDNSServerAddress.py ./Providers/Scripts/3.x/Scripts/nxDNSServerAddress.py ./Providers/Scripts/2.4x-2.5x/Scripts/nxComputer.py ./Providers/Scripts/2.6x-2.7x/Scripts/nxComputer.py ./Providers/Scripts/3.x/Scripts/nxComputer.py ./Providers/Scripts/2.4x-2.5x/Scripts/nxIPAddress.py ./Providers/Scripts/2.6x-2.7x/Scripts/nxIPAddress.py ./Providers/Scripts/3.x/Scripts/nxIPAddress.py ./Providers/Scripts/2.4x-2.5x/Scripts/nxFirewall.py ./Providers/Scripts/2.6x-2.7x/Scripts/nxFirewall.py ./Providers/Scripts/3.x/Scripts/nxFirewall.py

# Remove tests associated with above providers
rm -rf ./Providers/Scripts/2.4x-2.5x/Scripts/Tests ./Providers/Scripts/2.6x-2.7x/Scripts/Tests ./Providers/Scripts/3.x/Scripts/Tests

# sed out Makefile stuff for Providers removed
cat ./Providers/Makefile \
    | sed "s@PROVIDERS+=nxDNSServerAddress@#PROVIDERS+=nxDNSServerAddress@" \
    | sed "s@PROVIDERS+=nxComputer@#PROVIDERS+=nxComputer@" \
    | sed "s@PROVIDERS+=nxIPAddress@#PROVIDERS+=nxIPAddress@" \
    | sed "s@PROVIDERS+=nxFirewall@#PROVIDERS+=nxFirewall@" \
    > ./tmp_makefile
mv -f ./tmp_makefile ./Providers/Makefile


# add "BUILD_LOCAL=1" to configure
sed '2 aBUILD_LOCAL=1' ./configure > ./tmp_configure
mv -f ./tmp_configure ./configure
chmod +x ./configure

# Remove stuff from Providers/Extras
rm -rf ./Providers/Extras/Config* ./Providers/Extras/Exampl* ./Providers/Extras/Provider* ./Providers/Extras/Scripts/*.ps1 ./Providers/Extras/Threat* ./Providers/Extras/Window* ./Providers/Extras/nx*/nxComputer* ./Providers/Extras/nx*/nxNetworking*

rm -f `find . -name "*~"`
rm -f `find . -name .tpattributes`

cd ..
tar --numeric-owner -c -z -f /tmp/PSDSC.tar.gz ./dsc
if [ $? -eq 0 ]; then
    echo "Created tarball at /tmp/PSDSC.tar.gz"
else
    echo "Error: Unable to create tarball."
    exit 1
fi
cleanup_and_exit 0
