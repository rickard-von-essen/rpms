# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Piece-MySQL

Summary: Perl module adds MySQL-specific methods to Time::Piece
Name: perl-Time-Piece-MySQL
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Piece-MySQL/

Source: http://www.cpan.org/modules/by-module/Time/Time-Piece-MySQL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
perl-Time-Piece-MySQL is a Perl module adds MySQL-specific methods
to Time::Piece.

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
%doc %{_mandir}/man3/Time::Piece::MySQL.3pm*
%dir %{perl_vendorlib}/Time/
%dir %{perl_vendorlib}/Time/Piece/
%{perl_vendorlib}/Time/Piece/MySQL.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
