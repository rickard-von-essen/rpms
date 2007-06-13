# $Id$
# Authority: dag
# Upstream: Steven Knight <knight$baldmt,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Cmd

Summary: Perl module for portable testing of commands and scripts
Name: perl-Test-Cmd
Version: 1.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Cmd/

Source: http://www.cpan.org/modules/by-module/Test/Test-Cmd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-Test-Cmd is a Perl module for portable testing of commands and scripts.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Test::Cmd.3pm*
%doc %{_mandir}/man3/Test::Common.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Cmd/
%{perl_vendorlib}/Test/Cmd.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
