#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	OLE
%define	pnam	Storage
Summary:	Perl OLE::Storage module
Summary(pl):	Modu³ Perla OLE::Storage
Name:		perl-OLE-Storage
Version:	0.386
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.perl.com/CPAN/modules/by-module/OLE/OLE-Storage-%{version}.readme
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Startup
BuildRequires:	perl-Unicode-Map
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OLE::Storage gives access to the standard Microsoft Windows OLE
documents (e.g. done by Microsoft Word or Star Word).

%description -l pl
OLE::Storage umo¿liwia dostêp do dokumentów zapisanych w standardzie
Microsoft Windows OLE (np. stworzonych przy pomocy Microsoft Word lub
Star Word).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README 
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/OLE/Storage
%{perl_sitelib}/OLE/*.pm
%{_mandir}/man[13]/*
