Summary:	Program which makes cpio-format archives.
Summary(pl):	Pakiet zawiera program do tworzenia archiwów w formacie cpio. 
Name:		afio
Version:	2.4.5
Release:	8
License:	Unknown
Group:		Applications/Archiving
Group(de):	Applikationen/Archivierung
Group(pl):	Aplikacje/Archiwizacja
Source:	%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup  -q

%build
%{__make} clean
%{__make} CFLAGS1="-Wformat -fomit-frame-pointer $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

install afio $RPM_BUILD_ROOT%{_bindir}
install afio.1* $RPM_BUILD_ROOT%{_mandir}
mv script* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf afio.lsm HISTORY SCRIPTS README PORTING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc afio.lsm* HISTORY* SCRIPTS* README* PORTING*
%attr(755,root,root) %{_bindir}/afio
%{_mandir}/afio.*
%{_examplesdir}/%{name}
