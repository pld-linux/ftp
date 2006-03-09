Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(de):	Standardm��iger Unix-FTP-Client (file transfer protocol)
Summary(es):	Cliente FTP padr�n Unix (protocolo de transmisi�n de archivo)
Summary(fr):	Client FTP (file transfer protocol) standard d'Unix
Summary(pl):	Standardowy klient FTP (file transfer protocol)
Summary(pt_BR):	Cliente FTP padr�o Unix (protocolo de transmiss�o de arquivo)
Summary(ru):	����������� FTP (file transfer protocol) ������ Unix
Summary(tr):	Standart UN*X FTP istemcisi
Summary(uk):	����������� FTP (file transfer protocol) �̦��� Unix
Name:		ftp
Version:	0.17
Release:	23
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
Obsoletes:	inetutils-ftp
Obsoletes:	lukemftp
Obsoletes:	tnftp

%description
The FTP package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description -l de
Dadurch wird der Standard-Unix-Befehlszeilen-FTP-Client
bereitgestellt. FTP ist das Standard-Internet-Dateitransfer-Protokoll,
das sich sowohl f�r Dateiarchive als auch f�r Dateitransfers zwischen
Individuen gro�er Beliebtheit erfreut.

%description -l es
Este paquete provee el cliente FTP padr�n Unix para la l�nea de
comando. FTP es el protocolo padr�n de transferencia de archivos en
Internet, y es extremamente popular.

%description -l fr
Contient le client FTP en ligne de commande standard d'Unix.  est
FTP
le protocole standard de transfert de fichiers sur l'Internet. Il est
tr�s utilis� pour les archives et les transferts de fichiers entre
individus.

%description -l pl
Pakiet FTP udost�pnia standardowego klienta FTP obs�ugiwanego z linii
polece� jaki jest obecny w r�nych systemach uniksowych. FTP jest
protoko�em do przesy�ania plik�w (File Transfer Protocol), b�d�cym
jednym z cz�ciej u�ywanych protoko��w do przesy�ania i archiwizacji
plik�w mi�dzy komputerami w Internecie.

%description -l pt_BR
Este pacote prov� o cliente FTP padr�o Unix para a linha de comando. O
FTP � o protocolo padr�o de transfer�ncia de arquivos na Internet, e �
extremamente popular.

%description -l ru
����� FTP �������� ����������� FTP-������ Unix, ���������� ��
��������� ������. FTP - ��� ������ ������������ �������� ��� ��������
������ � ��������� � ��� ������������� ������.

%description -l tr
Bu pakette UN*X'in standart komut sat�r� FTP istemcisi bulunmaktad�r.
Ger�i grafik arabirimlerin egemen oldu�u bir �a�da biraz demode gibi
g�z�kebilir ancak anonim dosya ar�ivleri ve ki�iler aras� dosya
iletimi i�in hala yayg�n olarak kullan�lmaktad�r.

%description -l uk
����� FTP ͦ����� ����������� FTP-�̦��� Unix, ���� ������ �
���������� �����. FTP - �� ������ ���������������� �������� ���
������ަ ���̦� � �������Ԧ �� ��� ��Ȧ��æ� ���̦�.

%package pftp
Summary:	Passive mode FTP client
Summary(pl):	Tryb pasywny klienta FTP
Group:		Applications/Networking
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	%{name} >= 0.17-13
Conflicts:	pftp

%description pftp
This package contains a symlink to the FTP client used to call the
client in passive mode.

%description pftp -l pl
Pakiet ten zawiera dowi�zanie do klienta FTP, wywo�uj�ce go w trybie
pasywnym.

%prep
%setup -q -n netkit-ftp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CFLAGS="%{rpmcflags}" \
./configure \
	--with-c-compiler="%{__cc}"
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
