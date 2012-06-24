Summary:	The standard UNIX FTP (file transfer protocol) client.
Summary(de):	Standardm��iger Unix-ftp-Client (file transfer protocol) 
Summary(fr):	Client ftp (file transfer protocol) standard d'Unix
Summary(tr):	Standart UN*X ftp istemcisi
Name:		ftp
Version:	0.15
Release:	2
Copyright:	BSD
Group:		Applications/Internet
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/file-transfer/netkit-ftp-%{version}.tar.gz
Source1:	ftp.1.pl
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The ftp package provides the standard UNIX command-line FTP client. FTP is
the file transfer protocol, which is a widely used Internet protocol for
transferring files and for archiving files.

%description -l de
Dadurch wird der Standard-Unix-Befehlszeilen-FTP-Client bereitgestellt.  ftp
ist das Standard-Internet-Dateitransfer-Protokoll, das sich sowohl f�r
Dateiarchive als auch f�r Dateitransfers zwischen Individuen gro�er
Beliebtheit erfreut.

%description -l fr
Contient le client ftp en ligne de commande standard d'Unix. ftp est le
protocole standard de transfert de fichiers sur l'Internet. Il est tr�s
utilis� pour les archives et les transferts de fichiers entre individus.

%description -l tr
Bu pakette UN*X'in standart komut sat�r� ftp istemcisi bulunmaktad�r. Ger�i
grafik arabirimlerin egemen oldu�u bir �a�da biraz demode gibi g�z�kebilir
ancak anonim dosya ar�ivleri ve ki�iler aras� dosya iletimi i�in hala yayg�n
olarak kullan�lmaktad�r.

%prep
%setup -q -n netkit-ftp-%{version}

%build
make CFLAGS="$RPM_OPT_FLAGS -Wall -W -Wpointer-arith -Wbad-function-cast \
	-Wcast-qual -Wstrict-prototypes -Wmissing-prototypes \
	-Wmissing-declarations -Wnested-externs -Winline -Wcast-align" \
	USE_READLINE=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}}

make install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/ftp.1

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1
echo ".so ftp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1

echo ".so ftp.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/pftp.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/{man1/*,pl/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%attr(755,root,root) %{_bindir}/pftp
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
