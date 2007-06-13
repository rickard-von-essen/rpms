# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UNIVERSAL-moniker

Summary: Perl module named UNIVERSAL-moniker
Name: perl-UNIVERSAL-moniker
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UNIVERSAL-moniker/

Source: http://www.cpan.org/modules/by-module/UNIVERSAL/UNIVERSAL-moniker-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-UNIVERSAL-moniker is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/UNIVERSAL::moniker.3pm*
%dir %{perl_vendorlib}/UNIVERSAL/
%{perl_vendorlib}/UNIVERSAL/moniker.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
