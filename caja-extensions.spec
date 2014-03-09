Summary:	Extensions for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenia dla zarządcy plików Caja ze środowiska MATE
Name:		caja-extensions
Version:	1.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	bc56df2c6b0445b574040222b40813bd
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	caja-devel >= 1.1.0
BuildRequires:	dbus-devel >= 1.0.2
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-devel >= 0.13
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	caja >= 1.1.0
Requires:	glib2 >= 1:2.28.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensions for Caja (MATE file manager).

%description -l pl.UTF-8
Rozszerzenia dla zarządcy plików Caja ze środowiska MATE.

%package gksu
Summary:	gksu extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE
Requires:	gksu
Requires(post,postun):	glib2 >= 1:2.14.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mate-file-manager-extension-gksu

%description gksu
gksu extension for Caja (MATE file manager). It's a fork of
nautilus-gksu extension.

%description gksu -l pl.UTF-8
Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE. Jest to
odgałęzienie rozszerzenia nautilus-gksu.

%package image-converter
Summary:	Caja (MATE file manager) extension to mass resize or rotate images
Summary(pl.UTF-8):	Rozszerzenie zarządcy plików Caja pozwalające masowo zmieniać rozmiar i obracać pliki graficzne
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick
Suggests:	ImageMagick-coder-jpeg
Suggests:	ImageMagick-coder-jpeg2
Suggests:	ImageMagick-coder-png
Suggests:	ImageMagick-coder-tiff
Obsoletes:	mate-file-manager-extension-image-converter

%description image-converter
The Caja-Image-Converter extension allows you to resize/rotate images
from Caja (MATE file manager).

Caja-Image-Converter is a fork of Nautilus-Image-Converter.

%description image-converter -l pl.UTF-8
Rozszerzenie Caja-Image-Converter pozwala na zmianę rozmiaru i
obracanie rozmiarów obrazów z poziomu zarządców plików Caja,
przeznaczonego dla środowiska MATE.

Caja-Image-Converter to odgałęzienie rozszerzenia
Nautilus-Image-Converter.

%package open-terminal
Summary:	open-terminal extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie open-terminal dla zarządcy plików Caja ze środowiska MATE
Requires(post,postun):	glib2 >= 1:2.14.0
Requires:	%{name} = %{version}-%{release}
Requires:	mate-terminal
Obsoletes:	mate-file-manager-extension-open-terminal

%description open-terminal
This is a proof-of-concept Caja extension which allows you to open a
terminal in arbitrary local folders.

This is a fork of nautilus-open-terminal extension.

%description open-terminal -l pl.UTF-8
Rozszerzenie zarządcy plików Caja, pozwalające na otwieranie terminala
w dowolnych folderach lokalnych.

Jest to odgałęzienie rozszerzenia nautilus-open-terminal.

%package sendto
Summary:	Caja context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe zarządcy plików Caja do wysyłania plików
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{version}-%{release}
Suggests:	engrampa
Obsoletes:	mate-file-manager-sendto

%description sendto
Caja sendto provides a Caja context menu for sending files via other
desktop applications. It's a fork of nautilus-sendto from GNOME.

%description sendto -l pl.UTF-8
Caja sendto dostarcza menu kontekstowe dla zarządcy plików Caja do
wysyłania plików poprzez inne aplikacje biurkowe. Jest to odgałęzienie
programu nautilus-sendto z GNOME.

%package sendto-burn
Summary:	caja-extensions-sendto CD/DVD Creator plugin
Summary(pl.UTF-8):	Wtyczka caja-extensions-sendto dla kreatora CD/DVD
Requires:	%{name}-sendto = %{version}-%{release}
Requires:	brasero
Obsoletes:	mate-file-manager-sendto-burn

%description sendto-burn
A caja-extensions-sendto plugin for sending files to CD/DVD Creator
(Brasero).

%description sendto-burn -l pl.UTF-8
Wtyczka mate-file-manager-sendto do wysyłania plików do kreatora
CD/DVD (Brasero).

%package sendto-emailclient
Summary:	caja-extensions-sendto e-mail client plugin
Summary(pl.UTF-8):	Wtyczka caja-extensions-sendto dla klienta poczty elektronicznej
Requires:	%{name}-sendto = %{version}-%{release}
Obsoletes:	mate-file-manager-sendto-emailclient

%description sendto-emailclient
A caja-extensions-sendto plugin for sending files via e-mail client.
Supported e-mail clients are: Evolution 2.0 through 3.0, Balsa,
Thunderbird/Icedove, Seamonkey/Iceape, Sylpheed/Claws Mail, Anjal.

%description sendto-emailclient -l pl.UTF-8
Wtyczka caja-extensions-sendto do wysyłania plików poprzez klienta
poczty elektronicznej. Obsługiwane są: Evolution 2.0 do 3.0, Balsa,
Thunderbird/Icedove, Seamonkey/Iceape, Sylpheed/Claws Mail, Anjal.

%package sendto-gajim
Summary:	caja-extensions-sendto Gajim plugin
Summary(pl.UTF-8):	Wtyczka caja-extensions-sendto dla Gajima
Requires:	%{name}-sendto = %{version}-%{release}
Requires:	dbus >= 1.0.2
Requires:	gajim >= 0.10.1
Obsoletes:	mate-file-manager-sendto-gajim

%description sendto-gajim
A caja-extensions-sendto plugin for sending files via Gajim.

%description sendto-gajim -l pl.UTF-8
Wtyczka caja-extension-sentdo do wysyłania plików poprzez Gajima.

%package sendto-pidgin
Summary:	caja-extensions-sendto Pidgin plugin
Summary(pl.UTF-8):	Wtyczka caja-extensions-sendto dla Pidgina
Requires:	%{name}-sendto = %{version}-%{release}
Requires:	pidgin >= 2.0
Obsoletes:	mate-file-manager-sendto-pidgin

%description sendto-pidgin
A caja-extensions-sendto plugin for sending files via Pidgin.

%description sendto-pidgin -l pl.UTF-8
Wtyczka caja-extension-sentdo do wysyłania plików poprzez Pidgina.

%package sendto-upnp
Summary:	caja-extensions-sendto UPnP media server plugin
Summary(pl.UTF-8):	Wtyczka caja-extensions-sendto dla serwera multimediów UPnP
Requires:	%{name}-sendto = %{version}-%{release}
Requires:	gupnp-tools
Obsoletes:	mate-file-manager-sendto-upnp

%description sendto-upnp
A caja-extensions-sendto plugin for sending files to UPnP media
server.

%description sendto-upnp -l pl.UTF-8
Wtyczka caja-extensions-sendto do wysyłania plików do serwera
multimediów UPnP.

%package sendto-devel
Summary:	Header files for caja-sendto extensions
Summary(pl.UTF-8):	Pliki nagłówkowe dla rozszerzeń caja-sendto
Group:		Development/Libraries
# doesn't require base
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+2-devel >= 2:2.18
Obsoletes:	mate-file-manager-sendto-devel

%description sendto-devel
Header files for caja-sendto extensions.

%description sendto-devel -l pl.UTF-8
Pliki nagłówkowe dla rozszerzeń caja-sendto.

%package sendto-apidocs
Summary:	caja-sendto API documentation
Summary(pl.UTF-8):	Dokumentacja API caja-sendto
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	mate-file-manager-sendto-apidocs

%description sendto-apidocs
caja-sendto API documentation.

%description sendto-apidocs -l pl.UTF-8
Dokumentacja API caja-sendto.

%package share
Summary:	Share extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie share dla zarządcy plików Caja ze środowiska MATE
Requires:	%{name} = %{version}-%{release}
Requires:	samba-client
Obsoletes:	mate-file-manager-extension-share

%description share
mate-file-manager share extension allows you to quickly share a folder
from the MATE Caja file manager without requiring root access. It uses
Samba, so your folders can be accessed by any operating system.

%description share -l pl.UTF-8
Rozszerzenie share dla mate-file-managera pozwala szybko udostępnić
folder z poziomu zarządcy plików Caja (ze środowiska MATE) bez dostępu
do uprawnień administratora. Wykorzystuje Sambę, więc foldery są
dostępne z dowolnego systemu operacyjnego.


%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules \
	--disable-static \
	--enable-gtk-doc \
	--enable-gksu \
	--enable-image-converter \
	--enable-open-terminal \
	--enable-sendto \
	--enable-share \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja-sendto/plugins/*.la

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cmn

# mate < 1.5 did not exist in PLD, avoid dependency on mate-conf
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/caja-open-terminal.convert
%{__rm} $RPM_BUILD_ROOT%{_datadir}/MateConf/gsettings/caja-sendto-convert

%find_lang caja-extensions

%clean
rm -rf $RPM_BUILD_ROOT

%post	gksu
%glib_compile_schemas

%postun	gksu
%glib_compile_schemas

%post	open-terminal
%glib_compile_schemas

%postun	open-terminal
%glib_compile_schemas

%post	sendto
%glib_compile_schemas

%postun	sendto
%glib_compile_schemas

%files -f caja-extensions.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/caja-extensions

%files gksu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-gksu.so

%files image-converter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui

%files open-terminal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

%files sendto
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caja-sendto
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%attr(755,root,root)
%{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja-extensions/caja-sendto.ui
%{_mandir}/man1/caja-sendto.1*

%files sendto-burn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstburn.so

%files sendto-emailclient
%defattr(644,root,root,755)
%attr(755,root,root)
%{_libdir}/caja-sendto/plugins/libnstemailclient.so

%files sendto-gajim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstgajim.so

%files sendto-pidgin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files sendto-upnp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstupnp.so

%files sendto-devel
%defattr(644,root,root,755)
%{_includedir}/caja-sendto
%{_pkgconfigdir}/caja-sendto.pc

%files sendto-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/caja-sendto

%files share
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
