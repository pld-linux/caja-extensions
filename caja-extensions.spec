Summary:	Extensions for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenia dla zarządcy plików Caja ze środowiska MATE
Name:		caja-extensions
Version:	1.28.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# Source0-md5:	364a23d43d4b10020448ec1f192497c0
URL:		https://wiki.mate-desktop.org/mate-desktop/components/caja-extensions/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	caja-devel >= 1.21.3
BuildRequires:	dbus-devel >= 1.0.2
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	gupnp-devel >= 0.13
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-desktop-devel >= 1.17.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	caja >= 1.21.3
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.22
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Extensions for Caja (MATE file manager).

%description -l pl.UTF-8
Rozszerzenia dla zarządcy plików Caja ze środowiska MATE.

%package -n caja-extension-av
Summary:	Audio/video properties extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie własności audio/wideo dla zarządcy plików Caja ze środowiska MATE
Requires:	%{name} = %{version}-%{release}

%description -n caja-extension-av
Audio/video (Totem) properties extension for Caja (MATE file manager).

%description -n caja-extension-av -l pl.UTF-8
Rozszerzenie własności audio/wideo (odtwarzacza Totem) dla zarządcy
plików Caja ze środowiska MATE.

%package -n caja-extension-gksu
Summary:	gksu extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie gksu dla zarządcy plików Caja ze środowiska MATE
Requires:	gksu
Requires(post,postun):	glib2 >= 1:2.50.0
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mate-file-manager-extension-gksu < 1.8.0

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
Obsoletes:	mate-file-manager-extension-image-converter < 1.8.0

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
Requires(post,postun):	glib2 >= 1:2.50.0
Requires:	%{name} = %{version}-%{release}
Requires:	mate-desktop-libs >= 1.17.0
Requires:	mate-terminal
Obsoletes:	mate-file-manager-extension-open-terminal < 1.8.0

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
Requires(post,postun):	glib2 >= 1:2.50.0
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib >= 0.60
Requires:	dbus-libs >= 1.0.2
Requires:	gupnp >= 0.13
Suggests:	caja-extension-sendto-burn
Suggests:	caja-extension-sendto-emailclient
Suggests:	caja-extension-sendto-gajim
Suggests:	caja-extension-sendto-pidgin
Suggests:	caja-extension-sendto-upnp
Suggests:	engrampa
Obsoletes:	mate-file-manager-sendto < 1.8.0

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
Obsoletes:	mate-file-manager-sendto-burn < 1.8.0

%description -n caja-extension-sendto-burn
A caja-extension-sendto plugin for sending files to CD/DVD Creator
(Brasero).

%description -n caja-extension-sendto-burn -l pl.UTF-8
Wtyczka caja-extension-sendto do wysyłania plików do kreatora
CD/DVD (Brasero).

%package -n caja-extension-sendto-emailclient
Summary:	caja-extension-sendto e-mail client plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla klienta poczty elektronicznej
Requires:	caja-extension-sendto = %{version}-%{release}
Obsoletes:	mate-file-manager-sendto-emailclient < 1.8.0

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
Obsoletes:	mate-file-manager-sendto-gajim < 1.8.0

%description -n caja-extension-sendto-gajim
A caja-extension-sendto plugin for sending files via Gajim.

%description -n caja-extension-sendto-gajim -l pl.UTF-8
Wtyczka caja-extension-sendto do wysyłania plików poprzez Gajima.

%package -n caja-extension-sendto-pidgin
Summary:	caja-extension-sendto Pidgin plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla Pidgina
Requires:	caja-extension-sendto = %{version}-%{release}
Requires:	pidgin >= 2.0
Obsoletes:	mate-file-manager-sendto-pidgin < 1.8.0

%description -n caja-extension-sendto-pidgin
A caja-extension-sendto plugin for sending files via Pidgin.

%description -n caja-extension-sendto-pidgin -l pl.UTF-8
Wtyczka caja-extension-sendto do wysyłania plików poprzez Pidgina.

%package -n caja-extension-sendto-upnp
Summary:	caja-extension-sendto UPnP media server plugin
Summary(pl.UTF-8):	Wtyczka caja-extension-sendto dla serwera multimediów UPnP
Requires:	caja-extension-sendto = %{version}-%{release}
Requires:	gupnp-tools
Obsoletes:	mate-file-manager-sendto-upnp < 1.8.0

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
Requires:	glib2-devel >= 1:2.50.0
Requires:	gtk+3-devel >= 3.22
Obsoletes:	mate-file-manager-sendto-devel < 1.8.0

%description -n caja-extension-sendto-devel
Header files for caja-sendto extensions.

%description -n caja-extension-sendto-devel -l pl.UTF-8
Pliki nagłówkowe dla rozszerzeń caja-sendto.

%package -n caja-extension-sendto-apidocs
Summary:	caja-sendto API documentation
Summary(pl.UTF-8):	Dokumentacja API caja-sendto
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	mate-file-manager-sendto-apidocs < 1.8.0
BuildArch:	noarch

%description -n caja-extension-sendto-apidocs
caja-sendto API documentation.

%description -n caja-extension-sendto-apidocs -l pl.UTF-8
Dokumentacja API caja-sendto.

%package -n caja-extension-share
Summary:	Share extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie share dla zarządcy plików Caja ze środowiska MATE
Requires:	%{name} = %{version}-%{release}
Requires:	samba-client
Obsoletes:	mate-file-manager-extension-share < 1.8.0

%description -n caja-extension-share
Caja share extension allows you to quickly share a folder from the
MATE Caja file manager without requiring root access. It uses Samba,
so your folders can be accessed by any operating system.

%description -n caja-extension-share -l pl.UTF-8
Rozszerzenie share dla zarządcy plików Caja pozwala szybko udostępnić
folder z poziomu zarządcy plików Caja (ze środowiska MATE) bez dostępu
do uprawnień administratora. Wykorzystuje Sambę, więc foldery są
dostępne z dowolnego systemu operacyjnego.

%package -n caja-extension-wallpaper
Summary:	Set as wallpaper extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie ustawiania jako tapety dla zarządcy plików Caja ze środowiska MATE
Requires:	%{name} = %{version}-%{release}

%description -n caja-extension-wallpaper
Caja wallpaper extension allows you to set a file as MATE wallpaper.

%description -n caja-extension-wallpaper -l pl.UTF-8
Rozszerzenie wallpaper dla zarządcy plików Caja pozwala ustawić plik
jako tapetę w środowisku MATE.

%package -n caja-extension-xattr-tags
Summary:	Xattr tags extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie xattr tags dla zarządcy plików Caja ze środowiska MATE
Requires:	%{name} = %{version}-%{release}

%description -n caja-extension-xattr-tags
Xattr tags extension for Caja (MATE file manager).

%description -n caja-extension-xattr-tags -l pl.UTF-8
Rozszerzenie xattr tags dla zarządcy plików Caja ze środowiska MATE.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules \
	--disable-static \
	--enable-gksu \
	--enable-gtk-doc \
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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{frp,ie,jv,ku_IQ,pms,es_ES}

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

%files -n caja-extension-av
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-av.so
%{_datadir}/caja/extensions/libcaja-av.caja-extension

%files -n caja-extension-gksu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-gksu.so
%{_datadir}/caja/extensions/libcaja-gksu.caja-extension

%files -n caja-extension-image-converter
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-image-converter.so
%{_datadir}/caja/extensions/libcaja-image-converter.caja-extension

%files -n caja-extension-open-terminal
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-open-terminal.so
%{_datadir}/glib-2.0/schemas/org.mate.caja-open-terminal.gschema.xml
%{_datadir}/caja/extensions/libcaja-open-terminal.caja-extension

%files -n caja-extension-sendto
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/caja-sendto
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-sendto.so
%dir %{_libdir}/caja-sendto
%dir %{_libdir}/caja-sendto/plugins
%attr(755,root,root) %{_libdir}/caja-sendto/plugins/libnstremovable_devices.so
%{_datadir}/glib-2.0/schemas/org.mate.Caja.Sendto.gschema.xml
%{_datadir}/caja/extensions/libcaja-sendto.caja-extension
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
%{_datadir}/caja/extensions/libcaja-share.caja-extension

%files -n caja-extension-wallpaper
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-wallpaper.so
%{_datadir}/caja/extensions/libcaja-wallpaper.caja-extension

%files -n caja-extension-xattr-tags
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-xattr-tags.so
%{_datadir}/caja/extensions/libcaja-xattr-tags.caja-extension
