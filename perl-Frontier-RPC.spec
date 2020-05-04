#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Frontier
%define	pnam	RPC
Summary:	Frontier::RPC2 - encode/decode RPC2 format XML
Summary(pl.UTF-8):	Frontier::RPC2 - kodowanie/dekodowanie formatu XML RPC2
Name:		perl-Frontier-RPC
Version:	0.07
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/K/KM/KMACLEOD/Frontier-RPC-%{version}b4.tar.gz
# Source0-md5:	c04582da604f11bdbe60606738f92457
URL:		https://metacpan.org/pod/Frontier::RPC2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-XML-Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote Procedure
Calls using Extensible Markup Language). Frontier::RPC includes both a
client module for making requests to a server and several server
modules for implementing servers using CGI, Apache, and standalone
with HTTP::Daemon.

%description -l pl.UTF-8
Frontier::RPC implementuje XML RPC (Remote Procedure Calls - zdalne
wywołania przy użyciu języku XML) UserLand Software. Frontier::RPC
zawiera zarówno moduł kliencki do wysyłania żądań do serwera, a także
kilka modułów serwerowych do implementowania serwerów przy użyciu CGI,
Apache'a, a także samodzielnie z użyciem HTTP::Daemon.

%prep
%setup -q -n Frontier-RPC-%{version}b4

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog Changes docs README
%{perl_vendorlib}/Apache/XMLRPC.pm
%{perl_vendorlib}/Frontier
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
