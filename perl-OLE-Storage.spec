%include	/usr/lib/rpm/macros.perl
Summary:	Perl OLE-Storage module
Summary(pl):	Modu³ Perla OLE-Storage
Name:		perl-OLE-Storage
Version:	0.386
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/OLE/OLE-Storage-%{version}.tar.gz
URL:		http://www.perl.com/CPAN/modules/by-module/OLE/OLE-Storage-%{version}.readme
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Startup
BuildRequires:	perl-Unicode-Map
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OLE-Storage gives access to the standard Microsoft Windows OLE
documents (e.g. done by Microsoft Word or Star Word).

%description -l pl
OLE-Storage umo¿liwia dostêp do dokumentów zapisanych w standardzie
Microsoft Windows OLE (np. stworzonych przy pomocy Microsoft Word lub
Star Word).

%prep
%setup -q -n OLE-Storage-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_sitearch}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/OLE/Storage/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
	README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,Changes}.gz
%attr(755,root,root) %{_bindir}/*

%dir %{perl_sitelib}/OLE
%{perl_sitelib}/OLE/Storage
%{perl_sitelib}/OLE/*.pm

%dir %{perl_sitearch}/auto/OLE
%{perl_sitearch}/auto/OLE/Storage

%{_mandir}/man[13]/*
