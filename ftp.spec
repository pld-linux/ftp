Summary: The standard UNIX FTP (file transfer protocol) client.
Name: ftp
Version: 0.10
Release: 22
Copyright: BSD
Group: Applications/Internet
Source0: ftp://sunsite.unc.edu/pub/Linux/system/network/file-transfer/netkit-ftp-0.10.tar.gz
Patch0: netkit-ftp-0.10-misc.patch
Requires: inetd
BuildRoot: /var/tmp/%{name}-root

%description
The ftp package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

If your system is on a network, you should install ftp in order to do
file transfers.

%prep
%setup -n netkit-ftp-0.10
%patch0 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make INSTALLROOT=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/ftp
/usr/bin/pftp
/usr/man/man1/ftp.1
/usr/man/man1/pftp.1
