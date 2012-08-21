Summary:	xrdb application - X server resource database utility
Summary(pl.UTF-8):	Aplikacja xrdb - narzędzie do bazy danych zasobów serwera X
Name:		xorg-app-xrdb
Version:	1.0.9
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrdb-%{version}.tar.bz2
# Source0-md5:	ed2e48cf33584455d74615ad4bbe4246
URL:		http://xorg.freedesktop.org/
BuildRequires:	pkgconfig >= 1:0.19
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 1.8
Requires:	mcpp
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
	--with-cpp=/usr/bin/mcpp

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
%{_mandir}/man1/xrdb.1*
