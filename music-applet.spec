%define name music-applet
%define version 2.2.0
%define release %mkrel 1

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
BuildRequires: gnome-panel-devel
BuildRequires: libeel-devel
BuildRequires: scrollkeeper
BuildRequires: perl-XML-Parser
BuildRequires: rhythmbox
BuildRequires: banshee
BuildRequires: muine
BuildRequires: pygtk2.0-devel
Requires: rhythmbox
Requires: pygtk2.0-libglade

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

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_libdir}/bonobo/servers/GNOME_Music_Applet.server
%{_libdir}/music-applet
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.png
%{_libdir}/gnome-2.0/ui/GNOME_Music_Applet.xml
%{_datadir}/%{name}/*.glade
%{py_platsitedir}/musicapplet/*
%{_datadir}/icons/*

