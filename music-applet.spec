%global	python_module_name	musicapplet

%define name music-applet
%define version 2.5.1
%define release %mkrel 6
%define build_xmms2 0
Summary: Music control applet for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: http://www.kuliniewicz.org/music-applet/downloads/%{name}-%{version}.tar.gz
License: GPLv2+
Group: Sound
Url: https://www.kuliniewicz.org/music-applet/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	GConf2
BuildRequires:	gettext
BuildRequires:	gnome-panel-devel
BuildRequires:	intltool
BuildRequires:	libglade2.0-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	pygtk2.0-libglade
BuildRequires:  gnome-python-devel
BuildRequires:  pyxmms
BuildRequires:  python-mpd
Requires:	dbus-python >= 0.80
Requires:	gnome-python-applet
Requires:	gnome-python-applet
Requires:	gnome-python-gconf
Requires:	gnome-python-desktop
Requires:	hicolor-icon-theme
Requires:	python-notify
Requires:	pygtk2.0
Requires:	python-numeric
Requires:	PyXML
Requires:  python-mpd

Requires(post):	GConf2
Requires(preun):	GConf2

Provides:	gnome-applet-rhythmbox
Provides:	rhythmbox-applet
Obsoletes:	gnome-applet-rhythmbox
Obsoletes:	rhythmbox-applet
Provides:	%name-amarok
Obsoletes:	%name-amarok

%description
Music Applet is a small, simple GNOME panel applet that lets you
control a variety of different music players from the panel.

Music Applet provides easy access to information about the current
song and the most important playback controls.

Music Applet currently supports the following music players:

* Amarok
* Audacious
* Banshee
* Exaile
* MPD
* Muine
* Quod Libet
* Rhythmbox
* VLC
* XMMS
%if %build_xmms2
* XMMS2
%endif

Music Applet is the successor to Rhythmbox Applet.

%package xmms
Group: Sound
Summary: Music control applet for the GNOME panel - xmms 1 plugin
Requires: %name = %epoch:%version
Requires: pyxmms

%description xmms
Music Applet is a small, simple GNOME panel applet that lets you
control a variety of different music players from the panel.

Music Applet provides easy access to information about the current
song and the most important playback controls.

Install this for xmms 1 support.

%if %build_xmms2
%package xmms2
Group: Sound
Summary: Music control applet for the GNOME panel - xmms 2 plugin
Requires: %name = %epoch:%version
Requires: python-xmms2

%description xmms2
Music Applet is a small, simple GNOME panel applet that lets you
control a variety of different music players from the panel.

Music Applet provides easy access to information about the current
song and the most important playback controls.

Install this for xmms 2 support.
%endif

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
#gw install all python modules in the arch-dependant dir, else the C module
#is not found by python
%make pythondir=%py_platsitedir

%install
rm -rf %buildroot
%makeinstall_std pythondir=%py_platsitedir
%find_lang %name --with-gnome
#gw kde 3.x
rm -f %buildroot%py_platsitedir/%python_module_name/plugins/amarok.*
%if !%build_xmms2
rm -f %buildroot%{py_platsitedir}/%{python_module_name}/plugins/xmms2*
rm -f %buildroot%{py_platsitedir}/%{python_module_name}/widgets.la
%endif

%post
%post_install_gconf_schemas %name
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %name

%postun
%clean_icon_cache hicolor

%clean
rm -rf %buildroot

%files -f music-applet.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING FAQ NEWS README README.plugins THANKS
%{_sysconfdir}/gconf/schemas/music-applet.schemas
%{_libdir}/bonobo/servers/GNOME_Music_Applet.server
%{_libdir}/gnome-2.0/ui/GNOME_Music_Applet.xml
%dir %{py_platsitedir}/%{python_module_name}/
%dir %{py_platsitedir}/%{python_module_name}/plugins
%{py_platsitedir}/%{python_module_name}/*.py*
%{py_platsitedir}/%{python_module_name}/plugins/__init__*
%{py_platsitedir}/%{python_module_name}/plugins/amarok*
%{py_platsitedir}/%{python_module_name}/plugins/audacious*
%{py_platsitedir}/%{python_module_name}/plugins/banshee*
%{py_platsitedir}/%{python_module_name}/plugins/exaile*
%{py_platsitedir}/%{python_module_name}/plugins/mpd*
%{py_platsitedir}/%{python_module_name}/plugins/muine*
%{py_platsitedir}/%{python_module_name}/plugins/quodlibet*
%{py_platsitedir}/%{python_module_name}/plugins/rhythmbox*
%{py_platsitedir}/%{python_module_name}/plugins/vlc*
%{py_platsitedir}/%{python_module_name}/widgets.so
%{_libexecdir}/music-applet/
%{_datadir}/music-applet/
%{_datadir}/icons/hicolor/*/apps/music-applet-*

%files xmms
%defattr(-,root,root,-)
%{py_platsitedir}/%{python_module_name}/plugins/xmms1*

%if %build_xmms2
%files xmms2
%defattr(-,root,root,-)
%{py_platsitedir}/%{python_module_name}/plugins/xmms2*
%endif
