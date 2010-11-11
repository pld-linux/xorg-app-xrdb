# TODO
# - split cpp into separate package so we don't pull whole gcc suite to get cpp only
#   cpp pkg was killed here somewhy (no explanation ....)
#   http://cvs.pld-linux.org/cgi-bin/cvsweb.cgi/packages/gcc/gcc.spec.diff?r1=1.217.2.75;r2=1.217.2.76;f=h
#   The explanation is that GNU cpp depends on language frontend (cc1 in case of traditional cpp mode).
Summary:	xrdb application - X server resource database utility
Summary(pl.UTF-8):	Aplikacja xrdb - narzędzie do bazy danych zasobów serwera X
Name:		xorg-app-xrdb
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrdb-%{version}.tar.bz2
# Source0-md5:	93f54f04e0b531b5fb77d3f051cbf22a
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	cpp >= 6:4.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrdb is used to get or set the contents of the RESOURCE_MANAGER
property on the root window of screen 0, or the SCREEN_RESOURCES
property on the root window of any or all screens, or everything
combined. You would normally run this program from your X startup
file.

%description -l pl.UTF-8
xrdb służy do odczytu lub ustawiania zawartości właściwości
RESOURCE_MANAGER głównego okna ekranu 0 lub właściwości
SCREEN_RESOURCES głównego okna dowolnego z ekranów, lub wszystkiego
razem. Zwykle używa się tego programu z poziomu skryptu startowego X.

%prep
%setup -q -n xrdb-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-cpp=/usr/bin/cpp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xrdb
%{_mandir}/man1/xrdb.1x*
