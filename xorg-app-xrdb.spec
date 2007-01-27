Summary:	xrdb application - X server resource database utility
Summary(pl):	Aplikacja xrdb - narz�dzie do bazy danych zasob�w serwera X
Name:		xorg-app-xrdb
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xrdb-%{version}.tar.bz2
# Source0-md5:	380b2ef545306354cc150834de567be7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
# just xmuu
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	cpp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xrdb is used to get or set the contents of the RESOURCE_MANAGER
property on the root window of screen 0, or the SCREEN_RESOURCES
property on the root window of any or all screens, or everything
combined. You would normally run this program from your X startup
file.

%description -l pl
xrdb s�u�y do odczytu lub ustawiania zawarto�ci w�a�ciwo�ci
RESOURCE_MANAGER g��wnego okna ekranu 0 lub w�a�ciwo�ci
SCREEN_RESOURCES g��wnego okna dowolnego z ekran�w, lub wszystkiego
razem. Zwykle u�ywa si� tego programu z poziomu skryptu startowego X.

%prep
%setup -q -n xrdb-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-cpp-path=/usr/bin/cpp

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xrdb
%{_mandir}/man1/xrdb.1x*
