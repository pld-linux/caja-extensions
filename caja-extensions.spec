Summary:	Extensions for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenia dla zarządcy plików Caja ze środowiska MATE
Name:		caja-extensions
Version:	1.8.0
Release:	5
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

%package -n caja-extension-gksu
Summary:	gksu extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE
Requires:	gksu
Requires(post,postun):	glib2 >= 1:2.14.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mate-file-manager-extension-gksu

%description -n caja-extension-gksu
gksu extension for Caja (MATE file manager). It's a fork of
nautilus-gksu extension.

%description -n caja-extension-gksu -l pl.UTF-8
Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE. Jest to
odgałęzienie rozszerzenia nautilus-gksu.

%package -n caja-extension-image-converter
Summary:	Caja (MATE file manager) extension to mass resize or rotate images
Summary(pl.UTF-8):	Rozszerzenie zarządcy plików Caja pozwalające masowo zmieniać rozmiar i obracać pliki graficzne
Requires:	%{name} = %{version}-%{release}
Requires:	ImageMagick
Suggests:	ImageMagick-coder-jpeg
Suggests:	ImageMagick-coder-jpeg2
Suggests:	ImageMagick-coder-png
Suggests:	ImageMagick-coder-tiff
Obsoletes:	mate-file-manager-extension-image-converter

%description -n caja-extension-image-converter
The Caja-Image-Converter extension allows you to resize/rotate images
from Caja (MATE file manager).

Caja-Image-Converter is a fork of Nautilus-Image-Converter.

%description -n caja-extension-image-converter -l pl.UTF-8
Rozszerzenie Caja-Image-Converter pozwala na zmianę rozmiaru i
obracanie rozmiarów obrazów z poziomu zarządców plików Caja,
przeznaczonego dla środowiska MATE.

Caja-Image-Converter to odgałęzienie rozszerzenia
Nautilus-Image-Converter.

%package -n caja-extension-open-terminal
Summary:	open-terminal extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie open-terminal dla zarządcy plików Caja ze środowiska MATE
Requires(post,postun):	glib2 >= 1:2.14.0
Requires:	%{name} = %{version}-%{release}
Requires:	mate-terminal
Obsoletes:	mate-file-manager-extension-open-terminal

%description -n caja-extension-open-terminal
This is a proof-of-concept Caja extension which allows you to open a
terminal in arbitrary local folders.

This is a fork of nautilus-open-terminal extension.

%description -n caja-extension-open-terminal -l pl.UTF-8
Rozszerzenie zarządcy plików Caja, pozwalające na otwieranie terminala
w dowolnych folderach lokalnych.

Jest to odgałęzienie rozszerzenia nautilus-open-terminal.

%package -n caja-extension-sendto
Summary:	Caja context menu for sending files
Summary(pl.UTF-8):	Menu kontekstowe zarządcy plików Caja do wysyłania plików
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name} = %{version}-%{release}
Suggests:	caja-extension-sendto-burn
Suggests:	caja-extension-sendto-emailclient
Suggests:	caja-extension-sendto-gajim
Suggests:	caja-extension-sendto-pidgin
Suggests:	caja-extension-sendto-upnp
Suggests:	engrampa
Obsoletes:	mate-file-manager-sendto

%description -n caja-extension-sendto
Caja sendto provides a Caja context menu for sending files via other
desktop applications. It's a fork of nautilus-sendto from GNOME.

%description -n caja-extension-sendto -l pl.UTF-8
Caja sendto dostarcza menu kontekstowe dla zarządcy plików Caja do
wysyłania plików poprzez inne aplikacje biurkowe. Jest to odgałęzienie
programu nautilus-sendto z GNOME.

%package -n caja-extension-sendto-burn
Summary:	caja-extension-sendto CD/DVD Creator plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla kreatora CD/DVD
Requires:	brasero
Requires:	caja-extension-sendto = %{version}-%{release}
Obsoletes:	mate-file-manager-sendto-burn

%description -n caja-extension-sendto-burn
A caja-extension-sendto plugin for sending files to CD/DVD Creator
(Brasero).

%description -n caja-extension-sendto-burn -l pl.UTF-8
Wtyczka mate-file-manager-sendto do wysyłania plików do kreatora
CD/DVD (Brasero).

%package -n caja-extension-sendto-emailclient
Summary:	caja-extension-sendto e-mail client plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla klienta poczty elektronicznej
Requires:	caja-extension-sendto = %{version}-%{release}
Obsoletes:	mate-file-manager-sendto-emailclient

%description -n caja-extension-sendto-emailclient
A caja-extension-sendto plugin for sending files via e-mail client.
Supported e-mail clients are: Evolution 2.0 through 3.0, Balsa,
Thunderbird/Icedove, Seamonkey/Iceape, Sylpheed/Claws Mail, Anjal.

%description -n caja-extension-sendto-emailclient -l pl.UTF-8
Wtyczka caja-extension-sendto do wysyłania plików poprzez klienta
poczty elektronicznej. Obsługiwane są: Evolution 2.0 do 3.0, Balsa,
Thunderbird/Icedove, Seamonkey/Iceape, Sylpheed/Claws Mail, Anjal.

%package -n caja-extension-sendto-gajim
Summary:	caja-extension-sendto Gajim plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla Gajima
Requires:	caja-extension-sendto = %{version}-%{release}
Requires:	dbus >= 1.0.2
Requires:	gajim >= 0.10.1
Obsoletes:	mate-file-manager-sendto-gajim

%description -n caja-extension-sendto-gajim
A caja-extension-sendto plugin for sending files via Gajim.

%description -n caja-extension-sendto-gajim -l pl.UTF-8
Wtyczka caja-extension-sentdo do wysyłania plików poprzez Gajima.

%package -n caja-extension-sendto-pidgin
Summary:	caja-extension-sendto Pidgin plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla Pidgina
Requires:	caja-extension-sendto = %{version}-%{release}
Requires:	pidgin >= 2.0
Obsoletes:	mate-file-manager-sendto-pidgin

%description -n caja-extension-sendto-pidgin
A caja-extension-sendto plugin for sending files via Pidgin.

%description -n caja-extension-sendto-pidgin -l pl.UTF-8
Wtyczka caja-extension-sentdo do wysyłania plików poprzez Pidgina.

%package -n caja-extension-sendto-upnp
Summary:	caja-extension-sendto UPnP media server plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla serwera multimediów UPnP
Requires:	caja-extension-sendto = %{version}-%{release}
Requires:	gupnp-tools
Obsoletes:	mate-file-manager-sendto-upnp

%description -n caja-extension-sendto-upnp
A caja-extension-sendto plugin for sending files to UPnP media server.

%description -n caja-extension-sendto-upnp -l pl.UTF-8
Wtyczka caja-extension-sendto do wysyłania plików do serwera
multimediów UPnP.

%package -n caja-extension-sendto-devel
Summary:	Header files for caja-sendto extensions
Summary(pl.UTF-8):	Pliki nagłówkowe dla rozszerzeń caja-sendto
Group:		Development/Libraries
# doesn't require base
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+2-devel >= 2:2.18
Obsoletes:	mate-file-manager-sendto-devel

%description -n caja-extension-sendto-devel
Header files for caja-sendto extensions.

%description -n caja-extension-sendto-devel -l pl.UTF-8
Pliki nagłówkowe dla rozszerzeń caja-sendto.

%package -n caja-extension-sendto-apidocs
Summary:	caja-sendto API documentation
Summary(pl.UTF-8):	Dokumentacja API caja-sendto
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	mate-file-manager-sendto-apidocs
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n caja-extension-sendto-apidocs
caja-sendto API documentation.

%description -n caja-extension-sendto-apidocs -l pl.UTF-8
Dokumentacja API caja-sendto.

%package -n caja-extension-share
Summary:	Share extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie share dla zarządcy plików Caja ze środowiska MATE
Requires:	%{name} = %{version}-%{release}
Requires:	samba-client
Obsoletes:	mate-file-manager-extension-share

%description -n caja-extension-share
mate-file-manager share extension allows you to quickly share a folder
from the MATE Caja file manager without requiring root access. It uses
Samba, so your folders can be accessed by any operating system.

%description -n caja-extension-share -l pl.UTF-8
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

%post	-n caja-extension-gksu
%glib_compile_schemas

%postun	-n caja-extension-gksu
%glib_compile_schemas

%post	-n caja-extension-open-terminal
%glib_compile_schemas

%postun	-n caja-extension-open-terminal
%glib_compile_schemas

%post	-n caja-extension-sendto
%glib_compile_schemas

%postun	-n caja-extension-sendto
%glib_compile_schemas

%files -f caja-extensions.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/caja-extensions

%files -n caja-extension-gksu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-gksu.so

%files -n caja-extension-image-converter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja-extensions/caja-image-resize.ui
%{_datadir}/caja-extensions/caja-image-rotate.ui

%files -n caja-extension-open-terminal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml

%files -n caja-extension-sendto
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

%files -n caja-extension-sendto-burn
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstburn.so

%files -n caja-extension-sendto-emailclient
%defattr(644,root,root,755)
%attr(755,root,root)
%{_libdir}/caja-sendto/plugins/libnstemailclient.so

%files -n caja-extension-sendto-gajim
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstgajim.so

%files -n caja-extension-sendto-pidgin
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstpidgin.so

%files -n caja-extension-sendto-upnp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstupnp.so

%files -n caja-extension-sendto-devel
%defattr(644,root,root,755)
%{_includedir}/caja-sendto
%{_pkgconfigdir}/caja-sendto.pc

%files -n caja-extension-sendto-apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/caja-sendto

%files -n caja-extension-share
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/caja-extensions/share-dialog.ui
