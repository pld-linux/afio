Summary:	Program which makes cpio-format archives
Summary(pl):	Pakiet zawiera program do tworzenia archiwów w formacie cpio
Name:		afio
Version:	2.4.5
Release:	8
License:	Freeware
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/Backup/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Afio is best used as an 'archive engine' in a backup script. It can
make compressed archives that are much safer than compressed tar or
cpio archives because it deals somewhat gracefully with input data
corruption and supports multi-volume archives.

This version has been patched to handle remote tape drives exactly the
same as GNU tar - ie you can specify the backup file as
"user@machine:/dev/tape".

%prep
%setup  -q

%build
%{__make} clean
%{__make} CFLAGS1="-Wformat -fomit-frame-pointer \
	%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"

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
%doc *,gz
%attr(755,root,root) %{_bindir}/afio
%{_mandir}/man1/afio.*
%{_examplesdir}/%{name}
