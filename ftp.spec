Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(de):	Standardmäßiger Unix-ftp-Client (file transfer protocol)
Summary(fr):	Client ftp (file transfer protocol) standard d'Unix
Summary(pl):	Standardowy klient ftp (file transfer protocol)
Summary(tr):	Standart UN*X ftp istemcisi
Name:		ftp
Version:	0.17
Release:	1
License:	BSD
Group:		Applications/Networking
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
Source1:	ftp.1.pl
Patch0:		netkit-ftp-macro-quit.patch
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	lukemftp

%description
The ftp package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description -l de
Dadurch wird der Standard-Unix-Befehlszeilen-FTP-Client
bereitgestellt. Ftp ist das Standard-Internet-Dateitransfer-Protokoll,
das sich sowohl für Dateiarchive als auch für Dateitransfers zwischen
Individuen großer Beliebtheit erfreut.

%description -l fr
Contient le client ftp en ligne de commande standard d'Unix. ftp est
le protocole standard de transfert de fichiers sur l'Internet. Il est
très utilisé pour les archives et les transferts de fichiers entre
individus.

%description -l pl
Pakiet ftp udostêpnia standardowego klienta FTP obs³ugiwanego z linii
poleceñ jaki jest obecny w ró¿nych systemach uniksowych. FTP jest
ptotoko³em do przesy³ania plików (File Transfer Protocol), bêd±cym
jednym z czê¶ciej u¿ywanych protoko³ów do przesy³ania i archiwizacji
plików miêdzy komputerami w Internecie.

%description -l tr
Bu pakette UN*X'in standart komut satýrý ftp istemcisi bulunmaktadýr.
Gerçi grafik arabirimlerin egemen olduðu bir çaðda biraz demode gibi
gözükebilir ancak anonim dosya arþivleri ve kiþiler arasý dosya
iletimi için hala yaygýn olarak kullanýlmaktadýr.

%prep
%setup -q -n netkit-ftp-%{version}
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
LDFLAGS="-s" \
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}}

%{__make} install \
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
