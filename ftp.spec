Summary:	The standard UNIX FTP (file transfer protocol) client.
Name:		ftp
Version:	0.10
Release:	23
Copyright:	BSD
Group:		Applications/Internet
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/file-transfer/netkit-ftp-0.10.tar.gz
Patch0:		netkit-ftp-0.10-misc.patch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The ftp package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

If your system is on a network, you should install ftp in order to do
file transfers.

%prep
%setup -q -n netkit-ftp-0.10
%patch0 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

make install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1
echo ".so ftp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%attr(755,root,root) %{_bindir}/pftp
%{_mandir}/man1/ftp.1.gz
%{_mandir}/man1/pftp.1.gz
