Summary:	Program which makes cpio-format archives
Summary(pl.UTF-8):	Pakiet zawiera program do tworzenia archiwów w formacie cpio
Name:		afio
Version:	2.5
Release:	3
License:	Artistic
Group:		Applications/Archiving
Source0:	http://www.ibiblio.org/pub/linux/system/backup/%{name}-%{version}.tgz
# Source0-md5:	8c6665e0f875dcd8e1bdb18644b59688
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afio is best used as an 'archive engine' in a backup script. It can
make compressed archives that are much safer than compressed tar or
cpio archives because it deals somewhat gracefully with input data
corruption and supports multi-volume archives.

This version has been patched to handle remote tape drives exactly the
same as GNU tar - ie you can specify the backup file as
"user@machine:/dev/tape".

%description -l pl.UTF-8
Afio jest programem używanym przez skrypty tworzące kopie zapasowe.
Potrafi tworzyć kompresowane archiwa, które są bardziej bezpieczne niż
kopie tworzone za pomocą programów tar lub cpio ponieważ potrafi
poradzić sobie z uszkodzonymi danymi. Można tym programem tworzyć
także wielowolumenowe kopie zapasowe.

Program ten został poprawiony, by można było wyspecyfikować zdalne
urządzenie kopii zapasowej tak jak w programie GNU tar, np.:
"user@machine:/dev/tape".

%prep
%setup  -q

%build
%{__make} clean
%{__make} \
	CC="%{__cc}" \
	CFLAGS1="-Wformat -fomit-frame-pointer -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

install afio $RPM_BUILD_ROOT%{_bindir}
install afio.1* $RPM_BUILD_ROOT%{_mandir}/man1
mv -f script* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc afio.lsm HISTORY SCRIPTS README PORTING
%attr(755,root,root) %{_bindir}/afio
%{_mandir}/man1/afio.*
%{_examplesdir}/%{name}-%{version}
