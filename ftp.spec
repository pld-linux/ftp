Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(de):	Standardmäßiger Unix-ftp-Client (file transfer protocol)
Summary(es):	Cliente ftp padrón Unix (protocolo de transmisión de archivo)
Summary(fr):	Client ftp (file transfer protocol) standard d'Unix
Summary(pl):	Standardowy klient ftp (file transfer protocol)
Summary(pt_BR):	Cliente ftp padrão Unix (protocolo de transmissão de arquivo)
Summary(ru):	óÔÁÎÄÁÒÔÎÙÊ FTP (file transfer protocol) ËÌÉÅÎÔ Unix
Summary(tr):	Standart UN*X ftp istemcisi
Summary(uk):	óÔÁÎÄÁÒÔÎÉÊ FTP (file transfer protocol) ËÌ¦¤ÎÔ Unix
Name:		ftp
Version:	0.17
Release:	21
License:	BSD
Group:		Applications/Networking
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
# Source0-md5:	94441610c9b86ef45c4c6ec609444060
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	5f8919e12c6878fa538a339f3ff2095d
Source2:	%{name}.desktop
Source3:	%{name}.png
Patch0:		netkit-%{name}-macro-quit.patch
Patch1:		netkit-%{name}-acct.patch
Patch2:		netkit-%{name}-usagi-ipv6.patch
Patch3:		netkit-%{name}-input_line.patch
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	lukemftp
Obsoletes:	tnftp

%description
The ftp package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description -l de
Dadurch wird der Standard-Unix-Befehlszeilen-FTP-Client
bereitgestellt. Ftp ist das Standard-Internet-Dateitransfer-Protokoll,
das sich sowohl für Dateiarchive als auch für Dateitransfers zwischen
Individuen großer Beliebtheit erfreut.

%description -l es
Este paquete provee el cliente ftp padrón Unix para la línea de
comando. ftp es el protocolo padrón de transferencia de archivos en
Internet, y es extremamente popular.

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

%description -l pt_BR
Este pacote provê o cliente ftp padrão Unix para a linha de comando. O
ftp é o protocolo padrão de transferência de arquivos na Internet, e é
extremamente popular.

%description -l ru
ðÁËÅÔ ftp ÓÏÄÅÒÖÉÔ ÓÔÁÎÄÁÒÔÎÙÊ FTP-ËÌÉÅÎÔ Unix, ÒÁÂÏÔÁÀÝÉÊ ÉÚ
ËÏÍÁÎÄÎÏÊ ÓÔÒÏËÉ. FTP - ÜÔÏ ÛÉÒÏËÏ ÉÓÐÏÌØÚÕÅÍÙÊ ÐÒÏÔÏËÏÌ ÄÌÑ ÐÅÒÅÄÁÞÉ
ÆÁÊÌÏ× × éÎÔÅÒÎÅÔÅ É ÄÌÑ ÁÒÈÉ×ÉÒÏ×ÁÎÉÑ ÆÁÊÌÏ×.

%description -l tr
Bu pakette UN*X'in standart komut satýrý ftp istemcisi bulunmaktadýr.
Gerçi grafik arabirimlerin egemen olduðu bir çaðda biraz demode gibi
gözükebilir ancak anonim dosya arþivleri ve kiþiler arasý dosya
iletimi için hala yaygýn olarak kullanýlmaktadýr.

%description -l uk
ðÁËÅÔ ftp Í¦ÓÔÉÔØ ÓÔÁÎÄÁÒÔÎÉÊ FTP-ËÌ¦¤ÎÔ Unix, ÑËÉÊ ÐÒÁÃÀ¤ Ú
ËÏÍÁÎÄÎÏÇÏ ÒÑÄËÁ. FTP - ÃÅ ÛÉÒÏËÏ ×ÉËÏÒÉÓÔÏ×Õ×ÁÎÉÊ ÐÒÏÔÏËÏÌ ÄÌÑ
ÐÅÒÅÄÁÞ¦ ÆÁÊÌ¦× × ¶ÎÔÅÒÎÅÔ¦ ÔÁ ÄÌÑ ÁÒÈ¦×ÁÃ¦§ ÆÁÊÌ¦×.

%package pftp
Summary:	Passive mode FTP client
Summary(pl):	Tryb pasywny klienta ftp
Group:		Applications/Networking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	%{name} >= 0.17-13
Conflicts:	pftp

%description pftp
This package contains a symlink to the FTP client used to call the
client in passive mode.

%description pftp -l pl
Pakiet ten zawiera dowi±zanie do klienta FTP, wywo³uj±ce go w trybie
pasywnym.

%prep
%setup -q -n netkit-ftp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CFLAGS="%{rpmcflags}" \
./configure --with-c-compiler=%{__cc}
%{__make} LIBTERMCAP=-ltinfo CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1
echo ".so ftp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*
%{_mandir}/man5/netrc.5*
%lang(ja) %{_mandir}/ja/man1/ftp.1*
%lang(pl) %{_mandir}/pl/man1/ftp.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/ftp.1*
%{_desktopdir}/*
%{_pixmapsdir}/*

%files pftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pftp
%{_mandir}/man1/pftp*
%lang(ja) %{_mandir}/ja/man1/pftp.1*
%lang(pl) %{_mandir}/pl/man1/pftp.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/pftp.1*
