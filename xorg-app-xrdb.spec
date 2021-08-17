#
# Conditional build:
%bcond_without	mcpp	# gcc's cpp instead of mcpp
#
Summary:	xrdb application - X server resource database utility
Summary(pl.UTF-8):	Aplikacja xrdb - narzędzie do bazy danych zasobów serwera X
Name:		xorg-app-xrdb
Version:	1.2.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xrdb-%{version}.tar.bz2
# Source0-md5:	85f04a810e2fb6b41ab872b421dce1b1
URL:		https://xorg.freedesktop.org/
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.25
BuildRequires:	xorg-util-util-macros >= 1.8
%if %{with mcpp}
Requires:	mcpp
%else
Requires:	cpp
%endif
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
%configure \
	--with-cpp=/usr/bin/%{?with_mcpp:m}cpp \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xrdb
%{_mandir}/man1/xrdb.1*
