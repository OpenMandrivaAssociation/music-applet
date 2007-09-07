%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global	python_module_name	musicapplet

%define name music-applet
%define version 2.2.0
%define release %mkrel 2

Summary: Music control applet for the GNOME panel
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: http://www.kuliniewicz.org/music-applet/downloads/%{name}-%{version}.tar.bz2
Patch1: src.musicapplet.applet.py.patch 
License: GPL
Group: Monitoring
Url: http://www.kuliniewicz.org/music-applet/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	GConf2
BuildRequires:	gettext
BuildRequires:	gnome-panel-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	pygtk2.0-libglade
BuildRequires:  gnome-python

Requires:	dbus-python >= 0.80
Requires:	gnome-python-applet
Requires:	gnome-python-applet
Requires:	gnome-python-gconf
Requires:	gnome-python-gnomekeyring
Requires:	hicolor-icon-theme
Requires:	notify-python
Requires:	pygtk2
Requires:	python-numeric
Requires:	PyXML

Requires(pre):	GConf2

Requires(post):	GConf2

Requires(preun):	GConf2

Provides:	gnome-applet-rhythmbox
Provides:	music-applet
Provides:	rhythmbox-applet

Obsoletes:	gnome-applet-rhythmbox
Obsoletes:	music-applet
Obsoletes:	rhythmbox-applet

%description
Rhythmbox Applet is a small, simple GNOME panel applet 
that lets you control Rhythmbox's playback from a panel. 

Advantages that this applet has over using the icon 
Rhythmbox puts in the notification area include:

    * One-click access to the main operations needed 
      during playback, without needing to use a context menu.
    * Display of the current playing time without 
      requiring a mouse-over.
    * Display of the current song's album in the song information.
    * More in the spirit of the GNOME Human Interface Guidelines. 

%prep
%setup -q

%patch1 -p1 -b .musicapplet

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std
%find_lang %name --with-gnome

%post
%post_install_gconf_schemas %name

%preun
%preun_uninstall_gconf_schemas %name

%clean
rm -rf %buildroot

%files -f music-applet.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING FAQ NEWS README README.plugins THANKS   
%{_sysconfdir}/gconf/schemas/music-applet.schemas
%{_libdir}/bonobo/servers/GNOME_Music_Applet.server
%{_libdir}/gnome-2.0/ui/GNOME_Music_Applet.xml
%dir %{python_sitelib}/%{python_module_name}/
%dir %{python_sitelib}/%{python_module_name}/plugins
%exclude %{python_sitelib}/%{python_module_name}/*.la
%{python_sitelib}/%{python_module_name}/*.py*
%{python_sitelib}/%{python_module_name}/plugins/*.py*
%{python_sitelib}/%{python_module_name}/*.so
%{_libexecdir}/music-applet/
%{_datadir}/music-applet/
%{_datadir}/icons/hicolor/*/apps/music-applet-*
