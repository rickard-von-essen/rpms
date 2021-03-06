# $Id$
# Authority: shuff
# Upstream: Dimitar Zhekov <jimmy$is-vn,bg>

### EL6 ships with terminus-fonts-4.30-1.el6
# ExclusiveDist: el2 el3 el4 el5

%define terminus_fontdir %{_datadir}/fonts/terminus

Summary: A clean fixed-width font
Name: terminus-fonts
Version: 4.30
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://www.is-vn.bg/hamster/

Source: http://www.is-vn.bg/hamster/terminus-font-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: xorg-x11-font-utils
Requires: chkfontpath
Requires: fontconfig
Requires: initscripts
Requires: xorg-x11-xfs

%description
Terminus Font is designed for long (8 and more hours per day) work with
computers. Version 4.30 contains 850 characters, covers about 120 language sets
and supports ISO8859-1/2/5/7/9/13/15/16, Paratype-PT154/PT254, KOI8-R/U/E/F,
Esperanto, many IBM, Windows and Macintosh code pages, as well as the IBM VGA,
vt100 and xterm pseudographic characters.

The sizes present are 6x12, 8x14, 8x16, 10x20, 11x22, 12x24, 14x28 and 16x32.
The styles are normal and bold (except for 6x12), plus EGA/VGA-bold for 8x14
and 8x16.

Note: this package contains only the PCF fonts for X11, not the console fonts.

%prep
%setup -n terminus-font-%{version}

%build
%configure --x11dir=%{terminus_fontdir}
%{__make} pcf

%install
%{__rm} -rf %{buildroot}
%{__make} install-pcf DESTDIR=%{buildroot}

%{_bindir}/gunzip %{buildroot}%{terminus_fontdir}/*

%{_bindir}/mkfontdir %{buildroot}%{terminus_fontdir}
%{_bindir}/mkfontscale %{buildroot}%{terminus_fontdir}

%post
%{_sbindir}/chkfontpath -q --remove=''
%{_sbindir}/chkfontpath -q --add='%{terminus_fontdir}'
/sbin/service xfs reload 2>&1 >/dev/null
%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
    %{_sbindir}/chkfontpath -q --remove='%{terminus_fontdir}'
    /sbin/service xfs reload
	%{_bindir}/fc-cache %{_datadir}/fonts/ 2>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc README README-BG
%{terminus_fontdir}

%changelog
* Thu Mar 18 2010 Steve Huff <shuff@vecna.org> - 4.30-1
- Initial package.
