Summary:	Program which makes cpio-format archives
Summary(pl):	Pakiet zawiera program do tworzenia archiwów w formacie cpio
Name:		afio
Version:	2.4.7
Release:	1
License:	Freeware
Group:		Applications/Archiving
Source0:	http://www.ibiblio.org/pub/linux/system/backup/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afio is best used as an 'archive engine' in a backup script. It can
make compressed archives that are much safer than compressed tar or
cpio archives because it deals somewhat gracefully with input data
corruption and supports multi-volume archives.

This version has been patched to handle remote tape drives exactly the
same as GNU tar - ie you can specify the backup file as
"user@machine:/dev/tape".

%description -l pl
Afio jest programem u¿ywanym przez skrypty tworz±ce kopie zapasowe.
Potrafi tworzyæ kompresowane archiwa, które s± bardziej bezpieczne niz
kopie tworzone za pomoc± programów tar lub cpio poniewa¿ umie poradziæ
sobie z uszkodzonymi danymi. Mo¿na tym programem tworzyæ tak¿e
wielowolumenowe kopie zapasowe.

Program ten zosta³ poprawiony, by mo¿na by³o wyspecyfikowaæ zdalne
urz±dzenie kopii zapasowej tak jak w programie GNU tar, np.:
"user@machine:/dev/tape".

%prep
%setup  -q

%build
%{__make} clean
%{__make} CFLAGS1="-Wformat -fomit-frame-pointer \
	%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}}

install afio $RPM_BUILD_ROOT%{_bindir}
install afio.1* $RPM_BUILD_ROOT%{_mandir}/man1
mv -f script* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf afio.lsm HISTORY SCRIPTS README PORTING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/afio
%{_mandir}/man1/afio.*
%{_examplesdir}/%{name}
