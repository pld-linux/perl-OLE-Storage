#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	OLE
%define	pnam	Storage
Summary:	OLE::Storage - an interface to Structured Storage documents
Summary(pl):	OLE::Storage - interfejs do dokumentów "Structured Storage"
Name:		perl-OLE-Storage
Version:	0.386
Release:	13
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d87e521546fb3c10270d492ab50f7bab
URL:		http://www.perl.com/CPAN/modules/by-module/OLE/OLE-Storage-%{version}.readme
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Startup
BuildRequires:	perl-Unicode-Map
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/OLE/Storage
%{perl_vendorlib}/OLE/*.pm
%{_mandir}/man[13]/*
