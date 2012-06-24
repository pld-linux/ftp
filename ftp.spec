Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(de):	Standardm��iger Unix-ftp-Client (file transfer protocol)
Summary(fr):	Client ftp (file transfer protocol) standard d'Unix
Summary(pl):	Standardowy klient ftp (file transfer protocol)
Summary(tr):	Standart UN*X ftp istemcisi
Name:		ftp
Version:	0.17
Release:	8
License:	BSD
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	ftp://ftp.linux.org.uk/pub/linux/Networking/netkit/netkit-%{name}-%{version}.tar.gz
Source1:	%{name}.1.pl
Patch0:		netkit-%{name}-macro-quit.patch
BuildRequires:	ncurses-devel >= 5.2
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	lukemftp

%description
The ftp package provides the standard UNIX command-line FTP client.
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description -l de
Dadurch wird der Standard-Unix-Befehlszeilen-FTP-Client
bereitgestellt. Ftp ist das Standard-Internet-Dateitransfer-Protokoll,
das sich sowohl f�r Dateiarchive als auch f�r Dateitransfers zwischen
Individuen gro�er Beliebtheit erfreut.

%description -l fr
Contient le client ftp en ligne de commande standard d'Unix. ftp est
le protocole standard de transfert de fichiers sur l'Internet. Il est
tr�s utilis� pour les archives et les transferts de fichiers entre
individus.

%description -l pl
Pakiet ftp udost�pnia standardowego klienta FTP obs�ugiwanego z linii
polece� jaki jest obecny w r�nych systemach uniksowych. FTP jest
ptotoko�em do przesy�ania plik�w (File Transfer Protocol), b�d�cym
jednym z cz�ciej u�ywanych protoko��w do przesy�ania i archiwizacji
plik�w mi�dzy komputerami w Internecie.

%description -l tr
Bu pakette UN*X'in standart komut sat�r� ftp istemcisi bulunmaktad�r.
Ger�i grafik arabirimlerin egemen oldu�u bir �a�da biraz demode gibi
g�z�kebilir ancak anonim dosya ar�ivleri ve ki�iler aras� dosya
iletimi i�in hala yayg�n olarak kullan�lmaktad�r.

%prep
%setup -q -n netkit-ftp-%{version}
%patch0 -p1

%build
CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}" \
./configure --with-c-compiler=gcc
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{,pl}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/ftp.1

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1
echo ".so ftp.1" > $RPM_BUILD_ROOT%{_mandir}/man1/pftp.1

echo ".so ftp.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/pftp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%attr(755,root,root) %{_bindir}/pftp
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
